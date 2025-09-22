import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler


"Task1.1"

df= pd.read_csv(r'D:\DATA\AI-ML\Titanic-Dataset.csv', index_col=0,na_values=["??"])

print("\nDimension of dataset:\n", df.shape)
print("\nData types of dataset:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

"Task 1.2"""

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

"Task 1.3"

le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])    
df['Embarked'] = le.fit_transform(df['Embarked'])  
print(df)

"Task1.4"

scaler = StandardScaler()
num_cols = ['Age', 'Fare']
df[num_cols] = scaler.fit_transform(df[num_cols])

"Task1.5"

for col in num_cols:
    sns.boxplot(x=df[col])
    plt.title(f"Outliers in {col}")
    plt.show()

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]
    
    
print(df.head())
print(df.info())

