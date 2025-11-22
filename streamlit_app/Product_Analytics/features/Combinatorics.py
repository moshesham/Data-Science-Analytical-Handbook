import math
import time
from itertools import combinations, permutations
from math import comb

import numpy as np  # Used for stars and bars visualization
import streamlit as st


def main():
    st.set_page_config(page_title="Combinatorics", page_icon="🧮", layout="wide")

    st.title("Combinatorics: Counting Possibilities")
    st.write(
        "Master the art of counting arrangements and selections – essential for probability, algorithm design, and more."
    )

    with st.expander("📖 Theoretical Concepts"):
        st.markdown(
            """
        Combinatorics is the study of counting.  It's fundamental to many areas of data science.

        ### 1. Basic Principles

        *   **Sum Rule:** If you can do task A in *n* ways and task B in *m* ways (and they're mutually exclusive), you can do *either* A *or* B in *n + m* ways.
        *   **Product Rule:** If you can do task A in *n* ways and *then* task B in *m* ways, you can do *both* A *and* B in *n * m* ways.

        ### 2. Factorials

        *   **n! (n factorial):**  Product of integers from 1 to *n*.  `n! = n * (n-1) * ... * 2 * 1`
        *   **Example:** 5! = 5 * 4 * 3 * 2 * 1 = 120
        *   **Crucial:** 0! = 1 (by definition)

        ### 3. Permutations (Order *Matters*)

        *   **Permutation:** An ordered arrangement of objects.
        *   **_nPr_:**  Ways to arrange *r* objects from a set of *n*.
        *   **Formula:** `_nPr_ = n! / (n-r)!`
        *   **Example:** Arranging 3 books out of 5: _5P3_ = 5! / (5-3)! = 60

        ### 4. Combinations (Order *Doesn't Matter*)

        *   **Combination:** A selection of objects where order is irrelevant.
        *   **_nCr_:** Ways to choose *r* objects from a set of *n*.
        *   **Formula:** `_nCr_ = n! / (r! * (n-r)!)`
        *   **Example:** Choosing a 2-person committee from 5 people: _5C2_ = 10

        ### 5. Advanced Concepts

        *   **Permutations with Repetition:** Arranging objects with duplicates (e.g., "GOOGLE"). Formula: `n! / (n1! * n2! * ... * nk!)`, where n1, n2,... are counts of each distinct object.
        *   **Combinations with Repetition:** Choosing with replacement (e.g., 3 scoops from 5 ice cream flavors). Formula: `_(n+r-1)Cr_`.
        *   **Binomial Theorem:** Expands (x + y)^n:  `(x + y)^n = Σ [k=0 to n] (_nCk_ * x^(n-k) * y^k)`
        *   **Pigeonhole Principle:** If you have more pigeons than pigeonholes, at least one hole has > 1 pigeon.  Used for existence proofs.
        *   **Inclusion-Exclusion Principle:**  Counts elements in the union of sets. For two sets: `|A ∪ B| = |A| + |B| - |A ∩ B|`.  Generalizes.
        *   **Stars and Bars:**  A technique for counting ways to distribute *indistinguishable* objects into *distinguishable* containers.

        **Further Reading:** (Same excellent links)
            * [Combinatorics (Wikipedia)](https://en.wikipedia.org/wiki/Combinatorics)
            * [Permutations and Combinations (Khan Academy)](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb)
        """
        )

    st.header("🔄 Interactive Demo")
    demo_type = st.selectbox(
        "Select a Concept:",
        [
            "Factorials",
            "Permutations",
            "Combinations",
            "Permutations with Repetition",
            "Combinations with Repetition",
            "Stars and Bars",
        ],
    )

    if demo_type == "Factorials":
        # 1. Input Validation: Prevent negative input.
        n = st.number_input(
            "Enter a non-negative integer (n):",
            min_value=0,
            max_value=20,
            value=5,
            step=1,
        )
        if st.button("Calculate and Animate"):
            result = 1
            steps = []
            # 2. Animated Calculation: Show the factorial calculation building up.
            for i in range(1, n + 1):
                result *= i
                steps.append(str(i))
                st.write(
                    " * ".join(steps) + f" = {result}"
                )  # Display intermediate results
                time.sleep(0.5)  # Pause for animation
            st.write(f"{n}! = {result}")

    elif demo_type in ["Permutations", "Combinations"]:
        n = st.number_input(
            "Enter n (total items):", min_value=1, max_value=20, value=5, step=1
        )
        r = st.number_input(
            "Enter r (items to choose):", min_value=0, max_value=n, value=2, step=1
        )

        if st.button(f"Calculate and Show {demo_type}"):
            if demo_type == "Permutations":
                result = math.perm(n, r)
                func = permutations
            else:
                result = math.comb(n, r)
                func = combinations

            st.write(f"{n}{'P' if demo_type == 'Permutations' else 'C'}{r} = {result}")

            # 3. Dynamic Example Display: Uses a generator for efficiency.
            with st.expander(f"Show Example {demo_type}"):
                items = list(range(1, n + 1))  # More readable than chr(65 + i)
                count = 0
                for item in func(items, r):
                    st.write(str(item))  # Consistent string representation
                    count += 1
                    if count > 100:
                        st.write("... (more)")
                        break

    elif demo_type == "Permutations with Repetition":
        word = st.text_input("Enter a word (e.g., MISSISSIPPI):", "MISSISSIPPI").upper()
        # 4. Input Sanitization:  Handle empty input gracefully.
        if not word:
            st.warning("Please enter a word.")
        elif st.button("Calculate Permutations"):
            counts = {}
            for char in word:
                counts[char] = counts.get(char, 0) + 1

            n = len(word)
            denominator = 1
            for count in counts.values():
                denominator *= math.factorial(count)

            result = math.factorial(n) // denominator
            st.write(f"Number of distinct permutations of '{word}': {result}")

            if len(word) <= 7:
                with st.expander("Show Example Permutations"):
                    perms = set()
                    for p in permutations(word):
                        perms.add("".join(p))
                    for p in sorted(list(perms)):
                        st.write(p)
            else:
                st.write("Too many permutations to display.")

    elif demo_type == "Combinations with Repetition":
        n = st.number_input(
            "Enter n (number of types):", min_value=1, max_value=10, value=3, step=1
        )
        r = st.number_input(
            "Enter r (number to choose):", min_value=1, max_value=10, value=2, step=1
        )
        if st.button("Calculate Combinations with Repetition"):
            result = comb(n + r - 1, r)
            st.write(f"Number of combinations with repetition: {result}")

            with st.expander("Show Example Combinations"):
                if n <= 5 and r <= 5:
                    items = list(range(1, n + 1))
                    combinations_list = []

                    # 5. Corrected Combination Generation: Uses a recursive helper function.
                    def find_combinations(current_combination, remaining, start_index):
                        if remaining == 0:
                            combinations_list.append(tuple(sorted(current_combination)))
                            return
                        for i in range(start_index, n + 1):
                            find_combinations(
                                current_combination + [i], remaining - 1, i
                            )

                    find_combinations([], r, 1)  # Start index is now used correctly
                    for c in sorted(
                        list(set(combinations_list))
                    ):  # removes duplicates and sorts
                        st.write(str(c))  # Consistent string output

                else:
                    st.write("Too many combinations to display.")
    elif demo_type == "Stars and Bars":
        # 6. Stars and Bars Visualization:  Illustrates the concept graphically.
        n = st.number_input(
            "Enter n (number of identical objects, e.g., candies):",
            min_value=1,
            max_value=15,
            value=5,
            step=1,
        )
        k = st.number_input(
            "Enter k (number of distinct containers, e.g., children):",
            min_value=1,
            max_value=10,
            value=3,
            step=1,
        )

        if st.button("Visualize Stars and Bars"):
            result = comb(n + k - 1, k - 1)  # Or comb(n + k - 1, n)
            st.write(f"Number of ways to distribute: {result}")

            # Create a visual representation of one possible distribution
            stars = ["*"] * n
            bars = ["|"] * (k - 1)
            example_arrangement = []
            # Randomly interleave stars and bars for *one* example distribution
            indices = sorted(np.random.choice(n + k - 1, k - 1, replace=False))
            star_idx = 0
            bar_idx = 0
            for i in range(n + k - 1):
                if bar_idx < len(indices) and i == indices[bar_idx]:
                    example_arrangement.append(bars[bar_idx])
                    bar_idx += 1
                else:
                    example_arrangement.append(stars[star_idx])
                    star_idx += 1

            st.write("Example Distribution:")
            st.write(" ".join(example_arrangement))  # Display the stars and bars
            st.write("Where '*' represents an object and '|' separates the containers.")

    st.header("💪 Practice Exercises")
    st.write(
        "Apply your combinatorics knowledge to these problems:"
    )  # More engaging prompt
    st.markdown(
        """
    1.  **Book Arrangement:** How many ways can you arrange 5 distinct books on a shelf?
    2.  **Pizza Toppings:** A pizza shop offers 8 toppings.  How many different *3-topping* pizzas are possible (assuming no double toppings)?
    3.  **Word Permutations:** How many distinct arrangements of the letters in the word 'BANANA' are there?
    4.  **Ice Cream Scoops:** You have 4 flavors of ice cream. You can get 3 scoops, and you *can* repeat flavors. How many different combinations of scoops are possible?
    """
    )  # Used markdown for better formatting

    if st.button("Show Answers and Explanations"):
        st.markdown(
            """
        1.  **Book Arrangement:** 5! = 120 (This is a permutation: order matters)
            *   **Explanation:** You have 5 choices for the first book, 4 for the second, 3 for the third, 2 for the fourth, and 1 for the last.  5 * 4 * 3 * 2 * 1 = 120

        2.  **Pizza Toppings:** 8C3 = 56 (This is a combination: order *doesn't* matter)
            *   **Explanation:**  We're choosing 3 toppings out of 8, and the order we choose them in doesn't change the pizza.  8! / (3! * 5!) = 56

        3.  **Word Permutations:** 6! / (3! * 2! * 1!) = 60 (Permutation with repetition)
            *   **Explanation:** We have 6 letters total, with 'A' repeated 3 times, 'N' repeated twice, and 'B' once.  We divide by the factorials of the repetition counts.

        4.  **Ice Cream Scoops:** (4 + 3 - 1)C3 = 6C3 = 20 (Combination with repetition)
            *    **Explanation:** This uses the formula for combinations with repetition: _(n+r-1)Cr_, where *n* is the number of types (flavors) and *r* is the number to choose (scoops).
        """
        )

    st.header("🌍 Real-world Applications")
    st.markdown(
        """
    Combinatorics is surprisingly prevalent in various fields:

    *   **Probability:** Calculating probabilities often fundamentally relies on counting favorable and total outcomes, which is pure combinatorics.
    *   **Computer Science:**
        *   **Algorithm Analysis:** Determining the efficiency of algorithms (e.g., counting comparisons in sorting algorithms, analyzing time complexity).
        *   **Data Structures:** Counting the number of possible data structures of a given type (e.g., binary trees).
        *   **Cryptography:** Analyzing the strength of encryption schemes (counting possible keys, analyzing attack complexity).
    *   **Product Analytics:**
        *   **A/B Testing:** Determining the number of possible test variations (combinations of different elements).
        *   **UI/UX Design:** Counting the number of ways to arrange elements on a screen or within a navigation flow.
        *   **Feature Combinations:** Analyzing how many combinations of features a user might interact with.  This helps understand user behavior and feature importance.
    *   **Operations Research:** Optimizing resource allocation, scheduling, and logistics (e.g., finding the number of possible routes).
    *   **Bioinformatics:** Analyzing DNA sequences and protein structures (counting combinations of nucleotides or amino acids).
    *   **Game Theory:** Calculating the number of possible game states or strategies.
    *   **Network Design:** Calculating the number of possible network topologies or connections.
    """
    )

    st.header("✅ Knowledge Check")
    # 7. Improved Feedback and Solutions: Provides feedback and detailed solutions.
    quiz_questions = [
        {
            "question": "What is the value of 6! (6 factorial)?",
            "options": ["6", "36", "120", "720"],
            "answer": "720",
            "solution": "6! = 6 * 5 * 4 * 3 * 2 * 1 = 720",
        },
        {
            "question": "How many ways can you choose a committee of 3 people from a group of 10?",
            "options": ["30", "120", "720", "1000"],
            "answer": "120",
            "solution": "This is a combination problem (order doesn't matter).  We use _10C3_ = 10! / (3! * 7!) = (10 * 9 * 8) / (3 * 2 * 1) = 120",
        },
        {
            "question": "How many different ways can you arrange the letters in the word 'APPLE'?",
            "options": ["120", "60", "24", "5"],
            "answer": "60",
            "solution": "This is a permutation with repetition.  There are 5 letters total, with 'P' repeated twice.  The formula is 5! / 2! = (5 * 4 * 3 * 2 * 1) / (2 * 1) = 60",
        },
        {
            "question": "Which principle states that if you have more pigeons than pigeonholes, at least one pigeonhole must have more than one pigeon?",
            "options": [
                "Sum Rule",
                "Product Rule",
                "Pigeonhole Principle",
                "Inclusion-Exclusion Principle",
            ],
            "answer": "Pigeonhole Principle",
            "solution": "The Pigeonhole Principle states exactly this.  It's a simple but powerful concept for proving existence.",
        },
        {
            "question": "What is the formula for combinations *with* repetition (choosing *r* items from *n* types with replacement)?",
            "options": ["_nPr_", "_nCr_", "_(n+r-1)Cr_", "n! / (r! * (n-r)!)"],
            "answer": "_(n+r-1)Cr_",
            "solution": "The formula for combinations with repetition is _(n+r-1)Cr_, which is equivalent to _(n+r-1)C(n-1)_.  This represents choosing *r* items from *n* types, allowing repetition.",
        },
        {
            "question": "In how many ways can you arrange 4 different cars in a line?",
            "options": ["4", "8", "16", "24"],
            "answer": "24",
            "solution": "This is a permutation of 4 objects taken 4 at a time: _4P4_ = 4! = 4 * 3 * 2 * 1 = 24",
        },
        {
            "question": "A pizza shop offers 5 toppings. You want exactly 2 *different* toppings. How many combinations are there?",
            "options": ["5", "10", "20", "25"],
            "answer": "10",
            "solution": "This is a combination (order doesn't matter): _5C2_ = 5! / (2! * 3!) = (5 * 4) / (2 * 1) = 10",
        },
        {
            "question": "You have 3 types of fruit (apples, bananas, oranges).  You want to choose 4 pieces of fruit.  You can choose multiple of the same type.  How many combinations are there?",
            "options": ["7", "15", "84", "12"],
            "answer": "15",
            "solution": "This is a combination *with* repetition: _(n+r-1)Cr_ = _(3+4-1)C4_ = _6C4_ = _6C2_ = 6! / (2! * 4!) = (6*5)/2 = 15",
        },
        {
            "question": "How many distinct permutations are there of the letters in the word 'STATISTICS'?",
            "options": ["3628800", "5040", "50400", "3360"],
            "answer": "50400",
            "solution": "This is a permutation with repetition.  There are 10 letters with: S (3 times), T (3 times), A (1 time), I (2 times), C (1 time).  The formula is 10! / (3! * 3! * 1! * 2! * 1!) = 50400",
        },
        {
            "question": "You are creating an 8-character password. You can use uppercase letters (A-Z), lowercase letters (a-z), and digits (0-9). How many possible passwords are there?",
            "options": ["8^62", "62^8", "8 * 62", "8!"],
            "answer": "62^8",
            "solution": "Each of the 8 characters has 62 possibilities (26 uppercase + 26 lowercase + 10 digits).  By the product rule, there are 62 * 62 * ... (8 times) = 62^8 possibilities.",
        },
        {
            "question": "What is the coefficient of x^2*y^3 in the expansion of (x + y)^5?",
            "options": ["5", "10", "20", "1"],
            "answer": "10",
            "solution": "By the Binomial Theorem, the coefficient of x^(n-k) * y^k in (x + y)^n is _nCk_.  Here, n=5, k=3, so we have _5C3_ = 5! / (3! * 2!) = 10.",
        },
        {
            "question": "A company is A/B testing 3 different website headlines and 2 different button colors. How many total test variations are there?",
            "options": ["5", "6", "9", "3^2"],
            "answer": "6",
            "solution": "This is a direct application of the product rule: 3 headline choices * 2 color choices = 6 total variations.",
        },
        {
            "question": "What does 0! (zero factorial) equal?",
            "options": ["0", "1", "Undefined", "Infinity"],
            "answer": "1",
            "solution": "0! is defined to be 1. This is necessary for many combinatorial formulas to work correctly.",
        },
        {
            "question": "You are distributing 5 identical candies to 3 children. How many ways can you do this?",
            "options": ["10", "15", "21", "120"],
            "answer": "21",
            "solution": "This is a stars and bars problem.  We have 5 candies (stars) and 2 dividers (bars) to separate the candies among the 3 children.  The formula is _(n+k-1)C(k-1)_, where n=5 and k=3.  So, _(5+3-1)C(3-1)_ = _7C2_ = 7! / (2! * 5!) = 21",
        },
        {
            "question": "When is the order of selection important?",
            "options": ["Combinations", "Permutations", "Factorials", "Stars and Bars"],
            "answer": "Permutations",
            "solution": "Permutations are arrangements where the order of the objects matters. Combinations are selections where order *doesn't* matter.",
        },
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(
            "Select an answer:", question["options"], key=f"quiz_{i}"
        )
        user_answers.append(user_answer)

    # 8.  Store Results:  Keep track of correct/incorrect answers.
    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1

        # 9.  Provide Overall Feedback:  Show score and summary.
        st.write(
            f"You got {correct_count} out of {len(quiz_questions)} questions correct."
        )

        # 10. Detailed Solutions: Show solutions for *all* questions.
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
