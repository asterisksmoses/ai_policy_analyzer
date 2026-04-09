import streamlit as st

MIN_TEXT_LENGTH = 100
MAX_CHARS = 6000


def check_api_key(api_key):
    """Check if the API key exists on startup."""
    if not api_key:
        st.error("GROQ_API_KEY not found. Please check your .env file.")
        st.stop()


def extract_pdf_text(uploaded_file):
    """
    Safely extract text from an uploaded PDF.
    Returns (text, total_pages) or stops the app on critical failure.
    """
    import pdfplumber

    text = ""
    total_pages = 0

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            total_pages = len(pdf.pages)
            for i, page in enumerate(pdf.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
                except Exception:
                    st.warning(f"Could not extract text from page {i + 1}. Skipping.")
                    continue

    except Exception:
        st.error("Failed to open PDF. The file may be corrupted, password-protected, or in an unsupported format.")
        st.info("Try saving the document as a new PDF and re-uploading.")
        st.stop()

    return text, total_pages


def validate_extracted_text(text):
    """
    Validate the quality and size of extracted text.
    Returns True if text is usable, False otherwise.
    """
    if not text.strip():
        st.error("No text could be extracted from this PDF.")
        st.warning("This document appears to be scanned or image-based.")
        st.info("**Suggested fix:** Use an OCR tool such as smallpdf.com to convert it to a searchable PDF, then re-upload.")
        st.stop()

    if len(text.strip()) < MIN_TEXT_LENGTH:
        st.warning("Very little text was extracted. Analysis quality may be poor.")
        return False

    if len(text) > MAX_CHARS:
        st.warning(f"Large document detected ({len(text):,} characters). Only the first {MAX_CHARS:,} characters will be analyzed. For best results, upload a specific chapter or section.")

    return True


def handle_api_error(error):
    """
    Categorize and display a user-friendly API error message.
    """
    error_message = str(error)

    if "rate_limit" in error_message.lower() or "429" in error_message:
        st.error("Rate limit reached. Please wait 60 seconds and try again.")
    elif "timeout" in error_message.lower():
        st.error("The request timed out. Please try again — this is usually temporary.")
    elif "api_key" in error_message.lower() or "401" in error_message:
        st.error("Invalid API key. Please check your GROQ_API_KEY in your .env file.")
    else:
        st.error(f"An unexpected error occurred: {error_message}")

    st.stop()


def validate_api_response(response):
    """
    Check that the API returned a usable response.
    """
    if not response.choices or not response.choices[0].message.content.strip():
        st.error("The AI returned an empty response. Please try again.")
        st.stop()