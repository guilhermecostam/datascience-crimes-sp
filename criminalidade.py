#import de bibliotecas importantes
import streamlit as st
import pandas as pd
import pydeck as pdk

#carregando dados
df = pd.read_csv('dataset\criminalidade_sp.csv')

#dashboard
st.title('Criminalidade em São Paulo')
st.markdown(
    """
    A criminalidade é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de **Ciências de Dados** conseguimos
    entender melhor o que está acontecendo e gerar insights que direcionem ações capazes de diminuir os
    índices de criminalidade. Vemos aqui as taxas de criminalidade em **São Paulo**:
    """
)

#sidebar
st.sidebar.info("Foram carregadas {} linhas.".format(df.shape[0]))

if st.sidebar.checkbox('Ver tabelas com dados'):
    st.header('Raw Data')
    st.write(df)

#slider na sidebar para escolha do ano de visualização dos crimes
df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider("Escolha um ano", 2010, 2018, 2015)
df_selecionado = df[df.time.dt.year == ano_selecionado]


#mapa
#st.map(df_selecionado) <-----mapa simples

st.subheader("Mapa da Criminalidade")
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=-23.567145	,
        longitude=-46.648936,
        zoom=8,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df_selecionado[['latitude', 'longitude']],
            get_position='[longitude,latitude]',
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,
            coverage=1
        )
    ],
))