import streamlit as st
import pandas as pd
import plotly.express as px
from Chat_UI import display_chat

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def display_sidebar_content():
    st.sidebar.markdown("About")
    st.sidebar.markdown("Dataset Link: [Pokemon Dataset](https://www.kaggle.com/datasets/rohanpatil63/pokemon-dataset)")
    st.sidebar.markdown("You can support it by staring:star: the project, Github Link: [PokiVerse](https://github.com/codingis4noobs2/PokiVerse)")
    st.sidebar.markdown("Credits:")

def main():
    # page configuration
    st.set_page_config(
        page_title="PokiVerse", 
        page_icon="pokeball.ico", 
        initial_sidebar_state="collapsed"
    )

    # main page starts
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image("https://i.ibb.co/thqDjK0/Pokichat.png")

    st.write("\n")
    st.markdown("---")
    df = load_data('pokemon.csv')
    display_chat(df)
    # sidebar
    display_sidebar_content()

if __name__ == "__main__":
    main()
