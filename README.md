# SpySignals
Simple SMA (Simple-Moving-Average) trading signal program using python

# What the program calculates
- This program uses SMAs (Simple-Moving-Average) on a daily chart
- When the 10 Day SMA is above the 50 Day SMA and the derivative of the 10 Day SMA is greater than 0 it will open a LONG position until the derivative goes to 0
- When the 10 Day SMA is below the 50 Day SMA and the derivative of the 10 Day SMA is less than 0 it will open a SHORT position until the derivative goes to 0

# How to use
- main.py
  - This program retraces and pulls data from Yahoo Finance including (Open/Close Prices and SMA) and output it in a spreadsheet
  - In the spreadsheet there will be an unformated version of the signals aswell
- parse.py
  - This will go through the unformatted signals and format them in pairs of two, LONG LONG and SHORT SHORT
  - The first one is always the entry and the second one that follows it is the exit
- reader.py
  - This will calculate the profitability of using the spreadsheet as if you were trading with this strategy
  - It will also give you the percent comparision between the avg stock price and the profit
