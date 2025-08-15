import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('mymoviedb.csv' , lineterminator='\n')
# print(df.head(5)) 
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
# We want to remove the unwanted columns 
df.drop(columns=['Overview','Original_Language','Poster_Url'], axis=1 , inplace=True)
print(df.head())
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)
df['Release_Date'] = df['Release_Date'].dt.year
print(df['Release_Date'].dtypes)
print(df.columns)
# Categorizing Vote Average column -> Data preprocessing
# We will categorize into - popular , average , below average , not popular 
def categorize(df , col ,labels):
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col] , edges , labels=labels , duplicates='drop')
    return df   

labels = ['not_popular' , 'below_average' , 'average' , 'popular']
# Calling functions
categorize(df , 'Vote_Average' , labels)
print(df['Vote_Average'].unique())
print(df.head())
# we want to count how many lables it has from each category
print(df['Vote_Average'].value_counts())
df.dropna(inplace=True)
print(df.isna().sum())
# we would split genres into a list and then explode our dataframe to have only one genre per row for each movie
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)
print(df.head())
# Casting column into category
df['Genre'] = df['Genre'].astype('category')
print(df['Genre'].dtypes)
print(df.info())
# gives number of unique elements
print(df.nunique())

# Q1. What is the most frequent genre of movies released on Netflix?
print(df['Genre'].describe())
sns.catplot(y = 'Genre' , data=df , kind='count' ,  order=df['Genre'].value_counts().index , color='#4287f5')
plt.title('Genre column distribution')
plt.show()
# Q2 . Which has highest vote in vote average column?
print(df['Vote_Average'].describe())
sns.catplot(y='Vote_Average' , data=df , kind='count', order=df['Vote_Average'].value_counts().index , color='#4287f5')
plt.title('Votes Distribution')
plt.show()

# What movie got the highest popularity ? what's it's genre?
print(df[df['Popularity'] == df['Popularity'].max()])

# What movie got the lowest popularity ? what's it's genre?
print(df[df['Popularity'] == df['Popularity'].min()])

# Which year has the most filmmed movies?
df['Release_Date'].hist()
plt.title('Release Date Column distribution')
plt.show()

print(df[df['Vote_Count'] == df['Vote_Count'].max()])
