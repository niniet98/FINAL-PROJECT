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
    employment_type = {
        'Jornada completa': 4,
        'Media jornada': 3,
        'Contrato_por_obra': 2,
        'Prácticas': 1
    }
    df['employment_type'] = df.employment_type.replace(employment_type)

    # 4. experience_level
    experience_categories = {
        'Director': 6,
        'Ejecutivo': 5,
        'Algo de responsabilidad': 4,
        'Intermedio': 3,
        'Sin experiencia': 2,
        'Temporal': 1,
        'Prácticas': 0
    }
    df["experience_level"] = df.experience_level.replace(experience_categories)

    # 5. company_size
    oneonehotencoder = ps.OneHotEncoder()
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




