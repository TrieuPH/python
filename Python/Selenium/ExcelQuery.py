import pandas as pd

excel_location = r"C:\Users\Trieu Pham\Dropbox\PorfolioTracking.xlsx"

def read_excel():
    df = pd.read_excel(excel_location)
    #print(df)
    #print(df.query("Month == 11"))
    #df['Date'] = pd.to_datetime(df['Date'])
    
    max_por = df['Por'].max()
    print(df.query("Por == %s" %max_por))

    min_por = df['Por'].min()
    print(df.query("Por == %s" %min_por))

    

read_excel()