# Importing required libraries
import io
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Function to display a single message
def display_message(text, is_user='Ash'):
    """
    Function to display a chat message on the user interface.

    Parameters:
    text (str): The content of the message.
    sender (str): The sender of the message, default is 'Ash'.
    """
    # Assign avatar and styles based on the sender
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

# Function to create a radar chart
def create_radar_chart(pokemon_name, pokemon_stats):
    """
    Creates and displays a radar chart representing the stats of a specific Pokémon.

    Parameters:
    pokemon_name (str): The name of the Pokémon for which the chart is created.
    pokemon_stats (DataFrame): A DataFrame containing the Pokémon's stats. 
                               The DataFrame should contain columns for 'HP', 'Attack', 'Defense', 
                               'Sp. Atk', 'Sp. Def', and 'Speed'.
    """
    hp = pokemon_stats['HP'].values[0]
    attack = pokemon_stats['Attack'].values[0]
    defense = pokemon_stats['Defense'].values[0]
    sp_atk = pokemon_stats['Sp. Atk'].values[0]
    sp_def = pokemon_stats['Sp. Def'].values[0]
    speed = pokemon_stats['Speed'].values[0]
    fig = px.line_polar(
        r = [hp, attack, defense, sp_atk, sp_def, speed], 
        theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'], 
        line_close=True
    )
    fig.update_layout(title=f"Stats of {pokemon_name}")
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)

# Function to display Pokémon comparator
def display_comparator(pokemon_name_1, pokemon_stats_1, pokemon_name_2, pokemon_stats_2):
    """
    Creates and displays a radar chart comparing the stats of two specific Pokémon.

    Parameters:
    pokemon_name_1 (str): The name of the first Pokémon to compare.
    pokemon_stats_1 (DataFrame): A DataFrame containing the first Pokémon's stats. 
                                 The DataFrame should contain columns for 'HP', 'Attack', 'Defense', 
                                 'Sp. Atk', 'Sp. Def', and 'Speed'.
    pokemon_name_2 (str): The name of the second Pokémon to compare.
    pokemon_stats_2 (DataFrame): A DataFrame containing the second Pokémon's stats. 
                                 The DataFrame should contain columns for 'HP', 'Attack', 'Defense', 
                                 'Sp. Atk', 'Sp. Def', and 'Speed'.
    """
    categories = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    hp1, hp2 = pokemon_stats_1['HP'].values[0], pokemon_stats_2['HP'].values[0]
    attack1, attack2 = pokemon_stats_1['Attack'].values[0], pokemon_stats_2['Attack'].values[0]
    defense1, defense2 = pokemon_stats_1['Defense'].values[0], pokemon_stats_2['Defense'].values[0]
    sp_atk1, sp_atk2 = pokemon_stats_1['Sp. Atk'].values[0], pokemon_stats_2['Sp. Atk'].values[0]
    sp_def1, sp_def2 = pokemon_stats_1['Sp. Def'].values[0], pokemon_stats_2['Sp. Def'].values[0]
    speed1, speed2 = pokemon_stats_1['Speed'].values[0], pokemon_stats_2['Speed'].values[0]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[hp1, attack1, defense1, sp_atk1, sp_def1, speed1],
        theta=categories,
        fill='toself',
        name=pokemon_name_1
    ))

    fig.add_trace(go.Scatterpolar(
        r=[hp2, attack2, defense2, sp_atk2, sp_def2, speed2],
        theta=categories,
        fill='toself',
        name=pokemon_name_2
    ))

    fig.update_layout(title=f"Stats of {pokemon_name_1} vs {pokemon_name_2}")
    st.plotly_chart(fig)


# Function to display the conversation
def display_chat(df):
    """
    Function to display a all of the messages on the user interface.

    Parameters:
    dataframe (df): Dataframe
    """

    # Conversation 1
    display_message("Hey Ash👋🏼, Dawn sent me this image. She was wondering what you were doing with those graphs and charts?🤔", "May")
    st.image("https://i.ibb.co/Tq1JrvJ/Ash-doing-Analysis.png", width=400)
    display_message("Hey May👋🏼, I was analyzing the Pokémon dataset. It's part of the esteemed Angelhack Monthly Challenge Series, and it has an overall prize pool of 5000 Pokémon Dollars💵", "Ash")
    display_message("Sounds exciting, Ash. I'm eager to learn more about this dataset. It might assist us in our explorations.", "May")
    display_message("Absolutely, May. This dataset is indeed a valuable resource for our adventures.", "Ash")


    # Conversation 2
    display_message("I'm new to this whole data analysis field, though. 😭", "May")
    display_message("No worries, May. We're in this together.", "Ash")
    display_message("Let's kick off by loading the dataset. I've even included the code for you, in case you're unsure about how to do this.", "Ash")
    
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        st.dataframe(df, height=220)
    with tab2:
        st.code(
            """
            import pandas as pd

            # pd.read_csv() is used to read data from a CSV (Comma-Separated Values) file and create a DataFrame, 
            # which is a two-dimensional tabular data structure.
            df = pd.read_csv('pokemon.csv')
            print(df)
            """,
            language="python"
        )


    # Conversation 3
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


    # Conversation 4
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
            import plotly.express as px

            type1_counts = df['Type1'].value_counts()
            type2_counts = df['Type2'].value_counts()
            fig = px.pie(values=type1_counts.values, names=type1_counts.index, title='Type 1 Distribution')
            fig.show()
            fig = px.pie(values=type2_counts.values, names=type2_counts.index, title='Type 2 Distribution')
            fig.show()
            """
        )


    # Conversation 5
    display_message("This visualization makes it so easy to discern that Water has the highest count in Type-1, while Flying has highest count in Type-2.", "May")
    display_message("Great observation, May! Let's now dive into the distribution of Pokémon stats.", "Ash")
    stat = st.selectbox("Choose a stat to visualize", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    
    tab1, tab2 = st.tabs(['Results', 'Code'])
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


    # Conversation 6
    display_message("Let's see which Type in Type1 has highest Total Power")
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        plt.figure(figsize=(14,6))
        type1_total = df.groupby('Type1')['Total'].mean().sort_values()
        sns.barplot(x=type1_total.index, y=type1_total.values)
        plt.title('Average Total Power by Type1')
        plt.xticks(rotation=90)
        st.pyplot(plt)
        display_message("Let's see which Type in Type2 has highest Total Power")
        plt.figure(figsize=(14,6))
        type1_total = df.groupby('Type2')['Total'].mean().sort_values()
        sns.barplot(x=type1_total.index, y=type1_total.values)
        plt.title('Average Total Power by Type1')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    with tab2:
        st.code(
            """
            plt.figure(figsize=(14,6))
            type1_total = df.groupby('Type1')['Total'].mean().sort_values()
            sns.barplot(x=type1_total.index, y=type1_total.values)
            plt.title('Average Total Power by Type1')
            plt.xticks(rotation=90)
            st.pyplot(plt)
            display_message("Let's see which Type in Type2 has highest Total Power")
            plt.figure(figsize=(14,6))
            type1_total = df.groupby('Type2')['Total'].mean().sort_values()
            sns.barplot(x=type1_total.index, y=type1_total.values)
            plt.title('Average Total Power by Type1')
            plt.xticks(rotation=90)
            st.pyplot(plt)
            """
        )


    # Conversation 7
    display_message("It's fascinating how useful these libraries can be!", "May")
    display_message("But I'm still having difficulty understanding this, If I want to identify the number of Pokémons with stats superior to a given value, how can I do that?", "May")
    display_message("That's easy. Let me show you how.", "Ash")
    stat_choosen = st.selectbox("Choose a stat to get the number of Pokémon having better stats than a given value", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        x = st.slider(
        "Select X", 
        int(df[stat_choosen].min()), 
        int(df[stat_choosen].max())
    )
    higher_total_pokemon = df[df[stat_choosen] > x].shape[0]
    st.write(f"{higher_total_pokemon} Pokémon have better {stat_choosen} than {x} {stat_choosen} Value")
    with tab2:
        st.code(
            """
            # x can be any value between min & max value of that stat
            higher_total_pokemon = df[df[stat_choosen] > x].shape[0]
            """
        )

    
    # Conversation 8
    display_message("Amazing! Thanks to you, I can now ascertain the number of Pokémon that exceed a specified value.", "May")
    display_message("Wait a second! We seemed to have skipped the very basic part", "Ash")
    display_message("What did we miss, Ash?", "May")
    display_message("We should find out the top 5 strongest and weakest Pokémon based on their stats. Let me demonstrate how.", "Ash")
    stat_choosen = st.selectbox("Choose a stat to get the 5 Pokémon with the highest/lowest stats", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    top_five = df.nlargest(5, stat_choosen)[['Names', stat_choosen]]
    bottom_five = df.nsmallest(5, stat_choosen)[['Names', stat_choosen]]
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Pokemons Having Highest {stat_choosen}")
            st.write(top_five)
        with col2:
            st.write(f"Pokemons Having Lowest {stat_choosen}")
            st.write(bottom_five)
    with tab2:
        st.code(
            """
            top_five = df.nlargest(5, stat_choosen)[['Names', stat_choosen]]
            bottom_five = df.nsmallest(5, stat_choosen)[['Names', stat_choosen]]
            """
        )
   

    # Conversation 9
    display_message("Similary, we can get the best pokemons of any Type with indiviual stats or total stats")
    stat_choosen = st.selectbox("Choose a stat to get the 5 Pokémon with the highest/lowest stats of a Type", ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    type_choosen = st.selectbox("Choose a Type", df['Type1'].unique())
    choosen_pokemon = df[df['Type1'] == type_choosen]
    sorted_choosen_pokemon_top = choosen_pokemon.sort_values(stat, ascending=False).head(5)[['Names', stat_choosen]]
    sorted_choosen_pokemon_bottom = choosen_pokemon.sort_values(stat, ascending=True).head(5)[['Names', stat_choosen]]
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"{type_choosen} Type Pokemons Having Highest {stat_choosen}")
            st.dataframe(sorted_choosen_pokemon_top)
        with col2:
            st.write(f"{type_choosen} Type Pokemons Having Lowest {stat_choosen}")
            st.dataframe(sorted_choosen_pokemon_bottom)
    with tab2:
        st.code(
            """
            choosen_pokemon = df[df['Type1'] == type_choosen]
            sorted_choosen_pokemon_top = choosen_pokemon.sort_values(stat, ascending=False).head(5)[['Names', stat_choosen]]
            sorted_choosen_pokemon_bottom = choosen_pokemon.sort_values(stat, ascending=True).head(5)[['Names', stat_choosen]]
            """
        )


    # Conversation 10
    display_message("This is incredible! I'm gaining so much knowledge today!!", "May")
    display_message("Let's proceed to analyze Pokémon stats using a radar chart.", "Ash")
    pokemon_name = st.selectbox("Select a Pokémon to analyze", df['Names'])
    pokemon_stats = df[df['Names'] == pokemon_name]
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        create_radar_chart(pokemon_name, pokemon_stats)
    with tab2:
        st.code(
            """
            hp = pokemon_stats['HP'].values[0]
            attack = pokemon_stats['Attack'].values[0]
            defense = pokemon_stats['Defense'].values[0]
            sp_atk = pokemon_stats['Sp. Atk'].values[0]
            sp_def = pokemon_stats['Sp. Def'].values[0]
            speed = pokemon_stats['Speed'].values[0]
            fig = px.line_polar(
                r = [hp, attack, defense, sp_atk, sp_def, speed], 
                theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'], 
                line_close=True
            )
            fig.update_layout(title=f"Stats of {pokemon_name}")
            fig.update_traces(fill='toself')
            fig.show()
            """
        )
    

    # Conversation 11
    display_message("Wait i got an idea💡", "Ash")
    display_message("Since we already have a stat tracker for individual Pokémon, why don't we create a Pokémon comparator too?", "Ash")
    pokemon_name_1 = st.selectbox("Select the first Pokémon", df['Names'], key="1")
    pokemon_name_2 = st.selectbox("Select the second Pokémon", df['Names'], key="2")
    pokemon_stats_1 = df[df['Names'] == pokemon_name_1]
    pokemon_stats_2 = df[df['Names'] == pokemon_name_2]
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        display_comparator(
            pokemon_name_1, 
            pokemon_stats_1, 
            pokemon_name_2, 
            pokemon_stats_2
        )
    with tab2:
        st.code(
            """
            categories = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
            hp1, hp2 = pokemon_stats_1['HP'].values[0], pokemon_stats_2['HP'].values[0]
            attack1, attack2 = pokemon_stats_1['Attack'].values[0], pokemon_stats_2['Attack'].values[0]
            defense1, defense2 = pokemon_stats_1['Defense'].values[0], pokemon_stats_2['Defense'].values[0]
            sp_atk1, sp_atk2 = pokemon_stats_1['Sp. Atk'].values[0], pokemon_stats_2['Sp. Atk'].values[0]
            sp_def1, sp_def2 = pokemon_stats_1['Sp. Def'].values[0], pokemon_stats_2['Sp. Def'].values[0]
            speed1, speed2 = pokemon_stats_1['Speed'].values[0], pokemon_stats_2['Speed'].values[0]

            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=[hp1, attack1, defense1, sp_atk1, sp_def1, speed1],
                theta=categories,
                fill='toself',
                name=pokemon_name_1
            ))

            fig.add_trace(go.Scatterpolar(
                r=[hp2, attack2, defense2, sp_atk2, sp_def2, speed2],
                theta=categories,
                fill='toself',
                name=pokemon_name_2
            ))

            fig.update_layout(title=f"Stats of {pokemon_name_1} vs {pokemon_name_2}")
            fig.show()
            """
        )
    display_message("Woohooo🥳, This comparison is gonna help us very much in our exploration", "May")


    # Conversation 12
    display_message("What do you think May, Is it possible there exists a Pokemon who has all same stats?")
    display_message("Woah, that maybe possible though", "May")
    display_message("Let's see, we can try")
    df_equal_stats = df[df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].apply(lambda x: x.nunique() == 1, axis=1)]
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        st.dataframe(df_equal_stats)
    with tab2:
        st.code(
            """
            df_equal_stats = df[df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].apply(lambda x: x.nunique() == 1, axis=1)]
            """
        )
    display_message("There exists some Pokemons who have such stats👀, This is crazy")


    # Conversation 13
    display_message("Let's try Comparing One Type vs Another Type")
    display_message("Yes, that will give even more details about the Pokemon nature", "May")
    fire_pokemon = df[(df['Type1'] == 'Fire') | ((df['Type2']) == "Fire")] #contains all fire pokemons
    water_pokemon = df[(df['Type1'] == 'Water') | ((df['Type2']) == "Water")]  #all water pokemons
    tab1, tab2 = st.tabs(['Results', 'Code'])
    with tab1:
        plt.figure(figsize=(10, 6))
        plt.scatter(fire_pokemon.Attack.head(50), fire_pokemon.Defense.head(50), color = 'red', label = 'Fire',marker = "*",s = 50)
        plt.scatter(water_pokemon.Attack.head(50), water_pokemon.Defense.head(50), color = 'blue', label = "Water",s = 25)
        plt.xlabel("Attack")
        plt.ylabel("Defense")
        plt.legend()
        plt.plot()
        fig=plt.gcf()
        fig.set_size_inches(12,6)
        st.pyplot(fig)
    with tab2:
        st.code(
            """
            plt.figure(figsize=(10, 6))
            plt.scatter(fire_pokemon.Attack.head(50), fire_pokemon.Defense.head(50), color = 'red', label = 'Fire',marker = "*",s = 50)
            plt.scatter(water_pokemon.Attack.head(50), water_pokemon.Defense.head(50), color = 'blue', label = "Water",s = 25)
            plt.xlabel("Attack")
            plt.ylabel("Defense")
            plt.legend()
            plt.plot()
            fig=plt.gcf()
            fig.set_size_inches(12,6)
            st.pyplot(fig)

            # fire_pokemon = df[df['Type1'] == 'Fire']
            # water_pokemon = df[df['Type1'] == 'Water']

            # fire_total_mean = fire_pokemon['Total'].mean()
            # water_total_mean = water_pokemon['Total'].mean()

            # fire_attack_mean = fire_pokemon['Attack'].mean()
            # water_attack_mean = water_pokemon['Attack'].mean()

            # fire_defense_mean = fire_pokemon['Defense'].mean()
            # water_defense_mean = water_pokemon['Defense'].mean()

            # fire_sp_atk_mean = fire_pokemon['Sp. Atk'].mean()
            # water_sp_atk_mean = water_pokemon['Sp. Atk'].mean()

            # fire_sp_def_mean = fire_pokemon['Sp. Def'].mean()
            # water_sp_def_mean = water_pokemon['Sp. Def'].mean()

            # fire_speed_mean = fire_pokemon['Speed'].mean()
            # water_speed_mean = water_pokemon['Speed'].mean()
            """
        )
    display_message("This shows that Fire type pokemons have a better attack than Water type pokemons but have a lower defence than water type.")
    display_message("Let's check this by getting the average values of both types, If you want to compare other stats Feel free to do so")
    display_message("Have a look in the Code section, you have to just change the Type and stat you want to compare!")
    display_message("Great work Ash!!")
