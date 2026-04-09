# Gender & Development Policy Analyzer

An AI-powered tool that extracts structured policy insights from PDF reports —
built for gender and development policy officers at government ministries and NGOs.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![LLaMA](https://img.shields.io/badge/LLaMA_3.3-70b-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## The Problem

Policy officers working on gender equality, human rights, and development
programmes regularly process lengthy reports — CEDAW periodic reviews, SDG
progress reports, ministerial briefs — often under time pressure. Extracting
actionable insights, identifying implementation gaps, and mapping findings to
specific policy frameworks manually is slow and inconsistent.

## The Solution

This tool allows a policy officer to upload any text-based PDF report and receive
a structured analysis in under 30 seconds, including:

- Executive summary
- Key thematic areas
- Concrete policy recommendations
- Implementation gaps and risks
- Framework alignment (CEDAW, SDGs, AU Agenda 2063, Kenya Sexual Offences Act)
- Suggested next steps

## Live Demo

🔗 [Launch App} {🔗 [Launch App](https://aipolicyanalyzer-53oflnrydwap5do4vf8zgt.streamlit.app/)}

## Technical Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | LLaMA 3.3-70b-versatile via Groq API |
| PDF Processing | pdfplumber |
| Language | Python 3.13 |
| Architecture | 3-file separation of concerns |

## Project Structure
ai_policy_analyzer/
├── app.py            # Application flow and LLM integration
├── ui.py             # All styling and layout rendering
├── error_handler.py  # PDF validation and API error handling
├── requirements.txt  # Dependencies
└── .env.example      # Environment variable template

## Key Design Decisions

**Domain-specific prompting**
The system prompt is calibrated for Sub-Saharan African policy context, not
generic document summarization. Framework alignment cites specific CEDAW articles
(e.g. Articles 2, 10, 11) rather than stating vague general alignment.

**Separation of concerns**
UI rendering, error handling, and application logic are split across three files.
Each layer is independently readable and maintainable.

**User-controlled context**
The sidebar lets users set the policy framework and output purpose before
analysis, dynamically adjusting the prompt. A ministerial submission gets a
different analysis depth than a general policy brief.

**Graceful error handling**
Scanned PDFs, corrupted files, API rate limits, and empty responses are each
handled with specific user guidance rather than raw Python tracebacks.

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/ai-policy-analyzer.git
cd ai-policy-analyzer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your environment variables**
```bash
cp .env.example .env
```
Open `.env` and add your Groq API key:

Get a free key at: https://console.groq.com

**4. Run the app**
```bash
streamlit run app.py
```

## How to Use

1. Select a **policy framework** from the sidebar — e.g. CEDAW, SDGs
2. Select your **output purpose** — e.g. Ministerial submission
3. Upload a text-based PDF policy report
4. Click **Run Analysis**
5. Review the structured output and download as `.txt`

## Current Limitations

- Analyzes the first 6,000 characters of a document. For large reports,
  upload a specific chapter or section for best results.
- Requires text-based PDFs. Scanned documents need OCR conversion first
  — try smallpdf.com or Adobe Acrobat.

## Author

Moses Mbuba — BA Gender and Development Studies, Software Engineering Certificate (ALX Africa)
Building at the intersection of AI and development policy in Sub-Saharan Africa.

📧 mosesmbuba3@gmail.com | 🔗 www.linkedin.com/in/moses-mbuba-072261373

---

*Built as a portfolio project targeting the Dalberg DDI AI Engineering Fellowship,
August 2026 cohort.*
