# Import the necessary modules
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
#import seaborn as sns

cali = fetch_california_housing()
cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
cali_df['MedHouseValue'] = pd.Series(cali.target)
# open table file in write mode as txt
table = open("C:/Users/cgrab/OneDrive/Documents/{ } Documents/Class Files/Python Programming/Lab 13/caliHousing.txt", "w")

def mLineReg():
    
    X = pd.DataFrame(cali_df.loc[:, 'MedInc':"Longitude"]) # create x data
    y = pd.DataFrame(cali_df['MedHouseValue']) # create y data
    
    X_train, X_test, y_train, y_test = train_test_split(cali.data, cali.target, random_state=11) # split data into training and testing sets
    
     # create a object
    lReg = LinearRegression()
    # adapt the model using training data
    lReg.fit(X_train, y_train) 
    # attempt to predict the response
    y_pred = lReg.predict(X_test) 
    
    r2Score = metrics.r2_score(y_test, y_pred) # calculate r2 value
    mSqEr = metrics.mean_squared_error(y_test, y_pred) # calculate mse value
    
    # print out to console
    print("Multiple Linear Regression using All Features")
    print("R2 Score: ", r2Score)
    print("MSE Score: ", mSqEr)
    
    # write same print to table file
    table.write("Multiple Linear Regression using All Features \n")
    table.write("R2 Score: " + str(r2Score)  + "\nMSE Score: "+ str(mSqEr) + "\n")


def sLineReg(index): # create data for line regression and print / output to a file
    X = pd.DataFrame(cali_df[cali.feature_names[index]]) # create x data
    y = pd.DataFrame(cali_df['MedHouseValue']) # create y data
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11) # split data into training and testing sets

    # create a object
    lReg = LinearRegression()
    # adapt the model using training data
    lReg.fit(X = X_train,y = y_train) 
    # attempt to predict the response
    y_pred = lReg.predict(X_test) 
    
    r2Score = metrics.r2_score(y_test, y_pred) # calculate r2 value
    mSqEr = metrics.mean_squared_error(y_test, y_pred) # calculate mse value
    
    # print out and save values to table
    print("Feature " + str(index) + " has R2 score: " + str(r2Score))
    print("\n\tMSE Score: " + str(mSqEr) + "\n \n")
    
    table.write("Feature " + str(index) + " has R2 score: " + str(r2Score))
    table.write("\n\tMSE Score: " + str(mSqEr) + "\n")
    
    
mLineReg() # call multiple linear regression function

for n in range(len(cali.feature_names)): # loop through all features
    sLineReg(n) # call single linear regression function
    
    
