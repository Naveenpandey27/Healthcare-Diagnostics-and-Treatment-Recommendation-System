# Healthcare-Diagnostics-and-Treatment-Recommendation-System

# 🧠 SmartMed AI

Welcome to **SmartMed AI** — an AI-powered healthcare assistant that uses multiple intelligent agents to generate **preliminary medical diagnoses** and **personalized treatment plans** based on patient-provided information. This interactive web application is built using modern AI frameworks and can be accessed remotely through an automatically generated public URL using **Ngrok**.

> ⚠️ **Disclaimer**: This AI-generated diagnosis and treatment plan is for informational purposes only. Always consult a qualified healthcare professional for actual medical advice, diagnosis, or treatment.

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Public Sharing via Ngrok](#public-sharing-via-ngrok)
* [Configuration](#configuration)
* [Examples](#examples)
* [Troubleshooting](#troubleshooting)
* [What is a Multi-Agent System?](#what-is-a-multi-agent-system)
* [Contributors](#contributors)

---

## 🌟 Overview

![saved](https://github.com/user-attachments/assets/55f4a3ac-5ad5-4082-990c-429459505535)

SmartMed AI allows users to enter basic patient details, such as age, gender, symptoms, and medical history. Once submitted, the system uses a pair of specialized AI agents — one for diagnosis and the other for treatment — to generate intelligent medical insights in real time.

The application can also be **shared live over the internet** using **Ngrok**, so that others can interact with the AI from anywhere without any deployment setup.

---

## 🚀 Features

* 👤 Collects patient demographics and health inputs
* 🧠 Uses multiple AI agents for diagnosis and treatment
* 📄 Provides ranked diagnoses with supporting evidence
* 💊 Suggests treatment plans with medications, lifestyle advice, and follow-ups
* 🌐 Real-time internet access using search and scraping tools
* 🔗 Shareable live app via Ngrok for remote testing or demos

---

## 🛠 Technologies Used

| Technology             | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| **Streamlit**          | Builds the user interface                             |
| **CrewAI**             | Defines and manages multi-agent workflows             |
| **LangChain + OpenAI** | Powers the LLM reasoning (GPT-4 / GPT-4O-MINI)        |
| **SerperDevTool**      | Integrates web search capabilities                    |
| **ScrapeWebsiteTool**  | Enables real-time web scraping for additional data    |
| **python-dotenv**      | Manages API keys and sensitive config values securely |
| **Ngrok**              | Publishes the app to the internet for external access |
| **Google Colab**       | Sample platform used for experimentation              |

---

## 🧩 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Naveenpandey27/Healthcare-Diagnostics-and-Treatment-Recommendation-System.git
   cd Healthcare-Diagnostics-and-Treatment-Recommendation-System
   ```

2. **Create a Virtual Environment** *(optional but recommended)*:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in your project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

5. **(Optional) Install Ngrok**:

   ```bash
   pip install pyngrok
   ```

---

## 💻 Usage

### Running the Application Locally

```bash
streamlit run main.py
```

### Running the Application and Exposing it with Ngrok

In `ngrok_runner.py` or in your notebook, use the following:

```python
import os
from threading import Thread
from pyngrok import ngrok

def run_streamlit():
    os.system('streamlit run /content/main.py --server.port 8503')

thread = Thread(target=run_streamlit)
thread.start()

public_url = ngrok.connect(addr='8503', proto='http', bind_tls=True)
print('Streamlit app is alive at :', public_url)
```

### Result:

After a few seconds, the terminal will print a public URL like:

```
Streamlit app is alive at : https://abcd1234.ngrok.io
```

You can send this link to anyone for real-time testing.

---

## ⚙️ Configuration

You can change the model (`gpt-4o-mini`), temperature, or token limits directly in the script. The `.env` file must contain valid API keys for:

* `OPENAI_API_KEY`
* `SERPER_API_KEY`

---

## 🧪 Examples

### Sample Input:

```
Gender: Female
Age: 42
Symptoms: shortness of breath, fatigue, swelling in legs
Medical History: hypertension, type 2 diabetes
```

### Sample Output:

* **Diagnosis**:

  1. Congestive Heart Failure
  2. Chronic Kidney Disease (possible comorbidity)

* **Treatment Plan**:

  * Start low-sodium diet
  * Diuretic therapy (Furosemide)
  * Cardiology follow-up
  * Lifestyle changes (weight monitoring, fluid intake tracking)

---

## 🛠 Troubleshooting

| Issue                 | Solution                                                          |
| --------------------- | ----------------------------------------------------------------- |
| App doesn’t launch    | Check that Streamlit and dependencies are installed               |
| Blank/empty responses | Verify that API keys are valid and not rate-limited               |
| Ngrok URL not working | Ensure Ngrok is installed, check for port conflicts               |
| Delays in response    | Allow processing time due to agent collaboration (optimize model) |

---

## 🧠 What is a Multi-Agent System?

A **multi-agent system** involves several intelligent agents working collaboratively. In this application:

* The **Medical Diagnostician Agent** evaluates symptoms and medical history to form a ranked list of possible diagnoses.
* The **Treatment Advisor Agent** uses the diagnoses to formulate a suitable treatment plan, including medications, lifestyle changes, and follow-up care.

This modular, cooperative setup mirrors real-world medical workflows and improves the decision-making process.

---

## 👥 Contributors

* **Naveen Pandey**
