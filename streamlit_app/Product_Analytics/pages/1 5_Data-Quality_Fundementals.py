import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Data Governance Essentials", page_icon="🛡️", layout="wide")

    st.title("Data Governance Essentials: Quality, Legacy, and Compliance")
    st.write("An introduction to key concepts in data governance.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Data governance is a comprehensive framework for managing data throughout its lifecycle. It encompasses policies, processes, and standards to ensure data quality, security, and compliance.  This introduction covers three critical aspects: data quality, data legacy management, and compliance frameworks.

        ### 1. Data Quality

        *   **Definition:** The degree to which data is accurate, complete, consistent, timely, valid, and unique.  High-quality data is "fit for purpose."
        *   **Dimensions of Data Quality:**
            *   **Accuracy:**  Reflects the real world correctly.
            *   **Completeness:**  All required data is present.
            *   **Consistency:**  Data is uniform across different systems and datasets.
            *   **Timeliness:**  Data is available when needed.
            *   **Validity:**  Data conforms to defined rules and constraints.
            *   **Uniqueness:**  No duplicate records.
        *   **Importance:**  Poor data quality leads to inaccurate insights, flawed decision-making, operational inefficiencies, and compliance risks.
        *   **Data Quality Management:**  Involves processes for profiling, cleansing, validating, and monitoring data quality.

        ### 2. Data Legacy Management

        *   **Definition:**  The process of managing older, often outdated data systems and the data they contain.  Legacy systems may be difficult to integrate with newer systems.
        *   **Challenges:**
            *   **Data Silos:**  Data isolated in legacy systems, hindering access and analysis.
            *   **Data Format Incompatibilities:**  Older data formats may not be supported by modern tools.
            *   **Lack of Documentation:**  Understanding the meaning and structure of legacy data can be difficult.
            *   **Security Risks:**  Legacy systems may have vulnerabilities.
        *   **Strategies:**
            *   **Data Migration:**  Moving data from legacy systems to modern systems.
            *   **Data Integration:**  Connecting legacy systems to newer systems using APIs or middleware.
            *   **Data Archiving:**  Storing legacy data in a secure, accessible format for long-term retention.
            *   **System Modernization:**  Replacing or upgrading legacy systems.

        ### 3. Compliance Frameworks

        *   **Definition:**  Sets of regulations and guidelines that organizations must follow to protect data and ensure privacy.
        *   **Examples:**
            *   **GDPR (General Data Protection Regulation):**  EU regulation on data protection and privacy.
            *   **CCPA (California Consumer Privacy Act):**  California law granting consumers rights over their personal data.
            *   **HIPAA (Health Insurance Portability and Accountability Act):**  US law protecting sensitive patient health information.
            *   **SOX (Sarbanes-Oxley Act):**  US law regulating financial reporting and corporate governance.
            *   **PCI DSS (Payment Card Industry Data Security Standard):**  Security standards for organizations that handle credit card data.
        *   **Importance:**  Non-compliance can lead to significant fines, legal penalties, and reputational damage.
        *   **Data Governance Role:**  Data governance programs help organizations meet compliance requirements by establishing data policies, controls, and monitoring mechanisms.

        **Further Reading:**
            *   [Data Quality (Wikipedia)](https://en.wikipedia.org/wiki/Data_quality)
            *   [Legacy System (Wikipedia)](https://en.wikipedia.org/wiki/Legacy_system)
            *   [GDPR (Official Website)](https://gdpr-info.eu/)
            *   [CCPA (Official Website)](https://oag.ca.gov/privacy/ccpa)
        """)

    st.header("🔍 Interactive Overview")

    topic = st.selectbox("Select a Topic:", ["Data Quality", "Data Legacy Management", "Compliance Frameworks"])

    if topic == "Data Quality":
        st.subheader("Data Quality Dimensions")
        dimension = st.selectbox("Select a Dimension:", ["Accuracy", "Completeness", "Consistency", "Timeliness", "Validity", "Uniqueness"])

        if dimension == "Accuracy":
            st.markdown("""
                **Accuracy:**  The degree to which data correctly reflects the real-world objects or events it represents.

                **Example:**  A customer's address in a database should match their actual physical address.

                **Challenges:**  Data entry errors, outdated information, system integration issues.
                """)
            with st.expander("Interactive Example"):
                # Simulate an accuracy issue
                correct_address = "123 Main St, Anytown, USA"
                entered_address = st.text_input("Enter Customer Address:", "123 Mane St, Anytown, USA")
                if entered_address != correct_address:
                    st.error(f"Accuracy Issue: The entered address '{entered_address}' does not match the correct address '{correct_address}'.")
                else:
                    st.success("Accuracy Check: The entered address is accurate.")


        elif dimension == "Completeness":
            st.markdown("""
                **Completeness:**  The extent to which all required data is present.

                **Example:**  A customer record should have values for all mandatory fields (e.g., name, email, phone number).

                **Challenges:**  Missing data due to user input errors, system failures, or incomplete data migration.
                """)
            with st.expander("Interactive Example"):
                name = st.text_input("Name:")
                email = st.text_input("Email:")
                phone = st.text_input("Phone:")

                if not all([name, email, phone]):
                    st.error("Completeness Issue:  Missing required fields.  Name, email, and phone are mandatory.")
                else:
                    st.success("Completeness Check: All required fields are present.")
        elif dimension == "Consistency":
            st.markdown("""
                **Consistency:**  The uniformity of data across different datasets or systems.

                **Example:**  A customer's name should be represented the same way in all systems (e.g., "John Doe" vs. "Doe, John").

                **Challenges:**  Different data entry practices, lack of data standards, system integration problems.
            """)
            with st.expander("Interactive Example"):
                system1_name = st.text_input("System 1 - Customer Name:", "John Doe")
                system2_name = st.text_input("System 2 - Customer Name:", "Doe, John")
                if system1_name != system2_name:
                    if system1_name.replace(" ", "") == system2_name.replace(" ", "").replace(",", ""): #handle formatting
                        st.warning(f"Consistency Issue: Name format is different, but values represent the same entity.")
                    else:
                        st.error(f"Consistency Issue: Customer name is different across systems: '{system1_name}' vs. '{system2_name}'.")
                else:
                    st.success("Consistency Check: Customer name is consistent across systems.")

        elif dimension == "Timeliness":
            st.markdown("""
                **Timeliness:**  The availability of data when it is needed.

                **Example:**  Sales data should be updated in a timely manner to provide an accurate view of current performance.

                **Challenges:**  Delays in data processing, batch processing limitations, real-time data integration issues.
            """)
            with st.expander("Interactive Example"):
                data_needed_by = pd.to_datetime("2024-01-15")  # Example: Data needed by Jan 15, 2024
                data_available_on = pd.to_datetime(st.date_input("Data Available On:", value=pd.to_datetime("2024-01-16")))

                if data_available_on > data_needed_by:
                    st.error(f"Timeliness Issue: Data was needed by {data_needed_by.strftime('%Y-%m-%d')}, but was only available on {data_available_on.strftime('%Y-%m-%d')} .")
                else:
                    st.success("Timeliness Check: Data is available on time.")

        elif dimension == "Validity":
            st.markdown("""
                **Validity:**  The extent to which data conforms to defined rules, constraints, or formats.

                **Example:**  An email address should follow a valid format (e.g., user@domain.com).

                **Challenges:**  Data entry errors, lack of input validation, system integration issues.
            """)
            with st.expander("Interactive Example"):
                email = st.text_input("Enter Email Address:", "invalid-email")
                import re
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Basic email format check
                    st.error("Validity Issue: Invalid email format.")
                else:
                    st.success("Validity Check: Email format is valid.")

        elif dimension == "Uniqueness":
            st.markdown("""
                **Uniqueness:**  Ensuring that there are no duplicate records in a dataset.

                **Example:**  A customer database should not have multiple entries for the same customer.

                **Challenges:**  Data entry errors, system integration issues, lack of unique identifiers.
            """)
            with st.expander("Interactive Example"):
                customer_ids = st.text_input("Enter Customer IDs (comma-separated):", "1, 2, 3, 2, 4")
                ids = [cid.strip() for cid in customer_ids.split(',')]
                if len(ids) != len(set(ids)):  # Check for duplicates
                    st.error("Uniqueness Issue: Duplicate customer IDs found.")
                else:
                    st.success("Uniqueness Check: No duplicate customer IDs.")
    elif topic == "Data Legacy Management":
        st.subheader("Data Legacy Management Challenges and Strategies")
        challenge = st.selectbox("Select a Challenge:", ["Data Silos", "Data Format Incompatibilities", "Lack of Documentation", "Security Risks"])

        if challenge == "Data Silos":
            st.markdown("""
                **Data Silos:**  Data isolated within legacy systems, making it difficult to access and integrate with other data.

                **Example:**  Customer data stored in an old mainframe system that cannot be easily accessed by modern analytics tools.

                **Strategies:**
                *   **Data Integration:**  Connect the legacy system to other systems using APIs or middleware.
                *   **Data Migration:**  Move the data to a modern data warehouse or data lake.
            """)

        elif challenge == "Data Format Incompatibilities":
            st.markdown("""
                **Data Format Incompatibilities:**  Older data formats may not be supported by modern tools.

                **Example:**  Data stored in a proprietary format used by a discontinued software application.

                **Strategies:**
                *   **Data Conversion:**  Convert the data to a modern format (e.g., CSV, JSON, Parquet).
                *   **Data Transformation:**  Restructure the data to fit a new data model.
            """)

        elif challenge == "Lack of Documentation":
            st.markdown("""
                **Lack of Documentation:**  Understanding the meaning, structure, and quality of legacy data can be difficult without proper documentation.

                **Example:**  A legacy database with unclear column names and no data dictionary.

                **Strategies:**
                *   **Data Profiling:**  Analyze the data to understand its characteristics and identify potential issues.
                *   **Reverse Engineering:**  Attempt to reconstruct the data model and business rules.
                *   **Knowledge Capture:**  Interview former employees or users of the legacy system.
            """)

        elif challenge == "Security Risks":
            st.markdown("""
                **Security Risks:**  Legacy systems may have known vulnerabilities that are no longer patched or supported.

                **Example:**  An outdated operating system running on a server that hosts a legacy database.

                **Strategies:**
                *   **System Modernization:**  Replace or upgrade the legacy system.
                *   **Security Patching (if possible):**  Apply any available security patches.
                *   **Network Segmentation:**  Isolate the legacy system from other parts of the network.
                *   **Monitoring:**  Implement security monitoring to detect and respond to threats.
            """)
    elif topic == "Compliance Frameworks":
        st.subheader("Common Compliance Frameworks")
        framework = st.selectbox("Select a Framework:", ["GDPR", "CCPA", "HIPAA", "SOX", "PCI DSS"])

        if framework == "GDPR":
            st.markdown("""
                **GDPR (General Data Protection Regulation):**

                *   **Jurisdiction:** European Union (EU)
                *   **Purpose:** Protects the data privacy and security of individuals within the EU.
                *   **Key Principles:** Lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity, and confidentiality.
                *   **Rights of Individuals:** Right to access, right to rectification, right to erasure ("right to be forgotten"), right to restrict processing, right to data portability, right to object.
            """)

        elif framework == "CCPA":
            st.markdown("""
                **CCPA (California Consumer Privacy Act):**

                *   **Jurisdiction:** California, USA
                *   **Purpose:** Gives California consumers more control over their personal information.
                *   **Rights of Consumers:** Right to know what personal information is collected, right to delete personal information, right to opt-out of the sale of personal information, right to non-discrimination for exercising CCPA rights.
            """)

        elif framework == "HIPAA":
            st.markdown("""
                **HIPAA (Health Insurance Portability and Accountability Act):**

                *   **Jurisdiction:** United States
                *   **Purpose:** Protects the privacy and security of individuals' health information (Protected Health Information - PHI).
                *   **Covered Entities:** Healthcare providers, health plans, healthcare clearinghouses.
                *   **Key Rules:** Privacy Rule, Security Rule, Breach Notification Rule.
            """)

        elif framework == "SOX":
            st.markdown("""
                **SOX (Sarbanes-Oxley Act):**

                *   **Jurisdiction:** United States
                *   **Purpose:** Regulates financial reporting and corporate governance to protect investors from fraudulent accounting practices.
                *   **Key Provisions:**  Requires companies to establish internal controls over financial reporting and to have those controls audited.
            """)

        elif framework == "PCI DSS":
            st.markdown("""
                **PCI DSS (Payment Card Industry Data Security Standard):**

                *   **Jurisdiction:** Global
                *   **Purpose:**  Protects cardholder data and prevents credit card fraud.
                *   **Applicability:**  Any organization that stores, processes, or transmits cardholder data.
                *   **Key Requirements:**  Build and maintain a secure network, protect cardholder data, maintain a vulnerability management program, implement strong access control measures, regularly monitor and test networks, maintain an information security policy.
            """)

    st.header("💪 Practice Exercises")
    st.markdown("""
    1. **Identify data quality issues in a sample dataset.**  Look for missing values, inconsistencies, outliers, and invalid data.
    2. **Develop a plan to migrate data from a legacy system to a modern system.**  Consider data mapping, transformation, and validation steps.
    3. **Research the specific requirements of a compliance framework (e.g., GDPR, CCPA) that is relevant to your organization or industry.**
    4. **Create a data quality checklist.** Include checks for accuracy, completeness, consistency, timeliness, validity, and uniqueness.
    5. **Assess the risks associated with a legacy system.** Consider data security, data integrity, and business continuity.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Data governance principles are applied across various industries and functions:

    *   **Finance:**  Ensuring data accuracy for financial reporting and regulatory compliance (SOX).
    *   **Healthcare:**  Protecting patient privacy and data security (HIPAA).
    *   **Retail:**  Managing customer data for marketing and personalization, while complying with privacy regulations (GDPR, CCPA).
    *   **E-commerce:**  Securing payment card data (PCI DSS).
    *   **Government:**  Managing citizen data responsibly and ensuring data transparency.
    """)
    st.header("✅ Knowledge Check")
    quiz_questions = [
    {
        "question": "What are the six dimensions of data quality?",
        "options": ["Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness",
                    "Availability, Confidentiality, Integrity, Usability, Relevance, Security",
                    "Accuracy, Privacy, Security, Completeness, Consistency, Timeliness",
                    "Validity, Reliability, Precision, Accuracy, Completeness, Consistency"],
        "answer": "Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness",
        "solution": "These six dimensions are widely recognized as key aspects of data quality."
    },
    {
        "question": "What is the primary challenge of data legacy management?",
        "options": ["Integrating data from multiple sources", "Ensuring data accuracy", "Managing older, often outdated data systems and the data they contain", "Complying with data privacy regulations"],
        "answer": "Managing older, often outdated data systems and the data they contain",
        "solution": "Legacy systems often pose challenges due to their age, technology, and lack of integration with modern systems."
    },
    {
        "question": "Which of the following is NOT a typical strategy for data legacy management?",
        "options": ["Data migration", "Data integration", "Data deletion", "System modernization"],
        "answer": "Data deletion",
        "solution": "While data deletion *might* be part of an overall strategy, it's not a primary *management* strategy. The other options are common approaches to dealing with legacy data."
    },
    {
        "question": "What does GDPR stand for?",
        "options": ["General Data Privacy Regulation", "Global Data Protection Regulation", "General Data Protection Requirement", "General Data Protection Regulation"],
        "answer": "General Data Protection Regulation",
        "solution": "GDPR is a key data protection and privacy regulation in the EU."
    },
    {
        "question": "Which compliance framework is primarily focused on protecting health information?",
        "options": ["GDPR", "CCPA", "HIPAA", "SOX"],
        "answer": "HIPAA",
        "solution": "HIPAA (Health Insurance Portability and Accountability Act) sets standards for protecting sensitive patient data."
    },
    {
        "question": "What is a data silo?",
        "options": ["A secure storage location for data",
                    "A system for organizing and classifying data",
                    "Data that is isolated within a specific system or department, hindering access and integration",
                    "A type of data visualization"],
        "answer": "Data that is isolated within a specific system or department, hindering access and integration",
        "solution": "Data silos are a common problem, especially with legacy systems."
    },
     {
        "question": "What is data profiling?",
        "options": ["Creating a visual representation of data",
                    "Analyzing data to understand its characteristics, quality, and structure",
                    "Encrypting data to protect it from unauthorized access",
                    "Moving data from one system to another"],
        "answer": "Analyzing data to understand its characteristics, quality, and structure",
        "solution": "Data profiling is a crucial step in data quality management and legacy data migration."
    },
    {
        "question": "Which compliance framework focuses on financial reporting and corporate governance?",
        "options":["GDPR", "CCPA", "HIPAA", "SOX"],
        "answer": "SOX",
        "solution": "SOX is important for public companies in the US"
    },
    {
        "question": "Which right is granted to individuals under GDPR?",
        "options":["Right to data deletion", "Right to be forgotten", "Right to access", "All of the above"],
        "answer": "All of the above",
        "solution": "GDPR gives individuals many rights regarding their personal information."
    },
    {
        "question": "What does 'data validity' refer to?",
        "options":["Data is accessible when needed", "Data entries are unique with no duplicates", "Data entries follow required constraints and formatting", "Data across databases is free of contradictions"],
        "answer":"Data entries follow required constraints and formatting",
        "solution": "Data validity refers to values following appropriate ranges, types and formatting."
    }
]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(f"Select an answer:", question["options"], key=f"quiz_{i}")
        user_answers.append(user_answer)

    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1

        st.write(f"You got {correct_count} out of {len(quiz_questions)} questions correct.")

        with st.expander("Show Detailed Solutions"):
            for i, question in enumerate(quiz_questions):
                st.markdown(f"**Question {i+1}:** {question['question']}")
                st.markdown(f"**Your Answer:** {user_answers[i]}")
                st.markdown(f"**Correct Answer:** {question['answer']}")
                st.markdown(f"**Solution:** {question['solution']}")
                if user_answers[i] == question['answer']:
                    st.success("Correct!")
                else:
                    st.error("Incorrect.")

if __name__ == "__main__":
    main()
