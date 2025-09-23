Titanic Dataset Analysis

This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset to uncover survival patterns and correlations between passenger features.  

---

Project Structure
- `titanic_analysis.py` → Python script containing data loading, cleaning, visualization, and correlation analysis.  
- `README.md` → Documentation of the project, workflow, and findings.  

---

Libraries Used
- **Pandas** → Data handling and preprocessing  
- **NumPy** → Numerical operations  
- **Matplotlib / Seaborn** → Data visualization  
- **Scikit-learn (LabelEncoder)** → Encoding categorical values  

Steps Performed

1. Data Loading & Summary
- Loaded Titanic dataset from CSV.  
- Displayed statistics using `df.describe()` and checked datatypes.  
- Identified missing values.  

2. Handling Missing Values
- Filled missing `Age` with **median**.  
- Filled missing `Embarked` with **mode**.  

3. Encoding
- Converted categorical columns (`Sex`, `Embarked`) into numerical form using **LabelEncoder**.  

4. Visualizations
- **Histogram**: Age distribution of passengers.  
- **Boxplot**: Age distribution across passenger classes (Pclass).  
- **Correlation Heatmap**: Shows feature relationships with survival and other variables.  

5. Trends & Inferences
- Women and children survived more.  
- Higher class → higher survival.  
- Higher fare → higher survival.  
- Medium family size → better survival.  
- Missing/anomalous data in **Age**, **Cabin**, and **Fare**.  


Observations

1. Sex 
   - Female passengers had a much higher survival rate than male passengers.  
   - *Reason*: “Women and children first” policy.  

2. Pclass (Passenger Class) 
   - 1st class passengers had higher survival than 2nd and 3rd class.  
   - *Reason*: Wealthier passengers had better access to lifeboats.  

3. Age 
   - Children (Age < 12) had slightly higher survival.  
   - *Reason*: “Women and children first” rule partially followed.  

4. Fare  
   - Higher fare correlated with higher survival.  
   - *Reason*: Indicates 1st class/luxury cabins.  

5. Family Size (SibSp + Parch) 
   - Medium family size (1–3 members) survived more than solo travelers or very large families.  


