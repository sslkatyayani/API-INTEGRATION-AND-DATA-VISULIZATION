import requests
import pandas as pd
import matplotlib.pyplot as plt

try:
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Get top 5 countries with highest cases
    top_countries = sorted(data, key=lambda x: x["cases"], reverse=True)[:5]

    df = pd.DataFrame([{
        "Country": country["country"],
        "Total Cases": country["cases"],
        "Total Deaths": country["deaths"],
        "Recovered": country["recovered"]
    } for country in top_countries])

    df.to_csv("top_5_covid_countries.csv", index=False)
    print("CSV saved as top_5_covid_countries.csv")

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(df["Country"], df["Total Cases"], color="orange")
    plt.title("Top 5 Countries - COVID-19 Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.tight_layout()
    plt.savefig("covid_chart.png")
    print("Chart saved as covid_chart.png")

except Exception as e:
    print("Something went wrong:", e)