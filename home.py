import requests
import pandas as pd
import streamlit as st
import json

username = 'gilissantos'
url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()


st.set_page_config(
    page_title='Perfil GitHub',
    page_icon='https://w7.pngwing.com/pngs/914/758/png-transparent-github-social-media-computer-icons-logo-android-github-logo-computer-wallpaper-banner-thumbnail.png'
)

st.title('Perfil Professional')
st.image(data['avatar_url'], width=80)
st.write('Name: ', data['name'])
st.write('Location: ', data['location'])
st.write('Biography: ', 'Data Engineer, Superior in Database Technology, Analytics and Data Visualization.')
st.write('Company: ', data['company'])

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.text('Python')
    st.image('https://w7.pngwing.com/pngs/780/811/png-transparent-logo-python-logos-and-brands-icon.png', width=20)

with col2:
    st.text('SQL')
    st.image('https://e7.pngegg.com/pngimages/170/924/png-clipart-microsoft-sql-server-microsoft-azure-sql-database-microsoft-text-logo-thumbnail.png', width=20)

with col3:
    st.text('Snowflake')
    st.image('https://cdn-icons-png.flaticon.com/512/2530/2530064.png', width=20)

with col4:
    st.text('Databricks')
    st.image('https://w7.pngwing.com/pngs/496/62/png-transparent-databricks-logo-thumbnail-tech-companies-thumbnail.png', width=20)


project1, project2 = st.columns(2)

with project1:
    st.markdown('###### Analista de planejamento | Uranet - 2018')    
    st.text('''
            Automação de processos
            Desenvolvimento de pessoas 
            Cultura data driven
            Desenvolvimento de reports
        ''')

with project2:
    st.markdown('###### Analista de Dados | Actionline - 2020')    
    st.text('''
            Engenharia de dados
            Automação de processos
            Desenvolvimento de reports 
            Melhoria contínua de processos
            Análise de processos e projetos de dados
        ''')
