import pandas as pd
import numpy as np
import re

def linkedin_cleaning():
    linkedin = pd.read_csv('../data/linkedin.csv')

    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'NC', 'SC', 'CO', 'CT', 'ND', 'SD', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NJ', 'NY', 'NH', 'NM', 'OH', 'OK', 'OR', 'PA', 'RI', 'TN', 'TX', 'UT',
          'UT', 'VT', 'VA', 'WV', 'WA', 'WI', 'WY']
