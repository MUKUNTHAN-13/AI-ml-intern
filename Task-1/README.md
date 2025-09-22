Titanic Dataset Preprocessing
Steps Done
1. Load Dataset

Loaded Titanic dataset using pandas.

Checked dataset dimensions, data types, and missing values.

2. Handle Missing Values

Filled missing Age with median.

Filled missing Embarked with mode.

3. Encode Categorical Data

Converted Sex and Embarked into numerical values using LabelEncoder.

4. Scale Numerical Features

Standardized Age and Fare using StandardScaler.

5. Handle Outliers

Used Boxplots to visualize outliers.

Removed outliers using IQR (Interquartile Range) method.

6. Final Dataset

Displayed cleaned and processed dataset.