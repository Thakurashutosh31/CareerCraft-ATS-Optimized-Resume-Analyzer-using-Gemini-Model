#Load The Gemini Pro Pre-Trained Model

from dotenv import load_dotenv

import streamlit as st

from streamlit_extras import add_vertical_space as avs

import google.generativeai as genai

import os

import PyPDF2

from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


# implementation a fuction to get  gemini response

def get_gemini_response(input): 
    response = model.generate_content(input) 
    return response.text


# implementation a funtion to read a pdf file

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReer (uploaded_file) 
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages [page_num]  
        text += str(page.extract_text())

    return text



# Prompt template for the Gemini model (from the provided image)
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing 
Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, 
DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, 
Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, 
and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. 
In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. 
Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy.

resume: {text}
description: {jd}


I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response, put some space to separate all the three sections.

"""
import spacy
from spacy.matcher import Matcher

def assess_resume(resume_text, job_description_text):
    """Assesses a resume against a job description."""

    # Load the SpaCy model
    nlp = spacy.load("en_core_web_lg")

    # Process the resume and job description
    resume_doc = nlp(resume_text)
    job_description_doc = nlp(job_description_text)

    # Extract keywords from both documents
    resume_keywords = extract_keywords(resume_doc)
    job_description_keywords = extract_keywords(job_description_doc)

    # Calculate matching percentage
    matching_percentage = calculate_matching_percentage(resume_keywords, job_description_keywords)

    # Identify missing keywords
    missing_keywords = identify_missing_keywords(resume_keywords, job_description_keywords)

    # Generate profile summary
    profile_summary = generate_profile_summary(resume_doc, job_description_doc, matching_percentage, missing_keywords)

    return matching_percentage, missing_keywords, profile_summary

def extract_keywords(doc):
    """Extracts keywords from a SpaCy document."""
    # Implement your keyword extraction logic here, e.g., using named entity recognition or custom rules
    keywords = []
    for entity in doc.ents:
        keywords.append(entity.text)
    return keywords

def calculate_matching_percentage(resume_keywords, job_description_keywords):
    """Calculates the matching percentage between resume keywords and job description keywords."""
    # Implement your matching percentage calculation logic here, e.g., using Jaccard similarity or cosine similarity
    matching_percentage = 0  # Placeholder
    return matching_percentage

def identify_missing_keywords(resume_keywords, job_description_keywords):
    """Identifies missing keywords from the resume."""
    # Implement your missing keyword identification logic here, e.g., by finding keywords in the job description that are not in the resume
    missing_keywords = []
    return missing_keywords

def generate_profile_summary(resume_doc, job_description_doc, matching_percentage, missing_keywords):
    """Generates a profile summary based on the assessment results."""
    # Implement your profile summary generation logic here, e.g., by combining information from the resume, job description, matching percentage, and missing keywords
    profile_summary = ""
    return profile_summary

# Example usage
resume_text = "This is a sample resume"
job_description_text = "This is a sample job description"
matching_percentage, missing_keywords, profile_summary = assess_resume(resume_text, job_description_text)

print("Matching percentage:", matching_percentage)
print("Missing keywords:", missing_keywords)
print("Profile summary:", profile_summary)





##streamlit UI
st.set_page_config(page_title="RESUME ATS TRACKING", layout="wide")

avs.add_vertical_space(4)

col1 , col2 = st.columns([3, 2])

with col1:

    st.title("CareerCraft")

    st.header("Navigate the Job Market with Confidence!")

    st.markdown("""<p style='text-align: justify;'>

    Introducing CareerCraft, an ATS-Optimized Resume Analyzer your ultimate solution for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions. From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market. Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success! </p>""", unsafe_allow_html=True)

with col2:

    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)

avs.add_vertical_space(10)


col1, col2 =st.columns([3, 2])

with col2:

    st.header("Wide Range of Offerings")

    st.write('ATS-Optimized Resume Analysis')

    st.write('Resume Optimization')

    st.write('Skill Enhancement ')

    st.write('Career Progression Guidance')

    st.write('Tailored Profile Summaries')

    st.write('Streamlined Application Process')

    st.write('Personalized Recommendations')

    st.write('Efficient Career Navigation')

with col1:

    img1= Image.open("images/icon1.png")

    st.image(img1, use_column_width=True)

avs.add_vertical_space(10)


coll, col2= st.columns([3, 2])

with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)

    jd=st.text_area("Paste the Job Description")
    uploaded_file=st.file_uploader("Upload Your Resume", type="pdf", help="Please uplaod the pdf")

    submit= st.button("submit")

    if submit:

        if uploaded_file is not None:
                text=input_pdf_text(uploaded_file)
                response=get_gemini_response(input_prompt) 
                st.subheader(response)

with col2:
    img2= Image.open("Images/icon2.png")
    st.image(img2, use_column_width=True)

avs.add_vertical_space(10)



col1, col2 =st.columns([2, 3])

with col2:

    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)

    st.write("Question: How does CareerCraft analyze resumes and job descriptions?")

    st.write("""Answer: Care Craft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.""")

    avs.add_vertical_space(3)

    st.write("Question: Can CareerCraft suggest improvements for my resume?")

    st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with

    desired job roles.""")

    avs.add_vertical_space(3)

    st. write("Question: Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.""")

with coll:

    img3 = Image.open("images/icon3.png")

    st.image(img3, use_column_width=True)




