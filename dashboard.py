import pandas as pd #pip install pandas
import plotly.express as px
import streamlit as st


st.set_page_config(page_title = "Dashboard Puntajes",
                   page_icon = ":bar_chart:",
                   layout ="wide"
)

#Leer archivo .xslx
df = pd.read_excel(
    io = 'Prueba_practica_analista_programador.xlsx',
    engine= 'openpyxl',
    sheet_name = 'Puntajes',

)



df['PORCENTAJE DE LOGRO TOTAL PRUEBA '] = df['PORCENTAJE DE LOGRO TOTAL PRUEBA '].apply(lambda p: f"{round(p*100)}")
df['% de logro tema 1'] = df['% de logro tema 1'].apply(lambda p: f"{round(p*100)}")
df['% de logro tema 2'] = df['% de logro tema 2'].apply(lambda p: f"{round(p*100)}")
df['% de logro tema 3'] = df['% de logro tema 3'].apply(lambda p: f"{round(p*100)}")
df['% de logro tema 4'] = df['% de logro tema 4'].apply(lambda p: f"{round(p*100)}")
df['% de logro tema 5'] = df['% de logro tema 5'].apply(lambda p: f"{round(p*100)}")
df['% de logro tema 6'] = df['% de logro tema 6'].apply(lambda p: f"{round(p*100)}")


st.sidebar.header("Filtrar")

zona = st.sidebar.multiselect(
    "Seleccionar zona: ",
    options = df["Zona"].unique(),
    default= df["Zona"].unique()
)


df_selection = df.query(
    "Zona == @zona"
)


st.title(":bar_chart: Dashboard Puntajes")
st.markdown("##")

total_personas = int(df_selection["Nombre"].count())


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total de personas: ")
    st.subheader(f"{total_personas:,}")


st.dataframe(df_selection)

st.markdown("---")




total_omitidas = df_selection["Cantidad de omitidas"].apply(lambda p :0 if p == " - " else int(p)).sum()

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Porcentaje de logro tema 1")

    # Convertir la columna "% de logro tema 1" a tipo numérico
    df_selection['% de logro tema 1'] = df_selection['% de logro tema 1'].astype(float)

    # Calcular el promedio de logro de tema por zona
    promedio_logro_zona = round(df_selection.groupby('Zona')['% de logro tema 1'].mean().reset_index(),1)

    # Crear gráfico de barras con el promedio de logro de tema por zona
    fig_bar = px.bar(promedio_logro_zona, y='Zona', x='% de logro tema 1', title='Promedio de logro de tema 1 por Zona',color='Zona',text_auto=True, orientation="h",width=500,height=350)
    #fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)


with middle_column:
    st.subheader("Porcentaje de logro tema 2")

    # Convertir la columna "% de logro tema 2" a tipo numérico
    df_selection['% de logro tema 2'] = df_selection['% de logro tema 2'].astype(float)

    # Calcular el promedio de logro de tema por zona
    promedio_logro_zona = round(df_selection.groupby('Zona')['% de logro tema 2'].mean().reset_index(),1)

    # Crear gráfico de barras con el promedio de logro de tema por zona
    fig_bar = px.bar(promedio_logro_zona, y='Zona', x='% de logro tema 2', title='Promedio de logro de tema 2 por Zona',color='Zona',text_auto=True,orientation="h",width=500,height=350)
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)

with right_column:
    st.subheader("Porcentaje de logro tema 3")

    # Convertir la columna "% de logro tema 3" a tipo numérico
    df_selection['% de logro tema 3'] = df_selection['% de logro tema 3'].astype(float)

    # Calcular el promedio de logro de tema por zona
    promedio_logro_zona = round(df_selection.groupby('Zona')['% de logro tema 3'].mean().reset_index(),1)

    # Crear gráfico de barras con el promedio de logro de tema por zona
    fig_bar = px.bar(promedio_logro_zona, y='Zona', x='% de logro tema 3', title='Promedio de logro de tema 3 por Zona',color='Zona',text_auto=True,orientation="h",width=500,height=350)
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)

with left_column:
    st.subheader("Porcentaje de logro tema 4")

    # Convertir la columna "% de logro tema 4" a tipo numérico
    df_selection['% de logro tema 4'] = df_selection['% de logro tema 4'].astype(float)

    # Calcular el promedio de logro de tema por zona
    promedio_logro_zona = round(df_selection.groupby('Zona')['% de logro tema 4'].mean().reset_index(),1)

    # Crear gráfico de barras con el promedio de logro de tema por zona
    fig_bar = px.bar(promedio_logro_zona, y='Zona', x='% de logro tema 4', title='Promedio de logro de tema 4 por Zona',color='Zona',text_auto=True,orientation="h",width=500,height=350)
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)

with middle_column:
    st.subheader("Porcentaje de logro tema 5")

    # Convertir la columna "% de logro tema 5" a tipo numérico
    df_selection['% de logro tema 5'] = df_selection['% de logro tema 5'].astype(float)

    # Calcular el promedio de logro de tema por zona
    promedio_logro_zona = round(df_selection.groupby('Zona')['% de logro tema 5'].mean().reset_index(),1)

    # Crear gráfico de barras con el promedio de logro de tema por zona
    fig_bar = px.bar(promedio_logro_zona, y='Zona', x='% de logro tema 5', title='Promedio de logro de tema 5 por Zona',color='Zona',text_auto=True,orientation="h",width=500,height=350)
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)

with right_column:
    st.subheader("Porcentaje de logro tema 6")

    # Convertir la columna "% de logro tema 6" a tipo numérico
    df_selection['% de logro tema 6'] = df_selection['% de logro tema 6'].astype(float)

    # Calcular el promedio de logro de tema por zona
    promedio_logro_zona = round(df_selection.groupby('Zona')['% de logro tema 6'].mean().reset_index(),1)

    # Crear gráfico de barras con el promedio de logro de tema por zona
    fig_bar = px.bar(promedio_logro_zona, y='Zona', x='% de logro tema 6', title='Promedio de logro de tema 6 por Zona',color='Zona',text_auto=True,orientation="h",width=500,height=350)
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)




st.markdown("---")



left_column,middle_column,right_column = st.columns(3)

with middle_column:
    st.subheader("Total de omitidas")
    st.subheader(f"{total_omitidas:,}")
    # Convertir la columna 'Cantidad de omitidas' a tipo numérico
    df_selection['Cantidad de omitidas'] = pd.to_numeric(df_selection['Cantidad de omitidas'], errors='coerce')

    # Eliminar filas con valores no numéricos en la columna 'Cantidad de omitidas'
    df_selection = df_selection.dropna(subset=['Cantidad de omitidas'])

    # Calcular el total de la cantidad de omitidas por perfil
    total_omitidas_perfil = df_selection.groupby('Perfil')['Cantidad de omitidas'].sum().reset_index()

    # Crear gráfico de barras con el total de la cantidad de omitidas por perfil
    fig_total_omitidas = px.bar(total_omitidas_perfil, 
                                x='Perfil', y='Cantidad de omitidas', 
                                title='Total de cantidad de omitidas por Perfil',
                                color='Perfil', text_auto=True)
    st.plotly_chart(fig_total_omitidas)






st.markdown("---")

