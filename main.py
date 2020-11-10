import pandas as pd 
from boon import *

# read in excel file
df = pd.read_excel('boon.xlsx')

# create a list of objects made from the excel file
table = []
for i in range(len(df)):
    table.append(Boon(df.loc[i, 'boon'], df.loc[i, 'god1'], df.loc[i, 'god2'], df.loc[i, 'god1Boons'], df.loc[i, 'god2Boons']))

# initializing variables for loop
ansList = []
counter = 0

# prompting user for input
print("Type a maximum of 8 gods.\nType 'exit' to quit.")

while(True):
    # getting input and interating counter
    ans = input("")
    counter += 1

    # stop condition for loop - if not stopping then append input to list
    if ans.lower() == 'exit':
        break
    else:
        ansList.append(ans)

    # skipping first input from user
    if counter == 1:
        continue

    # creating the output 
    text = ""
    for i in range(len(df)):
        data = table[i].containsGod(ansList, counter)
        if data != None:
            text += data

    print("===========================")
    print(text)