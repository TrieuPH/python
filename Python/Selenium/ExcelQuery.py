from sqlite3 import Date
import pandas as pd
import datetime
excel_location1 = r"C:\Users\Trieu Pham\Dropbox\PorfolioTracking.xlsx"
excel_location2 = r"C:\Users\trieu.pham\Dropbox\PorfolioTracking.xlsx"
def read_excel():
    try:
        df = pd.read_excel(excel_location1)
    except:
        df = pd.read_excel(excel_location2)
    #print(df)
    #print(df.query("Month == 11"))
    #df['Date'] = pd.to_datetime(df['Date'])
    
    max_por = df['Por'].max()
    #print(df.query("Por == %s" %max_por))

    min_por = df['Por'].min()   
    #print(df.query("Por == %s" %min_por))
    
    #print(datetime.date.today())
    to_day =  datetime.date.today()
    print(type(to_day))
    #print(df['Date'] == to_day)
    print(df.dtypes)

read_excel()