import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analyseur de Données Pro", layout="wide")

st.title("📊 Application d'Analyse de Données")
st.markdown("""
Cette application vous permet de charger un fichier CSV pour explorer et visualiser vos données rapidement.
""")

# Sidebar pour le chargement des données
st.sidebar.header("Configuration")
uploaded_file = st.sidebar.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    # Lecture des données
    df = pd.read_csv(uploaded_file)
    
    # Affichage des données
    st.subheader("👀 Aperçu des données")
    st.dataframe(df.head())
    
    # Statistiques descriptives
    st.subheader("📈 Statistiques descriptives")
    st.write(df.describe())
    
    # Visualisation dynamique
    st.subheader("🎨 Visualisation personnalisée")
    columns = df.columns.tolist()
    
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Axe X", columns)
    with col2:
        y_axis = st.selectbox("Axe Y", columns)
        
    chart_type = st.radio("Type de graphique", ["Nuage de points", "Lignes", "Barres"])
    
    if chart_type == "Nuage de points":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} en fonction de {x_axis}")
    elif chart_type == "Lignes":
        fig = px.line(df, x=x_axis, y=y_axis, title=f"Évolution de {y_axis} par {x_axis}")
    else:
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"Distribution de {y_axis} par {x_axis}")
        
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("💡 Veuillez charger un fichier CSV dans la barre latérale pour commencer.")
    # Exemple de données pour la démonstration
    if st.checkbox("Utiliser un exemple de données"):
        example_data = {
            'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai'],
            'Ventes': [100, 150, 130, 180, 210],
            'Dépenses': [80, 90, 85, 100, 110]
        }
        df_example = pd.DataFrame(example_data)
        st.write(df_example)
