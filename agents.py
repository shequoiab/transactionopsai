from google import genai
from google.genai import errors
from dotenv import load_dotenv
from web_utils import (
    fetch_website_text,
    search_public_web,
    format_search_results
)
import os
import time

load_dotenv(override=True)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_with_fallback(prompt):
    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-3.1-flash-lite"
    ]

    last_error = None

    for model in models:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                return response.text

            except errors.ServerError as e:
                last_error = e

                if attempt < 2:
                    time.sleep(2 ** attempt)

            except Exception as e:
                last_error = e
                break

    return (
        "The AI service is temporarily unavailable after multiple retries. "
        f"Last error: {last_error}"
    )


def company_intelligence_agent(
    company_name,
    company_url,
    product_name,
    product_category,
    value_proposition
):
    company_web_text = fetch_website_text(company_url)

    company_search = search_public_web(
        f"{company_name} recent news strategy growth expansion"
    )

    company_search_text = format_search_results(
        company_search
    )

    prompt = f"""
    You are the Company Intelligence Agent for a B2B sales intelligence system.

    Prospect Company:
    {company_name}

    Prospect Website:
    {company_url}

    Public Website Content:
    {company_web_text}

    Recent Public Web Research:
    {company_search_text}

    Product Being Sold:
    {product_name}

    Product Category:
    {product_category}

    Value Proposition:
    {value_proposition}

    Return:

    1. Company Overview
    2. Business Strategy
    3. Operational Relevance
    4. Potential Product Fit

    Rules:
    - Use the supplied website and public research when available.
    - Do not invent facts.
    - Clearly label inferences.
    - If reliable information is unavailable, say so.
    - When using public research, include the supporting URL.
    - Do not cite a source for a claim that the source does not support.
    """

    return generate_with_fallback(prompt)


def operations_signal_agent(
    company_name,
    company_url,
    product_name,
    value_proposition
):
    company_web_text = fetch_website_text(company_url)

    operations_search = search_public_web(
        f"{company_name} jobs hiring loan officer processor "
        f"operations transaction coordinator"
    )

    operations_search_text = format_search_results(
        operations_search
    )

    prompt = f"""
    You are the Operations Signal Agent for a B2B sales intelligence system
    focused on residential real estate and mortgage companies.

    Prospect Company:
    {company_name}

    Prospect Website:
    {company_url}

    Public Website Content:
    {company_web_text}

    Public Hiring and Operations Research:
    {operations_search_text}

    Product:
    {product_name}

    Value Proposition:
    {value_proposition}

    Analyze:

    1. Hiring Signals
    2. Growth Signals
    3. Operational Complexity
    4. Technology Signals
    5. Sales Implication

    Relevant roles include:
    - Loan Officers
    - Loan Officer Assistants
    - Mortgage Processors
    - Underwriters
    - Closers
    - Transaction Coordinators
    - Operations Managers
    - Branch Managers

    Rules:
    - Use the supplied website and public research when available.
    - Do not invent specific facts.
    - Clearly distinguish verified facts from inference.
    - Do not claim the prospect has a problem without evidence.
    - When using public research, include the supporting URL.
    - Do not cite a source for a claim that the source does not support.
    """

    return generate_with_fallback(prompt)


def leadership_agent(
    company_name,
    company_url,
    target_customer,
    product_name
):
    company_web_text = fetch_website_text(company_url)

    leadership_search = search_public_web(
        f"{company_name} leadership COO operations executive"
    )

    leadership_search_text = format_search_results(
        leadership_search
    )

    prompt = f"""
    You are the Leadership Intelligence Agent for a B2B sales intelligence system.

    Prospect Company:
    {company_name}

    Prospect Website:
    {company_url}

    Public Website Content:
    {company_web_text}

    Public Leadership Research:
    {leadership_search_text}

    Target Customer:
    {target_customer}

    Product:
    {product_name}

    Return:

    1. Most Relevant Decision-Maker Roles
    2. Leadership Relevance
    3. Public Leadership Signals
    4. Recommended Entry Point

    Prioritize roles such as:
    - Chief Operating Officer
    - SVP or VP of Operations
    - VP of Mortgage Operations
    - Director of Operations
    - Head of Processing
    - Regional Manager
    - Branch Manager
    - Broker/Owner
    - Managing Broker
    - Transaction Manager

    Rules:
    - Use supplied website and public research when available.
    - Do not invent executive names.
    - Clearly distinguish known information from inference.
    - When using public research, include the supporting URL.
    - Do not cite a source for a claim that the source does not support.
    """

    return generate_with_fallback(prompt)


def competitor_intelligence_agent(
    company_name,
    company_url,
    competitor_1,
    competitor_2,
    product_name
):
    company_web_text = fetch_website_text(company_url)
    competitor_1_text = fetch_website_text(competitor_1)
    competitor_2_text = fetch_website_text(competitor_2)

    competitor_search = search_public_web(
        f"{company_name} competitors mortgage technology operations"
    )

    competitor_search_text = format_search_results(
        competitor_search
    )

    prompt = f"""
    You are the Competitor Intelligence Agent for a B2B sales intelligence
    system focused on the real estate and mortgage industries.

    Prospect Company:
    {company_name}

    Prospect Website:
    {company_url}

    Prospect Website Content:
    {company_web_text}

    Competitor 1:
    {competitor_1}

    Competitor 1 Website Content:
    {competitor_1_text}

    Competitor 2:
    {competitor_2}

    Competitor 2 Website Content:
    {competitor_2_text}

    Additional Public Competitor Research:
    {competitor_search_text}

    Product:
    {product_name}

    Return:

    1. Competitor Overview
    2. Competitive Positioning
    3. Operational Comparison
    4. Sales Opportunity
    5. Recommended Competitive Talking Point

    Rules:
    - Use supplied website and public research when available.
    - Do not invent competitor facts.
    - Clearly distinguish verified information from inference.
    - Do not make unsupported claims about technology usage.
    - When using public research, include the supporting URL.
    - Do not cite a source for a claim that the source does not support.
    """

    return generate_with_fallback(prompt)


def sales_strategy_agent(
    company_name,
    target_customer,
    product_name,
    value_proposition,
    company_analysis,
    operations_analysis,
    leadership_analysis,
    competitor_analysis
):
    prompt = f"""
    You are the Sales Strategy and Synthesis Agent for a B2B sales intelligence
    system focused on real estate and mortgage companies.

    Prospect:
    {company_name}

    Target Customer:
    {target_customer}

    Product:
    {product_name}

    Value Proposition:
    {value_proposition}

    Company Intelligence:
    {company_analysis}

    Operations Intelligence:
    {operations_analysis}

    Leadership Intelligence:
    {leadership_analysis}

    Competitor Intelligence:
    {competitor_analysis}

    Return:

    1. Executive Summary
    2. Why This Prospect May Be a Fit
    3. Recommended Sales Angle
    4. Recommended Decision Maker
    5. Three Discovery Questions
    6. Two Potential Objections and Responses
    7. Recommended Next Step

    Rules:
    - Base the strategy only on the supplied agent outputs.
    - Do not invent facts.
    - Clearly distinguish inference from verified information.
    - Keep the output concise enough for a one-page sales brief.
    """

    return generate_with_fallback(prompt)


def evidence_validation_agent(
    company_name,
    company_analysis,
    operations_analysis,
    leadership_analysis,
    competitor_analysis,
    sales_strategy
):
    prompt = f"""
    You are the Evidence Validation Agent for a B2B sales intelligence system.

    Prospect Company:
    {company_name}

    Company Intelligence:
    {company_analysis}

    Operations Intelligence:
    {operations_analysis}

    Leadership Intelligence:
    {leadership_analysis}

    Competitor Intelligence:
    {competitor_analysis}

    Sales Strategy:
    {sales_strategy}

    Review all supplied findings and classify them into three categories.

    1. Verified Facts
    List claims that appear to be supported by a supplied public source,
    company website, press release, job posting, leadership source, or
    competitor source.

    For each verified fact include:
    - Claim
    - Supporting source or URL when available

    2. Reasonable Inferences
    List conclusions that may logically follow from the evidence but are
    not directly confirmed facts.

    Clearly label each item as an inference.

    3. Unsupported or Weak Claims
    Identify statements that do not appear adequately supported by the
    supplied evidence.

    Explain briefly why each should be removed, softened, or researched
    further.

    4. Confidence Assessment
    Provide an overall confidence rating:
    - High
    - Moderate
    - Low

    Explain the rating in 2 to 3 sentences.

    Important rules:
    - Do not create new facts.
    - Do not invent citations.
    - Only treat something as verified when evidence is actually present.
    - If a source does not clearly support a claim, classify it as inference
      or unsupported.
    - Be conservative.
    """

    return generate_with_fallback(prompt)


def final_report_agent(
    company_name,
    company_url,
    product_name,
    target_customer,
    company_analysis,
    operations_analysis,
    leadership_analysis,
    competitor_analysis,
    sales_strategy,
    validation_analysis
):
    prompt = f"""
    You are the Final Report Agent for a B2B sales intelligence system.

    Create a concise ONE-PAGE sales intelligence brief.

    Prospect Company:
    {company_name}

    Prospect Website:
    {company_url}

    Product Being Sold:
    {product_name}

    Target Customer:
    {target_customer}

    Company Intelligence:
    {company_analysis}

    Operations Intelligence:
    {operations_analysis}

    Leadership Intelligence:
    {leadership_analysis}

    Competitor Intelligence:
    {competitor_analysis}

    Sales Strategy:
    {sales_strategy}

    Evidence Validation:
    {validation_analysis}

    Create the final report using exactly these sections:

    # {company_name} - Sales Intelligence Brief

    ## Prospect Overview
    Provide a short 2 to 3 sentence company summary.

    ## Company Strategy & Operational Signals
    Summarize the strongest verified strategy, growth, hiring,
    technology, or operational signals.

    ## Leadership & Recommended Decision Maker
    Identify relevant leadership and the recommended role to approach.

    ## Competitive Landscape
    Summarize the most relevant competitor findings.

    ## Product Fit
    Explain why {product_name} may or may not fit this prospect.

    ## Recommended Sales Approach
    Give a concise recommended sales angle and next step.

    ## Key Discovery Questions
    Provide exactly 3 questions.

    ## Sources
    Include only URLs that appeared in the supplied research.
    Do not invent URLs.

    Important rules:
    - Keep the report concise enough to reasonably fit on one page.
    - Prioritize verified information over speculation.
    - Clearly label material inferences.
    - Remove claims identified as unsupported by the validation agent.
    - Do not invent names, statistics, sources, or facts.
    - Do not repeat the same information across sections.
    """

    return generate_with_fallback(prompt)
