# 🤖 AI Research Assistant

AI Research Assistant is a multi-agent system that automatically researches a topic, analyzes the findings, and generates a structured report. The system uses AI agents built with CrewAI and a fast LLM powered by Groq.

---

## 🚀 Project Overview

This application allows users to:

* Enter a research topic
* Automatically collect information about the topic
* Analyze important insights
* Generate a structured research report
* Download the generated report

The system uses multiple AI agents working together to perform different tasks in the research pipeline.

---

## 🧠 How the System Works

The AI Research Assistant follows a **multi-agent workflow**:

1. **Research Agent**

   * Collects key facts about the topic.

2. **Data Analyst Agent**

   * Analyzes the research results.
   * Extracts insights and patterns.

3. **Writer Agent**

   * Generates a structured research report.
   * Saves the report to a file.

---

## 🏗 Project Architecture

```
User Input
     │
     ▼
Research Agent
     │
     ▼
Data Analyst Agent
     │
     ▼
Writer Agent
     │
     ▼
Generated Research Report
```

---

## 📂 Project Structure

```
AI-Research-Assistant
│
├── agents
│   ├── research_specialist.py
│   ├── data_analyst.py
│   └── content_writer.py
│
├── tasks
│   ├── research_task.py
│   ├── analyst_task.py
│   └── write_task.py
│
├── app.py
├── crew.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* CrewAI
* Streamlit
* Groq LLM
* LiteLLM
* Python-Dotenv

---

## 🧩 Key Features

* Multi-Agent AI Workflow
* Automated Research & Analysis
* Structured Report Generation
* Downloadable Research Report
* Interactive Web Interface

---

## 💻 Installation

Clone the repository:

```
git clone https://github.com/prasad200904/AI-Research-Assistant.git
```

Move to the project folder:

```
cd AI-Research-Assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

Then open the browser and access the interface.

---

## 🌐 Deployment

This project can be deployed easily using Streamlit Cloud.

Steps:

1. Push the project to GitHub
2. Login to Streamlit Cloud
3. Connect your GitHub repository
4. Deploy the app

---

## 📊 Example Use Case

Input Topic:

```
Artificial Intelligence in Healthcare
```

Output:

* Introduction
* Key Insights
* Important Trends
* Conclusion

---

## 🎯 Future Improvements

* Research history dashboard
* Export reports as PDF
* Add more AI agents
* Integrate vector database for memory
* Improve UI design

---

## 👨‍💻 Author

**Prasad**

AI Developer | Python | Machine Learning | Generative AI

---

## ⭐ Support

If you found this project helpful, consider giving it a star on GitHub.
