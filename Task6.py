import pandas as pd
def clean_gender(df):
    df['gender'] = df['gender'].replace(to_replace=r'^Female.?', value='Female', regex=True)
    df['gender'] = df['gender'].replace(to_replace=r'^Male.?', value='Male', regex=True)
    df['gender'] = df['gender'].replace(to_replace=r'^nan.?', value='Unknown', regex=True)
    return df


def handle_missing_values(df):
    for column in df.columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df


def categorize_age(df):
    bins = [0, 17, 29, 49, df['Age'].max()]
    labels = ['0-17', '18-29', '30-49', '50+']
    df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    return df

def analyze_age_groups_per_country(df):
    age_group_counts = df.groupby(['Country', 'age_group']).size()
    print(age_group_counts)

df = pd.read_csv("Data\modified_data.csv")
df = clean_gender(df)
df = handle_missing_values(df)
df = categorize_age(df)
analyze_age_groups_per_country(df)
df.to_csv("Data\modified_data.csv", index=False) 
print(df)
