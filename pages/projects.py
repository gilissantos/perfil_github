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

st.title('Projects')
st.write('''Ao longo desses quase 10 anos de carreira em Tecnologia da informação, 
         participei e criei alguns projetos diversificados, 
         porém com ênfase em Dados.\n Listei os principais projetos abaixo:''')


st.markdown("")
st.markdown('##### Konecta/Uranet | Analista de planejamento - 2018')
st.markdown('''
**Problema:** monitoramento de indicadores, processos manuais e reports semi-estruturado, porém a empresa com sistemas e banco de dados integrados, atraso no envio de reports e falta de validação.

**Solução:** automação de processos, monitoramento em tempo real, validação e envio de reports mais confiáveis. Maior interação com os demais departamentos da empresa. 
Treinamento e padronização que resolveu a falta de informação por parte dos funcionários da área.

**Áreas impactadas:** planejamento, suporte e área de vendas.

            
''')

st.markdown('')
st.markdown('##### Analista de dados (Estrutura e engenharia de dados) - Actionline - 2020')
st.markdown('''
**Problema:** uma empresa de Call Center com vários CRMs, diversas planilhas e um ERP com todos os dados cadastrais dos funcionários, porém sem nenhum tipo de armazenamento adequado para estes dados e sem padrão definido.

**Solução:** criei uma estrutura de banco de dados para armazenar todos os dados dos colaboradores da empresa. Criar padrão de arquivos, layout e tipo de dados. Desenvolver rotinas e processo de ETL, armazenar o histórico e adicionar novos dados, além da automação de processos, digitalização de documentos, ou seja, do arquivo em papel para o banco de dados. Armazenamento organizado, seguro e de alta disponibilidade.

**Áreas impactadas:** AP, Recursos Humanos, Financeiro, Vendas, Qualidade e Treinamento.
            
**Principais mudanças:** otimização de tempo e pessoal, após a automação de processos, os funcionários ganharam tempo, pois não necessitam mais de tarefas repetitivas, desta maneira conseguem focar os seus esforços com outras atividades mais produtivas, sobra de tempo para reciclagens e treinamentos.

Confiabilidade na qualidade dos dados para gerar informações, estudos e análises com mais agilidade e precisão nos números. 

Padronização e facilidade em medir indicadores, desde o histórico até o dado mais recente.

Alta disponibilidade, pois todos os diretores e gestores com acesso as informações com a adição de ferramentas de análise e envio de reports automatizados.
            
''')


st.markdown('')
st.markdown('##### People Analytics – Actionline - Actionline - 2021')
st.markdown('''
**Problema:** Turnover, baixo desempenho de vendas, qualidade, Absenteísmo, problemas de disciplinas e demais conflitos.

**Solução:** Análise de desempenho de vendas, qualidade e comportamental. Cruzamento e relacionamento de dados que identificamos alguns padrões de ocorrências, pesquisas de clima, mapeamento de possíveis problemas disciplinares.
            
Melhoria dos treinamentos e dos processos de qualidade, acompanhamento do turnover com mapeamento de recrutamento e seleção. Jornada do colaborador, onboarding, reciclagens, palestras direcionadas com o mapeamento dos problemas mais frequentes, retenção de talentos e entrevista de desligamento.
            

**Áreas impactadas:** AP, Recursos Humanos, Financeiro, Vendas, Qualidade e Treinamento.
            
**Principais mudanças:** otimização de tempo e pessoal, após a automação de processos, os funcionários ganharam tempo, pois não necessitam mais de tarefas repetitivas, desta maneira conseguem focar os seus esforços com outras atividades mais produtivas, sobra de tempo para reciclagens e treinamentos.

Confiabilidade na qualidade dos dados para gerar informações, estudos e análises com mais agilidade e precisão nos números. 

Padronização e facilidade em medir indicadores, desde o histórico até o dado mais recente.

Alta disponibilidade, pois todos os diretores e gestores com acesso as informações com a adição de ferramentas de análise e envio de reports automatizados.
            
''')