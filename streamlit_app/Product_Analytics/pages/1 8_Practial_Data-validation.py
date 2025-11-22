import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to simulate different data issues
def create_dirty_data(n_rows=100, missing_rate=0.1, outlier_rate=0.05, inconsistency_rate=0.05, random_state=42):
    np.random.seed(random_state)
    data = {
        'Age': np.random.randint(18, 70, n_rows),
        'Income': np.random.randint(20000, 100000, n_rows),
        'Purchase': np.random.choice(['Yes', 'No'], n_rows),
        'Rating': np.random.randint(1, 6, n_rows),
        'Date': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365, n_rows), unit='D')
    }
    df = pd.DataFrame(data)

    # Introduce missing values
    for col in df.columns:
        mask = np.random.choice([True, False], n_rows, p=[missing_rate, 1 - missing_rate])
        df.loc[mask, col] = np.nan

    # Introduce outliers (in numerical columns)
    for col in ['Age', 'Income']:
        num_outliers = int(n_rows * outlier_rate)
        outlier_indices = np.random.choice(df.index, num_outliers, replace=False)
        df.loc[outlier_indices, col] *= np.random.choice([5, -5], num_outliers) #make them very high

    # Introduce inconsistencies (in categorical and date columns)
    df['Purchase'] = df['Purchase'].str.lower()
    inconsistency_indices = np.random.choice(df.index, int(n_rows * inconsistency_rate), replace=False)
    df.loc[inconsistency_indices, 'Purchase'] = df.loc[inconsistency_indices, 'Purchase'].str.upper()

    date_inconsistency_indices = np.random.choice(df.index, int(n_rows * inconsistency_rate), replace=False)
    df.loc[date_inconsistency_indices, 'Date'] = df.loc[date_inconsistency_indices, 'Date'].apply(lambda x: x + pd.DateOffset(years=10) if pd.notna(x) else x)


    return df

def main():
    st.set_page_config(page_title="Data Validation and Cleaning", page_icon="🧼", layout="wide")

    st.title("Data Validation and Cleaning: A Hands-On Guide")
    st.write("Learn how to identify and handle common data quality issues.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Data validation and cleaning are crucial steps in any data analysis or machine learning project.  Clean data leads to more accurate results and better decisions.

        ### 1. Common Data Quality Issues

        *   **Missing Values:**  Data points that are absent (represented as NaN, None, null, etc.).
        *   **Outliers:**  Extreme values that deviate significantly from the rest of the data.
        *   **Inconsistencies:**  Data that is not uniform (e.g., different capitalization, date formats).
        *   **Duplicates:**  Repeated entries in the dataset.
        *   **Incorrect Data Types:**  Data stored in the wrong format (e.g., numbers as strings).
        * **Invalid Values:** Data outside expected ranges or categories.

        ### 2. Techniques for Handling Issues

        *   **Missing Values:**
            *   **Deletion:**  Remove rows or columns with missing values (use with caution!).
            *   **Imputation:**  Replace missing values with:
                *   Mean/Median/Mode
                *   Constant value
                *   Predicted value (using machine learning)
                *   Forward/Backward fill (for time series)
        *   **Outliers:**
            *   **Visualization:**  Box plots, scatter plots, histograms.
            *   **Statistical Methods:**  Z-score, IQR (Interquartile Range).
            *   **Transformation:**  Log transformation, winsorizing.
            *   **Removal:**  If justified (but document the decision!).
        *   **Inconsistencies:**
            *   **Standardization:**  Convert to lowercase/uppercase, consistent date formats, etc.
            *   **Mapping:**  Create dictionaries to map inconsistent values to standardized ones.
        *   **Duplicates:**
            *   **Identification:**  Use Pandas' `duplicated()` method.
            *   **Removal:**  Use Pandas' `drop_duplicates()` method.
        *   **Incorrect Data Types:**
            *   **Conversion:**  Use Pandas' `astype()` or `to_datetime()` methods.
        *  **Invalid Values:**
           * **Filtering:** Remove the rows based on logical checks.
           * **Replacement:** Replace with a more appropriate value.

        **Further Reading:**
            *   [Pandas Documentation on Working with Missing Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
            *   [Data Cleaning (Wikipedia)](https://en.wikipedia.org/wiki/Data_cleansing)
        """)

    st.header("🔄 Interactive Demo")

    # Data Upload or Generation
    data_source = st.radio("Choose data source:", ["Generate Synthetic Data", "Upload CSV"])
    if data_source == "Generate Synthetic Data":
      n_rows = st.slider("Number of Rows:", min_value=50, max_value=500, value=100, step=50)
      missing_rate = st.slider("Missing Value Rate:", min_value=0.0, max_value=0.5, value=0.1, step=0.05)
      outlier_rate = st.slider("Outlier Rate:", min_value=0.0, max_value=0.2, value=0.05, step=0.05)
      inconsistency_rate = st.slider("Inconsistency Rate:", min_value=0.0, max_value=0.2, value=0.05, step=0.05)
      df = create_dirty_data(n_rows, missing_rate, outlier_rate, inconsistency_rate)
      st.write("Generated Dirty Data:")
      st.dataframe(df)
    else:
      uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
      if uploaded_file is not None:
          try:
            df = pd.read_csv(uploaded_file)
            st.write("Uploaded Data:")
            st.dataframe(df)
          except Exception as e:
            st.error(f"Error reading the CSV file: {e}")
            df = None #ensure df isn't used later
      else:
        df = None # Ensure df is not used without valid input


    if df is not None: #Only proceed if we have a valid df
        st.subheader("Data Validation and Cleaning Steps")

        # Missing Values
        with st.expander("Missing Values"):
            st.write("Missing Values Summary:")
            st.write(df.isnull().sum())

            missing_value_handling = st.selectbox("Handle Missing Values:", ["None", "Drop Rows", "Impute (Mean)", "Impute (Median)", "Impute (Mode)"])
            if missing_value_handling != "None":
                if missing_value_handling == "Drop Rows":
                    df.dropna(inplace=True)
                else:
                    for col in df.columns:
                        if df[col].isnull().any():
                            if df[col].dtype in ['int64', 'float64']:
                                if missing_value_handling == "Impute (Mean)":
                                    df[col].fillna(df[col].mean(), inplace=True)
                                elif missing_value_handling == "Impute (Median)":
                                    df[col].fillna(df[col].median(), inplace=True)

                            elif df[col].dtype == 'object' or df[col].dtype == 'datetime64[ns]': #Categorical and datetime
                                if missing_value_handling == "Impute (Mode)":
                                    df[col].fillna(df[col].mode()[0], inplace=True)


                st.write("Data after handling missing values:")
                st.dataframe(df)
                st.write(df.isnull().sum())

        # Outliers
        with st.expander("Outliers"):
            st.write("Detecting Outliers (Numerical Columns Only):")
            for col in df.select_dtypes(include=['number']):
                fig, ax = plt.subplots()
                sns.boxplot(x=df[col], ax=ax)
                ax.set_title(f"Boxplot of {col}")
                st.pyplot(fig)

                outlier_handling = st.selectbox(f"Handle Outliers in {col}:", ["None", "Remove", "Winsorize (95th percentile)"], key=f"outlier_{col}")
                if outlier_handling == "Remove":
                    # Simple outlier removal using IQR
                    Q1 = df[col].quantile(0.25)
                    Q3 = df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
                    st.write(f"Data after removing outliers in {col}:")
                    st.dataframe(df)


                elif outlier_handling == "Winsorize (95th percentile)":
                    upper_limit = df[col].quantile(0.95)
                    df[col] = np.where(df[col] > upper_limit, upper_limit, df[col])
                    st.write(f"Data after winsorizing {col}:")
                    st.dataframe(df)


        # Inconsistencies
        with st.expander("Inconsistencies"):
            st.write("Handling Inconsistencies (Categorical Columns Only):")
            for col in df.select_dtypes(include='object'):
                st.write(f"Unique values in {col}:", df[col].unique())
                inconsistency_handling = st.selectbox(f"Handle Inconsistencies in {col}:", ["None", "Convert to Lowercase", "Convert to Uppercase"], key=f"inconsistency_{col}")
                if inconsistency_handling == "Convert to Lowercase":
                    df[col] = df[col].str.lower()
                elif inconsistency_handling == "Convert to Uppercase":
                    df[col] = df[col].str.upper()

                if inconsistency_handling != "None": #display after handling
                   st.write(f"Unique values in {col} after handling:", df[col].unique())

        #Date Inconsistencies
        with st.expander("Date Inconsistencies"):
            st.write("Handling Inconsistencies (Date Columns Only):")
            for col in df.select_dtypes(include='datetime64[ns]'):
                st.write(f"Date range in {col}:", df[col].min(), "to", df[col].max())
                # No specific handling option here, just visualization - or could add specific transformations

        # Duplicates
        with st.expander("Duplicates"):
            st.write("Number of Duplicate Rows:", df.duplicated().sum())
            if st.button("Remove Duplicate Rows"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicate Rows Removed.")
                st.write("Number of Duplicate Rows:", df.duplicated().sum())

        # Incorrect Data Types
        with st.expander("Incorrect Data Types"):
            st.write("Current Data Types:")
            st.write(df.dtypes)
            for col in df.columns:
                current_type = df[col].dtype
                available_types = ['infer', 'integer', 'float', 'boolean', 'datetime64[ns]', 'object'] # 'infer' added
                #Move current type to front, if possible
                if str(current_type) in available_types:
                    available_types.remove(str(current_type))
                    available_types.insert(0, str(current_type))

                new_type = st.selectbox(f"Change data type of '{col}':", available_types, key=f"dtype_{col}")
                if new_type != 'infer' and str(current_type) != new_type: #only change if different type
                    try:
                        if new_type == 'datetime64[ns]':
                            df[col] = pd.to_datetime(df[col], errors='coerce')  # Handle parsing errors
                        else:
                            df[col] = df[col].astype(new_type)
                        st.write(f"Data type of '{col}' changed to {new_type}.")
                    except ValueError as e:
                        st.error(f"Error converting '{col}' to {new_type}: {e}")
            st.write("New Data Types:")  # Show after potential changes
            st.write(df.dtypes)

        #Invalid data
        with st.expander("Invalid Values"):
            st.write("Handling Invalid Values (Custom Rules):")
            for col in df.columns:
                if df[col].dtype in ['int64', 'float64']:
                    min_val = st.number_input(f"Minimum valid value for '{col}':", value=df[col].min(), key=f"min_{col}") #Defaults shown
                    max_val = st.number_input(f"Maximum valid value for '{col}':", value=df[col].max(), key=f"max_{col}")
                    if st.button(f"Filter Invalid Values in {col}", key=f'filter_{col}'):
                        df = df[(df[col] >= min_val) & (df[col] <= max_val)]
                        st.write(f"Rows with invalid values in '{col}' removed.")
                        st.dataframe(df)


    st.header("💪 Practice Exercises")
    st.markdown("""
    1. **Load a dataset (CSV or generate one).** Identify and handle missing values using different imputation techniques. Compare the results.
    2. **Create a dataset with outliers.** Visualize the outliers, then apply different outlier handling methods (removal, winsorizing, transformation). Analyze the impact on summary statistics.
    3. **Find a dataset with inconsistent categorical values.** Standardize the values using appropriate string manipulation techniques.
    4. **Practice data type conversion.** Change the data types of columns in a dataset and observe the effects.
    5. **Load a real-world dataset with known data quality problems.** Apply a combination of cleaning techniques to improve the data quality. Document your steps and justify your choices.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Data validation and cleaning are essential in numerous domains:

    *   **Business Analytics:**  Ensuring accurate reporting, forecasting, and decision-making.
    *   **Machine Learning:**  Improving model performance and preventing biased results.
    *   **Data Science Research:**  Maintaining data integrity for reliable research findings.
    *   **Healthcare:**  Cleaning patient data for accurate diagnosis and treatment.
    *   **Finance:**  Validating financial transactions to prevent fraud and errors.
    """)

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "What is the term for extreme values that deviate significantly from the rest of the data?",
            "options": ["Missing values", "Outliers", "Inconsistencies", "Duplicates"],
            "answer": "Outliers",
            "solution": "Outliers are data points that lie far away from the majority of the data."
        },
        {
            "question": "Which of the following is NOT a common technique for handling missing values?",
            "options": ["Deletion", "Imputation", "Duplication", "Forward fill"],
            "answer": "Duplication",
            "solution": "Duplication refers to creating copies of data, which is not a way to handle missing values. The other options are valid missing value handling methods."
        },
        {
            "question": "What is the purpose of standardizing categorical values?",
            "options": ["To create outliers", "To introduce missing values", "To ensure consistency", "To change data types"],
            "answer": "To ensure consistency",
            "solution": "Standardization (e.g., converting to lowercase) makes sure categorical values are uniform (e.g., 'Yes', 'yes', 'YES' all become 'yes')."
        },
        {
            "question": "What Pandas method is used to remove duplicate rows?",
            "options": ["duplicated()", "drop_duplicates()", "fillna()", "astype()"],
            "answer": "drop_duplicates()",
            "solution": "`drop_duplicates()` removes rows that are exact copies of other rows. `duplicated()` *identifies* duplicates, but doesn't remove them."
        },
        {
            "question": "What is a common way to visualize outliers in a numerical column?",
            "options": ["Bar chart", "Box plot", "Line chart", "Pie chart"],
            "answer": "Box plot",
            "solution": "Box plots (or box-and-whisker plots) clearly show the median, quartiles, and potential outliers of a dataset."
        },
        {
            "question": "Replacing missing numerical values with the average value is called:",
            "options":["Mean imputation", "Mode imputation", "Median imputation", "Deletion"],
            "answer": "Mean imputation",
            "solution": "Imputing with the mean involves replacing missing values with the average of the non-missing values."
        },
        {
            "question": "If a column containing years is stored as strings, what should you do?",
            "options": ["Leave it as is", "Convert it to lowercase", "Convert it to an appropriate numerical or datetime type", "Remove the column"],
            "answer": "Convert it to an appropriate numerical or datetime type",
            "solution": "Years should be represented as numbers (integers) or, if more precise dates are involved, as datetime objects for proper analysis."
        },
         {
            "question": "What does 'winsorizing' a variable involve?",
            "options": ["Removing outliers completely", "Replacing outliers with the mean", "Capping extreme values at a specified percentile", "Converting the variable to a categorical type"],
            "answer": "Capping extreme values at a specified percentile",
            "solution": "Winsorizing limits extreme values by replacing them with a specified percentile value (e.g., replacing all values above the 95th percentile with the 95th percentile value itself)."
        },
        {
            "question": "Which of the following is a good practice BEFORE handling missing values or outliers?",
            "options": ["Immediately remove all rows with missing values.", "Impute all missing values with the mean.", "Always remove outliers.", "Understand the *reason* for missing values and outliers."],
            "answer": "Understand the *reason* for missing values and outliers.",
            "solution": "It's crucial to understand *why* data is missing or why outliers exist.  This understanding informs the best cleaning strategy."
        },
        {
            "question": "You have a 'Gender' column with values 'Male', 'Female', 'M', and 'F'.  What data quality issue does this represent?",
            "options": ["Missing values", "Outliers", "Inconsistencies", "Incorrect data type"],
            "answer": "Inconsistencies",
            "solution": "The different representations of male and female ('Male' vs. 'M', etc.) represent inconsistencies that need standardization."
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
