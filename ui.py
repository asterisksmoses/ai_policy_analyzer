import streamlit as st


def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;700&family=DM+Sans:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* --- Header --- */
    .analyzer-badge {
        display: inline-block;
        font-size: 11px;
        font-weight: 500;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background-color: #E6F1FB;
        color: #185FA5;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 10px;
    }

    .analyzer-title {
        font-family: 'Syne', sans-serif;
        font-size: 32px;
        font-weight: 700;
        line-height: 1.15;
        margin-bottom: 8px;
    }

    .analyzer-title span {
        color: #185FA5;
    }

    .analyzer-subtitle {
        font-size: 14px;
        color: #6B7280;
        line-height: 1.6;
        margin-bottom: 2rem;
        max-width: 560px;
    }

    /* --- Sidebar --- */
    .sidebar-tip {
        background-color: #E6F1FB;
        border-radius: 8px;
        padding: 10px 12px;
        font-size: 12px;
        color: #185FA5;
        line-height: 1.5;
        margin-top: 1rem;
    }

    /* --- Upload Zone --- */
    [data-testid="stFileUploader"] {
        border: 1.5px dashed rgba(255,255,255,0.2);
        border-radius: 12px;
        padding: 1rem;
        background-color: rgba(255,255,255,0.05);
    }

    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] p,
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] div {
        color: inherit !important;
    }

    [data-testid="stMetric"] {
        background-color: rgba(255,255,255,0.08);
        border: 0.5px solid rgba(255,255,255,0.12);
        border-radius: 8px;
        padding: 12px 16px;
    }

    [data-testid="stMetricLabel"] > div {
        font-size: 10px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: rgba(255,255,255,0.5) !important;
    }

    [data-testid="stMetricValue"] > div {
        font-family: 'Syne', sans-serif !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        color: rgba(255,255,255,0.9) !important;
    }

    /* --- Run Button --- */
    [data-testid="stButton"] > button {
        width: 100%;
        background-color: #0F172A;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-family: 'Syne', sans-serif;
        font-size: 14px;
        font-weight: 500;
        letter-spacing: 0.02em;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }

    [data-testid="stButton"] > button:hover {
        background-color: #1E293B;
    }

    /* --- Result Sections --- */
    .result-section {
        border: 0.5px solid rgba(255,255,255,0.12);
        border-radius: 12px;
        margin-bottom: 12px;
        overflow: hidden;
    }

    .result-section-header {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 16px;
        background-color: rgba(255,255,255,0.05);
        border-bottom: 0.5px solid rgba(255,255,255,0.12);
    }

    .section-num {
        font-size: 10px;
        font-weight: 500;
        color: #185FA5;
        background-color: #E6F1FB;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .section-name {
        font-size: 11px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #6B7280;
    }

    .result-section-body {
        padding: 14px 16px;
        font-size: 14px;
        color: inherit;
        line-height: 1.75;
    }

    /* --- Download Button --- */
    [data-testid="stDownloadButton"] > button {
        background-color: white;
        color: #374151;
        border: 0.5px solid #D1D5DB;
        border-radius: 8px;
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        padding: 6px 16px;
    }

    [data-testid="stDownloadButton"] > button:hover {
        background-color: #F9FAFB;
    }

    /* --- Divider --- */
    hr {
        border: none;
        border-top: 0.5px solid #E5E7EB;
        margin: 1.5rem 0;
    }

    /* --- Version tag --- */
    .version-tag {
        font-size: 11px;
        color: #9CA3AF;
        font-family: 'DM Sans', monospace;
        text-align: right;
        margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    st.markdown("""
        <div class="version-tag">v1.0 · Powered by LLaMA 3.3-70b</div>
        <div class="analyzer-badge">Policy Intelligence Tool</div>
        <div class="analyzer-title">Gender & Development<br><span>Policy Analyzer</span></div>
        <div class="analyzer-subtitle">
            Extract structured insights from reports — ready for briefs, 
            submissions, and programme design.
        </div>
    """, unsafe_allow_html=True)


def render_sidebar():
    st.sidebar.markdown("### Analysis Context")

    framework = st.sidebar.selectbox(
        "Policy Framework",
        ["None", "CEDAW", "Kenya National Policy on Gender",
         "SDGs", "AU Agenda 2063", "Kenya Sexual Offences Act"]
    )

    output_use = st.sidebar.selectbox(
        "Output Purpose",
        ["General policy brief", "Ministerial submission",
         "Programme design", "Stakeholder report"]
    )

    st.sidebar.markdown("""
        <div class="sidebar-tip">
            Select a framework before running analysis for article-level alignment mapping.
        </div>
    """, unsafe_allow_html=True)

    return framework, output_use


def render_metadata(uploaded_file, total_pages, text):
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Document", uploaded_file.name)
    col2.metric("Pages", total_pages)
    col3.metric("Characters Extracted", f"{len(text):,}")


def render_results(analysis, uploaded_file):
    st.markdown("<hr>", unsafe_allow_html=True)

    results_col, download_col = st.columns([4, 1])
    with results_col:
        st.markdown("#### Analysis Results")
    with download_col:
        st.download_button(
            label="Download .txt",
            data=analysis,
            file_name=f"analysis_{uploaded_file.name.replace('.pdf', '')}.txt",
            mime="text/plain"
        )

    sections = [
        "EXECUTIVE SUMMARY",
        "KEY THEMES",
        "POLICY RECOMMENDATIONS",
        "IMPLEMENTATION GAPS & RISKS",
        "FRAMEWORK ALIGNMENT",
        "SUGGESTED NEXT STEPS"
    ]

    section_map = {
        "1. EXECUTIVE SUMMARY": ("1", "Executive Summary"),
        "2. KEY THEMES": ("2", "Key Themes"),
        "3. POLICY RECOMMENDATIONS": ("3", "Policy Recommendations"),
        "4. IMPLEMENTATION GAPS & RISKS": ("4", "Implementation Gaps & Risks"),
        "5. FRAMEWORK ALIGNMENT": ("5", "Framework Alignment"),
        "6. SUGGESTED NEXT STEPS": ("6", "Suggested Next Steps"),
    }

    # Split analysis into sections and render each as a card
    import re
    parts = re.split(r'(\*\*\d+\.\s+[A-Z &]+\*\*)', analysis)

    if len(parts) <= 1:
        # Fallback: render as plain markdown if parsing fails
        st.markdown(analysis)
        return

    current_header = None
    current_body = []

    for part in parts:
        clean = part.strip().replace("**", "")
        if clean in section_map:
            if current_header and current_body:
                _render_section_card(current_header, " ".join(current_body))
            num, name = section_map[clean]
            current_header = (num, name)
            current_body = []
        else:
            if part.strip():
                current_body.append(part.strip())

    if current_header and current_body:
        _render_section_card(current_header, " ".join(current_body))


def _render_section_card(header, body):
    num, name = header
    body_html = body.replace("\n", "<br>")
    st.markdown(f"""
        <div class="result-section">
            <div class="result-section-header">
                <div class="section-num">{num}</div>
                <div class="section-name">{name}</div>
            </div>
            <div class="result-section-body">{body_html}</div>
        </div>
    """, unsafe_allow_html=True)