#import de bibliotecas importantes
import streamlit as st
import pandas as pd
import pydeck as pdk

#carregando dados
df = pd.read_csv('dataset\criminalidade_sp_2.csv')

#dashboard
st.title('Criminalidade em São Paulo')
st.markdown(
    """
    A criminalidade é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de **Ciências de Dados** conseguimos
    entender melhor o que está acontecendo e gerar insights que direcionem ações capazes de diminuir os
    índices de criminalidade.
    """
)

if st.checkbox('Ver tabelas com dados'):
    st.write(df)