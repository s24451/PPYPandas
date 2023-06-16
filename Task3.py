import pandas as pd

def compare_gender_wealth(data):
    data['gender'] = data['gender'].replace({'^Male.*': 'Male', '^Female.*': 'Female'}, regex=True)
    data['income'] = pd.to_numeric(data['income'], errors='coerce')

    average_wealth_by_gender = data.groupby('gender')['income'].mean().reset_index()
    average_wealth_by_gender = average_wealth_by_gender[average_wealth_by_gender['gender'] != 'nan&']
    average_wealth_by_gender = average_wealth_by_gender.dropna()

    average_wealth_by_gender.columns = ['gender', 'income']

    return average_wealth_by_gender

df = pd.read_csv('Data\modified_data.csv')


gender_wealth_comparison = compare_gender_wealth(df)
print(gender_wealth_comparison)
