# Predictive Model of Salaries in Job Offers

## Description

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

## Model

## Organization

## Next Steps

## Links
[Canva Support](https://www.canva.com/design/DAF2A4HqE8Y/VBn4UNJj9l0F8H_xmCQH8Q/edit?utm_content=DAF2A4HqE8Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)