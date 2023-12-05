from src import scrapping, assemble, cleaning, feature_engineering as fe

if __name__ == '__main__':
    scrapping.scrapping()
    assemble.assemble_dataset()
    cleaning.linkedin_cleaning()