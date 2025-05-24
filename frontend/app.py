import streamlit as st
import requests

# Set up page config
st.set_page_config(page_title="Your Study Mentor", layout="wide")

# ---------------------------
# Custom CSS Styling
# ---------------------------
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            padding: 2rem 1rem;
        }
        .css-1d391kg { padding-top: 1rem; }
        .main { background-color: #ffffff; padding: 2rem; border-radius: 10px; }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            border: none;
            border-radius: 5px;
            padding: 0.6em 1.5em;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .header-style {
            color: #333;
            font-size: 2em;
            font-weight: bold;
            padding-bottom: 10px;
        }
        .icon {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar Navigation (Static with Buttons)
# ---------------------------
st.sidebar.title("Your Study Mentor")

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Sidebar Navigation Buttons
if st.sidebar.button("🏠 Home"):
    st.session_state.current_page = "Home"
if st.sidebar.button("📖 Ask a Question"):
    st.session_state.current_page = "Ask"
if st.sidebar.button("🎯 Quiz Master"):
    st.session_state.current_page = "Quiz"
if st.sidebar.button("🧠 Revision Coach"):
    st.session_state.current_page = "Revise"

# ---------------------------
# HOME PAGE
# ---------------------------
if st.session_state.current_page == "Home":
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the ratio as needed
    with col2:
        st.image("Untitled_design.png", width=300)


    st.markdown('<div class="header-style">📚 Your Study Mentor</div>', unsafe_allow_html=True)
    st.markdown("Your personal Gen-AI study coach for **exams,tests,revision and more!**")
    st.info("The **Your Study Mentor** is a next-generation AI-powered academic support tool designed to help students enhance their understanding and excel in exams. It offers a suite of intelligent agents that assist with explaining complex topics, generating custom quizzes, and providing personalized study plans tailored to individual learning styles and goals.One of its key features is the ability to upload your own course materials—such as lecture slides, notes, textbooks, or syllabi—so the AI can deliver guidance that's specifically aligned with your curriculum. This ensures highly relevant explanations, practice questions, and study strategies.Whether you're preparing for a test, catching up on missed content, or aiming to deepen your comprehension, Your Study Mentor offers an accessible, efficient, and personalized learning experience to help you stay on track and improve academic performance.")
# ---------------------------
# ASK A QUESTION SECTION
# ---------------------------
elif st.session_state.current_page == "Ask":
    st.markdown('<div class="header-style">📖 Ask the Explanation Guru</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload NCERT PDF or image", type=["pdf", "png", "jpg"])
    query = st.text_input("Ask a study question (e.g., What is Ohm's law?)")

    if st.button("Submit") and (uploaded_file or query):
        with st.spinner("Analyzing..."):
            files = {"file": uploaded_file} if uploaded_file else None
            response = requests.post(
                "http://localhost:5000/api/query",
                files=files,
                data={"query": query}
            )
            if response.ok:
                st.success("✅ Response:")
                st.markdown(response.json().get("answer", "No answer returned"))
            else:
                st.error("❌ Failed to get response.")

# ---------------------------
# QUIZ MASTER SECTION
# ---------------------------
elif st.session_state.current_page == "Quiz":
    st.markdown('<div class="header-style">🎯 Quiz Master Agent</div>', unsafe_allow_html=True)
    topic = st.text_input("Enter topic (e.g., 'Electric current', 'World War II'):")
    uploaded_file = st.file_uploader("Optional: Upload NCERT PDF to generate quiz from it", type=["pdf"])

    if st.button("Generate Quiz"):
        with st.spinner("Generating quiz..."):
            files = {"file": uploaded_file} if uploaded_file else None
            response = requests.post(
                "http://localhost:5000/api/query",
                files=files,
                data={"query": f"quiz on {topic}"}
            )
            if response.ok:
                st.success("✅ Quiz Ready!")
                st.markdown(response.json().get("answer", "No quiz generated."))
            else:
                st.error("❌ Failed to generate quiz.")

# ---------------------------
# REVISION COACH SECTION
# ---------------------------
elif st.session_state.current_page == "Revise":
    st.markdown('<div class="header-style">🧠 Exam Coach Agent</div>', unsafe_allow_html=True)
    subject_plan = st.text_input("Which subject or topic do you want to revise?")
    uploaded_file = st.file_uploader("Optional: Upload NCERT PDF for targeted study plan", type=["pdf"])

    if st.button("Get Study Plan"):
        with st.spinner("Creating a 5-day revision plan..."):
            files = {"file": uploaded_file} if uploaded_file else None
            response = requests.post(
                "http://localhost:5000/api/query",
                files=files,
                data={"query": f"revise {subject_plan}"}
            )
            if response.ok:
                st.success("📅 Here is your plan:")
                st.markdown(response.json().get("answer", "No plan generated."))
            else:
                st.error("❌ Failed to generate plan.")
