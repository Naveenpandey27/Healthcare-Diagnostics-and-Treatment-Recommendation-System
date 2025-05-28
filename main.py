import streamlit as st
from crewai import Agent, Task, Crew, Process
import os
from google.colab import userdata
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from docx import Document
from io import BytesIO
import base64

# Load environment variables
load_dotenv()

# Custom CSS to improve the app's appearance
st.markdown("""
<style>
    .reportview-container {
        background-color: #f0f2f6;
    }
    .big-font {
        font-size: 20px !important;
    }
    .stButton>button {
        background-color: #021526;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 5px;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown("<h1 style='text-align: center; color: Black;'>SmartMed AI</h1>", unsafe_allow_html=True)
st.markdown("""
    <p class="big-font">Welcome to SmartMedAI, where advanced AI agents work collaboratively to analyze patient information and provide preliminary insights. Designed to support healthcare professionals, SmartMedAI offers data-driven suggestions. Remember, it's a tool, not a replacement for professional medical advice. Always consult a healthcare provider for personalized care.</p>
""", unsafe_allow_html=True)

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    st.subheader("Patient Information")
    gender = st.selectbox('Select Gender', ('Male', 'Female', 'Other'))
    age = st.number_input('Enter Age', min_value=0, max_value=120, value=25)

with col2:
    st.subheader("Medical Details")
    symptoms = st.text_area('Enter Symptoms', placeholder='e.g., fever, cough, headache')
    medical_history = st.text_area('Enter Medical History', placeholder='e.g., diabetes, hypertension')

# AI setup
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["SERPER_API_KEY"] = os.getenv('SERPER_API_KEY')

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, max_tokens=8192)

# Agent and Task definitions
diagnostician = Agent(
    role="Medical Diagnostician",
    goal="Provide accurate and comprehensive preliminary diagnoses based on patient symptoms and medical history.",
    backstory="""You are an experienced medical diagnostician with extensive knowledge across various medical fields.
    Your expertise lies in analyzing complex symptom patterns and connecting them with potential underlying conditions.
    You have a keen eye for detail and always consider the full context of a patient's health before making a diagnosis.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm
)

treatment_advisor = Agent(
    role="Treatment Advisor",
    goal="Develop personalized, effective treatment plans based on diagnoses and patient-specific factors.",
    backstory="""You are a seasoned treatment advisor with a wealth of experience in creating tailored treatment plans.
    Your strength lies in balancing the latest medical research with practical considerations for each patient's unique situation.
    You always strive to recommend treatments that are both effective and manageable for the patient.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm
)

diagnose_task = Task(
    description="""
    1. Carefully analyze the patient's reported symptoms: {symptoms}
    2. Review the patient's medical history in detail: {medical_history}
    3. Consider potential interactions between symptoms and pre-existing conditions
    4. Develop a list of possible diagnoses, ranked by likelihood
    5. For each potential diagnosis, provide:
       a) Key symptoms supporting this diagnosis
       b) Any contradicting factors
       c) Recommended follow-up tests or examinations to confirm or rule out the diagnosis
    6. Summarize your findings in a clear, concise manner
    7. If multiple conditions could be present, discuss possible comorbidities
    8. Highlight any red flags or urgent concerns that require immediate attention
    """,
    expected_output="""A comprehensive preliminary diagnosis report including:
    - Ranked list of potential conditions
    - Supporting evidence for each diagnosis
    - Recommended follow-up actions
    - Summary of key findings and any urgent concerns""",
    agent=diagnostician
)

treatment_task = Task(
    description="""
    1. Review the diagnosis provided by the Medical Diagnostician
    2. Analyze the patient's current symptoms: {symptoms}
    3. Consider the patient's medical history: {medical_history}
    4. Develop a personalized treatment plan addressing:
       a) Immediate symptom relief
       b) Long-term management of diagnosed condition(s)
       c) Preventive measures to avoid complications
    5. For each recommended treatment:
       a) Explain the purpose and expected benefits
       b) Discuss potential side effects and how to manage them
       c) Provide dosage information (if applicable)
    6. Suggest lifestyle modifications to support recovery and overall health
    7. Outline a follow-up care plan, including:
       a) Recommended check-ups
       b) Milestones for assessing treatment effectiveness
    8. Address potential drug interactions or contraindications based on the patient's history
    9. Provide patient education resources related to the diagnosis and treatment
    """,
    expected_output="""A detailed, personalized treatment plan including:
    - Specific treatments with explanations
    - Medication recommendations (if applicable)
    - Lifestyle modification suggestions
    - Follow-up care schedule
    - Patient education resources""",
    agent=treatment_advisor
)

crew = Crew(
    agents=[diagnostician, treatment_advisor],
    tasks=[diagnose_task, treatment_task],
    verbose=True
)

# Execution
if st.button("Get Diagnosis and Treatment Plan"):
    if not symptoms or not medical_history:
        st.warning("Please enter both symptoms and medical history before proceeding.")
    else:
        with st.spinner('Generating recommendations... This may take a few minutes.'):
            result = crew.kickoff(inputs={"symptoms": symptoms, "medical_history": medical_history})

            st.markdown("<div class='output-container'>", unsafe_allow_html=True)
            st.subheader("AI-Generated Diagnosis and Treatment Plan")
            st.markdown(f"<div class='big-font'>{result}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# Disclaimer
st.markdown("""
    <div style='background-color: #ffcccc; padding: 10px; border-radius: 5px;'>
        <p class='big-font'><strong>Disclaimer:</strong> This AI-generated diagnosis and treatment plan is for informational purposes only. Always consult with a qualified healthcare professional for medical advice, diagnosis, or treatment.</p>
    </div>
""", unsafe_allow_html=True)