#!/usr/bin/python3

import pandas as pd

import matplotlib.pyplot as plt

def main():
    # define the name of our xls file
    excel_file = "datasets/movies.xls"

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
    #DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet1.head())
    # grab the next 2 sheets as well
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    #DFN has 5 rows and 24 colums (indexed by the title)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet3.head())

    #combine all DF's into a single DF called  movies
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    #number' of rows and column (5042, 24)
    print(movies.shape)

    #short Dataframe based on Gross Earnings
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    # Data is sorted by values in a colum
    # display the top 10 movies by Gross Earnings
    # passing the 10 values to head returns the top nt the default 5
    print(sorted_by_gross.head(10))

    #create a stacked bar graphs
    sorted_by_gross['Gross Earnings'] .head(10) .plot(kind="barh")
    # save the figure as stackedbar.png
    plt.savefig("stakedbar.png")

if __name__ == "__main__":
    main()

