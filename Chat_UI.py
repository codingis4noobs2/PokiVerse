import streamlit as st
import io
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

def display_message(text, is_user='Ash'):
    """
    This function is used to display the message UI.

    Parameters:
    text (str): The text to be displayed.
    is_user (bool): Whether the message is from the user or not.
    """
    if is_user == 'Ash':
        avatar_url = "https://i.ibb.co/PZ9KYmr/ash.png"
        message_alignment = "flex-end"
        message_bg_color = "linear-gradient(135deg, #00B2FF 0%, #006AFF 100%)"
        avatar_class = "user-avatar"
        st.write(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px; border: 1px solid #ccc;">
                    {text}
                </div>
                <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <div style="color: white; margin-right: 5px;">Ash</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        avatar_url = "https://i.ibb.co/C0tZHdd/may.png"
        message_alignment = "flex-start"
        message_bg_color = "#71797E"
        avatar_class = "bot-avatar"

        st.write(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px; border: 1px solid #ccc;">
                    {text}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <div style="color: white; margin-right: 5px;">May</div>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_chat(df):
    # Conversation 1
    display_message("Hey Ash👋🏼, Misty sent me this image. I was wondering what you were doing with those graphs and charts?🤔", "May")
    st.image("https://i.ibb.co/Tq1JrvJ/Ash-doing-Analysis.png")
    display_message("Hey May👋🏼, I was working on the Pokémon dataset. It's part of the prestigious Angelhack Monthly Challenge Series, and it has an overall prize pool of 5000 Pokémon Dollars💵", "Ash")
    display_message("That's great, Ash. I'm really interested in learning more about this dataset. It will also help us with our exploration.", "May")
    display_message("Yes, you're right May. This dataset will definitely aid in our exploration.", "Ash")
    display_message("But I know very little about data analysis😭", "May")
    display_message("HAHAHA, no worries May.", "Ash")
    display_message("Let's start by loading the dataset. Don't worry, if you don't know how to do this, I have included the code for you.", "Ash")
    tab1, tab2 = st.tabs(['Dataset', 'Code'])
    with tab1:
        st.dataframe(df, height=220)
    with tab2:
        st.code(
            """
            import pandas as pd


            df = pd.read_csv('pokemon.csv')
            print(df)
            # pd.read_csv() is used to read data from a CSV (Comma-Separated Values) file and create a DataFrame, 
            # which is a two-dimensional tabular data structure.
            """,
            language="python"
        )
    display_message("Wow, this dataset is quite extensive😱. How are we going to perform analysis on such a large dataset?", "May")
    display_message("The library I used to load the data and create a DataFrame from this dataset is Pandas. Pandas is widely used because it offers a vast number of useful methods to deal with data.", "Ash")
    display_message("That's great, Ash! I've learned something new today😊", "May")
    display_message("HAHAHA, enough talking. Let's jump right into the world of data!", "Ash")
    display_message("Let's start by getting some basic information about the dataset.", "Ash")
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    with tab2:
        st.code(
            """
            df.info()
            # The output of `df.info()` will typically include the following information for each column:
            # Column name, Count of non-null values, Data type of the column, Memory usage
            """,
            language="python"
        )
    display_message("The dataset consists of 13 columns and 1194 rows. Additionally, 9 columns have an integer datatype, and 4 columns have an object datatype.", "Ash")
    display_message("But I intentionally left out one detail. Can you guess what it is?", "Ash")
    display_message("Yes, yes! I noticed it. The Type-2 column has some null values in it.", "May")
    display_message("Great work, May👏🏻! It is important to clean the data before we start working with it.", "Ash")
    display_message("In this case, it is not necessary to replace the null values. We will simply ignore them.", "Ash")
    display_message("Ohh, great! Well, I was wondering where do we start from?", "May")
    display_message("We can start by analyzing the types of Pokémon. Let's create a pie chart to better understand the distribution of types in Type-1 and Type-2.", "Ash")
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        type1_counts = df['Type1'].value_counts()
        type2_counts = df['Type2'].value_counts()

        fig = px.pie(values=type1_counts.values, names=type1_counts.index, title='Type 1 Distribution')
        st.plotly_chart(fig)

        fig = px.pie(values=type2_counts.values, names=type2_counts.index, title='Type 2 Distribution')
        st.plotly_chart(fig)
    with tab2:
        st.code(
            """
            type1_counts = df['Type1'].value_counts()
            type2_counts = df['Type2'].value_counts()

            fig = px.pie(values=type1_counts.values, names=type1_counts.index, title='Type 1 Distribution')
            st.plotly_chart(fig)

            fig = px.pie(values=type2_counts.values, names=type2_counts.index, title='Type 2 Distribution')
            st.plotly_chart(fig)
            """
        )
    display_message("Ohh, this visualization makes it very easy to identify that Flying is the most common type in both Type-1 and Type-2.", "May")
    display_message("Good observation, May! Now, let's focus on the distribution of Pokémon stats.", "Ash")
    stat = st.selectbox("Choose a stat to visualize", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    tab1, tab2 = st.tabs(['Result', 'Code'])
    with tab1:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[stat], kde=True)
        plt.title(f'Distribution of Count vs {stat}')
        st.pyplot(plt)
    with tab2:
        st.code(
            """
            import matplotlib.pyplot as plt
            import seaborn as sns


            plt.figure(figsize=(10, 6))
            sns.histplot(df[stat], kde=True)
            plt.title(f'Distribution of Count vs {stat}')
            plt.show()
            """
        )
    display_message("Wow, I didn't know that these libraries could be so useful.", "May")
    display_message("But it's still hard for me to understand. If I want to know what percentage of Pokémon have better stats than a given value, how can I find that out?", "May")
    display_message("Don't worry, I've got you covered.", "Ash")
    stat = st.selectbox("Choose a stat to get the percentage of Pokémon having better stats than a given value", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    start = int(df[stat].min())
    end = int(df[stat].max())
    x = st.slider("Select X", min_value=start, max_value=end)
    total_pokemon = df.shape[0]
    higher_total_pokemon = df[df[stat] > x].shape[0]
    st.write(f"{higher_total_pokemon} Pokémon have better {stat} than {x} {stat}")
    display_message("Impressive! With your help, I can now determine the number of Pokémon that possess a higher value than the given benchmark.", "Ash")
    display_message("Wait! How can we forget the basics?", "May")
    display_message("Huh? What happened, Ash?", "May")
    display_message("We can get the top 5 strongest and weakest Pokémon based on their stats. Let me show you how.", "Ash")
    stat = st.selectbox("Choose a stat to get the 5 Pokémon with the highest/lowest stats", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    highest_total = df.nlargest(5, stat)[['Names', stat]]
    lowest_total = df.nsmallest(5, stat)[['Names', stat]]
    st.write(highest_total)
    display_message("That's great! I'm learning so much today!!", "May")
    display_message("Let's analyze the Pokémon stats using a radar chart.", "Ash")
    pokemon_name = st.selectbox("Select a Pokémon to analyze", df['Names'])
    pokemon = df[df['Names'] == pokemon_name]
    if not pokemon.empty:
        hp = pokemon['HP'].values[0]
        attack = pokemon['Attack'].values[0]
        defense = pokemon['Defense'].values[0]
        sp_atk = pokemon['Sp. Atk'].values[0]
        sp_def = pokemon['Sp. Def'].values[0]
        speed = pokemon['Speed'].values[0]
        fig = px.line_polar(df, r=[hp, attack, defense, sp_atk, sp_def, speed], theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'], line_close=True)
        fig.update_traces(fill='toself')
        st.plotly_chart(fig)
    display_message("As we have a stat looker for individual Pokémon, why not create a Pokémon comparison looker too?", "Ash")
