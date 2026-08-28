import streamlit as st

from agents import (
    company_intelligence_agent,
    operations_signal_agent,
    leadership_agent,
    competitor_intelligence_agent,
    sales_strategy_agent,
    evidence_validation_agent,
    final_report_agent
)

st.set_page_config(
    page_title="TransactionOps AI",
    page_icon="🏠",
    layout="wide"
)

st.title("TransactionOps AI")
st.subheader("Real Estate & Mortgage Sales Intelligence Assistant")

st.write(
    "Research prospective real estate and mortgage companies "
    "and identify potential operational sales opportunities."
)

st.divider()

st.header("Product Information")

product_name = st.text_input(
    "Product Name",
    value="TransactionOps AI"
)

product_category = st.text_input(
    "Product Category",
    value="AI-Powered Real Estate & Mortgage Transaction Operations"
)

value_proposition = st.text_area(
    "Value Proposition",
    value=(
        "Help real estate and mortgage professionals spend less time "
        "managing transactions and more time generating business by using "
        "AI agents to coordinate administrative workflows, deadlines, "
        "documents, communication, and transaction milestones."
    )
)

st.divider()

st.header("Prospect Information")

company_name = st.text_input(
    "Prospect Company Name",
    placeholder="Example: Rocket Mortgage"
)

company_url = st.text_input(
    "Prospect Company URL",
    placeholder="https://www.example.com"
)

target_customer = st.text_input(
    "Target Customer / Decision Maker",
    placeholder="Example: VP of Mortgage Operations"
)

st.divider()

st.header("Competitor Information")

competitor_1 = st.text_input(
    "Competitor URL 1",
    placeholder="https://www.competitor1.com"
)

competitor_2 = st.text_input(
    "Competitor URL 2",
    placeholder="https://www.competitor2.com"
)

st.divider()

st.header("Optional Product Material")

product_document = st.file_uploader(
    "Upload Product Overview",
    type=["pdf", "docx", "txt"]
)

st.divider()

if st.button("Generate Sales Intelligence"):

    missing_fields = []

    if not product_name:
        missing_fields.append("Product Name")

    if not product_category:
        missing_fields.append("Product Category")

    if not value_proposition:
        missing_fields.append("Value Proposition")

    if not company_name:
        missing_fields.append("Prospect Company Name")

    if not company_url:
        missing_fields.append("Prospect Company URL")

    if not target_customer:
        missing_fields.append("Target Customer")

    if not competitor_1:
        missing_fields.append("At Least One Competitor URL")

    if missing_fields:
        st.error(
            "Please complete the following required fields: "
            + ", ".join(missing_fields)
        )

    else:
        st.success("Inputs validated successfully.")

        with st.spinner("Running Company Intelligence Agent..."):
            company_analysis = company_intelligence_agent(
                company_name=company_name,
                company_url=company_url,
                product_name=product_name,
                product_category=product_category,
                value_proposition=value_proposition
            )

        with st.spinner("Running Operations Signal Agent..."):
            operations_analysis = operations_signal_agent(
                company_name=company_name,
                company_url=company_url,
                product_name=product_name,
                value_proposition=value_proposition
            )

        with st.spinner("Running Leadership Agent..."):
            leadership_analysis = leadership_agent(
                company_name=company_name,
                company_url=company_url,
                target_customer=target_customer,
                product_name=product_name
            )

        with st.spinner("Running Competitor Intelligence Agent..."):
            competitor_analysis = competitor_intelligence_agent(
                company_name=company_name,
                company_url=company_url,
                competitor_1=competitor_1,
                competitor_2=competitor_2,
                product_name=product_name
            )

        with st.spinner("Synthesizing Sales Strategy..."):
            sales_strategy = sales_strategy_agent(
                company_name=company_name,
                target_customer=target_customer,
                product_name=product_name,
                value_proposition=value_proposition,
                company_analysis=company_analysis,
                operations_analysis=operations_analysis,
                leadership_analysis=leadership_analysis,
                competitor_analysis=competitor_analysis
            )

        with st.spinner("Validating Evidence and Claims..."):
            validation_analysis = evidence_validation_agent(
                company_name=company_name,
                company_analysis=company_analysis,
                operations_analysis=operations_analysis,
                leadership_analysis=leadership_analysis,
                competitor_analysis=competitor_analysis,
                sales_strategy=sales_strategy
            )

        with st.spinner("Generating Final One-Page Brief..."):
            final_report = final_report_agent(
                company_name=company_name,
                company_url=company_url,
                product_name=product_name,
                target_customer=target_customer,
                company_analysis=company_analysis,
                operations_analysis=operations_analysis,
                leadership_analysis=leadership_analysis,
                competitor_analysis=competitor_analysis,
                sales_strategy=sales_strategy,
                validation_analysis=validation_analysis
            )

        st.divider()

        st.header("Final One-Page Sales Intelligence Brief")
        st.markdown(final_report)

        st.download_button(
            label="Download Sales Brief",
            data=final_report,
            file_name=f"{company_name.replace(' ', '_')}_sales_brief.md",
            mime="text/markdown"
        )

        st.divider()

        with st.expander("View Detailed Agent Research"):

            st.subheader("Company Intelligence")
            st.write(company_analysis)

            st.subheader("Operations Signals")
            st.write(operations_analysis)

            st.subheader("Leadership Intelligence")
            st.write(leadership_analysis)

            st.subheader("Competitor Intelligence")
            st.write(competitor_analysis)

            st.subheader("Recommended Sales Strategy")
            st.write(sales_strategy)

            st.subheader("Evidence Validation")
            st.write(validation_analysis)

        if product_document:
            st.divider()
            st.write(
                f"Uploaded Product Document: {product_document.name}"
            )
