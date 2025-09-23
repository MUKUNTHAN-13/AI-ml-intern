import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


#Stats summary

df= pd.read_csv(r'D:\DATA\AI-ML\Titanic-Dataset.csv', index_col=0,na_values=["??"])
print("Stats summary \n",df.describe())
print("Datatypes check \n",df.dtypes)
print("\nMissing values \n", df.isnull().sum())

#Handling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
print("\nMissing values \n", df.isnull().sum())

le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])    
df['Embarked'] = le.fit_transform(df['Embarked']) 

#Histogram for age distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20,color='skyblue')
plt.title('Age Distribution of Passengers')
plt.show()

# Box plot for Age
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Pclass'],y=df['Age'],color='lightgreen')
plt.title('Box Plot of Passenger Age')
plt.show()

#Correlation 
correlation_matrix = df.corr()
plt.figure(figsize=(9,7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

#Trends
"""Women and children survived more.

Higher class → higher survival.

Higher fare → higher survival.

Medium family size → better survival.

Some missing or anomalous data in Age, Cabin, and Fare.

Survival Trends

Sex: Women had a much higher survival rate than men.

Trend: Female passengers were prioritized during evacuation.

Pclass (Passenger Class):

1st class passengers had higher survival than 2nd, and 3rd class had the lowest.

Trend: Wealthier passengers had better access to lifeboats.

Age:

Children (Age < 12) had slightly higher survival.

Trend: “Women and children first” rule was partially followed."""




