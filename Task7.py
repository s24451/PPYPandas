import pandas as pd
import re
def clean_gender(df):
    df['gender'] = df['gender'].replace(to_replace=r'^Female.?', value='Female', regex=True)
    df['gender'] = df['gender'].replace(to_replace=r'^Male.?', value='Male', regex=True)
    df['gender'] = df['gender'].replace(to_replace=r'^nan.?', value='Unknown', regex=True)
    return df


def handle_missing_values(df):
    for column in df.columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df


def calculate_total_wealth_per_country(df):
    df['Country'] = df['Country'].str.replace(r'[^a-zA-Z\s]', '', regex=True).str.strip()
    total_wealth_per_country = df.groupby('Country')['income'].sum()
    return total_wealth_per_country.reset_index()

df = pd.read_csv("Data\modified_data.csv")
df['income'] = pd.to_numeric(df['income'], errors='coerce')  
df = handle_missing_values(df)
total_wealth_per_country = calculate_total_wealth_per_country(df)
total_wealth_per_country.to_csv("Data\\total_wealth_per_country.csv", index=False)
print(total_wealth_per_country)
df.to_csv("Data\modified_data.csv", index=False) 
print(df)
