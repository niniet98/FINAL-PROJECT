# Predictive Model of Salaries in Job Offers

## Description
In today's job search landscape, one critical piece of information often missing from job postings is the salary range. Addressing this gap, this project aims to provide predictive insights into salaries within the data field. Understanding the importance of salary information for job seekers, this initiative endeavors to offer a reliable estimation of salaries for various positions within the data domain.

The primary goal of this project is to use machine learning and data analytics techniques to predict salaries. By leveraging available data in linkedin related to job descriptions, qualifications, locations, and other pertinent factors, the project seeks to develop a predictive model that estimates salary ranges for different data-related job positions in the US.

## Workflow
![pipeline](https://github.com/niniet98/FINAL-PROJECT/blob/main/readme/workflow.png?raw=true)

### Scrapping
For the web scraping process, Selenium and Beautiful Soup libraries collaborated seamlessly. Selenium played the role of a user, navigating through diverse job offers, facilitating Beautiful Soup's access to the HTML content. This interaction allowed the extraction and saving of the HTML data into a text file.

### Reading HTML
From every text file stored in the preceding stage, the essential job offer information was extracted into lists. These lists were then utilized to construct a dataframe where each set of data represented a distinct row.

### Clean & Transform
After the data collection phase, it was imperative to cleanse the information, aiming to standardize categories such as job positions, modalities, experience levels, employment types, and more. This cleaning process was crucial to ensure consistency and reliability across the dataset.

### Visualization & Queries
After the dataset underwent cleaning, it was prepared for import into MySQL for query-based analysis, enabling the extraction of valuable insights. Additionally, Tableau was utilized for visualizations, incorporating SQL-derived queries to generate informative plots and charts, enhancing the understanding of the data.

### Feature Engineering
At this stage, an additional transformation was required for the dataset. Following standardization, the categorical variables were converted into numeric equivalents to facilitate the analysis of correlations between different features. This process aimed to identify the most correlated features with the target variable. Subsequently, a model was fitted using this modified data to predict salaries.

### Streamlit
We developed a small web demonstration to illustrate the user flow within LinkedIn, demonstrating the step-by-step process of how a user filters job searches to find a specific position. The demonstration showcases how the system predicts potential salaries in instances where salary information is not available, offering a comprehensive view of the user experience on the platform.

## Data Source
The dataset used for this project was curated exclusively from LinkedIn, a professional networking platform widely used for job postings and career-related information.

## Next Steps
- **Expand Data**: Broaden data not only in data field but in other tech fields and countries.
- **Optimize Salary Prediction Models**: Experiment with new models to pinpoint the most accurate for salary predictions.
- **Refine Streamlit App**: Improve the Streamlit app for better usability and functionality.


## Links
[Canva Support](https://www.canva.com/design/DAF2A4HqE8Y/VBn4UNJj9l0F8H_xmCQH8Q/edit?utm_content=DAF2A4HqE8Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)