# TransactionOps AI Sales Intelligence Assistant

TransactionOps AI is a multi-agent AI sales intelligence prototype designed for the real estate and mortgage industries.

The application helps a sales representative research prospective brokerages, mortgage companies, and lending organizations using public company information, website content, leadership research, competitor analysis, operational signals, and optional product documents.

The system then generates a concise one-page sales intelligence brief.

## Project Use Case

The product being sold is TransactionOps AI, an AI-powered real estate and mortgage transaction operations solution intended to reduce administrative workload and support transaction-related workflows.

## Key Features

- Streamlit user interface
- Prospect website retrieval
- Public web research
- Competitor analysis
- Leadership research
- Operations and hiring signal analysis
- Multi-agent LLM workflow
- Evidence validation
- One-page sales intelligence brief
- Downloadable report
- PDF, DOCX, and TXT product document parsing
- Gemini model retry and fallback logic

## Multi-Agent Workflow

User Input
↓
Streamlit Interface
↓
Website Retrieval + Public Web Search
↓
Company Intelligence Agent
↓
Operations Signal Agent
↓
Leadership Agent
↓
Competitor Intelligence Agent
↓
Sales Strategy Agent
↓
Evidence Validation Agent
↓
Final Report Agent
↓
One-Page Sales Intelligence Brief

## Project Files

- app.py — Streamlit interface and application orchestration
- agents.py — Gemini agents, prompts, chaining, retry, and fallback logic
- web_utils.py — website retrieval and public web search
- document_utils.py — PDF, DOCX, and TXT parsing
- requirements.txt — Python dependencies
- capstone_documentation.md — project documentation
- .gitignore — excludes local secrets and environment files

## Technology Stack

- Python
- Streamlit
- Google Gemini API
- google-genai
- python-dotenv
- requests
- BeautifulSoup
- DDGS
- pypdf
- python-docx

## Setup Instructions

Clone the repository:

git clone https://github.com/shequoiab/transactionopsai.git

Enter the project folder:

cd transactionopsai

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a local .env file containing:

GEMINI_API_KEY=your_api_key_here

Do not commit the .env file.

Run the application:

streamlit run app.py

Then open:

http://localhost:8501

## Sample Prospect

The final capstone example uses eXp Realty as the prospective account.

Relevant competitor examples include:

- Real Brokerage
- Keller Williams

The generated brief includes:

- Prospect Overview
- Company Strategy and Operational Signals
- Leadership and Recommended Decision Maker
- Competitive Landscape
- Product Fit
- Recommended Sales Approach
- Discovery Questions
- Supporting Sources

## Responsible AI and Data Quality

The system reduces unsupported claims by grounding prompts in retrieved content, retaining public source URLs, distinguishing facts from inference, and using an Evidence Validation Agent.

## Future Enhancements

Potential improvements include saved prospect monitoring, alerts, CRM integration, authentication, persistent account history, database storage, PDF report generation, scheduled monitoring, and team collaboration.