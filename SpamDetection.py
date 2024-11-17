import pandas as pd


#data frame
data = pd.read_csv('/home/alexander/machine/spam/spam.csv')
# Remove duplicates
data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['han','spam'],['Not Spam','Spam'])

