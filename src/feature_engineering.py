import pandas as pd
import numpy as np
import sklearn.preprocessing as ps

def categorizing_dataset(dframe):
    # ------ Cleaning: group
    df = dframe.copy()

    # 1. job_title
    job_categories = {
        'Deep Learning Engineer': 10,
        'Machine Learning Engineer': 9,
        'Research Engineer': 8,
        'BI Analyst': 7,
        'Data Scientist': 6,
        'Data Engineer': 5,
        'Data Analyst': 4,
        'Business Analyst': 3,
        'AI Engineer': 2,
        'BI Engineer': 1
    }
    df["job_title"] = df.job_title.replace(job_categories)

    # 2. remote_ratio
    remote_categories = {
        'En remoto': 100,
        'Híbrido': 50,
        'Presencial': 0
    }
    df["remote_ratio"] = df.remote_ratio.replace(remote_categories)

    # 3. employment_type
    oneonehotencoder = ps.OneHotEncoder()
    df[['Jornada completa', 'Contrato por obra', 'Prácticas']] = oneonehotencoder.fit_transform(df["employment_type"].values.reshape(-1, 1)).toarray()

    # 4. experience_level
    experience_categories = {
        'Director': 3,
        'Ejecutivo': 3,
        'Algo de responsabilidad': 2,
        'Intermedio': 2,
        'Sin experiencia': 1,
        'Prácticas': 0
    }
    df["experience_level"] = df.experience_level.replace(experience_categories)

    # 5. company_size
    df[['L', 'M', 'S']] = oneonehotencoder.fit_transform(df["company_size"].values.reshape(-1, 1)).toarray()

    return df


# MAIN FUNCTION
def feature_engineering():
    linkedin = pd.read_csv('./data/linkedin_standarized.csv')

    # Split dataframe by rows with null salary and the ones we need to use for fitting the model
    to_predict = linkedin[linkedin['salary'].isnull()]
    linkedin = linkedin[~linkedin['salary'].isnull()]

    # Saving the data for sql queries before the feature engineering
    linkedin.to_csv('../data/linkedin_salaries_sql.csv', index=False)

    # Drop nulls
    linkedin = linkedin.dropna()
    prepared_to_predict = to_predict.dropna(subset=to_predict.columns.difference(['salary']), how='any')

    # Feature Engineering
    prepared_linkedin = categorizing_dataset(linkedin)
    prepared_to_predict = categorizing_dataset(prepared_to_predict)




