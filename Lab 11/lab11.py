import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

""" Lab Questions:
1. Define a command to show only
'DC' comic movies fromthe sh DataFrame.
2. Define a command to show the Year,
Title and OpeningWeekendBoxOffice
columns from the sh DataFrame.
3. Define a command to show the Year
and Title of only 'Marvel' movies from
the sh DataFrame.
4. Define a command to plot a line() for
the AvgTicketPriceThatYear with Year on
the x axis. Make the line Black.     
"""

# START PROGRAM

sh_raw = pd.read_csv('/Users/cgrab/OneDrive/Desktop/movies.csv', header=None, names= 
            ['Year','Title','Comic','IMDB','RT',
             'CompositeRating','OpeningWeekendBoxOffice',
             'AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])a


# Normalizes the data and insert it into the DataFrame
def normal(sh):
    # Normalize the scores
    imdb_normalized = sh.IMDB / 10
    sh.insert(10,'IMDBNormalized',imdb_normalized)
    rt_normalized = sh.RT/100
    sh.insert(11, 'RTNormalized', rt_normalized)


def main():
    prompted = str(input("Enter a number \nList:\n1. DC\n2. Year Title Opening Weekend\n3. Marvel Year Title\n4. Plot AvgPrice vs Year\n5. Exit\n</>: "))
    
    
    
    if prompted == "1":
        # 1. Define a command to show only 'DC' comic movies from the sh DataFrame.
        sh = sh_raw[sh_raw.Comic == 'DC']
        
        normal(sh)
        
        print(sh.head(len(sh)))
    
    elif prompted == "2":
        # 2. Define a command to show the Year, Title and Opening Weekend Box Office columns from the sh DataFrame.
        sh = sh_raw[['Year','Title','OpeningWeekendBoxOffice']]
        print(sh.head(len(sh)))
            
    elif prompted == "3":
        # 3. Define a command to show the Year and Title of only 'Marvel' movies from the sh DataFrame.
        sh = sh_raw[sh_raw.Comic == 'Marvel']
        print(sh[['Year','Title']])
    
    elif prompted == "4":
        # 4. Define a command to plot a line() for the AvgTicketPriceThatYear with Year on the x axis. Make the line Black.

        sh = sh_raw[['Year','AvgTicketPriceThatYear']]

        
        # Create a composite score
        sh.plot.line(x ='Year',
        y ='AvgTicketPriceThatYear', color="black")
        plt.show()

        # make a graph of the composite score
        #print(sh[['Year','AvgTicketPriceThatYear']].corr())


        #print(sh[['Year','AvgTicketPriceThatYear']].describe())
    
    
    elif prompted == "5":
        # Quit the program
        print("Quitting...")
        quit()
               
    else:
        # Catch Invalid input
        print("Invalid Input")
    
    
    main() # loop back to front of main
        
main() # start the program

# END PROGRAM