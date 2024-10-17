import pandas as pd

##Defining function to load csv file
def load_data(file_path):                  
    return pd.read_csv(file_path)

##Functions to clean and preprocess the data
import pandas as pd
from sklearn.model_selection import train_test_split

def clean_data(df):
    df = df.dropna(subset=['age', 'gender', 'ethnicity'])
    df['height'].fillna(df['height'].mean(), inplace=True)
    df['weight'].fillna(df['weight'].mean(), inplace=True)
    df = pd.get_dummies(df, columns=['ethnicity'])
    df['gender'] = df['gender'].map({'M': 1, 'F': 0})
    return df

def split_data(df):
    X = df[['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
            'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']]
    y = df['diabetes_mellitus']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
