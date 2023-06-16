import pandas as pd


def country_level_summary(df):
    summary_df = df.groupby('Country').agg({
        'owned_goods': 'mean',
        'Age': 'min'
    })
    

    summary_df['owned_goods'] = summary_df['owned_goods'].round(2)
    
  
    summary_df.reset_index(inplace=True)
    
    
    summary_df.columns = ['Country', 'Average Owned Goods', 'Minimum Age']
    
    return summary_df


df = pd.read_csv('Data\modified_data.csv')
summary_df = country_level_summary(df)
print(summary_df)

