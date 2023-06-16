import pandas as pd


def clean_gender(df):
    df['gender'] = df['gender'].replace(to_replace=r'^Female.?', value='Female', regex=True)
    df['gender'] = df['gender'].replace(to_replace=r'^Male.?', value='Male', regex=True)
    df['gender'] = df['gender'].replace(to_replace=r'^nan.?', value='Unknown', regex=True)
    return df

def compare_gender_wealth(df):
    df['income'] = pd.to_numeric(df['income'], errors='coerce')  
    average_wealth_by_gender = df.groupby('gender')['income'].mean()
    return average_wealth_by_gender.reset_index()



def handle_missing_values(df):
    for column in df.columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df



def categorize_wealth(df):
    labels = ['Low', 'Medium', 'High', 'Very High']
    df['wealth_category'] = pd.qcut(df['income'], q=4, labels=labels)
    return df

    
df = pd.read_csv("Data\modified_data.csv")
df = clean_gender(df)
df = handle_missing_values(df)
df = categorize_wealth(df)
df.to_csv("Data\modified_data.csv", index=False) 
print(df)

