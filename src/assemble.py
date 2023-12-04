import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

remote_ratio = ['Presencial', 'Híbrido', 'En remoto']
employment_type = ['Jornada Completa', 'Media jornada', 'Prácticas']
experience_level = ['Sin experiencia', 'Intermedio', 'Algo de responsabilidad', 'Prácticas', 'Director', 'Ejecutivo']

def open_file(path):
    ''' This function extracts the information of interest to build a list of info about a job offer.
        Returns a list.
    '''
    with open(path, 'r') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        try:
            container = soup.find_all('div', {'class': 'jobs-unified-top-card'})[0]
            title = container.find_all('h1', {'class': 'job-details-jobs-unified-top-card__job-title'})[0].getText().strip()
            company_name = container.find_all('a', {'class': 'app-aware-link'})[1].getText().strip()
            state = container.find(string = lambda text: text and '· ' in text)
            line = container.find_all('li', {'class': 'job-details-jobs-unified-top-card__job-insight'})[0].getText().strip()
            line = line.split('\n')
            line = [i for i in line if i != '']
            line = [i for i in line if i != ' ']
            if len(line) == 4:
                salary_range = line[0]
                remote = line[1]
                employment = line[2]
                experience = line[3]
                company_size = container.find_all('li', {'class': 'job-details-jobs-unified-top-card__job-insight'})[1].find('span').getText().strip()
            elif len(line) == 3:
                if line[0] in remote_ratio and line[1] in employment_type and line[2] in experience_level:
                    salary_range = np.nan
                    remote = line[0]
                    employment = line[1]
                    experience = line[2]
                if '$' in line[0] and line[1] in employment_type and line[2] in experience_level:
                    salary_range = line[0]
                    remote = np.nan
                    employment = line[1]
                    experience = line[2]
                if '$' in line[0] and line[1] in remote_ratio and line[2] in employment_type:
                    salary_range = line[0]
                    remote = line[1]
                    employment = line[2]
                    experience = np.nan
                company_size = container.find_all('li', {'class': 'job-details-jobs-unified-top-card__job-insight'})[1].find('span').getText().strip()
            elif len(line) == 2:
                if '$' in line[0] and line[1] in employment_type:
                    salary_range = line[0]
                    remote = np.nan
                    employment = line[1]
                    experience = np.nan
                if line[0] in remote_ratio and line[1] in employment_type:
                    salary_range = np.nan
                    remote = line[0]
                    employment = line[1]
                    experience = np.nan
                if line[0] in employment_type and line[1] in experience_level:
                    salary_range = np.nan
                    remote = np.nan
                    employment = line[0]
                    experience = line[1]
                company_size = container.find_all('li', {'class': 'job-details-jobs-unified-top-card__job-insight'})[1].find('span').getText().strip()
        except:
            print("file not valid")
    return [title, company_name, state, salary_range, remote,employment, experience, company_size]


def assemble_dataset():
    '''This function reads each file in the "data/jobs_html/" directory and passes it to another function in order to receive a list of .'''
    directory_path = './data/jobs_html/'
    files = os.listdir(directory_path)

    rows = []
    for file_name in files:
        row = []
        job_id = file_name.replace('.txt', '')
        row.append(job_id)
        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            row.extend[open_file(file_path)]
            rows.append(row)

    columns = ['job_id', 'job_title', 'company_name', 'company_state', 'salary_range', 'remote_ratio', 'employment_type', 'experience_level', 'company_size']
    linkedin = pd.DataFrame(rows, columns=columns)
    linkedin.to_csv('./data/linkedin.csv', index=False)
