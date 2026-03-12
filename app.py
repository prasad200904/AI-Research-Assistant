import streamlit as st
import os
from crew import run_research

st.set_page_config(page_title="AI Research Assistant", page_icon="🤖", layout="wide")

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🤖 AI Research Assistant")

st.write("Generate AI-powered research reports instantly.")

# Sidebar Dashboard
st.sidebar.title("📊 Dashboard")
st.sidebar.write("Previous Searches")

if st.session_state.history:
    for item in st.session_state.history[::-1]:
        st.sidebar.write("🔎", item)
else:
    st.sidebar.write("No searches yet")

# Main input
topic = st.text_input("Enter Research Topic")

if st.button("Generate Report"):

    if topic.strip() == "":
        st.warning("Please enter a topic")

    else:
        with st.spinner("Generating report..."):

            try:
                result = run_research(topic)

                # Save search history
                st.session_state.history.append(topic)

                st.success("Report Generated Successfully")

                st.subheader("📄 Report Preview")

                if os.path.exists("report.txt"):

                    with open("report.txt", "r", encoding="utf-8") as f:
                        report = f.read()

                    st.text_area("Report", report, height=300)

                    st.download_button(
                        label="⬇ Download Report",
                        data=report,
                        file_name="report.txt",
                        mime="text/plain"
                    )

                else:
                    st.error("Report file not found")

            except Exception as e:
                st.error("Something went wrong")
                st.code(str(e))