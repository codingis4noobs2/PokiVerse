# PokiVerse
![PokiVerse](https://i.ibb.co/4g9vGt2/Poki-Verse.png)

# Table of Contents
1. [Introduction](#introduction)
2. [Where to access](#where-to-access)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Usage](#usage)
6. [Conclusions Gained](#conclusions-gained)

## Introduction
This project aims to explore and visualize the battle statistics of various Pokémon species using a [pokemon dataset](https://www.kaggle.com/datasets/rohanpatil63/pokemon-dataset). The main goal of this project is to identify the Patterns/Trends & Relationships among the data, Also the project is designed in such a way that even newbies can easily understand the process of data analytics. This Project will even teach you the basics of data analytics as well learn the best practices used in the industry.

## Where to access
1. Streamlit(Hosted Online): [Pokiverse](https://pokiverse.streamlit.app/)

## Features

- **Dataset Display**: The application loads and displays the Pokémon dataset, providing a tabular view of the data.

- **Basic Dataset Information**: Users can view basic information about the dataset, such as the number of rows, columns, and data types.

- **Type Distribution Visualization**: The application uses pie charts to visualize the distribution of Pokémon types in both Type-1 and Type-2 categories.

- **Stat Distribution Visualization**: Users can explore the distribution of Pokémon stats (such as Total, HP, Attack, Defense, etc.) using histograms.

- **Percentage Calculation**: The application calculates the percentage of Pokémon that have better stats than a user-specified value.

- **Top and Bottom Pokémon**: Users can find the top 5 strongest and weakest Pokémon based on their stats.

- **Stat Analysis**: The application provides a radar chart to analyze the stats of a selected Pokémon, allowing users to compare different stats visually.

## Technologies Used

- **Python**: The programming language used to build the application logic and data analysis functionality.

- **Streamlit**: The Python framework used for building the interactive web application.

- **Pandas**: A powerful library for data manipulation and analysis, used for loading and processing the Pokémon dataset.

- **Plotly Express**: A high-level data visualization library, used for creating pie charts and radar charts.

- **Matplotlib**: A popular plotting library in Python, used for creating histograms.

- **Seaborn**: A data visualization library built on top of Matplotlib, used for enhancing the visual aesthetics of the histograms.

## Usage

1. Clone this repository to your local machine.

2. Install the required dependencies using the following command: `pip install -r requirements.txt`

3. Run the application using the following command: `streamlit run app.py`

4. Access the application in your web browser at `http://localhost:8501`.

5. Follow the chat conversation between "Ash" and "May" to explore and analyze the Pokémon dataset interactively.

## Conclusions Gained

### Water Type has the highest count in Type-1, while Flying Type has highest count in Type-2.

### 5 Pokémon with Highest Total
|    | Names                    | Total |
|---:|:-------------------------|------:|
| 1  | Eternatus Eternamax      |  1125 |
| 2  | Mewtwo Mega Mewtwo X     |  780  |
| 3  | Mewtwo Mega Mewtwo Y     |  780  |
| 4  | Rayquaza Mega Rayquaza   |  780  |
| 5  | Kyogre Primal Kyogre     |  770  |

### 5 Pokémon with Lowest Total
|    | Names                    | Total |
|---:|:-------------------------|------:|
| 1  | Wishiwashi Solo Form     |  175  |
| 2  | Sunkern                  |  180  |
| 3  | Blipbug                  |  180  |
| 4  | Snom                     |  185  |
| 5  | Azurill                  |  190  |

...

### 5 Pokémon with Highest Speed
|    | Names                    | Speed |
|---:|:-------------------------|------:|
| 1  | Regieleki                |  200  |
| 2  | Deoxys Speed Forme       |  180  |
| 3  | Ninjask                  |  160  |
| 4  | Pheromosa                |  151  |
| 5  | Alakazam Mega Alakazam   |  150  |

### 5 Pokémon with Lowest Speed
|    | Names                    | Speed |
|---:|:-------------------------|------:|
| 1  | Shuckle                  |   5   |
| 2  | Munchlax                 |   5   |
| 3  | Pyukumuku                |   5   |
| 4  | Trapinch                 |  10   |
| 5  | Bonsly                   |  10   |

### There exists 19 such Pokemons which have same indiviual stats, i.e. HP == Attack == Defense == Sp. Atk == Sp. Def == Speed


Feel free to explore the dataset and analyze the Pokémon stats!!!
