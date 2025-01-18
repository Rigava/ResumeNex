from groq import Groq
import streamlit as st
groq_api_key ="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"


def ats_extractor(resume_data, jobdescription):

    prompt = '''
    You are an expert in evaluating resumes.
    You are provided with a CV and a job description. Use the job description as a guide to
    identify improvements that could be made to the CV. Improvements can include, but are 
    not limited to, mentioning certain skills present in the job description that are not present in
    the CV, and highlighting experiences that would better align with the 
    job description. You should provide 3-10 recommendations in your responses. 
    Also provide application tracking system score for the resume against the job description in a table format.
    '''
    
    client = Groq(
        api_key=groq_api_key) 

    messages = [
        {"role": "system", 
        "content": prompt},
        {"role": "user", 
        "content": f"Resume:\n{resume_data}\n\nJob Description:\n{jobdescription}"}
    ]

    response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.0,
                max_tokens=1500)
        
    data = response.choices[0].message.content

    return data
