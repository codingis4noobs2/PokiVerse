import streamlit as st
import io
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

def display_msg(text, is_user='Ash'):
    """
    This function is used to display the messages UI.

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
                    {text} \n </div>
                <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <div style="color: white; margin-right: 5px;">Ash\n</div>
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
                    {text} \n </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <div style="color: white; margin-right: 5px;">May\n</div>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_chat(df):
    # convo 1
    display_msg("Hey Ash👋🏼, I got this image from Misty. I was wondering what you were doing with those graphs and charts?🤔", "May")
    st.image("https://i.ibb.co/Tq1JrvJ/Ash-doing-Analysis.png")
    display_msg("Hey May👋🏼, I was working on the Pokémon dataset. It's part of the prestigious Angelhack Monthly Challenge Series and it has an overall prize pool of 5000 Pokémon Dollars💵", "Ash")
    display_msg("That's great, Ash. I really want to learn more about this dataset. It will help with our exploration too.", "May")
    display_msg("Yes, you're right May. This will help in our exploration.", "Ash")
    display_msg("But I know very little about data analysis😭", "May")
    display_msg("HAHAHA, no worries May.", "Ash")
    display_msg("Let's start by loading the dataset. Don't worry May, if you don't know how to do this, I have included the code for you.", "Ash")
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
    display_msg("Omg, this is a very big dataset😱. How are we going to do analysis on such a big dataset?", "May")
    display_msg("The library I used to load the data & create a dataframe from this dataset is Pandas, The reason why pandas is widely used is it offers a huge number of useful methods to deal with Data")
    display_msg("That's great Ash, Got to learn something new today😊", "May")
    display_msg("HAHAHA, Enough Talking now let's jump right into the World of Data")
    display_msg("Let's start by getting a raw information about the dataset")
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
    display_msg("It has 13 Columns & 1194 Rows, Additionally 9 Columns have int datatype and 4 Columns has object datatype")
    display_msg("But i intentionally left 1 detail, Can you think of it?")
    display_msg("Yes yes, I noticed it the Type-2 Column has some null values in it", "May")
    display_msg("Great work over there May👏🏻. It is important to clean data before we start working on it")
    display_msg("But in this it is not important to replace Null, we will simply ignore the value if its Null")
    display_msg("Ohh Great, Well i was wondering where do we start from?", "May")
    display_msg("We can start by analyzing the types of Pokemons, Let's make a Piechart to better understand the distribution of types in Type-1 and Type-2")
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
    display_msg("Ohh This Visualization makes it very easy to identify the Flying is the most common type of both Type-1 and Type-2", "May")
    display_msg("Good Oberservation May, Now lets focus on the Pokemon stats distribution")
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
    display_msg("Omg i didn't knew that this libraries can be too useful", "May")
    display_msg("But it is still hard for me to understand this as if i want to know that X% Pokemons have better stat than a given value, how could i know that?", "May")
    display_msg("Don't worry, I gotch you")
    stat = st.selectbox("Choose a stat to get X% of pokemon having better stat than given", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    start = int(df[stat].min())
    end = int(df[stat].max())
    x = st.slider("Select X", min_value=start, max_value=end)
    total_pokemon = df.shape[0]
    higher_total_pokemon = df[df[stat] > x].shape[0]
    st.write(f"{higher_total_pokemon} Pokemon have better {stat} than {x} {stat}")
    display_msg("Impressive! With your help, I can now determine the number of Pokémon that possess a higher value than the given benchmark.", "Msg")
    display_msg("Waitt!!, How can we forget the most basic ones😲")
    display_msg("Huh, What happened Ash?", "May")
    display_msg("We will get the top5 Strongest & Weakest Pokemon by their stats, Let me show you how")
    stat = st.selectbox("Choose a stat to get 5 Pokemons with highest/lowest stat", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    highest_total = df.nlargest(5, stat)[['Names', stat]]
    lowest_total = df.nsmallest(5, stat)[['Names', stat]]
    st.write(highest_total)
    display_msg("That's great, I am learning soo much today!!", "May")
    display_msg("Let's analyze the pokemon stats using a radar char")
    pokemon_name = st.selectbox("Select a Pokemon to analyze", df['Names'])
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
    display_msg("As we have a stat looker for a individual pokemon why not make a Pokemon comparison looker too")
    col1, col2 = st.columns(2)
    with col1:
        pokemon_1 = st.selectbox("Select First Pokemon to analyze", df['Names'])
    with col2:
        pokemon_2 = st.selectbox("Select Second Pokemon to analyze", df['Names'])
    pokemon1 = df[df['Names'] == pokemon_2]
    if not pokemon.empty:
        hp1 = pokemon['HP'].values[0]
        attack1 = pokemon['Attack'].values[0]
        defense1 = pokemon['Defense'].values[0]
        sp_atk1 = pokemon['Sp. Atk'].values[0]
        sp_def1 = pokemon['Sp. Def'].values[0]
        speed1 = pokemon['Speed'].values[0]
    pokemon2 = df[df['Names'] == pokemon_2]
    if not pokemon.empty:
        hp2 = pokemon['HP'].values[0]
        attack2 = pokemon['Attack'].values[0]
        defense2 = pokemon['Defense'].values[0]
        sp_atk2 = pokemon['Sp. Atk'].values[0]
        sp_def2 = pokemon['Sp. Def'].values[0]
        speed2 = pokemon['Speed'].values[0]
    fig3 = go.Figure()

    fig3.add_trace(go.Scatterpolar(
        r=[hp1, attack1, defense1, sp_atk1, sp_def1, speed1],
        theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'],
        fill='toself',
        name=pokemon_1
    ))
    fig3.add_trace(go.Scatterpolar(
        r=[hp2, attack2, defense2, sp_atk2, sp_def2, speed2],
        theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'],
        fill='toself',
        name=pokemon_2
    ))

    fig3.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=False
    )
    st.plotly_chart(fig3)
