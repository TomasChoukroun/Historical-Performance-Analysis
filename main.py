import numpy as np
import pandas as pd
import math
import statistics
import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Excel Import
df = http://pd.read_excel('Enter Sheet Name here', sheet_name='PYTHON')
Prices = df['Price'].tolist()
Dates = df['Date'].tolist()

# Collumn Arrays and Modelling
arr3 = np.array(Prices)
arr4 = np.array(Dates)
Nb_dates = len(Prices)

# Performance
First_Price = arr3[0]
Performance = arr3/First_Price
arr6 = np.array(Performance)
arr7 = np.array(Performance[0:Nb_dates-1])
arr8 = np.array(Performance[1:Nb_dates])

# Annualized Return
x = arr4[-1] - arr4[0]
x = x.days
Annualized_Return = ((arr6[-1]/arr6[0])**(365/x)-1)*100

# Annualized Volatility
Annualized_Volatility = math.sqrt(252)*statistics.stdev(np.log(arr8/arr7))*100

# Sharpe Ratio
Sharpe_Ratio = Annualized_Return/Annualized_Volatility

# Max Drawdown
Max_Drawdown = 0
for i in range(1, Nb_dates):
    Max_Drawdown = min(Max_Drawdown, arr6[i]/max(arr6[0:i])-1)

# Correlation & Beta (if other data set is provided)
a = input("Comparing Multiple Data Sets? (Yes/No): ")
if a == "Yes":
    df2 = http://pd.read_excel(r'C:\Users\tchoukroun\Documents\Backtest and Metrics - Call Ossiam SPX.xlsx', sheet_name='PYTHON 2')
    Dates2 = df2['Date'].tolist()
    Prices2 = df2['Price'].tolist()
    Nb_dates2 = len(Prices2)
    arr1Second = np.array(Prices2)
    First_Price2 = arr1Second[0]
    Performance2 = arr1Second / First_Price2
    arr9 = np.array(Performance2)
    arr10 = np.array(Performance2[0:Nb_dates2-1])
    arr11 = np.array(Performance2[1:Nb_dates2])
    LnFirst = np.log(arr8 / arr7)
    LnSecond = np.log(arr11 / arr10)
    r = (np.corrcoef(LnFirst, LnSecond))*100
    Variance = statistics.variance(LnSecond)
    Covariance = (np.cov(LnFirst, LnSecond / Variance))*100
    print("\n")
    print("HISTORICAL PERFORMANCE ANALYSIS")
    print("Annualized Return: ", Annualized_Return, "%")
    print("Annualized Volatility: ", Annualized_Volatility, "%")
    print("Sharpe Ratio: ", Sharpe_Ratio)
    print("Max Drawdown: ", Max_Drawdown, "%")
    print("Correlation: ", r[0, 1], "%")
    print("Beta: ", Covariance[0, 1], "%")
    print("\n")

else:
    print("\n")
    print("HISTORICAL PERFORMANCE ANALYSIS")
    print("Annualized Return: ", Annualized_Return, "%")
    print("Annualized Volatility: ", Annualized_Volatility, "%")
    print("Sharpe Ratio: ", Sharpe_Ratio)
    print("Max Drawdown: ", Max_Drawdown, "%")
    print("\n")

# Using Dates as an Input
k = input("Data for a specific time range? (Yes/No): ")
print("\n")

if k == "Yes":
    print("*Excluding Weekends & Public Holidays* (2002-09-03 to 2022-06-17)")
    # Year Inputs
    year1 = int(input("Initial Year: "))
    month1 = int(input("Initial Month: "))
    day1 = int(input("Initial Day: "))
    year2 = int(input("End Year: "))
    month2 = int(input("End Month: "))
    day2 = int(input("End Day: "))
    # Solving for t
    d0 = http://datetime.date(year1, month1, day1)
    d1 = http://datetime.date(year2, month2, day2)
    Date_Difference = d1 - d0
    t = Date_Difference.days
    RI = np.where(arr4 == d0)
    RE = np.where(arr4 == d1)
    # Index inputs
    g = RI[0][0]
    j = RE[0][0] + 1
    RI2 = RI[0][0] + 1
    RE2 = RE[0][0]
    print("\n")
    # Return (Given dates)
    Return = (((arr6[RE2] / arr6[g]) ** (365 / t)) - 1) * 100
    # Volatility (Given dates)
    Volatility = math.sqrt(252) * statistics.stdev(np.log(arr6[RI2:j] / arr6[g:RE2])) * 100
    # Sharpe Ratio (Given Dates)
    Sharpe_Ratio2 = Return / Volatility
    print("TIME SERIES PERFORMANCE ANALYSIS")
    print("Return: ", Return, "%")
    print("Volatility: ", Volatility, "%")
    print("Sharpe Ratio: ", Sharpe_Ratio2)
else:
    print("Complete")
