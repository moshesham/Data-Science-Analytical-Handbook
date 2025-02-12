import streamlit as st

def main():
    st.set_page_config(page_title="Problem Decomposition & Effective Communication", page_icon="🧩🗣️", layout="wide")

    st.title("Mastering Complexity: Problem Decomposition & Effective Communication")
    st.write("Learn to break down daunting challenges and communicate solutions with clarity and impact.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        In analytics and beyond, success hinges on two critical skills: the ability to tackle complex problems and the capacity to communicate your approach and findings effectively.

        ### Part 1: Problem Decomposition - Taming Complexity

        #### 1. Understanding Complex Problems
        *   **Definition:** Problems with multiple interconnected parts, ambiguous boundaries, and often lacking a single, obvious solution.
        *   **Characteristics:** Scale, ambiguity, interdependencies, novelty, and often involving multiple stakeholders.
        *   **Why Decompose?** Complexity overwhelms cognitive capacity. Decomposition makes problems understandable and solvable.

        #### 2. Benefits of Decomposition
        *   **Reduces Overwhelm:** Breaks a large task into smaller, less daunting steps.
        *   **Improves Clarity:** Makes the problem's components and relationships more visible.
        *   **Facilitates Planning:** Allows for phased approaches and better resource allocation.
        *   **Enables Collaboration:** Divides work among teams or individuals effectively.
        *   **Enhances Problem Solving:** Makes it easier to identify specific issues and targeted solutions.

        #### 3. Top-Down vs. Bottom-Up Decomposition
        *   **Top-Down:** Start with the overall problem and break it into progressively smaller sub-problems. (e.g., Start with "Increase Sales" -> "Improve Marketing" & "Enhance Product" -> ...).
        *   **Bottom-Up:** Identify individual components or tasks and build up to a larger solution. (e.g., Identify data sources, cleaning steps, model types, and combine them into a data analysis project).
        *   **Choosing Approach:** Top-down for well-defined goals; bottom-up when exploring or building from existing components.

        #### 4. Divide and Conquer Strategy
        *   **Principle:** Recursively break down a problem into independent sub-problems, solve them individually, and combine solutions.
        *   **Examples:** Algorithmic design (merge sort), project management (work breakdown structures).

        #### 5. Abstraction and Simplification
        *   **Abstraction:** Focus on essential details and ignore irrelevant complexities. Create simplified models or representations.
        *   **Simplification:** Make assumptions or reduce the scope of the problem initially to make it more tractable. Address complexities iteratively.

        #### 6. Visual Decomposition Tools
        *   **Mind Maps:** Visual hierarchical diagrams to break down a central problem into branches and sub-branches.
        *   **Flowcharts:** Diagrammatic representations of processes, breaking down complex workflows into sequential steps.
        *   **Work Breakdown Structures (WBS):** Hierarchical decomposition of project tasks, common in project management.

        ### Part 2: Effective Communication - Delivering Insights Clearly

        #### 7. Principles of Effective Communication
        *   **Clarity:**  Use precise language, avoid jargon, and structure your message logically.
        *   **Conciseness:**  Get to the point efficiently, eliminate unnecessary details.
        *   **Audience Awareness:** Tailor your message to your audience's background, needs, and level of technical understanding.
        *   **Visual Aids:** Use charts, graphs, diagrams, and other visuals to enhance understanding and engagement.
        *   **Storytelling:** Frame your message as a narrative to make it more memorable and relatable.

        #### 8. Structuring Your Communication
        *   **The Pyramid Principle:** Start with the main conclusion, then support it with key arguments, and then detailed data/evidence.
        *   **Problem-Solution-Benefit:** Frame communication around the problem, your proposed solution, and the benefits of that solution.
        *   **Executive Summary:** For reports or presentations, always start with a concise summary of key findings and recommendations.

        #### 9. Communication Channels
        *   **Written Communication:** Reports, emails, documentation. Emphasize clarity, structure, and appropriate tone.
        *   **Verbal Communication:** Presentations, meetings, informal discussions. Focus on clear delivery, visual aids, and audience engagement.
        *   **Visual Communication:** Dashboards, infographics, visualizations. Design for impact and easy interpretation.

        #### 10. Tailoring Communication to Different Audiences
        *   **Technical Audience (e.g., Data Scientists):** Can handle technical jargon, detailed methodology, and complex statistical concepts.
        *   **Non-Technical Audience (e.g., Executives, Clients):** Focus on business implications, high-level insights, and actionable recommendations. Avoid jargon, use analogies and visuals.
        *   **Bridging the Gap:** Practice translating technical findings into business-relevant language.

        **Further Reading:**
            *   [Mind Mapping Techniques (Tony Buzan)](https://tonybuzan.com/mind-mapping/)
            *   [The Pyramid Principle (Barbara Minto)](https://www.mckinsey.com/featured-insights/mckinsey-explainers/mckinsey-explainer-the-pyramid-principle)
            *   [Effective Communication Skills (SkillsYouNeed)](https://www.skillsyouneed.com/learn/communication-skills.html)
        """)

    st.header("🧩 Interactive Practice: Problem Decomposition")

    st.subheader("Break Down a Complex Task")
    complex_task = st.text_area("Enter a Complex Task or Problem:", "Plan and execute a comprehensive marketing campaign for a new product launch.")

    if complex_task:
        st.write("Let's decompose this task using a top-down approach:")
        level1_tasks = st.text_input("Level 1 Sub-Tasks (comma-separated, e.g., Research, Strategy, Execution):", "Research, Strategy, Execution")
        if level1_tasks:
            task_list_level1 = [task.strip() for task in level1_tasks.split(',')]
            st.write("Level 1 Tasks:")
            for task1 in task_list_level1:
                st.markdown(f"* **{task1}:**  (Break down further below)")
                level2_tasks = st.text_input(f"  Level 2 Sub-Tasks for '{task1}' (comma-separated):", key=f"level2_{task1}")
                if level2_tasks:
                    task_list_level2 = [task.strip() for task in level2_tasks.split(',')]
                    for task2 in task_list_level2:
                        st.markdown(f"    * {task2}")
                else:
                    st.write("  (No further breakdown yet)")
        else:
            st.write("Enter Level 1 Sub-Tasks to start decomposing.")

    st.header("🗣️ Interactive Practice: Effective Communication")

    st.subheader("Rephrasing for Different Audiences")
    technical_explanation = st.text_area("Enter a Technical Finding or Explanation:", "The algorithm achieved an F1-score of 0.85 on the test set, indicating strong performance in balancing precision and recall for the positive class. However, class imbalance in the dataset may require further investigation into precision-recall trade-offs.")

    if technical_explanation:
        st.write("Rephrase this explanation for:")
        non_technical_audience = st.text_area("Non-Technical Audience (e.g., Executive Summary):", "")
        technical_audience = st.text_area("Technical Audience (e.g., Data Science Team):", "")

        st.write("Compare and Contrast:")
        st.write("- **Non-Technical:** Focus on business impact, key takeaways, and avoid jargon.")
        st.write("- **Technical:** Can include technical details, metrics, and methodology, assuming a shared understanding.")

    st.header("💪 Practice Exercises")
    st.markdown("""
    1. **Problem Decomposition Challenge:** Choose a complex real-world problem (e.g., "Reduce traffic congestion in a city," "Improve customer retention for a subscription service").  Practice decomposing it using both top-down and bottom-up approaches. Compare the results.
    2. **Mind Mapping Exercise:**  Use a mind mapping tool (or pen and paper) to break down a complex project you are working on into smaller tasks and sub-tasks.
    3. **Communication Scenario - Data Findings:**  Imagine you have analyzed sales data and found a statistically significant increase in sales after a marketing campaign. Write three versions of a summary of your findings:
        *   One for the marketing team (focused on campaign effectiveness and metrics).
        *   One for the executive team (focused on business impact and ROI).
        *   One for the technical data team (focused on methodology and data quality).
    4. **Active Listening Practice:**  In a conversation, consciously practice active listening techniques (summarizing, asking clarifying questions, showing empathy). Reflect on how it changes the communication.
    5. **Presentation Skills Drill:**  Prepare a short presentation (5 minutes) on a technical topic for both a technical and a non-technical audience. Practice delivering both versions, focusing on tailoring your language and visuals.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    These skills are fundamental across all professional fields, but particularly critical in:

    *   **Data Science & Analytics:** Breaking down complex analytical problems, communicating insights to stakeholders.
    *   **Project Management:** Decomposing projects into manageable tasks, communicating project status and risks.
    *   **Consulting:** Analyzing client problems, developing solutions, and communicating recommendations clearly.
    *   **Software Engineering:** Breaking down software development tasks, communicating technical designs and progress.
    *   **Leadership & Management:**  Solving organizational challenges, communicating vision and strategy to teams.
    *   **Education & Training:**  Breaking down complex subjects for learners, communicating effectively in teaching.
    """)

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "Which of the following is a benefit of breaking down complex problems?",
            "options": ["Increases cognitive overwhelm", "Obscures problem components", "Facilitates planning and collaboration", "Makes resource allocation harder"],
            "answer": "Facilitates planning and collaboration",
            "solution": "Decomposition makes large tasks more manageable and allows for structured planning and teamwork."
        },
        {
            "question": "What is the 'Pyramid Principle' in effective communication?",
            "options": ["Start with detailed data, then conclusions", "Start with the main conclusion, then supporting arguments", "Structure communication chronologically", "Use complex jargon to impress the audience"],
            "answer": "Start with the main conclusion, then supporting arguments",
            "solution": "The Pyramid Principle emphasizes presenting the most important information first for clarity and impact."
        },
        {
            "question": "Which decomposition approach starts with the overall problem and breaks it into smaller parts?",
            "options": ["Bottom-Up", "Divide and Conquer", "Top-Down", "Abstraction"],
            "answer": "Top-Down",
            "solution": "Top-down decomposition begins with the 'big picture' and drills down into details."
        },
        {
            "question": "When communicating with a non-technical audience, what is most important to emphasize?",
            "options": ["Technical jargon and methodology", "Detailed statistical metrics", "Business implications and actionable insights", "Complex algorithms and equations"],
            "answer": "Business implications and actionable insights",
            "solution": "Non-technical audiences are primarily interested in the 'so what?' and business value."
        },
        {
            "question": "Which visual tool is best suited for breaking down project tasks hierarchically?",
            "options": ["Flowchart", "Mind Map", "Work Breakdown Structure (WBS)", "Scatter Plot"],
            "answer": "Work Breakdown Structure (WBS)",
            "solution": "WBS is specifically designed for hierarchical task decomposition in project management."
        },
        {
            "question": "What does 'abstraction' mean in problem-solving?",
            "options":["Focusing on every detail of a problem", "Ignoring all complexities", "Focusing on essential details and ignoring irrelevant complexities", "Solving a problem using only visual tools"],
            "answer": "Focusing on essential details and ignoring irrelevant complexities",
            "solution": "Abstraction is about creating simplified representations to manage complexity."
        },
        {
            "question": "In 'Divide and Conquer', what is the key strategy?",
            "options":["Solve the entire problem at once", "Recursively break down problems into independent sub-problems", "Use only top-down approach", "Ignore complex parts of the problem"],
            "answer": "Recursively break down problems into independent sub-problems",
            "solution": "Divide and Conquer is based on recursive decomposition and independent solutions."
        },
        {
            "question": "For written communication, what is crucial for effective messaging?",
            "options": ["Use of highly technical jargon", "Lengthy and detailed explanations", "Clarity, structure, and appropriate tone", "Focusing only on visual elements"],
            "answer": "Clarity, structure, and appropriate tone",
            "solution": "Written communication needs to be easily understood, well-organized, and appropriately styled."
        },
        {
            "question": "Which communication channel is best for conveying complex data insights quickly and engagingly?",
            "options": ["Detailed written reports", "Emails with text summaries", "Visual communication (dashboards, infographics)", "Long verbal presentations"],
            "answer": "Visual communication (dashboards, infographics)",
            "solution": "Visuals can convey complex information efficiently and are often more engaging than text or lengthy verbal explanations."
        },
        {
            "question": "What is a key aspect of 'audience awareness' in effective communication?",
            "options": ["Using the same message for all audiences", "Tailoring your message to your audience's background and understanding", "Avoiding visual aids to keep it simple", "Focusing only on your own communication style"],
            "answer": "Tailoring your message to your audience's background and understanding",
            "solution": "Audience-centric communication is crucial for ensuring your message is received and understood as intended."
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
