import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from error_handler import (
    check_api_key,
    extract_pdf_text,
    validate_extracted_text,
    handle_api_error,
    validate_api_response,
    MAX_CHARS
)
from ui import (
    apply_styles,
    render_header,
    render_sidebar,
    render_metadata,
    render_results
)

load_dotenv()

# --- Page Config ---
st.set_page_config(
    page_title="Gender Policy Analyzer",
    page_icon="📋",
    layout="wide"
)

# --- Apply Styles & Render Header ---
apply_styles()
render_header()

# --- Initialize Groq Client ---
api_key = os.getenv("GROQ_API_KEY")
check_api_key(api_key)
client = Groq(api_key=api_key)

# --- Sidebar ---
framework, output_use = render_sidebar()

# --- File Upload ---
uploaded_file = st.file_uploader(
    "Upload a policy report (PDF)",
    type="pdf",
    help="Text-based PDFs only. Scanned documents require OCR conversion first."
)

if uploaded_file:

    text, total_pages = extract_pdf_text(uploaded_file)
    validate_extracted_text(text)
    render_metadata(uploaded_file, total_pages, text)

    st.success("Text extracted successfully. Ready to analyze.")

    if st.button("Run Analysis"):
        with st.spinner("Analyzing document. This may take 15-30 seconds..."):

            framework_instruction = (
                f"Where relevant, explicitly cite specific articles or provisions of the **{framework}** framework that align with or are contradicted by the report's findings. Don't just state alignment — explain it with reference to specific obligations."
                if framework != "None"
                else ""
            )

            prompt = f"""
You are a senior policy analyst specializing in gender equality, human rights, and development governance in Sub-Saharan Africa.

A policy officer needs a structured analysis of the following report to inform a **{output_use}**.

{framework_instruction}

Provide your analysis in exactly these sections:

**1. EXECUTIVE SUMMARY**
3-5 sentences covering the report's purpose, scope, and primary argument.

**2. KEY THEMES**
List the 4-6 dominant thematic areas with a one-sentence explanation of each.

**3. POLICY RECOMMENDATIONS**
Extract or infer concrete, actionable recommendations. Present as numbered points.
Be specific — name specific legislation, institutions, or budget lines where possible.
Avoid vague language like "continue to implement" or "strengthen capacity" without specifying how.

**4. IMPLEMENTATION GAPS & RISKS**
Identify what the report flags as barriers, risks, or missing elements. Flag anything that would undermine implementation.

**5. FRAMEWORK ALIGNMENT**
Explicitly cite specific articles or provisions of relevant frameworks that align with or are contradicted by the report's findings.

**6. SUGGESTED NEXT STEPS**
Based on the analysis, suggest 2-3 concrete actions the policy officer should consider taking.

Report text:
{text[:MAX_CHARS]}
"""

            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a senior policy analyst specializing in gender equality, human rights, and development governance in Sub-Saharan Africa. Your outputs are used to inform government submissions and programme design. Be precise, structured, and avoid generic language."},
                        {"role": "user", "content": prompt}
                    ]
                )

                validate_api_response(response)
                analysis = response.choices[0].message.content

            except Exception as api_error:
                handle_api_error(api_error)

        render_results(analysis, uploaded_file)