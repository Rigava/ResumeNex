from groq import Groq

api_key = st.secrets.API_KEY


def ats_extractor(resume_data):

    prompt = '''
    You are an AI bot designed to act as a professional for parsing resumes. 
    You are given with resume and your job is to extract the following information from the resume:
    1. full name
    2. email id
    3. github portfolio
    4. linkedin id
    5. employment details
    6. technical skills
    7. soft skills
    Give the extracted information in json format only
    '''
    client = Groq(
        api_key=api_key) 

    messages=[
        {"role": "system", 
        "content": prompt}
        ]
    
    user_content = resume_data
    
    messages.append({"role": "user", "content": user_content})

    response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.0,
                max_tokens=1500)
        
    data = response.choices[0].message.content

    #print(data)
    return data
