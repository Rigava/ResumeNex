import streamlit as st
from resumereparser import ats_extractor
from PyPDF2 import PdfReader 

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Next-Gen Resume Parsing",
    page_icon="🧊",
    layout="centered"
)

# Add Phoenix Symbol
st.sidebar.image("https://images.wikia.com/harrypotter/images/5/5a/Dumbledores_phoenix_patronus.jpg", width=100)
# Header Section
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa;
    }
    .header {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.25rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="header">Elevate Your Recruitment with Cutting-Edge Resume Parsing</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Experience unparalleled efficiency and precision in hiring decisions with our next-generation resume parser.</div>', unsafe_allow_html=True)

def _read_file_from_path(path):
    reader = PdfReader(path) 
    data = ""

    for page_no in range(len(reader.pages)):
        page = reader.pages[page_no] 
        data += page.extract_text()

    return data 
def main():

    st.sidebar.subheader('Choose Model Function:')
    cv_data_extract = st.sidebar.checkbox('CV Data Extract', value=True)
    # cover_letter = st.sidebar.checkbox('Cover Letter Generator', value=True)
    with st.form('my_form'):
        text = st.text_area('Enter the extraction data points like name,skills,employee details', '')
        files = st.file_uploader("Upload Files:", type=["pdf"], accept_multiple_files=False)
        
        submitted = st.form_submit_button('Submit')

    if submitted:
        data = _read_file_from_path(files)
        ats_data = ats_extractor(data)
        st.markdown(ats_data)

if __name__ == "__main__":
   main()
