import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
country_wise = pd.read_csv('country_wise_latest.csv')
covid_clean = pd.read_csv('covid_19_clean_complete.csv')
day_wise = pd.read_csv('day_wise.csv')
full_grouped = pd.read_csv('full_grouped.csv')
worldometer = pd.read_csv('worldometer_data.csv')

# Fix column names for worldometer dataset
worldometer.rename(columns={"Country/Region": "Country", "Serious,Critical": "SeriousCritical"}, inplace=True)

# App layout
st.set_page_config(page_title="COVID-19 Data Dashboard", layout="wide")
st.title("COVID-19 Data Dashboard 🌍🦠")

# Sidebar Navigation
st.sidebar.title("Navigation 🧭")
page = st.sidebar.radio("Go to", 
                         ["Home 🏠", "Daily Cases Analysis 📅", "Country-wise Analysis 🌍", "Population vs Cases 🌍", 
                          "Additional Analysis 📊"])

# Home Page
if page == "Home 🏠":
    st.header("Welcome to the COVID-19 Data Dashboard 👋")
    st.markdown("""
    Explore insights into the COVID-19 pandemic using various datasets and interactive charts:
    - **📅 Daily Cases Analysis**: Track global daily trends.
    - **🌍 Country-wise Analysis**: Compare COVID cases for individual countries.
    - **📊 Population vs Cases**: Examine the relationship between population and COVID-19 cases.
    - **📈 Additional Analysis**: More in-depth analysis on cases, testing, fatality rates, etc.
    """)

# Daily Cases Analysis
elif page == "Daily Cases Analysis 📅":
    st.header("Global Daily Cases Analysis 📊")
    st.markdown("### Trends Over Time 📅")

    # Line chart for confirmed, deaths, and recovered cases
    fig = px.line(day_wise, x='Date', y=['Confirmed', 'Deaths', 'Recovered'], 
                  labels={'value': 'Cases', 'variable': 'Category'},
                  title="Global Daily Trends (Confirmed, Deaths, and Recovered)", 
                  color_discrete_map={'Confirmed': 'royalblue', 'Deaths': 'red', 'Recovered': 'green'})
    st.plotly_chart(fig)

    # Daily new cases bar chart
    st.markdown("### Global Daily New Cases 📈")
    fig_new_cases = px.bar(day_wise, x='Date', y='New cases', 
                           title="Global Daily New Cases",
                           labels={'New cases': 'New Cases'},
                           color='New cases', color_continuous_scale='Viridis')
    st.plotly_chart(fig_new_cases)

# Country-wise Analysis
elif page == "Country-wise Analysis 🌍":
    st.header("Country-wise COVID-19 Analysis 🌍")
    
    # Dropdown for country selection
    selected_country = st.selectbox("Select a Country 🇺🇳", country_wise['Country/Region'].unique())
    
    country_data = country_wise[country_wise['Country/Region'] == selected_country]
    st.write(f"### Data for {selected_country}")
    st.write(country_data)

    # Reshape data into long format for the bar chart
    country_data_long = country_data.melt(id_vars=["Country/Region"], value_vars=["Confirmed", "Deaths", "Recovered"],
                                          var_name="Metrics", value_name="Count")

    # Bar chart for Confirmed, Deaths, and Recovered cases
    fig_country = px.bar(country_data_long, x="Metrics", y="Count", 
                         labels={"Metrics": "Metric", "Count": "Count"},
                         title=f"{selected_country}: Confirmed, Deaths, and Recovered Cases",
                         color="Metrics", color_discrete_map={"Confirmed": "royalblue", "Deaths": "red", "Recovered": "green"})
    st.plotly_chart(fig_country)

# Population vs Cases
elif page == "Population vs Cases 🌍":
    st.header("Population vs Total COVID-19 Cases 🌍")
    
    # Handle missing values in ActiveCases
    worldometer['ActiveCases'] = worldometer['ActiveCases'].fillna(0)

    # Scatter plot showing relationship between population and total cases
    fig = px.scatter(worldometer, 
                     x='Population', 
                     y='TotalCases', 
                     size='ActiveCases', 
                     color='Continent', 
                     hover_name='Country',
                     title="Population vs Total Cases",
                     labels={'Population': 'Population', 'TotalCases': 'Total Cases'},
                     color_continuous_scale='Rainbow')
    st.plotly_chart(fig)

    st.markdown("""
    The size of the bubbles represents the number of active cases, while the color indicates the continent.
    """)

# Additional Analysis
elif page == "Additional Analysis 📊":
    st.sidebar.title("Explore Additional Analysis 🔍")
    additional_analysis = st.sidebar.radio("Select Analysis", 
                                           ["Top 10 Countries by Cases 🌍", "Case Fatality Rates 💀", "Testing vs Cases 🧪",
                                             "Confirmed Cases Growth 📈", "Continent-wise Comparison 🌍", "Top 10 Countries by Deaths 💀"])

    # Top 10 Countries by Cases
    if additional_analysis == "Top 10 Countries by Cases 🌍":
        st.header("Top 10 Countries by Total Cases 🌍")
        top10_cases = worldometer.nlargest(10, 'TotalCases')
        fig_top10 = px.bar(top10_cases, x='Country', y='TotalCases', 
                           title="Top 10 Countries by Total Cases",
                           labels={'TotalCases': 'Total Cases'},
                           color='TotalCases', color_continuous_scale='Blues')
        st.plotly_chart(fig_top10)

    # Case Fatality Rates
    elif additional_analysis == "Case Fatality Rates 💀":
        st.header("Case Fatality Rates (CFR) - Percentage of Deaths 💀")
        worldometer['CFR'] = (worldometer['TotalDeaths'] / worldometer['TotalCases']) * 100
        fig_cfr = px.scatter(worldometer, x='Country', y='CFR', 
                             size='TotalCases', color='Continent',
                             title="Case Fatality Rates by Country",
                             labels={'CFR': 'Case Fatality Rate (%)'},
                             color_continuous_scale='Jet')
        st.plotly_chart(fig_cfr)

    # Testing vs Cases
    elif additional_analysis == "Testing vs Cases 🧪":
        st.header("Testing vs Total Cases 🧪")
        fig_tests_cases = px.scatter(worldometer, 
                                     x='TotalTests', 
                                     y='TotalCases', 
                                     size='Population', 
                                     color='Continent',
                                     hover_name='Country',
                                     title="Testing vs Total Cases",
                                     labels={'TotalTests': 'Total Tests', 'TotalCases': 'Total Cases'},
                                     color_continuous_scale='Plasma')
        st.plotly_chart(fig_tests_cases)

    # Confirmed Cases Growth
    elif additional_analysis == "Confirmed Cases Growth 📈":
        st.header("Confirmed Cases Growth Over Time 📈")
        fig_growth = px.line(day_wise, x='Date', y='Confirmed', 
                             title="Growth of Confirmed COVID-19 Cases Over Time",
                             labels={'Date': 'Date', 'Confirmed': 'Confirmed Cases'},
                             color_discrete_sequence=['#ff6600'])
        st.plotly_chart(fig_growth)

    # Continent-wise Comparison
    elif additional_analysis == "Continent-wise Comparison 🌍":
        st.header("Continent-wise Comparison of COVID-19 Cases 🌍")
        fig_continent = px.bar(worldometer, x='Continent', y='TotalCases', 
                               title="COVID-19 Cases by Continent",
                               labels={'Continent': 'Continent', 'TotalCases': 'Total Cases'},
                               color='Continent', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig_continent)

    # Top 10 Countries by Deaths
    elif additional_analysis == "Top 10 Countries by Deaths 💀":
        st.header("Top 10 Countries by Deaths 💀")
        top10_deaths = worldometer.nlargest(10, 'TotalDeaths')
        fig_top10_deaths = px.bar(top10_deaths, x='Country', y='TotalDeaths', 
                                  title="Top 10 Countries by Total Deaths",
                                  labels={'TotalDeaths': 'Total Deaths'},
                                  color='TotalDeaths', color_continuous_scale='Reds')
        st.plotly_chart(fig_top10_deaths)

# Footer with Data Sources
st.markdown("### Data Sources 📚")
st.markdown("""
- **Country-wise Data:** `country_wise_latest.csv`
- **Daily Cases:** `day_wise.csv`
- **Global Trends:** `full_grouped.csv`
- **Worldometer Data:** `worldometer_data.csv`
""")
st.markdown("#### Made By Fatima")
