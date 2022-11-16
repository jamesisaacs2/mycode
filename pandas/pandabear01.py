#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create dataframes, and output graphs"""

import pandas as pd

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    # create a DataFrame (DF) object. EASY!
    # because we did not specify a sheet
    # only the first sheet was read into the DF
    movies = pd.read_excel(excel_file)

    # show the first five rows of our DF
    # DF has 5 rows and 25 columns (indexed by integer)
    print(movies.head())

    # Choose the first column "Title" as
    # index (index=0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    # DF has 5 rows and 24 columns (indexed by title)
    # print the top 10 movies in the dataframe
    print(movies_sheet1.head())

    # export 5 movies from the top dataframe to excel
    movies_sheet1.head(5).to_excel("5movies.xlsx")

    # export 5 movies from the top of the dataframe to json
    movies_sheet1.head(5).to_json("5movies.json")

    # export 5 movies from the top of the dataframe to csv
    movies_sheet1.head(5).to_csv("5movies.csv")


if __name__ == "__main__":
    main()


