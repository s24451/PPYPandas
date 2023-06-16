import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    data['Country'] = data['Country'].str.replace(r'[^a-zA-Z\s]', '', regex=True).str.strip()

    data['Country'] = data['Country'].fillna('Unknown')

   
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
    data['Age'] = data['Age'].fillna(data['Age'].mean())

    data['income'] = pd.to_numeric(data['income'], errors='coerce')
    data['income'] = data['income'].fillna(data['income'].mean())

    data = data.replace({'':np.nan, ';':np.nan})
    data = data.dropna()

    return data


def analyze_country_multiplicity(data):
    country_counts = data['Country'].value_counts()
    return country_counts


def count_owned_goods(data):
    goods_cols = ['owns_car', 'owns_TV', 'owns_house', 'owns_Phone']
    data[goods_cols] = data[goods_cols].replace({'^Yes.*': 1, '^No.*': 0, '^nan.*': np.nan}, regex=True)
    data['owned_goods'] = data[goods_cols].sum(axis=1)
    return data




data = load_and_clean_data("Data/people_data.csv")
country_counts = analyze_country_multiplicity(data)
print(country_counts)
data = count_owned_goods(data)
data.to_csv('Data\modified_data.csv', index=False)
