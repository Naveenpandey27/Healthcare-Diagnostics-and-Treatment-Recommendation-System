# Healthcare-Diagnostics-and-Treatment-Recommendation-System

# 🧠 SmartMed AI

Welcome to **SmartMed AI** — an AI-powered healthcare assistant that harnesses the capabilities of multi-agent systems to deliver preliminary medical diagnoses and personalized treatment recommendations. Built with cutting-edge tools like **Streamlit**, **CrewAI**, and **OpenAI**, this application is designed to support healthcare professionals with intelligent insights, not to replace them.

> ⚠️ **Disclaimer**: This AI-generated diagnosis and treatment plan is for informational purposes only. Always consult with a qualified healthcare professional for medical advice, diagnosis, or treatment.

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Examples](#examples)
* [Troubleshooting](#troubleshooting)
* [What is a Multi-Agent System?](#what-is-a-multi-agent-system)
* [Contributors](#contributors)
* [License](#license)

---

## 🌟 Overview

SmartMed AI provides a user-friendly interface where users can input patient information such as age, gender, symptoms, and medical history. Once submitted, two specialized AI agents — a **Medical Diagnostician** and a **Treatment Advisor** — collaborate to generate a preliminary diagnosis and a corresponding treatment plan.

---

## 🚀 Features

* 🧑‍⚕️ Collects and processes patient data
* 🩺 Offers AI-generated preliminary diagnoses
* 💊 Recommends personalized treatment plans
* 🔁 Employs a multi-agent system for collaboration
* 🌐 Uses real-time web scraping and search for current medical knowledge
* 🧵 User-friendly Streamlit web interface

---

## 🛠 Technologies Used

| Technology                 | Purpose                                                               |
| -------------------------- | --------------------------------------------------------------------- |
| **Streamlit**              | Builds the interactive web interface                                  |
| **CrewAI**                 | Defines and manages autonomous agents and tasks                       |
| **LangChain + OpenAI API** | Powers the intelligent reasoning behind diagnoses and recommendations |
| **SerperDevTool**          | Provides search capabilities for real-time data retrieval             |
| **ScrapeWebsiteTool**      | Enables agents to pull information from relevant web resources        |
| **dotenv**                 | Securely loads environment variables                                  |
| **Google Colab**           | Manages user data (example platform integration)                      |

---

## 🧩 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/smartmed-ai.git
   cd smartmed-ai
   ```

2. **Create a Virtual Environment** *(optional but recommended)*:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file with the following:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

---

## 💻 Usage

1. **Run the App**:

   ```bash
   streamlit run app.py
   ```

2. **Enter Patient Info**:

   * Select gender and age
   * Input symptoms and medical history

3. **Click “Get Diagnosis and Treatment Plan”**:

   * Wait for the multi-agent system to generate recommendations

4. **Review Results**:

   * Diagnoses and treatments appear in the main panel

---

## ⚙️ Configuration

* **OpenAI API Key** and **Serper API Key** are required to enable language model and search capabilities.
* All configurable parameters (like temperature, model name) are adjustable in the Python script (`gpt-4o-mini` is the default model).

---

## 🧪 Examples

### Example Input

```
Symptoms: persistent cough, fever, shortness of breath
Medical History: asthma, seasonal allergies
```

### Example Output

```
Diagnosis:
1. Acute Bronchitis
2. Pneumonia (Possible)

Treatment:
- Prescribed inhaler use
- 5-day antibiotic course
- Increase fluid intake
- Follow-up in 3 days
```

---

## 🛠 Troubleshooting

| Issue                 | Solution                                                         |
| --------------------- | ---------------------------------------------------------------- |
| Missing API Keys      | Ensure `.env` is correctly configured and placed in project root |
| Streamlit crashes     | Check for correct Python version and package installations       |
| Long wait times       | This is expected due to multi-agent processing (optimize later)  |
| Poor response quality | Try revising input descriptions or symptoms for clarity          |

---

## 🧠 What is a Multi-Agent System?

A **multi-agent system** is a collection of AI agents that work together to achieve complex goals. In SmartMed AI:

* The **Medical Diagnostician** analyzes symptoms and medical history to propose possible conditions.
* The **Treatment Advisor** takes the diagnosis and builds a personalized treatment strategy.

Together, they simulate a collaborative medical team, improving output quality and contextual understanding.

---

## 👥 Contributors

* **Naveen Pandey** – 
