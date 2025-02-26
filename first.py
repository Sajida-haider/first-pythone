import streamlit as st

# Custom CSS for better styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .main-title {
            color: #ff4b4b;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .question {
            font-size: 20px;
            font-weight: bold;
            color: #0084ff;
        }
        .correct {
            color: green;
            font-weight: bold;
        }
        .wrong {
            color: red;
            font-weight: bold;
        }
        .score-box {
            background-color: #0084ff;
            color: white;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu
st.sidebar.title("📌 Quiz Menu")
st.sidebar.markdown("👋 **Welcome to the Python Quiz!**")
st.sidebar.markdown("🔹 This quiz will test your knowledge of Python programming.")
st.sidebar.markdown("📜 **Instructions:**")
st.sidebar.markdown("✅ Read each question carefully.")
st.sidebar.markdown("✅ Select the correct answer.")
st.sidebar.markdown("✅ Click the 'Submit Answers' button to see your score.")
st.sidebar.markdown("🎯 **Quiz Categories:**")
st.sidebar.markdown("- 🟢 **Basics of Python**")
st.sidebar.markdown("- 🔵 **Data Types & Structures**")
st.sidebar.markdown("- 🟠 **Loops & Conditions**")
st.sidebar.markdown("- 🔴 **Functions & Modules**")

def main():
    st.markdown('<h1 class="main-title">🎯 Python Quiz App</h1>', unsafe_allow_html=True)
    st.markdown("### Test your Python knowledge and see how much you score! 🚀")

    questions = [
        ("Python kis tarah ki language hai?", ["Compiled", "Interpreted", "Machine", "Assembly"], "Interpreted"),
        ("Python ka creator kaun hai?", ["Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup"], "Guido van Rossum"),
        ("Python me list kis tarah ki data structure hai?", ["Immutable", "Mutable", "Constant", "None"], "Mutable"),
        ("Python me dictionary ka key kya ho sakta hai?", ["List", "Tuple", "Set", "All of these"], "Tuple"),
        ("Python me default data type kya hai jab hum bina decimal number likhte hain?", ["Float", "Integer", "Complex", "String"], "Integer"),
        ("Python me loop terminate karne ke liye kaunsa keyword use hota hai?", ["stop", "exit", "break", "terminate"], "break"),
        ("Python me kaunsa operator comparison ke liye use hota hai?", ["=", "==", "!=", "Both B and C"], "Both B and C"),
        ("Python me kaunsi function list ko sort karne ke liye use hoti hai?", ["sort()", "sorted()", "Both", "None"], "Both"),
        ("Python me kaunsa loop available hai?", ["for", "while", "Both", "None"], "Both"),
        ("Python me function define karne ka keyword kya hai?", ["def", "func", "define", "function"], "def")
    ]
    
    score = 0
    submitted = st.button("Submit Answers")  # Button to check answers

    if submitted:
        for i, (question, options, correct) in enumerate(questions):
            user_answer = st.session_state.get(f"q{i}")  # Get stored answer
            
            if user_answer:
                if user_answer == correct:
                    score += 1
                    st.markdown(f'<p class="correct">✅ **Q{i+1}: Good Job! Correct Answer!**</p>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<p class="wrong">❌ **Q{i+1}: Wrong Answer! Correct answer is:** {correct}</p>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(f'<div class="score-box">🏆 **Your Final Score: {score} / {len(questions)}**</div>', unsafe_allow_html=True)

        if score == len(questions):
            st.markdown("🎊 **Perfect Score! You're a Python Pro!** 🎊")
        elif score >= len(questions) // 2:
            st.markdown("🔥 **Great effort! Keep practicing.** 🔥")
        else:
            st.markdown("😔 **You can do better! Try again.**")

        # 🎈 Balloons only if the score is greater than 0
        if score > 0:
            st.balloons()

    else:
        for i, (question, options, correct) in enumerate(questions):
            st.markdown(f'<p class="question">**Q{i+1}: {question}**</p>', unsafe_allow_html=True)
            st.radio("", options, key=f"q{i}")

if __name__ == "__main__":
    main()








