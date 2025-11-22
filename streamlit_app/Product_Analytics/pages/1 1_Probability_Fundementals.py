import random
from itertools import product  # for sample space generation

import pandas as pd
import plotly.express as px  # For Venn Diagram and other charts
import streamlit as st


def generate_dice_roll(num_rolls=1):
    """Simulates dice rolls and returns outcomes.

    Args:
        num_rolls (int): The number of dice rolls to simulate.

    Returns:
        list: A list of integer outcomes from each dice roll (1 to 6).
    """
    return [random.randint(1, 6) for _ in range(num_rolls)]


def calculate_empirical_probability(outcomes, event):
    """Calculates empirical probability of an event given outcomes.

    Args:
        outcomes (list): A list of outcomes from an experiment.
        event (function): A function that takes an outcome and returns True if it's a favorable outcome for the event, False otherwise.

    Returns:
        float: The empirical probability of the event.
    """
    favorable_outcomes = sum(1 for outcome in outcomes if event(outcome))
    total_outcomes = len(outcomes)
    if total_outcomes == 0:
        return 0
    return favorable_outcomes / total_outcomes


def main():
    st.set_page_config(page_title="Probability Theory", page_icon="🎲", layout="wide")

    st.title("Introduction to Probability Theory")
    st.write(
        "Explore the fundamentals of probability, from basic concepts to real-world applications. Master the language of chance and uncertainty."
    )

    with st.expander("📖 Foundational Concepts"):
        st.markdown(
            """
        ### 1. Experiments, Sample Spaces, and Events
        Probability is the math of chance!  Let's start with the basics:

        *   **Experiment:** Any process that can be repeated and has a set of possible outcomes that are well-defined.
            *   *Example:* 🌿 Planting a seed and observing if it sprouts, 🪙 Flipping a coin, 🎲 rolling a die, 🃏 drawing a card.
        *   **Sample Space (S):** The set of **all** possible outcomes of an experiment. Think of it as the universe of possibilities for your experiment.
            *   *Example (Coin Flip):* S = {Heads, Tails} or more formally S = {H, T}
            *   *Example (Die Roll):* S = {1, 2, 3, 4, 5, 6}
        *   **Event (E):** A subset of the sample space. It's a specific outcome or a group of outcomes you're interested in. Think of it as a question about the sample space.
            *   *Example (Die Roll, Event of rolling an even number):* E = {2, 4, 6}.  Question: "Did we roll an even number?"

        ### 2. Defining Events: Simple, Compound, Mutually Exclusive, Exhaustive
        Events can be categorized further:

        *   **Simple Event:** An event with only **one** outcome.  It's the most basic type of event.
            *   *Example (Die Roll):*  Rolling a '3' is simple because there's only one way to roll a 3. E = {3}
            *   **Visual:**  Imagine a Venn Diagram where Event E is just a single point within the Sample Space S.
        *   **Compound Event:** An event with **more than one** outcome. It's made up of multiple simple events.
            *   *Example (Die Roll):* Rolling an even number is compound: E = {2, 4, 6}
            *   **Visual:**  Event E in a Venn Diagram now contains multiple points from within S.
        *   **Mutually Exclusive Events:** Events that **cannot happen at the same time**. If one occurs, the others are impossible in the same trial. Their intersection (overlap) is empty.
            *   *Example (Coin Flip - single flip):* Getting Heads and getting Tails are mutually exclusive. You can't get both on one flip.
            *   **Visual:**  In a Venn Diagram, Event A and Event B are separate circles with NO overlap.
        *   **Exhaustive Events:** A set of events that **covers the entire sample space**. At least one of them *must* occur when the experiment is performed. Their union (combination) is the whole sample space.
            *   *Example (Die Roll):*  Let E1 be rolling a number less than 4 (E1={1, 2, 3}) and E2 be rolling a number 4 or greater (E2={4, 5, 6}). E1 and E2 are exhaustive because *every* possible die roll (1, 2, 3, 4, 5, or 6) is in either E1 or E2 (or both in some cases, but in this case, *or* E1 *or* E2 covers all possibilities).  Another example: E1={Even}, E2={Odd} are also exhaustive for a die roll.
            *   **Visual:**  In a Venn Diagram, Event A and Event B circles combined *completely fill* the Sample Space S rectangle.

        ### 3. Set Theory and Probability
        Probability uses the language of **set theory** to precisely describe and work with events.

        *   **Set Theory in Probability:**
            *   **Union (∪ - "OR"):**  Event A ∪ B (A **or** B or both) -  Probability of A or B or both occurring:  `P(A ∪ B)`.  Includes all outcomes in A, all in B, and those in both.
                *   **Venn Diagram:** Shaded area includes both circles A and B, and their overlap.
            *   **Intersection (∩ - "AND"):** Event A ∩ B (A **and** B) - Probability of both A and B occurring: `P(A ∩ B)`. Only includes outcomes that are in *both* A and B.
                *   **Venn Diagram:** Shaded area is only the overlapping part of circles A and B.
            *   **Complement (A' - "NOT"):** Event A' (**not** A) - Probability of event A *not* occurring: `P(A')`. Includes all outcomes in the Sample Space S that are *NOT* in A.
                *   **Venn Diagram:** Shaded area is everything in the rectangle S *outside* of circle A.
        *   **Venn Diagrams:** Powerful visual tools to understand sample spaces, events, and their relationships.

        ### 4. Axioms of Probability: The Rules of the Game 📜
        Think of these as the unshakeable rules that *any* valid probability system must follow.  They ensure probability behaves logically.

        *   **Axiom 1: Non-negativity:** For any event E, the probability of E is always zero or positive:  `P(E) ≥ 0`.  Probabilities can't be negative – it doesn't make sense to have a -0.5 chance of something.
        *   **Axiom 2: Probability of Sample Space:** The probability of the entire sample space S is always exactly 1: `P(S) = 1`. This means that when you perform an experiment, *some* outcome from the sample space *must* happen. Probability of 1 represents certainty.
        *   **Axiom 3: Additivity for Mutually Exclusive Events:** If you have a group of mutually exclusive events (like E1, E2, E3,... which can't happen together), the probability that *any* of them happen is simply the sum of their individual probabilities:  `P(E1 ∪ E2 ∪ E3 ∪ ...) = P(E1) + P(E2) + P(E3) + ...`
            *   *Example:* Probability of rolling a 1 OR a 2 on a die = P(rolling a 1) + P(rolling a 2) = 1/6 + 1/6 = 2/6.

        These three axioms are the foundation of all probability theory. Every probability calculation and rule you'll learn is built upon these basic principles.  They guarantee that our system of assigning probabilities is consistent and makes logical sense.

        """
        )

    with st.expander("🎲 Types of Probability: Different Ways to Find the Chance"):
        st.markdown(
            """
        ### 1. Classical Probability (Theoretical Probability):  Perfect Worlds 🔮

        *   **Definition:**  This is probability in its purest, most ideal form. It's used when you can assume all possible outcomes are **equally likely**.  This often applies to fair games of chance.
        *   **Formula:**  `P(Event) = (Number of favorable outcomes) / (Total number of possible outcomes)`
        *   **Example (Fair Die):** Probability of rolling a '4' on a fair six-sided die.
            *   Favorable outcomes: {4}  (Just one outcome – rolling a 4)
            *   Total possible outcomes: {1, 2, 3, 4, 5, 6} (Six equally likely outcomes)
            *   P(rolling a '4') = 1/6  ≈ 0.167

        *   **When to Use:**  Ideal for situations with symmetry and fairness, like coins, dice, cards, and perfectly random selections.
        *   **Limitation:**  The real world isn't always fair or symmetrical.  Many situations don't have equally likely outcomes.

        ### 2. Empirical Probability (Experimental Probability):  Learning from Experience 🔬

        *   **Definition:**  Probability based on **real-world observations and experiments**.  Instead of assuming fairness, we look at what actually *happens* when we repeat an experiment many times.  This is probability grounded in data.
        *   **Formula:** `P(Event) ≈ (Number of times event occurred in experiment) / (Total number of trials)`
        *   **Example (Biased Coin):** Imagine you have a coin that you suspect is bent.  To find the probability of getting heads, you flip it 1000 times and observe that it lands on heads 550 times.
            *   Number of times "Heads" occurred: 550
            *   Total number of flips (trials): 1000
            *   Empirical P(Heads) ≈ 550/1000 = 0.55

        *   **When to Use:** When you can perform experiments or have historical data, and you *cannot* assume equally likely outcomes.  This is crucial in science, engineering, and many real-world applications where we learn probabilities from data.
        *   **Key Idea:** Empirical probability gets closer to the "true" probability as you perform more and more trials (Law of Large Numbers).

        ### 3. Subjective Probability (Bayesian Probability - Introduction):  Personal Beliefs 🧠 (and Updating Them!)

        *   **Definition:** Probability as a measure of **personal belief or confidence** in the occurrence of an event. It's based on your own judgment, experience, and available (often incomplete) information. It acknowledges that probability isn't always just about numbers from experiments, but also about *degrees of certainty*.
        *   **Use Cases:** Situations where there's no repeatable experiment or equally likely outcomes, and data might be scarce or uncertain.
            *   *Examples:* Predicting the success of a brand new product launch, estimating the probability of a specific political candidate winning an election, judging the likelihood of rain based on current weather conditions.
        *   **Bayesian Probability (Introduction):** The beauty of subjective probability, especially in its Bayesian form, is that it allows you to **update your initial beliefs (prior probabilities) as you get new evidence**. Bayes' Theorem is the mathematical tool for this updating process.
            *   *Think of it as:* Starting with a guess (prior), then refining your guess based on what you observe (evidence) to get a more informed belief (posterior).

        *   **Example (Startup Success):**  Before launching a tech startup, an entrepreneur might subjectively estimate a 60% probability of success based on market research and their team's expertise (prior probability).  After the first year (new evidence), if they see strong user growth and positive reviews, they might *revise* their subjective probability of long-term success upwards (posterior probability).

        *   **Key Idea:** Subjective probability is not arbitrary guesswork.  It's about making the best possible probability judgment based on all available knowledge, and being ready to adjust those judgments as you learn more. Bayesian methods provide a rigorous way to do this.

        """
        )

        st.subheader("Interactive Demo: Empirical Probability with Dice Rolls 🎲")
        num_dice_rolls = st.slider(
            "Number of Dice Rolls:",
            min_value=10,
            max_value=10000,
            value=1000,
            step=100,
            help="Increase rolls for empirical probability to approach theoretical (1/6)",
        )
        target_number = st.selectbox(
            "Event: Rolling a Number:",
            [1, 2, 3, 4, 5, 6],
            index=3,
            help="Select which number you want to calculate the empirical probability for",
        )  # Default to 4

        if st.button("Simulate Dice Rolls"):
            with st.spinner(f"Rolling dice {num_dice_rolls} times..."):
                dice_outcomes = generate_dice_roll(num_dice_rolls)
                event_probability = calculate_empirical_probability(
                    dice_outcomes, lambda x: x == target_number
                )
                theoretical_probability = 1 / 6  # For a fair die

                st.write(
                    f"Empirical Probability (after {num_dice_rolls:,} rolls): **{event_probability:.4f}**"
                )
                st.write(
                    f"Classical (Theoretical) Probability: **{theoretical_probability:.4f}**"
                )
                st.write(
                    "*Notice how as you increase the number of rolls, the empirical probability gets closer to the theoretical probability (Law of Large Numbers)*"
                )

                counts = pd.Series(dice_outcomes).value_counts().sort_index()
                fig = px.bar(
                    x=counts.index,
                    y=counts.values,
                    labels={"x": "Dice Outcome", "y": "Frequency"},
                    title="Distribution of Dice Roll Outcomes",
                )  # plotly for interactive chart
                st.plotly_chart(fig, use_container_width=True)

    with st.expander(
        " 🧮 Conditional Probability and Independence: When Knowledge Changes Everything"
    ):
        st.markdown(
            """
        ### 1. Conditional Probability: The Impact of Prior Knowledge 💡

        *   **Definition:**  Conditional probability is about **changing probabilities when you learn new information**. It's the probability of an event A happening, *given that* we already know another event B has happened (or is assumed to have happened).  Written as `P(A|B)` (read as "probability of A *given* B").
        *   **Formula:**  `P(A|B) = P(A ∩ B) / P(B)`,  **important:**  this only works if `P(B) > 0` (you can't condition on something impossible).
        *   **Intuition:**  Knowing that event B occurred can drastically change the probability of event A.  Think of it as narrowing down your focus.  Event B effectively **reduces the sample space** to only the outcomes where B has occurred.  Within this *smaller* sample space, we then calculate the probability of A.
        *   **Example (Drawing Cards - revisited):**  Imagine you draw a card from a standard deck, but you don't look at it. Someone else peeks and tells you, "It's a face card (Jack, Queen, or King)."  Now, what's the probability that the card you drew is a King? This is conditional probability because you have *new information*.
            *   Event A: Drawing a King
            *   Event B: Drawing a Face Card (we *know* this happened)
            *   `P(A ∩ B)`: Probability of drawing a card that is both a King *and* a Face Card.  If a card is a King, it's automatically a face card, so  `P(A ∩ B) = P(Drawing a King) = 4/52` (4 Kings in a deck).
            *   `P(B)`: Probability of drawing a Face Card = 12/52 (12 face cards: Jacks, Queens, Kings of all suits).
            *   `P(A|B) = P(A ∩ B) / P(B) = (4/52) / (12/52) = 4/12 = 1/3`  ≈ 0.333
            *   **Before knowing it was a face card**, P(Drawing a King) = 4/52 ≈ 0.077.
            *   **After knowing it's a face card**, P(Drawing a King | Face Card) = 1/3 ≈ 0.333.
            *   **See how the probability of drawing a King *significantly increased* because of the new information (it's a face card)?**

        ### 2. Bayes' Theorem: Reversing Conditional Probability - The Power of Updating Beliefs 🔄

        *   **Formula:** `P(A|B) = [P(B|A) * P(A)] / P(B)`
        *   **Purpose:**  Bayes' Theorem is like a **probability "reverse gear"**.  It lets you calculate `P(A|B)` (probability of A given B) when it's *easier to know* (or estimate) `P(B|A)` (probability of B given A), along with the individual probabilities `P(A)` and `P(B)`.  It's all about updating probabilities as you get new evidence!
        *   **Components - Unpacking the Formula:**
            *   `P(A|B)`: **Posterior probability** (probability of A *after* considering B) - This is what you want to find – your updated belief about A.
            *   `P(B|A)`: **Likelihood** (probability of B *given* A) - This is often easier to know or calculate directly.  It's how likely the evidence (B) is if A is true.
            *   `P(A)`: **Prior probability** (probability of A *before* considering B) - Your initial belief about A *before* you saw the evidence.
            *   `P(B)`: **Evidence** (probability of B) - This acts as a normalizing constant to make sure the probabilities add up correctly.  It's the overall probability of seeing the evidence B, regardless of whether A is true or not.  You can often calculate it using the Law of Total Probability: `P(B) = P(B|A)P(A) + P(B|A')P(A')`

        *   **Example (Medical Testing - Deeper Dive):** Let's understand Bayes' Theorem with the medical test example more fully. A test for a rare disease is 95% accurate.  The disease prevalence is 1% (rare!). If someone tests positive, what's the *actual* probability they have the disease? (This is surprisingly low!)
            *   Event A: Person *has* the disease.  `P(A) = 0.01` (prior probability - prevalence in population is low)
            *   Event A': Person *does not* have the disease. `P(A') = 1 - 0.01 = 0.99`
            *   Event B: Test result is **positive**.
            *   `P(B|A)`: Probability of a **positive test *given* the person has the disease** (true positive rate) = 0.95 (test accuracy)
            *   `P(B|A')`: Probability of a **positive test *given* the person does *not* have the disease** (false positive rate) = `1 - 0.95 = 0.05` (because accuracy is 95%, so 5% false positives)
            *   `P(B)` (Evidence): Probability of getting a positive test result overall.  We use the Law of Total Probability to find this:
                `P(B) = P(B|A)P(A) + P(B|A')P(A') = (0.95 * 0.01) + (0.05 * 0.99) = 0.0095 + 0.0495 = 0.059`

            *   Now, apply Bayes' Theorem to find the **posterior probability**:  `P(A|B)` (probability of having the disease *given* a positive test):
                `P(A|B) = [P(B|A) * P(A)] / P(B) = (0.95 * 0.01) / 0.059 ≈ 0.161`  ≈ 16.1%

            *   **Surprising Result!** Even with a 95% accurate test and a positive result, there's only about a 16.1% chance the person *actually has* the disease.  Why so low? Because the disease is rare (low prior probability).  False positives become significant in this case! Bayes' Theorem helps to correctly interpret test results, especially for rare conditions.

        ### 3. Independence of Events: When Events Don't Influence Each Other 🕊️

        *   **Definition:** Two events A and B are **independent** if the occurrence (or non-occurrence) of one event **does not change the probability** of the other event occurring. They have no influence on each other.
        *   **Condition for Independence (Mathematical Test):**  Events A and B are independent **if and only if** `P(A ∩ B) = P(A) * P(B)`
            *   Another way to think about it: If A and B are independent, then knowing B happened doesn't change the probability of A:  `P(A|B) = P(A)` (as long as P(B) > 0). Similarly, `P(B|A) = P(B)`.

        *   **Example (Coin Flips - Independent Trials):** Each coin flip is independent of the others.  The outcome of the first flip has absolutely no effect on the outcome of the second flip.
            *   Probability of getting Heads on 1st flip **AND** Heads on 2nd flip (both events happening) *if they are independent* = `P(Heads on 1st flip) * P(Heads on 2nd flip) = (1/2) * (1/2) = 1/4`

        *   **Important Note:**  Don't confuse "mutually exclusive" with "independent".  Mutually exclusive events *cannot* happen together. Independent events *can* happen together, but one doesn't influence the other's probability.  In fact, if two events with non-zero probabilities *are* mutually exclusive, they *cannot* be independent (because if one happens, the probability of the other becomes 0!).

        """
        )

        st.markdown("---")  # Separator for emphasis
        st.markdown("**Key Takeaways on Conditional Probability and Independence:**")
        st.markdown(
            "*   **Conditional Probability:** Probabilities change when you have new information. `P(A|B)` is the probability of A given B is known."
        )
        st.markdown(
            "*   **Bayes' Theorem:**  A powerful tool to *reverse* conditioning and update beliefs based on evidence.  Crucial for interpreting data and making informed decisions in uncertain situations."
        )
        st.markdown(
            "*   **Independence:** Events are independent when one doesn't affect the other's probability. Mathematically checked by: `P(A ∩ B) = P(A) * P(B)`."
        )

    with st.expander("📊 Random Variables: Bridging Outcomes to Numbers"):
        st.markdown(
            """
        ### 1. Definition of a Random Variable: Quantifying Randomness 🔢

        *   **Definition:** A **random variable** is the bridge between the abstract world of sample spaces and the concrete world of numbers.  It's a **variable** (something that can take on different values), but its value is a **numerical outcome** from a **random phenomenon** (experiment).  Formally, it's a function that maps outcomes in the sample space to real numbers.
        *   **Think of it as:**  You perform a random experiment. The outcome isn't directly a number, but you *define* a rule to assign a number to each outcome. This rule is your random variable.
        *   **Notation:** We use uppercase letters like X, Y, Z to represent random variables themselves.  Lowercase letters (x, y, z) represent specific *values* that a random variable can take.
        *   **Example (Coin Flips - Number of Heads):**  Consider flipping a fair coin **twice**.
            *   Sample Space:  `S = {HH, HT, TH, TT}` (These are the outcomes, not numbers yet)
            *   Let **X be the random variable** representing the **number of heads** in two flips.  (We're turning outcomes into numbers!)
            *   Possible values of X:  `0, 1, 2` (These are the numbers X can be)
            *   Mapping (how outcomes link to values of X):
                *   `X(TT) = 0`  (Outcome TT (no heads) gets mapped to the number 0)
                *   `X(HT) = 1, X(TH) = 1` (Outcomes HT and TH (one head) both get mapped to the number 1)
                *   `X(HH) = 2`  (Outcome HH (two heads) gets mapped to the number 2)

            *   **In short:**  X takes the *non-numerical outcomes* of coin flips (HH, HT, TH, TT) and turns them into *numerical values* (0, 1, 2) representing the count of heads.  *X is the rule for this conversion*.

        ### 2. Types of Random Variables: Discrete vs. Continuous - Counting or Measuring? 📏

        Random variables are broadly classified into two main types, based on the *nature of the values they can take on*:

        *   **Discrete Random Variable:**  Think "counting".  A discrete RV can only take on a **countable number of distinct values**.  Usually, these are integers (whole numbers), and the set of possible values is often finite, or countably infinite (you can list them out, even if the list goes on forever).
            *   *Examples:*
                *   **Number of heads** in 10 coin flips (possible values: 0, 1, 2, ..., 10 - finite list).
                *   **Number of defective items** in a batch of manufactured goods (possible values: 0, 1, 2, ... up to batch size - finite list).
                *   **Number of customers arriving** at a store in an hour (possible values: 0, 1, 2, 3, ... - countably infinite, integers starting from 0).
            *   **Key characteristic:** Values are separate, distinct points on the number line – you can "count" them. You can't have values "in-between" the possible values in a meaningful way (e.g., you can't have 2.5 heads).

        *   **Continuous Random Variable:** Think "measuring". A continuous RV can take on **any value within a given range or interval**.  The possible values are uncountable.
            *   *Examples:*
                *   **Height of a person** (can be 1.75 meters, 1.753 meters, 1.7531 meters, and so on – values between 1.5m and 2.1m, for instance, are infinitely many).
                *   **Temperature of a room** (can be 22.3 degrees Celsius, 22.35 degrees, 22.357 degrees...).
                *   **Time until a light bulb burns out** (can be 1000 hours, 1000.5 hours, 1000.52 hours...).
                *   **Weight of a product**
            *   **Key characteristic:** Values can fall anywhere along a continuous scale. Between any two possible values, there are infinitely many other possible values.

        *   **Analogy:**  Think of stairs (discrete - you can only stand on specific steps) vs. a ramp (continuous - you can be at any point along the ramp).

        """
        )

    with st.expander(
        " 🚀 Advanced Topics in Probability (Brief Overview): Beyond the Basics"
    ):
        st.markdown(
            """
        Probability theory is a vast and deep field.  This introduction just scratches the surface.  Here's a very brief glimpse into a few advanced areas that build upon these foundations and are essential in cutting-edge data science, AI, and beyond:

        ### 1. Bayesian Inference:  Probability as a Dynamic Learning Process 🔄

        *   **Building on Bayes' Theorem:** Bayesian inference isn't just about applying Bayes' Theorem once.  It's a complete **framework for statistical inference and learning from data**.  It sees probability as representing degrees of belief that are *updated* as new evidence comes in.  It's a dynamic, iterative process.
        *   **Subjective Probabilities and Priors - Embracing Prior Knowledge:** Bayesian methods explicitly incorporate **prior beliefs** (prior probabilities) about parameters or hypotheses *before* seeing any data. These priors are subjective – they reflect existing knowledge, expert opinions, or even just reasonable initial guesses.  The data then *modifies* these priors to give **posterior probabilities**, representing updated beliefs *after* observing the data.
        *   **Applications – Ubiquitous in Modern Data Science:** Bayesian inference is incredibly versatile and widely used:
            *   **Bayesian Statistics:**  A whole branch of statistics centered around Bayesian methods for estimation, hypothesis testing, and model comparison.
            *   **Machine Learning:**  Bayesian Neural Networks, Bayesian Optimization, Bayesian Nonparametrics – Bayesian approaches are increasingly used in ML to handle uncertainty, improve model robustness, and enable better decision-making.
            *   **Data Analysis and Decision-Making:**  Anywhere you need to update your understanding or make decisions in the face of uncertainty and new data, Bayesian methods offer a powerful framework.  From medical diagnosis to financial forecasting, from A/B testing to scientific hypothesis validation, Bayesian inference is at the core of modern data-driven reasoning.

        ### 2. Markov Chains and Markov Processes: Modeling Systems That Evolve Step-by-Step 🚶‍♂️➡️🚶‍♀️➡️🚶 (with a Short Memory)

        *   **Modeling Sequences of Events - Systems Changing over Time:** Markov Chains and Markov Processes are mathematical tools for modeling systems that **change state over time in a random way**.  Think of a system moving from one state to another in discrete steps (Markov Chains) or continuously (Markov Processes).
        *   **The Markov Property - "Memorylessness":** The defining feature is the **Markov property (or memorylessness)**.  It states that the probability of transitioning to the next state depends *only* on the **current state**, not on the *entire history* of how the system arrived at the current state.  The past history beyond the present state is irrelevant for predicting the future.
        *   **States and Transitions - Building Blocks:**  Markov models are built from:
            *   **States:**  The possible conditions or situations the system can be in (e.g., in a weather model, states could be "Sunny", "Rainy", "Cloudy").
            *   **Transition Probabilities:**  Probabilities of moving from one state to another in a single step (e.g., probability of transitioning from "Sunny" today to "Rainy" tomorrow).
        *   **Applications – Modeling Sequential Data in Diverse Fields:** Markov models are surprisingly versatile and find applications in:
            *   **Queuing Theory:** Modeling waiting times and queue lengths in systems like call centers or traffic flow.
            *   **Genetics:** Modeling DNA sequences and gene evolution.
            *   **Finance:**  Modeling stock price movements (though often simplified Markov models are used).
            *   **Speech Recognition:**  Recognizing phonemes (basic units of sound) in speech as sequences of states.
            *   **Web Page Ranking (PageRank Algorithm - Google's original search algorithm):**  Modeled web surfing as a Markov process, with web pages as states and links as transitions to rank page importance.

        ### 3. Stochastic Processes:  Randomness Unfolding Continuously - The Flow of Chance 🌊

        *   **Random Phenomena Evolving Continuously Over Time:**  Stochastic processes are the even more general concept – they are mathematical models for **random phenomena that evolve *continuously* through time**.  Think of things that are constantly fluctuating and randomizing, not just changing in discrete jumps.
        *   **Generalization of Random Variables - From Snapshots to Movies of Randomness:** They are a powerful **generalization of random variables**. While a random variable gives you a snapshot of a random quantity at a single point in time, a stochastic process describes how a random quantity *changes over a whole period of time*.  It's like moving from a single frame of a movie (random variable) to the entire movie itself (stochastic process).
        *   **Types - A Zoo of Random Behaviors:** There's a rich "zoo" of different types of stochastic processes, each suited to model different kinds of random behavior:
            *   **Brownian Motion (Wiener Process):**  Models random movements like the jittering of pollen grains in water (and, famously, stock prices in simplified financial models).  Characterized by continuous, erratic fluctuations.
            *   **Poisson Processes:** Model the random occurrence of discrete events over time, like customer arrivals at a store, radioactive decay events, or insurance claims.  Focus is on the *number* of events in a given time interval.
            *   **Gaussian Processes:**  A powerful tool in machine learning for modeling functions probabilistically.  Instead of just predicting a single value, they predict a *distribution* of possible function values, useful for uncertainty quantification in regression and classification.
            *   **And many more...** (Levy processes, jump-diffusion processes, etc.)

        *   **Applications – Modeling the Dynamic and Unpredictable:** Stochastic processes are indispensable for modeling systems that are inherently dynamic and unpredictable:
            *   **Finance (Advanced Financial Modeling):** Modeling asset prices more realistically than simple Markov models, including jumps, volatility clustering, and other complex features of financial markets.
            *   **Physics (Statistical Physics, Thermodynamics):**  Brownian motion is a cornerstone of statistical physics. Stochastic processes are used to model diffusion, heat transfer, and other phenomena involving random fluctuations at the molecular level.
            *   **Biology (Population Dynamics, Neuroscience):** Modeling population growth, spread of diseases, neural firing patterns in the brain – biological systems are often inherently noisy and stochastic.
            *   **Telecommunications (Network Traffic Modeling):**  Modeling the random fluctuations in network traffic to design efficient communication networks.
            *   **Operations Research (Inventory Control, Queuing Systems):**  Optimizing inventory levels in the face of uncertain demand, managing queues and waiting times in service systems – stochastic processes are key tools.
        """
        )

    with st.expander("📚 Resources for Further Learning: Dive Deeper! "):
        st.markdown(
            """
        To truly master probability theory, continuous learning and practice are key. Here are excellent resources to take you further:

        *   **Textbooks - For Deeper Study:**
            *   **"Introduction to Probability Models" by Sheldon Ross:**  A true classic. Comprehensive, clear, and covers a vast range of topics from basic to advanced. Excellent for undergraduate and graduate studies. Known for its many examples and applications.
            *   **"Probability and Statistics for Engineering and the Sciences" by Jay L. Devore:**  Specifically geared towards engineering and science students. Focuses on applications with many real-world examples in these fields. Strong on statistical methods as well as probability foundations.
            *   **"Bayesian Methods for Hackers" by Cameron Davidson-Pilon (Free Online!):** If you are particularly interested in Bayesian probability and statistics, this is an outstanding and *free* online book.  It's very practical, uses Python code examples throughout, and makes Bayesian concepts accessible and less intimidating.  [http://www.probabilistic-programming.org/](http://www.probabilistic-programming.org/)

        *   **Online Courses - Structured Learning with Videos and Exercises:**
            *   **Khan Academy Probability and Statistics:**  Absolutely fantastic **free** resource. Covers probability and statistics from very basic introductions up to advanced levels.  Excellent video lessons, practice exercises with immediate feedback, and a great way to build a solid foundation. [https://www.khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability)
            *   **Coursera and edX Platforms:**  These platforms host university-level probability and statistics courses from top universities around the world (Stanford, MIT, Harvard, etc.). Search for courses with titles like "Introduction to Probability", "Statistical Inference", "Probabilistic Machine Learning".  Many are audit-free, or offer certificates for a fee.

        *   **Websites and Articles - Concise Explanations and Broader Perspectives:**
            *   **Probability Theory (Stanford Encyclopedia of Philosophy):** If you are interested in a more conceptual and philosophical understanding of probability (different interpretations of probability, its foundations, etc.), this is an excellent resource.  Very detailed and rigorous. [https://plato.stanford.edu/entries/probability/](https://plato.stanford.edu/entries/probability/)
            *   **Seeing Theory: A Visual Introduction to Probability and Statistics:** A truly unique and highly recommended website. It uses **interactive visualizations** to explain complex probability and statistics concepts in a very intuitive and engaging way.  If you are a visual learner, this is a must-visit.  [https://seeingtheory.brown.edu/](https://seeingtheory.brown.edu/)
        """
        )

    """Generates the interactive portion of the Probability Theory Streamlit page."""
    st.header("🕹️ Interactive Probability Explorations")

    with st.expander("🎲 Sample Spaces and Events"):
        st.subheader("Exploring Sample Spaces and Events with Dice")
        experiment_type = st.selectbox(
            "Choose Experiment:", ["Single Die Roll", "Two Dice Roll"]
        )

        if experiment_type == "Single Die Roll":
            st.write("Sample Space (S) = {1, 2, 3, 4, 5, 6}")
            event_options = [
                "Even Number",
                "Odd Number",
                "Number Greater than 4",
                "Specific Number (Select Below)",
            ]
            selected_event_type = st.selectbox("Select an Event:", event_options)

            if selected_event_type == "Specific Number (Select Below)":
                specific_number = st.slider("Choose a Number:", 1, 6, 3)
                event_description = f"Event: Rolling a {specific_number}"
                event = {specific_number}
            elif selected_event_type == "Even Number":
                event_description = "Event: Rolling an Even Number"
                event = {2, 4, 6}
            elif selected_event_type == "Odd Number":
                event_description = "Event: Rolling an Odd Number"
                event = {1, 3, 5}
            elif selected_event_type == "Number Greater than 4":
                event_description = "Event: Rolling a Number Greater than 4"
                event = {5, 6}
            else:
                event_description = "Select an Event"
                event = set()

            if event:
                st.write(event_description)
                st.write("Event (E) =", event)
                sample_space = {1, 2, 3, 4, 5, 6}
                favorable_outcomes = event.intersection(sample_space)
                st.write("Favorable Outcomes (E ∩ S) =", favorable_outcomes)
                classical_probability = len(favorable_outcomes) / len(sample_space)
                st.write(f"Classical Probability: P(E) = {classical_probability:.3f}")

        elif experiment_type == "Two Dice Roll":
            st.write(
                "Sample Space (S) = {(1,1), (1,2), ..., (6,6)} - 36 possible outcomes"
            )
            event_options_two_dice = [
                "Sum is 7",
                "Sum is Even",
                "Both Dice Show Same Number",
                "Custom Event (Describe Below)",
            ]
            selected_event_two_dice = st.selectbox(
                "Select an Event:", event_options_two_dice
            )

            sample_space_two_dice = list(
                product(range(1, 7), range(1, 7))
            )  # Generate all pairs

            if selected_event_two_dice == "Sum is 7":
                event_description = "Event: Sum of Two Dice is 7"
                event = {
                    outcome for outcome in sample_space_two_dice if sum(outcome) == 7
                }
            elif selected_event_two_dice == "Sum is Even":
                event_description = "Event: Sum of Two Dice is Even"
                event = {
                    outcome
                    for outcome in sample_space_two_dice
                    if sum(outcome) % 2 == 0
                }
            elif selected_event_two_dice == "Both Dice Show Same Number":
                event_description = "Event: Both Dice Show the Same Number"
                event = {
                    outcome
                    for outcome in sample_space_two_dice
                    if outcome[0] == outcome[1]
                }
            elif selected_event_two_dice == "Custom Event (Describe Below)":
                custom_event_text = st.text_input(
                    "Describe your custom event based on two dice sum/values:"
                )
                event_description = f"Custom Event: {custom_event_text}"
                event = (
                    set()
                )  # Placeholder for truly custom event - advanced to implement fully here

            else:
                event_description = "Select an Event"
                event = set()

            if event:
                st.write(event_description)
                st.write(f"Number of outcomes in Event (E): {len(event)}")
                st.write(
                    f"Number of outcomes in Sample Space (S): {len(sample_space_two_dice)}"
                )
                classical_probability = len(event) / len(sample_space_two_dice)
                st.write(f"Classical Probability: P(E) = {classical_probability:.3f}")

    with st.expander("📊 Types of Probability"):
        st.subheader("Empirical vs. Classical Probability")
        st.write("Revisit the Dice Roll Simulation to compare:")
        num_dice_rolls_demo = st.slider(
            "Number of Dice Rolls for Demo:",
            min_value=10,
            max_value=10000,
            value=1000,
            step=100,
            key="empirical_demo_slider",
        )
        target_number_demo = st.selectbox(
            "Event: Rolling a Number (for Demo):",
            [1, 2, 3, 4, 5, 6],
            index=3,
            key="empirical_demo_selectbox",
        )

        if st.button("Run Probability Demo"):
            with st.spinner("Simulating..."):
                dice_outcomes_demo = generate_dice_roll(num_dice_rolls_demo)
                empirical_prob_demo = calculate_empirical_probability(
                    dice_outcomes_demo, lambda x: x == target_number_demo
                )
                theoretical_prob_demo = 1 / 6

                st.write(
                    f"Empirical Probability (after {num_dice_rolls_demo:,} rolls): **{empirical_prob_demo:.4f}**"
                )
                st.write(
                    f"Classical (Theoretical) Probability: **{theoretical_prob_demo:.4f}**"
                )
                st.info(
                    "Observe how empirical probability approaches classical probability as number of rolls increases."
                )

    with st.expander("🧮 Conditional Probability"):
        st.subheader("Card Drawing and Conditional Probability")
        card_condition_options = [
            "No Condition",
            "Given it's a Red Card",
            "Given it's a Face Card",
        ]
        selected_card_condition = st.selectbox(
            "Select Condition:", card_condition_options
        )
        event_to_calculate = st.selectbox(
            "Calculate Probability of:", ["Drawing a King", "Drawing a Heart"]
        )

        prob_conditional = 0  # Initialize
        if selected_card_condition == "No Condition":
            if event_to_calculate == "Drawing a King":
                prob_conditional = 4 / 52
            elif event_to_calculate == "Drawing a Heart":
                prob_conditional = 13 / 52
        elif selected_card_condition == "Given it's a Red Card":
            if event_to_calculate == "Drawing a King":
                prob_conditional = 2 / 26  # 2 red kings out of 26 red cards
            elif event_to_calculate == "Drawing a Heart":
                prob_conditional = 13 / 26  # All 13 hearts are red
        elif selected_card_condition == "Given it's a Face Card":
            if event_to_calculate == "Drawing a King":
                prob_conditional = 4 / 12  # 4 kings out of 12 face cards
            elif event_to_calculate == "Drawing a Heart":
                prob_conditional = (
                    3 / 12
                )  # 3 heart face cards (J, Q, K) out of 12 face cards

        st.write(
            f"Probability of {event_to_calculate} { 'with no condition' if selected_card_condition == 'No Condition' else f'given that {selected_card_condition[7:].lower()}' }: **{prob_conditional:.3f}**"
        )  # Dynamic output

    with st.expander("🔄 Bayes' Theorem"):
        st.subheader("Bayes' Theorem Calculator (Medical Test Example)")
        st.write(
            "Explore how prior probability and test accuracy affect posterior probability."
        )
        prevalence = st.slider(
            "Disease Prevalence (Prior Probability P(Disease)):",
            min_value=0.001,
            max_value=0.10,
            value=0.01,
            step=0.001,
            format="%.3f",
        )
        test_accuracy = st.slider(
            "Test Accuracy (P(Positive|Disease) and P(Negative|No Disease)):",
            min_value=0.90,
            max_value=0.999,
            value=0.95,
            step=0.001,
            format="%.3f",
        )

        p_disease = prevalence
        p_no_disease = 1 - p_disease
        p_positive_given_disease = test_accuracy
        p_negative_given_disease = 1 - test_accuracy
        p_positive_given_no_disease = 1 - test_accuracy  # False positive rate
        p_negative_given_no_disease = test_accuracy

        # Law of total probability - P(Positive)
        p_positive = (p_positive_given_disease * p_disease) + (
            p_positive_given_no_disease * p_no_disease
        )

        # Bayes' Theorem
        p_disease_given_positive = (
            (p_positive_given_disease * p_disease) / p_positive if p_positive > 0 else 0
        )

        st.write(
            f"Prior Probability of Disease (Prevalence): P(Disease) = {p_disease:.3f}"
        )
        st.write(
            f"Test Accuracy: P(Positive|Disease) = {p_positive_given_disease:.3f},  P(Negative|No Disease) = {p_negative_given_no_disease:.3f}"
        )
        st.write(
            f"Probability of Positive Test (Overall): P(Positive) = {p_positive:.3f}"
        )
        st.write(
            f"**Posterior Probability (Disease given Positive Test): P(Disease|Positive) = {p_disease_given_positive:.3f}**"
        )
        st.info(
            "Adjust sliders to see how prevalence and accuracy change the posterior probability. Notice how even with high accuracy, low prevalence leads to surprisingly low posterior probability."
        )

    with st.expander("📈 Random Variables: Discrete or Continuous?"):
        st.subheader("Identify Random Variable Types")
        rv_examples = [
            "Number of heads in 5 coin flips",
            "Height of a randomly selected person",
            "Number of cars passing a point on a highway per hour",
            "Temperature of a room",
            "Time it takes for a light bulb to burn out",
            "Shoe size of a randomly selected adult",
            "Weight of a bag of apples",
        ]
        selected_rv_example = st.selectbox(
            "Select a Random Variable Example:", rv_examples
        )
        variable_type = "Unknown"  # Initialize

        if (
            selected_rv_example == "Number of heads in 5 coin flips"
            or selected_rv_example
            == "Number of cars passing a point on a highway per hour"
            or selected_rv_example == "Shoe size of a randomly selected adult"
        ):
            variable_type = "Discrete"
        elif (
            selected_rv_example == "Height of a randomly selected person"
            or selected_rv_example == "Temperature of a room"
            or selected_rv_example == "Time it takes for a light bulb to burn out"
            or selected_rv_example == "Weight of a bag of apples"
        ):
            variable_type = "Continuous"

        st.write(f"You selected: **{selected_rv_example}**")
        st.write(f"This Random Variable is likely **{variable_type}**.")
        if variable_type == "Discrete":
            st.success(
                "Correct! Discrete random variables take countable values, often integers (counts)."
            )
        elif variable_type == "Continuous":
            st.success(
                "Correct! Continuous random variables can take any value within a range (measurements)."
            )
        else:
            st.warning("Try selecting an example to see its classification.")

    with st.expander("🎲🎲 Probability Distribution of Sum of Two Dice (Discrete RV)"):
        st.subheader("Explore the Probability Distribution of the Sum of Two Dice")
        st.write("Roll virtual dice and see the distribution of their sums emerge!")
        num_virtual_dice_rolls = st.slider(
            "Number of Virtual Dice Rolls:",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="dice_sum_slider",
        )

        if st.button("Simulate Two Dice Rolls and Show Distribution"):
            with st.spinner("Rolling virtual dice..."):
                two_dice_sums = [
                    sum(generate_dice_roll(num_rolls=2))
                    for _ in range(num_virtual_dice_rolls)
                ]  # Simulate sum of two dice
                sum_counts = pd.Series(two_dice_sums).value_counts().sort_index()

                theoretical_probs = {
                    i: 0 for i in range(2, 13)
                }  # Initialize theoretical probs dict
                for outcome in product(
                    range(1, 7), range(1, 7)
                ):  # All two dice combinations
                    theoretical_probs[sum(outcome)] += (
                        1 / 36
                    )  # 1/36 probability for each combination

                theoretical_df = pd.DataFrame(
                    list(theoretical_probs.items()),
                    columns=["Sum", "Theoretical Probability"],
                )
                empirical_df = pd.DataFrame(
                    {"Sum": sum_counts.index, "Empirical Frequency": sum_counts.values}
                )

                # Debugging: Explicitly cast 'Sum' to integer before merge and print columns
                empirical_df["Sum"] = empirical_df["Sum"].astype(int)
                theoretical_df["Sum"] = theoretical_df["Sum"].astype(int)
                st.write(
                    "Empirical DataFrame columns:", empirical_df.columns
                )  # Debugging
                st.write(
                    "Theoretical DataFrame columns:", theoretical_df.columns
                )  # Debugging

                merged_df = pd.merge(
                    empirical_df, theoretical_df, on="Sum", how="outer"
                ).fillna(
                    0
                )  # Merge and handle missing

                st.dataframe(merged_df)  # Debugging: Display merged dataframe

                fig_dice_sum = px.bar(
                    merged_df,
                    x="Sum",
                    y=["Empirical Frequency", "Theoretical Probability"],
                    barmode="group",
                    title=f"Distribution of Sums of Two Dice ({num_virtual_dice_rolls:,} Rolls)",
                    labels={"value": "Frequency/Probability", "Sum": "Sum of Dice"},
                )  # plotly for grouped bar
                st.plotly_chart(fig_dice_sum, use_container_width=True)
                st.info(
                    "Observe how the empirical distribution of sums approaches the theoretical probability distribution as you increase the number of rolls."
                )
    st.header("💪 Practice Exercises: Put Your Probability Skills to Work!")
    st.markdown(
        """
    Practice is essential to solidify your understanding of probability. Work through these exercises to apply what you've learned.  Don't just read the solutions – try to solve them yourself first!

    1. **Coin Flips and Sample Space: Three Flips in Detail 🪙🪙🪙**
       *   Describe the **sample space** (S) for flipping a fair coin **three times**. List all possible outcomes.  *(Hint: Use H for Heads, T for Tails.  An outcome is a sequence like HTT).*
       *   Consider the **event E = {getting exactly two heads}**. List all the specific outcomes from your sample space S that are part of event E.
       *   Calculate the **classical probability of event E, P(E)** (getting exactly two heads in three coin flips, assuming a fair coin).  *Remember the formula for classical probability.*

    2. **Dice Rolls and Events: Exploring Events with a Single Die 🎲**
       *   For a single roll of a fair six-sided die, consider these two events:
           *   **Event A = {rolling an odd number}**
           *   **Event B = {rolling a number greater than 3}**
       *   **List the outcomes** that belong to event A and separately list the outcomes in event B.
       *   Are events A and B **mutually exclusive**?  Carefully explain *why or why not*.
       *   Calculate the **probability of event A, P(A)**, and the **probability of event B, P(B)**. Use classical probability.
       *   Find the **probability of the union of A and B, P(A ∪ B)** (the probability of rolling an odd number *or* a number greater than 3 *or* both).  *(Hint: You can use the formula: `P(A ∪ B) = P(A) + P(B) - P(A ∩ B)` . First, determine P(A ∩ B) - the probability of rolling a number that is BOTH odd AND greater than 3).*

    3. **Conditional Probability (Cards - Suits and Face Cards) 🃏❤️**
       *   You draw a single card from a standard, well-shuffled deck of 52 cards.  What is the probability of drawing a **heart** ❤️, *given that* you know the card you drew is a **red card** (hearts and diamonds are red suits)?  This is a conditional probability problem!

    4. **Bayes' Theorem (Medical Test - Accuracy Matters): Test with 99% Accuracy 🔬✅**
       *   Let's go back to the medical testing example in the "Conditional Probability" section.  Originally, the test was 95% accurate.  Now, consider a much more accurate test: Imagine the accuracy increases to **99%** (meaning: true positive rate = 99%, and true negative rate = 99%, so false positive rate = 1%, false negative rate = 1%).  The disease prevalence is still rare at **1%**.
       *   If a person takes this *99% accurate test* and the result is **positive**, what is the **new posterior probability,  P(Disease | Positive Test)**, that they actually have the disease?  Recalculate it using Bayes' Theorem with the updated accuracy.
       *   **Think about the Impact:**  How did increasing the test accuracy from 95% to 99% change the posterior probability?  Did it increase a lot?  A little?  What does this tell you about how test accuracy affects the interpretation of positive test results, especially for diseases that are rare in the population?  Is even a "highly accurate" test always enough to give a definitive diagnosis for a rare condition when the test is positive?

    5. **Random Variables (Sum of Two Dice - Discrete RV) 🎲🎲➕**
       *   Imagine you roll **two fair six-sided dice** (like in a game of craps).
       *   Let **X be the random variable** defined as:  **X = the sum of the numbers rolled on the two dice**.  When you roll two dice, you add up the numbers showing on their faces to get a sum.
       *   What are all the **possible values** that the random variable X can take?  (What's the minimum possible sum? What's the maximum possible sum? What values in between can you get?)
       *   Is X a **discrete or continuous random variable**? Explain your reasoning based on the nature of the possible values you listed in the previous step.
       *   **(Optional, more challenging):**  Think about how you might determine the **probability distribution of X**. That is, how would you find the probability of each possible value of X? (e.g., P(X=2), P(X=3), P(X=4), and so on, up to the maximum value).  *Hint:  Consider listing out all the possible combinations of two dice rolls (e.g., (1,1), (1,2), (1,3)...) and calculate their sums.*
    """
    )

    st.header("✅ Knowledge Check: Test Your Understanding")
    quiz_questions = [  # Quiz questions - same as before for now
        {
            "question": "Which of the following is NOT a fundamental axiom of probability?",
            "options": [
                "Non-negativity: P(E) ≥ 0",
                "Probability of Sample Space: P(S) = 1",
                "Additivity for Mutually Exclusive Events",
                "Multiplicativity for Independent Events",
            ],
            "answer": "Multiplicativity for Independent Events",
            "solution": "Multiplicativity for independent events is a consequence of the axioms, not an axiom itself. The three axioms are Non-negativity, Probability of Sample Space, and Additivity for Mutually Exclusive Events.",
        },
        {
            "question": "What is the formula for calculating classical probability?",
            "options": [
                "P(Event) = (Number of favorable outcomes) / (Total number of possible outcomes)",
                "P(Event) ≈ (Number of times event occurred) / (Total trials)",
                "P(A|B) = P(A ∩ B) / P(B)",
                "P(A|B) = [P(B|A) * P(A)] / P(B)",
            ],
            "answer": "P(Event) = (Number of favorable outcomes) / (Total number of possible outcomes)",
            "solution": "Classical probability applies when all outcomes are equally likely.",
        },
        {
            "question": "If events A and B are mutually exclusive, what is P(A ∩ B)?",
            "options": ["P(A) + P(B)", "P(A) * P(B)", "0", "1"],
            "answer": "0",
            "solution": "Mutually exclusive events cannot occur together, so their intersection is empty, and its probability is 0.",
        },
        {
            "question": "Bayes' Theorem is used to:",
            "options": [
                "Calculate empirical probability",
                "Reverse conditional probability",
                "Determine if events are independent",
                "Calculate classical probability",
            ],
            "answer": "Reverse conditional probability",
            "solution": "Bayes' Theorem allows us to find P(A|B) if we know P(B|A), P(A), and P(B).",
        },
        {
            "question": "Which type of random variable can take on any value within a given range?",
            "options": [
                "Discrete Random Variable",
                "Continuous Random Variable",
                "Categorical Random Variable",
                "Binary Random Variable",
            ],
            "answer": "Continuous Random Variable",
            "solution": "Continuous random variables have uncountable possible values within a range.",
        },
        {
            "question": "What is 'Empirical Probability' based on?",
            "options": [
                "Theoretical calculations",
                "Personal beliefs",
                "Observed data from experiments",
                "Mathematical axioms",
            ],
            "answer": "Observed data from experiments",
            "solution": "Empirical probability is derived from actual experiments or observations.",
        },
        {
            "question": "If events A and B are independent, then P(A ∩ B) = ?",
            "options": ["P(A) + P(B)", "P(A) * P(B)", "0", "1"],
            "answer": "P(A) * P(B)",
            "solution": "This is the condition for independence of events.",
        },
        {
            "question": "In Bayes' Theorem, P(A) represents the:",
            "options": [
                "Posterior probability",
                "Likelihood",
                "Prior probability",
                "Evidence",
            ],
            "answer": "Prior probability",
            "solution": "P(A) is the prior probability of event A, before considering event B.",
        },
        {
            "question": "Which field does NOT heavily rely on probability theory?",
            "options": ["Finance", "Physics", "Literature", "Machine Learning"],
            "answer": "Literature",
            "solution": "While probability might indirectly influence narrative structure in literature, it is not a *foundational* tool in the same way as in the other fields.",
        },
        {
            "question": "What is a 'sample space'?",
            "options": [
                "A subset of possible outcomes",
                "The set of all possible outcomes of an experiment",
                "A visual representation of probabilities",
                "A measure of risk",
            ],
            "answer": "The set of all possible outcomes of an experiment",
            "solution": "The sample space is the foundation for defining events and probabilities.",
        },
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(
            f"Select an answer:", question["options"], key=f"quiz_{i}"
        )
        user_answers.append(user_answer)

    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1
                st.success(f"Question {i+1}: Correct! 🎉")  # More engaging feedback
            else:
                st.error(
                    f"Question {i+1}: Incorrect. Let's review the solution below. 🧐"
                )  # More encouraging tone

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
