import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# --- Data Generation Functions ---


def generate_demand_data(
    n_periods=365,
    base_demand=100,
    seasonality_strength=0.3,
    noise_level=0.1,
    random_state=42,
):
    """Generates synthetic daily demand data with seasonality and noise."""
    np.random.seed(random_state)
    time = np.arange(n_periods)
    seasonality = np.sin(2 * np.pi * time / 365) * seasonality_strength * base_demand
    noise = np.random.randn(n_periods) * noise_level * base_demand
    demand = base_demand + seasonality + noise
    demand = np.maximum(demand, 10)  # Ensure demand is non-negative and reasonable min
    date_rng = pd.date_range(start="2023-01-01", periods=n_periods)
    df = pd.DataFrame({"Date": date_rng, "Demand": demand})
    df.set_index("Date", inplace=True)
    return df


def calculate_eoq(annual_demand, ordering_cost, holding_cost_per_unit):
    """Calculates Economic Order Quantity (EOQ)."""
    if holding_cost_per_unit <= 0:
        return (
            np.inf
        )  # Avoid division by zero and handle cases where holding cost is not positive
    eoq = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost_per_unit)
    return eoq


def calculate_reorder_point(lead_time_demand, safety_stock):
    """Calculates Reorder Point."""
    return lead_time_demand + safety_stock


# --- Main Streamlit App ---
def main():
    st.set_page_config(
        page_title="Supply Chain Analytics", page_icon="🚚", layout="wide"
    )

    st.title("Supply Chain Analytics: Optimizing Flow and Efficiency")
    st.write("Explore data-driven approaches to improve supply chain performance.")

    with st.expander("📖 Theoretical Overview"):
        st.markdown(
            """
        Supply chain analysis is the application of data analytics and operations research techniques to understand, optimize, and improve the performance of a supply chain. It's about making supply chains smarter, more resilient, and more efficient.

        ### 1. Core Components of Supply Chain Analysis

        *   **Demand Forecasting:** Predicting future demand to plan production, inventory, and resources effectively.
        *   **Inventory Management:** Optimizing inventory levels to balance holding costs and stockout risks.
        *   **Logistics and Transportation Optimization:** Minimizing transportation costs and delivery times.
        *   **Supplier Relationship Management:** Evaluating and managing supplier performance and risk.
        *   **Supply Chain Network Design:** Optimizing the structure and location of facilities within the supply chain.
        *   **Risk Management and Resilience:** Identifying and mitigating supply chain disruptions.

        ### 2. Analytical Techniques from Operations Research (OR)

        *   **Optimization Models:** Linear Programming, Network Flow Models, Integer Programming for resource allocation, scheduling, and network design.
        *   **Simulation:** Discrete-event simulation to model complex supply chain dynamics and test different scenarios.
        *   **Inventory Theory:** EOQ (Economic Order Quantity), Reorder Point models for inventory control.
        *   **Queueing Theory:** Analyzing and optimizing waiting times and bottlenecks in processes.

        ### 3. Data Analytics in Supply Chain

        *   **Descriptive Analytics:** KPIs (Key Performance Indicators) dashboards to monitor current supply chain performance (e.g., fill rate, inventory turnover, on-time delivery).
        *   **Predictive Analytics:** Machine learning models for demand forecasting, predicting lead times, identifying potential disruptions.
        *   **Prescriptive Analytics:** Using optimization and simulation to recommend actions (e.g., optimal inventory policies, best transportation routes, supplier selection).
        *   **Anomaly Detection:** Identifying unusual patterns or outliers in supply chain data that may indicate problems or inefficiencies.

        ### 4. Key Performance Indicators (KPIs) in Supply Chain

        *   **Efficiency KPIs:**
            *   **Inventory Turnover:** How efficiently inventory is sold and replenished.
            *   **Order Cycle Time:** Time taken to fulfill a customer order.
            *   **Transportation Costs:** Costs associated with moving goods.
        *   **Effectiveness KPIs:**
            *   **Fill Rate:** Percentage of customer demand fulfilled from available inventory.
            *   **On-Time Delivery:** Percentage of orders delivered on time.
            *   **Customer Satisfaction:** Measures of how well the supply chain meets customer needs.
        *   **Responsiveness & Resilience KPIs:**
            *   **Supply Chain Cycle Time:** Total time from raw material sourcing to delivery to customer.
            *   **Time to Recover from Disruption:** Ability to bounce back from unexpected events.

        **Further Reading:**
            *   [Council of Supply Chain Management Professionals (CSCMP)](https://www.cscmp.org/)
            *   [APICS (now ASCM) - Association for Supply Chain Management](https://www.ascm.org/)
            *   [Supply Chain Dive](https://www.supplychaindive.com/)
        """
        )

    st.header("📊 Interactive Supply Chain Analysis Tools")

    analysis_type = st.selectbox(
        "Select Analysis Tool:",
        ["Demand Data Exploration", "Inventory Optimization (EOQ)"],
    )

    if analysis_type == "Demand Data Exploration":
        st.subheader("Demand Data Visualization and Analysis")
        n_periods_demand = st.slider(
            "Number of Days to Simulate:",
            min_value=30,
            max_value=730,
            value=365,
            step=30,
            key="n_periods_demand",
        )
        base_demand_input = st.number_input(
            "Base Daily Demand:",
            min_value=10,
            max_value=500,
            value=100,
            step=10,
            key="base_demand_input",
        )
        seasonality_strength_input = st.slider(
            "Seasonality Strength:",
            min_value=0.0,
            max_value=1.0,
            value=0.3,
            step=0.05,
            key="seasonality_strength_input",
        )
        noise_level_input = st.slider(
            "Demand Noise Level:",
            min_value=0.0,
            max_value=0.5,
            value=0.1,
            step=0.05,
            key="noise_level_input",
        )

        if st.button("Generate and Analyze Demand Data"):
            demand_df = generate_demand_data(
                n_periods_demand,
                base_demand_input,
                seasonality_strength_input,
                noise_level_input,
            )
            st.line_chart(demand_df)

            st.subheader("Demand Statistics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Average Daily Demand", f"{demand_df['Demand'].mean():.2f}")
            with col2:
                st.metric(
                    "Demand Standard Deviation", f"{demand_df['Demand'].std():.2f}"
                )
            with col3:
                st.metric("Total Demand", f"{demand_df['Demand'].sum():.0f}")

            st.subheader("Seasonality Visualization")
            monthly_demand = demand_df.resample("M").mean()  # Monthly average demand
            fig_seasonal = px.line(
                monthly_demand,
                x=monthly_demand.index,
                y="Demand",
                title="Average Monthly Demand (Seasonality)",
            )
            st.plotly_chart(fig_seasonal)

    elif analysis_type == "Inventory Optimization (EOQ)":
        st.subheader("Economic Order Quantity (EOQ) Model")

        annual_demand_eoq = st.number_input(
            "Annual Demand:",
            min_value=1000,
            max_value=100000,
            value=10000,
            step=1000,
            key="annual_demand_eoq",
        )
        ordering_cost_eoq = st.number_input(
            "Ordering Cost per Order:",
            min_value=10,
            max_value=500,
            value=100,
            step=10,
            key="ordering_cost_eoq",
        )
        holding_cost_percent_eoq = st.slider(
            "Annual Holding Cost (% of unit cost):",
            min_value=1,
            max_value=30,
            value=20,
            step=1,
            format="%d%%",
            key="holding_cost_percent_eoq",
        )
        unit_cost_eoq = st.number_input(
            "Unit Cost:",
            min_value=1,
            max_value=50,
            value=10,
            step=1,
            key="unit_cost_eoq",
        )

        holding_cost_per_unit_eoq = (holding_cost_percent_eoq / 100) * unit_cost_eoq

        eoq_value = calculate_eoq(
            annual_demand_eoq, ordering_cost_eoq, holding_cost_per_unit_eoq
        )

        if eoq_value == np.inf:
            st.warning(
                "Holding cost per unit is zero or negative. EOQ is undefined (infinite order quantity). Please ensure holding cost is positive."
            )
        else:
            st.metric("Economic Order Quantity (EOQ)", f"{eoq_value:.2f} units")

            st.subheader("Cost Breakdown")
            num_orders = annual_demand_eoq / eoq_value
            total_ordering_cost = num_orders * ordering_cost_eoq
            total_holding_cost = (eoq_value / 2) * holding_cost_per_unit_eoq
            total_inventory_cost = total_ordering_cost + total_holding_cost

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Ordering Cost", f"${total_ordering_cost:.2f}")
            with col2:
                st.metric("Total Holding Cost", f"${total_holding_cost:.2f}")
            with col3:
                st.metric("Total Inventory Cost", f"${total_inventory_cost:.2f}")

            # Visualize Cost Components vs. Order Quantity (Simplified)
            order_quantities = np.linspace(
                eoq_value / 2, eoq_value * 2, 100
            )  # Range around EOQ
            ordering_costs_range = (
                annual_demand_eoq / order_quantities
            ) * ordering_cost_eoq
            holding_costs_range = (order_quantities / 2) * holding_cost_per_unit_eoq
            total_costs_range = ordering_costs_range + holding_costs_range

            cost_df = pd.DataFrame(
                {
                    "Order Quantity": order_quantities,
                    "Ordering Cost": ordering_costs_range,
                    "Holding Cost": holding_costs_range,
                    "Total Cost": total_costs_range,
                }
            )

            fig_cost = px.line(
                cost_df,
                x="Order Quantity",
                y=["Ordering Cost", "Holding Cost", "Total Cost"],
                title="Inventory Costs vs. Order Quantity",
            )
            fig_cost.add_vline(
                x=eoq_value,
                line_dash="dash",
                line_color="red",
                annotation_text=f"EOQ = {eoq_value:.0f}",
                annotation_position="top right",
            )
            st.plotly_chart(fig_cost)

    st.header("💪 Practice Exercises")
    st.markdown(
        """
    1. **Demand Forecasting Scenario:**  You are given historical sales data. Use time series forecasting techniques (e.g., moving average, exponential smoothing - or link to the Time Series page if you've created one) to predict future demand.
    2. **Inventory Optimization Problem:**  A retailer sells a product with the following parameters: annual demand, ordering cost, holding cost per unit, lead time. Calculate the EOQ and reorder point.  Experiment with changing input parameters and observe the impact on EOQ.
    3. **Transportation Cost Minimization:**  You need to ship goods from multiple warehouses to multiple customer locations.  (This is a more complex OR problem - consider simplifying it or pointing to resources on network flow optimization).  Perhaps focus on calculating total transportation cost given different routing options.
    4. **Supplier Selection:**  You have multiple suppliers offering different prices, lead times, and quality levels.  Develop a weighted scoring model to evaluate and select the best supplier.
    5. **Supply Chain Risk Assessment:**  Identify potential risks in a given supply chain (e.g., single supplier dependency, long lead times, geopolitical instability).  Develop mitigation strategies for these risks.
    """
    )

    st.header("🌍 Real-world Applications")
    st.markdown(
        """
    Supply chain analysis is applied across all industries that involve the movement of goods and services:

    *   **Retail:** Optimizing inventory, managing logistics for e-commerce fulfillment, demand forecasting for seasonal products.
    *   **Manufacturing:** Production planning, inventory control of raw materials and finished goods, optimizing supply networks.
    *   **Healthcare:** Managing the supply of pharmaceuticals, medical devices, and hospital supplies, ensuring timely delivery of critical items.
    *   **Logistics and Transportation:** Route optimization for delivery fleets, warehouse location planning, optimizing shipping schedules.
    *   **Food and Beverage:** Managing perishable goods inventory, optimizing cold chains, forecasting demand for food products.
    *   **Technology:** Supply chain management for electronics components, managing global manufacturing and distribution networks.
    """
    )

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "Which of the following is NOT a core component of supply chain analysis?",
            "options": [
                "Demand Forecasting",
                "Inventory Management",
                "Customer Relationship Management (CRM)",
                "Logistics Optimization",
            ],
            "answer": "Customer Relationship Management (CRM)",
            "solution": "While CRM is important for overall business, it's not typically considered a *core* component of *supply chain* analysis itself. The others are fundamental to SC optimization.",
        },
        {
            "question": "What is the primary goal of Economic Order Quantity (EOQ) model?",
            "options": [
                "To minimize transportation costs",
                "To maximize customer satisfaction",
                "To minimize total inventory costs (ordering and holding costs)",
                "To accurately forecast demand",
            ],
            "answer": "To minimize total inventory costs (ordering and holding costs)",
            "solution": "EOQ aims to find the order quantity that balances the trade-off between ordering and holding costs.",
        },
        {
            "question": "Which type of analytical technique from Operations Research is used to model complex supply chain dynamics and test 'what-if' scenarios?",
            "options": [
                "Linear Programming",
                "Simulation",
                "Inventory Theory",
                "Queueing Theory",
            ],
            "answer": "Simulation",
            "solution": "Simulation is excellent for modeling complex, dynamic systems like supply chains where analytical solutions are difficult.",
        },
        {
            "question": "Which KPI directly measures how efficiently inventory is sold and replenished?",
            "options": [
                "Fill Rate",
                "On-Time Delivery",
                "Inventory Turnover",
                "Order Cycle Time",
            ],
            "answer": "Inventory Turnover",
            "solution": "Inventory turnover is a key measure of inventory efficiency.",
        },
        {
            "question": "If a company wants to minimize transportation costs, which area of supply chain analysis would be most relevant?",
            "options": [
                "Demand Forecasting",
                "Inventory Management",
                "Logistics and Transportation Optimization",
                "Supplier Relationship Management",
            ],
            "answer": "Logistics and Transportation Optimization",
            "solution": "This area specifically focuses on optimizing the movement of goods.",
        },
        {
            "question": "What is 'prescriptive analytics' primarily used for in supply chain analysis?",
            "options": [
                "To describe past supply chain performance",
                "To predict future demand",
                "To recommend actions and decisions to optimize the supply chain",
                "To detect anomalies in supply chain data",
            ],
            "answer": "To recommend actions and decisions to optimize the supply chain",
            "solution": "Prescriptive analytics goes beyond prediction to suggest the best course of action.",
        },
        {
            "question": "Which KPI measures the percentage of customer demand fulfilled from available inventory?",
            "options": [
                "Inventory Turnover",
                "Fill Rate",
                "Order Cycle Time",
                "On-Time Delivery",
            ],
            "answer": "Fill Rate",
            "solution": "Fill rate is a direct measure of how well demand is being met from stock.",
        },
        {
            "question": "What is 'demand forecasting' primarily used for in supply chain management?",
            "options": [
                "To track current inventory levels",
                "To plan future production and inventory levels",
                "To analyze past sales data only",
                "To optimize transportation routes",
            ],
            "answer": "To plan future production and inventory levels",
            "solution": "Accurate demand forecasts are essential for proactive supply chain planning.",
        },
        {
            "question": "In the EOQ formula, what happens to the EOQ if annual demand increases?",
            "options": [
                "EOQ decreases",
                "EOQ increases",
                "EOQ remains the same",
                "EOQ becomes zero",
            ],
            "answer": "EOQ increases",
            "solution": "As annual demand increases, a larger order quantity becomes more economical to reduce the frequency of ordering.",
        },
        {
            "question": "Which statistical test is used in Chi-Square testing?",
            "options": ["T-test", "Chi-Square test", "Z-test", "F-test"],
            "answer": "Chi-Square test",
            "solution": "Chi-Square test is used to test for independence between categorical variables.",
        },
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(
            "Select an answer:", question["options"], key=f"quiz_{i}"
        )
        user_answers.append(user_answer)

    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1

        st.write(
            f"You got {correct_count} out of {len(quiz_questions)} questions correct."
        )

        with st.expander("Show Detailed Solutions"):
            for i, question in enumerate(quiz_questions):
                st.markdown(f"**Question {i+1}:** {question['question']}")
                st.markdown(f"**Your Answer:** {user_answers[i]}")
                st.markdown(f"**Correct Answer:** {question['answer']}")
                st.markdown(f"**Solution:** {question['solution']}")
                if user_answers[i] == question["answer"]:
                    st.success("Correct!")
                else:
                    st.error("Incorrect.")


if __name__ == "__main__":
    main()
