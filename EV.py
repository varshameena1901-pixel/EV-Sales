import pandas as pd
df =pd.read_csv("EV_Database.csv", low_memory=False)

#Basic check
df.head()
df.info()
df.isnull().sum()

df.columns = df.columns.str.strip()
# Fix data types

df['Date'] = pd.to_datetime(df['Date'],errors='coerce')
df['Year'] = df['Date'].dt.year
#fix hidden spaces in column names


#Handle missing value# ##
df['EV_Sales_Quantity']=df['EV_Sales_Quantity'].fillna(0)
# remove junk columns
df = df.loc[:,~df.columns.str.contains('^Unnamed')]
df.drop_duplicates(inplace=True)
#save clean data
df.to_csv('EV_Sales_clean.csv', index=False)
print(df.info())


