# Importing required libraries
import streamlit as st
import pandas as pd
from Chat_UI import display_chat


# Function to load data into DataFrame using pandas
@st.cache_data
def load_data(file_path):
    """Load data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

# Function to display content on the sidebar
def display_sidebar_content():
    """Displays content on the sidebar."""
    st.sidebar.markdown("About")
    st.sidebar.markdown("Dataset Link: [Pokemon Dataset](https://www.kaggle.com/datasets/rohanpatil63/pokemon-dataset)")
    st.sidebar.markdown("You can support it by starring:star: the project, Github Link: [PokiVerse](https://github.com/codingis4noobs2/PokiVerse)")
    st.sidebar.markdown("Credits:")

# Main function to run the app
def main():
    """Main function to run the app."""
    # Page configuration
    st.set_page_config(
        page_title="PokiVerse", 
        page_icon="pokeball.ico", 
        initial_sidebar_state="collapsed"
    )

    # Main page starts
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image("https://i.ibb.co/4g9vGt2/Poki-Verse.png")

    st.write("\n")
    st.markdown("---")
    
    # Load data
    df = load_data('pokemon.csv')
    
    # Display chat
    display_chat(df)
    
    # Display sidebar
    display_sidebar_content()

# Running the app
if __name__ == "__main__":
    main()
