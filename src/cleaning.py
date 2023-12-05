import pandas as pd
import numpy as np
import re

def fclean_company_state(df, states):
    for i in states:
        df['company_state'] = df['company_state'].apply(lambda row: i if i in str(row) else row)
    return df

def sclean_company_state(df, states):
    for key, value in states.items():
        df['company_state'] = df['company_state'].apply(lambda row: value if key in str(row) else row)
    return df

def clean_remote_ratio(df, list_):
    for i in list_:
        df['remote_ratio'] = df['remote_ratio'].apply(lambda row: i if i in str(row) else str(row))
    df['remote_ratio'] = df['remote_ratio'].apply(lambda row: np.nan if str(row) == 'nan' else str(row))
    return df

def clean_employment_type(df, list_):
    for i in list_:
        df['employment_type'] = df['employment_type'].apply(lambda row: i if i in str(row) else str(row))
    return df

def clean_employee(row):
    pattern1 = r"Más de (\d+\.?\d*) empleados"
    pattern2 = r"De (\d+\.?\d*) a (\d+\.?\d*) empleados"
    pattern3 = r"Entre (\d+\.?\d*) y (\d+\.?\d*) empleados"

    match1 = re.match(pattern1, str(row))
    match2 = re.match(pattern2, str(row))
    match3 = re.match(pattern3, str(row))
    if match1:
        return match1.group(1)
    elif match2:
        return match2.group(2)
    elif match3:
        return match3.group(2)
    else:
        return np.nan

def filter_employee(row):
    pattern1 = r"(Más de \d+\.?\d* empleados)"
    pattern2 = r"(De \d+\.?\d* a \d+\.?\d* empleados)"
    pattern3 = r"(Entre \d+\.?\d* y \d+\.?\d* empleados)"

    match1 = re.search(pattern1, str(row))
    match2 = re.search(pattern2, str(row))
    match3 = re.search(pattern3, str(row))

    if match1:
        return match1.group(1)
    elif match2:
        return match2.group(1)
    elif match3:
        return match3.group(1)
    else:
        return np.nan
    
def standarize_company_size(row):
    if pd.notnull(row):
        if int(row.replace('.', '')) < 50:
            return 'S'
        elif int(row.replace('.', '')) <= 250:
            return 'M'
        elif int(row.replace('.', '')) > 250:
            return 'L'
        else:
            return np.nan

def clean_salary(row, type=None):
    hour_pattern = r"(\d+) \$\/hr"
    year_pattern = r"(\d+\.?\d*) \$\/yr"
    hour_range_pattern = r"(\d+\,?\d*) \$\/h - (\d+\,?\d*) \$\/h"
    year_range_pattern = r"(\d+\.?\d*) \$\/año - (\d+\.?\d*) \$\/año"
    month_range_pattern = r"(\d+\.?\d*) \$\/mes - (\d+\.?\d*) \$\/mes"

    match_h = re.match(hour_pattern, str(row))
    match_y = re.match(year_pattern, str(row))
    match_rh = re.match(hour_range_pattern, str(row))
    match_ry = re.match(year_range_pattern, str(row))
    match_rm = re.match(month_range_pattern, str(row))
    if match_h:
        num_h = match_h.group(1)
        num_w = int(num_h) * 40
        return int(num_w * 48)
    elif match_y:
        sal = int(match_y.group(1).replace('.', ''))
        return sal
    elif match_rh:
        min_ = match_rh.group(1)
        max_ = match_rh.group(2)
        num_h = (float(min_.replace(',', '.')) + float(max_.replace(',', '.'))) / 2
        num_w = num_h * 40
        return int(num_w * 48)
    elif match_ry:
        min_ = match_ry.group(1)
        max_ = match_ry.group(2)
        if '.' not in max_:
            max_ += '000'
        if '.' not in min_:
            min_ += '000'
        num_y = (float(min_.replace('.', '')) + float(max_.replace('.', ''))) / 2
        return int(num_y)
    elif match_rm:
        min_ = match_rm.group(1)
        max_ = match_rm.group(2)
        num_m = (float(min_.replace('.', '')) + float(max_.replace('.', ''))) / 2
        return int(num_m * 12)
    else:
        return np.nan
    
def standarize_job(row):
    title = str(row).lower()
    if 'data engineer' in title:
        return 'Data Engineer'
    elif 'data analyst' in title:
        return 'Data Analyst'
    elif 'data scientist' in title:
        return 'Data Scientist'
    elif 'data' in title and 'junior' not in title:
        if 'engineer' in title:
            return 'Data Engineer'
        elif 'analyst' in title:
            return 'Data Analyst'
    elif ('machine' in title and 'learning' in title) or ('ml' in title and 'engineer' in title):
        return 'Machine Learning Engineer'
    elif 'deep' in title and 'learning' in title and 'engineer' in title:
        return 'Deep Learning Engineer'
    elif 'junior' in title:
        if 'data' in title and 'engineer' in title:
            return 'Data Engineer'
        elif 'data' in title and 'analyst' in title:
            return 'Data Analyst'
    elif 'business' in title:
        if 'intelligence' in title and 'analyst' in title:
            return 'BI Analyst'
        elif 'analyst' in title:
            return 'Business Analyst'
        else:
            return 'BI Engineer'
    elif 'artificial intelligence' in title or 'ai' in title:
        if 'research engineer' in title:
            return 'Research Engineer'
        elif 'ml' in title:
            return 'Machine Learning Engineer'
        elif 'engineer' in title:
            return 'AI Engineer'
        else:
            return title
    else:
        return str(row)


# MAIN FUNCTION
def linkedin_cleaning():
    linkedin = pd.read_csv('./data/linkedin.csv')

    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'NC', 'SC', 'CO', 'CT', 'ND', 'SD', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NJ', 'NY', 'NH', 'NM', 'OH', 'OK', 'OR', 'PA', 'RI', 'TN', 'TX', 'UT',
          'UT', 'VT', 'VA', 'WV', 'WA', 'WI', 'WY']
    
    left_states = {
        'Virginia': 'VA',
        'Minnesota': 'MN',
        'Washington': 'WA',
        'San Francisco': 'CA',
        'Nebraska': 'NE',
        'California': 'CA',
        'Texas': 'TX',
        'Nueva York': 'NY',
        'Michigan': 'MI',
        'Luisiana': 'LA',
        'Florida': 'FL',
        'Maryland': 'MD',
        'Nevada': 'NV',
        'Oregón': 'OR',
        'Oklahoma': 'OK',
        'Georgia': 'GA',
        'Carolina del Sur': 'SC',
        'Delaware': 'DE',
        'Ohio': 'OH',
        'Arkansas': 'AR',
        'Iowa': 'IA',
        'Carolina del Norte': 'NC',
        'Indiana': 'IN',
        'Nashville': 'TN',
        'Massachusetts': 'MA',
        'Tennessee': 'TN',
        'Enid': 'OK',
        'Chicago': 'IL',
        'América del Norte': 'USA',
        'Estados Unidos': 'USA',
        'Des Moines': 'IA',
        'Pittsburgh': 'PA',
        'Cincinnati': 'OH',
        'St. Louis': 'MO',
        'Illinois': 'IL',
        'Jacksonville': 'FL'
    }
    
    # Company state column
    linkedin = fclean_company_state(linkedin, states)
    linkedin = sclean_company_state(linkedin, left_states)
    linkedin = linkedin[~linkedin['company_state'].str.contains('Unión Europea', na=False)]

    # Remote ratio column
    remote_dict = [
        'Presencial',
        'Híbrido',
        'En remoto'
    ]
    linkedin = clean_remote_ratio(linkedin, remote_dict)
    linkedin.loc[linkedin['remote_ratio'] == 'nan', 'remote_ratio'] = np.nan

    # Employment type column
    remote_dict = [
        'Jornada completa',
        'Contrato por obra',
        'Media jornada',
        'Prácticas'
    ]
    linkedin = clean_employment_type(linkedin, remote_dict)

    # Company size column
    linkedin['company_size'] = linkedin['company_size'].apply(filter_employee)
    linkedin['employees'] = linkedin['company_size'].apply(clean_employee)
    linkedin['employees'] = linkedin['employees'].apply(standarize_company_size)

    # Salary column
    linkedin['salary'] = linkedin['salary_range'].apply(clean_salary)

    # Job title column
    linkedin['original_title'] = linkedin['job_title']
    linkedin['job_title'] = linkedin['job_title'].apply(standarize_job)
    categories = [
        'Data Engineer',
        'Data Analyst',
        'Data Scientist',
        'Machine Learning Engineer',
        'Deep Learning Engineer',
        'BI Analyst',
        'Business Analyst',
        'BI Engineer',
        'Research Engineer',
        'AI Engineer'
    ]
    linkedin = linkedin[linkedin['job_title'].isin(categories)]
    linkedin = linkedin.drop(columns=['employees', 'salary_range'])
    linkedin.to_csv('../data/linkedin_standarized.csv', index=False)

