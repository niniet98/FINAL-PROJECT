import streamlit as st
import streamlit.components.v1 as components
# from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="LinkedIn Salary Predictor", page_icon=":us:", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            marign: 2rem 4rem;
        }
        .block-container {
            padding-top: 2rem;
        }
        .st-emotion-cache-ocqkz7 div {
            display: flex;
            flex_direction: column;
            align-items: center;
        }
        #job-searcher-salary-predictor {
            color: #0077B5;
            margin-bottom: .5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

head, logo = st.columns([10, 2])

logo.image('../readme/linkedin_logo.png')

head.header('Job Searcher & Salary Predictor')

linkedin = pd.read_csv('../data/linkedin_standarized.csv')
filtered = pd.DataFrame()


row1_1, row1_2, row1_3 = st.columns(3)

with row1_1:
    st.text('Job Title')
    pos_lst = linkedin[linkedin['job_title'].notna()]
    position = st.selectbox('', set(pos_lst['job_title']), label_visibility="collapsed")

with row1_2:
    st.text('Experience Level')
    experience = st.selectbox('', linkedin['experience_level'].dropna().unique(), label_visibility="collapsed")

with row1_3:
    st.text('Modality')
    modality = st.selectbox('', linkedin['remote_ratio'].dropna().unique(), label_visibility='collapsed')
    
st.markdown(
    """
    <style>
        .stButton {
            display: flex;
            justify-content: flex-start;
        }
        .stButton button {
            background-color: #0077B5;
            color: white;
        }
        .stButton button:hover {
            background-color: white;
            color: #0077B5;
            border-color: #0077B5;
        }
        .stButton button:active {
            background-color: #0077B5;
                color: white;
            border-color: #0077B5;
        }
        .stButton button:focus,
        .stButton button:visited {
            background-color: #0077B5;
                color: white;
            border-color: #0077B5;
        }
    </style>
    """,
    unsafe_allow_html=True
)

search = st.button('Search', key='search') 
if search:
    filtered = linkedin[(linkedin['job_title'] == position) & (linkedin['experience_level'] == experience) & (linkedin['remote_ratio'] == modality)]
    
    if len(filtered) == 0:
        st.subheader('No results found for this search')
    else:
        for _, job in filtered.iterrows():

            st.markdown(
                    """
                    <style>
                    .stHorizontalBlock .e1f1d6gn2 {
                            padding: 0rem 2rem !important;
                        }
                    </style>
                    """
                    , unsafe_allow_html=True
                )
            img, info = st.columns([1, 11])

            with img:
                st.image(job['image_link'])
            with info:
                st.markdown(
                    """
                    <style>
                        h3 {
                            margin-top: 1.5rem;
                        }
                    </style>
                    """
                    , unsafe_allow_html=True
                )
                st.subheader(job['original_title'])
                if job['company_state'] != 'USA':
                    line1 = job['company_name'] + ' · ' + job['company_state'] + ', United States'
                else:
                    line1 = job['company_name'] + ' · ' + job['company_state']
                st.write(line1)

                st.markdown(
                    """
                    <style>
                        .stMarkdownContainer p {
                            margin-bottom: 0px;
                        }
                    </style>
                    """
                    , unsafe_allow_html=True
                )
                if str(job['salary_range']) != 'nan':
                    salary = str(job['salary_range']).split('/')
                    line2 = ':briefcase: ' + job['salary_range'] + ' · ' + job['remote_ratio'] + ' · ' + job['employment_type'] + ' · ' + job['experience_level']
                else:
                    line2 = ':briefcase: ' + job['remote_ratio'] + ' · ' + job['employment_type'] + ' · ' + job['experience_level']
                st.write(line2)

                line3 = ':office: ' + job['company_size']
                st.write(line3)

                if str(job['salary_range']) == 'nan':
                    predict = st.button(label='Predict Salary', key=job['job_id'])
                    if predict:
                        st.write('hola')


