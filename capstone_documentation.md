# CAP 931 Capstone Documentation
## TransactionOps AI Sales Intelligence Assistant

### 1. Project Overview

TransactionOps AI Sales Intelligence Assistant is a multi-agent AI prototype designed to help sales representatives research prospective real estate brokerages, mortgage companies, and lending organizations.

The system analyzes public company information, operational and hiring signals, leadership, competitors, and strategic activity. It then synthesizes the findings into a concise one-page sales intelligence brief.

The product being sold is TransactionOps AI, an AI-powered real estate and mortgage transaction operations solution designed to reduce administrative workload and support transaction-related workflows.

---

### 2. Problem Statement

Real estate agents and mortgage loan officers manage significant administrative and operational responsibilities throughout the transaction lifecycle.

These responsibilities can include document coordination, deadlines, client communication, transaction milestones, loan-processing activities, and multiple handoffs between parties.

These activities can reduce the amount of time available for revenue-generating activities such as prospecting, relationship management, client engagement, and business development.

TransactionOps AI is designed as a potential solution to help streamline administrative workflows, deadlines, communication, document coordination, and transaction milestones.

The sales intelligence prototype helps a sales representative identify brokerages and mortgage companies that may be strong prospects for the product.

---

### 3. Project Objectives

The prototype was designed to:

1. Collect prospect and product information through a Streamlit interface.
2. Research a prospect using its website and public web information.
3. Analyze company strategy and operational signals.
4. Identify relevant leadership and decision-maker roles.
5. Analyze supplied competitors.
6. Generate a recommended sales strategy.
7. Validate claims and separate facts from inference.
8. Produce a concise one-page sales intelligence brief.
9. Allow optional product documents to influence the analysis.

---

### 4. Technical Stack

The application uses:

- Python
- Streamlit
- Gemini API
- google-genai
- python-dotenv
- requests
- BeautifulSoup
- DDGS public web search
- pypdf
- python-docx

Python was used as the primary programming language because of its strong compatibility with LLM tools and data-processing libraries.

Streamlit was selected because it provides a lightweight Python-based interface for collecting user inputs and displaying generated reports.

---

### 5. Application Architecture

User / Sales Representative
        ↓
Streamlit Interface
        ↓
Input Validation
        ↓
Website Retrieval + Public Web Search
        ↓
Company Intelligence Agent
Operations Signal Agent
Leadership Agent
Competitor Intelligence Agent
        ↓
Sales Strategy Agent
        ↓
Evidence Validation Agent
        ↓
Final Report Agent
        ↓
One-Page Sales Intelligence Brief

The application uses specialized agent functions instead of one large prompt. Each agent performs a focused task, and later agents receive outputs from earlier agents.

This creates a chained multi-agent workflow.

---

### 6. Agent Responsibilities

#### Company Intelligence Agent

Analyzes the prospect's company profile, business strategy, growth signals, website information, and potential product relevance.

#### Operations Signal Agent

Looks for real estate and mortgage-specific operational signals such as:

- Loan Officer hiring
- Loan Officer Assistant hiring
- Processor hiring
- Underwriter hiring
- Transaction Coordinator hiring
- Operations hiring
- Branch growth
- Recruiting
- Technology adoption
- Workflow complexity

#### Leadership Intelligence Agent

Identifies leadership roles most relevant to the purchasing decision and evaluates available public leadership information.

Priority roles may include:

- Chief Operating Officer
- SVP/VP of Operations
- VP of Mortgage Operations
- Director of Operations
- Head of Processing
- Regional Manager
- Branch Manager
- Broker/Owner
- Managing Broker

#### Competitor Intelligence Agent

Analyzes competitor websites and public information to identify:

- Competitive positioning
- Operational differences
- Technology signals
- Market differences
- Potential competitive sales opportunities

#### Sales Strategy Agent

Synthesizes the research produced by the previous agents and generates:

- Executive summary
- Product-fit reasoning
- Recommended sales angle
- Recommended decision maker
- Discovery questions
- Potential objections
- Recommended next action

#### Evidence Validation Agent

Reviews the generated research and separates:

- Verified facts
- Reasonable inferences
- Unsupported or weak claims

The agent also provides an overall confidence assessment.

#### Final Report Agent

Condenses the research into a concise one-page sales intelligence brief containing:

- Prospect overview
- Company strategy
- Operational signals
- Leadership
- Competitor landscape
- Product fit
- Recommended sales approach
- Discovery questions
- Supporting URLs

---

### 7. Input Handling

The Streamlit interface collects:

- Product Name
- Product Category
- Value Proposition
- Prospect Company Name
- Prospect Company URL
- Target Customer / Decision Maker
- Competitor URL 1
- Competitor URL 2
- Optional Product Document

The application validates required fields before running the agents.

The optional product document supports:

- PDF
- DOCX
- TXT

Uploaded product content is parsed and passed into the sales strategy and final report generation process.

---

### 8. Data Integration

The application uses multiple sources of information.

#### Prospect Website

The application retrieves readable text from the company URL supplied by the user.

#### Competitor Websites

Competitor URLs are retrieved and parsed to provide additional competitive context.

#### Public Web Search

Public web search is used to identify information such as:

- Recent company news
- Company strategy
- Hiring activity
- Operations positions
- Leadership information
- Competitor information

Search results include titles, URLs, and snippets.

#### Product Documents

Optional uploaded product materials are parsed and supplied as additional product context.

---

### 9. LLM Model Selection

The project was initially configured to use the OpenAI API.

During development, the OpenAI API returned an insufficient quota error that required paid API usage.

Because cost was an important project constraint, the application was changed to use Google's Gemini API.

Gemini Flash models were selected because they provide a useful balance of:

- Response speed
- Reasoning capability
- Cost
- Availability for prototype development

The application also implements model retry and fallback behavior so that temporary model overload does not immediately cause the entire application to fail.

---

### 10. Prompt Engineering and Experiments

Several prompt and architecture approaches were tested.

#### Experiment 1 — General Company Prompt

A single broad company-analysis prompt was initially used.

Result:
The response was useful but broad and did not provide enough specialization for real estate and mortgage sales.

#### Experiment 2 — Specialized Agents

The application was divided into specialized agents for company intelligence, operations, leadership, and competitors.

Result:
Outputs became more focused and easier to use for sales analysis.

#### Experiment 3 — Public Website Content

Prospect and competitor website text was added to the prompts.

Result:
Responses became more grounded in information associated with the supplied organizations.

#### Experiment 4 — Public Web Search

Search results for company strategy, hiring, leadership, and competitors were added.

Result:
The system gained greater access to recent business and operational signals.

#### Experiment 5 — Evidence Validation

An Evidence Validation Agent was added to classify facts, inference, and unsupported claims.

Result:
The final system became more conservative about unsupported statements.

#### Experiment 6 — Synthesis and Final Report

Separate Sales Strategy and Final Report agents were added.

Result:
The output became more concise and more useful as a one-page sales intelligence brief.

---

### 11. Challenges and Solutions

#### Challenge: OpenAI API Quota

The initial OpenAI API configuration returned an insufficient quota error.

Solution:
The project was migrated to Gemini while maintaining the same multi-agent architecture.

#### Challenge: Gemini API Authentication

An initial Gemini API credential was rejected.

Solution:
A new valid Gemini API key was created and securely stored in an environment variable.

#### Challenge: Gemini Model Availability

Gemini occasionally returned HTTP 503 errors because models were experiencing high demand.

Solution:
Retry and model fallback logic was added.

#### Challenge: LLM Hallucination Risk

LLMs may generate unsupported assumptions when researching businesses.

Solution:
Prompts instruct agents not to invent facts, public URLs are retained, and an Evidence Validation Agent reviews claims before the final report is produced.

#### Challenge: URLs Are Not Automatically Research

Simply providing a company URL to an LLM does not guarantee that the page is actually read.

Solution:
The application retrieves website content directly using Python before passing that content to the agents.

#### Challenge: Broader Research

A company homepage alone may not reveal hiring, leadership, or recent strategic activity.

Solution:
A public web-search layer was added for company news, hiring activity, leadership, and competitor research.

---

### 12. Optional Enhancement

#### Prospect Monitoring Alert System

A future enhancement would allow users to save selected prospects and monitor them for meaningful business changes.

The system could periodically search for:

- New job postings
- Leadership changes
- Branch openings
- Geographic expansion
- Acquisitions or mergers
- Technology announcements
- Automation initiatives
- Operations-related announcements

When meaningful changes are detected, the system could alert the sales representative and regenerate the prospect's sales intelligence brief.

---

### 13. Production Deployment Plan

The current prototype runs locally using Streamlit.

A production version could be deployed through a cloud platform such as:

- Streamlit Community Cloud
- Google Cloud
- AWS
- Microsoft Azure

The frontend, research functions, AI processing layer, and persistent storage could be separated so that the components can scale independently.

#### Scalability

As usage increases:

- LLM requests could be processed asynchronously.
- Frequently researched prospect information could be cached.
- Stored research could reduce repeated API calls.
- Background jobs could perform prospect monitoring.
- A database could store prior reports and account history.

#### Security

API credentials should never be hard-coded into source code.

The current prototype uses environment variables for the Gemini API key.

A production system should also use:

- User authentication
- Role-based access controls
- Managed secret storage
- Encryption in transit
- Encryption at rest
- Secure logging
- File-retention policies

The current prototype primarily analyzes public company information.

A future transaction-management product that processes borrower or private mortgage information would require additional security, privacy, and regulatory controls.

#### Maintenance and Reliability

A production system should monitor:

- API failures
- Model availability
- Website retrieval errors
- Search failures
- Application performance
- Usage volume

The prototype already includes retry and fallback logic.

Production versions could also include:

- Structured logging
- Automated error alerts
- Prompt version control
- Model-version testing
- Usage monitoring

---

### 14. Data Quality and Responsible AI

Public web information can be incomplete, outdated, or ambiguous.

The application therefore uses several safeguards:

- Prompts prohibit fabricated facts.
- Agents distinguish facts from inference.
- Research URLs are retained.
- The Evidence Validation Agent reviews claims.
- Unsupported statements are removed or softened before the final report.

The system is designed to support human sales research rather than replace human judgment.

---

### 15. Time Management

Approximate project time allocation:

| Task | Approximate Time |
|---|---|
| Project concept and architecture | 1 hour |
| Environment and Streamlit setup | 1 hour |
| LLM/API configuration and troubleshooting | 2 hours |
| Multi-agent development | 3 hours |
| Website and public research integration | 2 hours |
| Evidence validation and final report | 1.5 hours |
| Product document parsing | 1 hour |
| Testing and debugging | 2 hours |
| Documentation and final review | 2 hours |

Actual development time varied because API authentication, model availability, and application debugging required additional troubleshooting.

---

### 16. System Output

The primary deliverable generated by the application is a one-page Sales Intelligence Brief.

The report contains:

- Prospect Overview
- Company Strategy & Operational Signals
- Leadership & Recommended Decision Maker
- Competitive Landscape
- Product Fit
- Recommended Sales Approach
- Three Discovery Questions
- Supporting Sources

Detailed outputs from each individual agent remain available through the Streamlit interface for users who want deeper research.

---

### 17. Future Development

Future versions could include:

- Prospect monitoring alerts
- CRM integrations
- Email alerts
- Saved prospect accounts
- Historical account research
- User authentication
- Team collaboration
- PDF report generation
- Automated presentation/deck generation
- Additional real estate verticals
- Transaction lifecycle support

A broader TransactionOps AI platform could ultimately support real estate agents and mortgage professionals with administrative workflows across the transaction lifecycle.

---

### 18. Conclusion

TransactionOps AI demonstrates how multiple specialized LLM agents can be combined with public web research, website retrieval, document parsing, validation, and synthesis to create a focused B2B sales intelligence application.

The project also demonstrates how an AI system can be specialized for the real estate and mortgage industries rather than functioning as a general-purpose chatbot.

The final prototype produces a practical sales intelligence brief while maintaining a distinction between verified evidence, inference, and unsupported claims.
