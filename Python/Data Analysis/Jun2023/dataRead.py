# def excel2csv
def DataCate(CateFileDir):
    """
    Read DataCate.xlsx file
    CateFileDir: the directory of DataCate.xlsx file
    Return: df_cate
    """
    import pandas as pd
    df_cate = pd.read_excel(CateFileDir,sheet_name='Sheet1', usecols=[0,2,3], skiprows=0)
    return df_cate
pass

def DataPayment(df_cate , DataPaymentDir, output_file_name ,output_file_dir):
    """
    Read DataPayment folder and merge all excel files into one dataframe
    df_cate: dataframe
    DataPaymentDir: the directory of DataPayment folder
    Return: df
    """
    import pandas as pd
    import glob
    # Get the list of excel files in the source folder
    excel_files = glob.glob(DataPaymentDir + "/*.xlsx")
    # Create an empty dataframe
    
    # Loop through the list of excel files
    for file in excel_files:
        # print access file name
        print("Reading file: ", file)
        
        # Read the excel file
        temp_df  = pd.read_excel(file, 'Sheet2', usecols=[0,2,4,6,7], skiprows=2)
        
        temp_df = temp_df.merge(df_cate, on='Barcode')

        # To csv file
        ToCsv(temp_df, output_file_name, output_file_dir)
    
pass

def merge(df, df_cate):
    """
    Merge df and df_cate
    df: dataframe
    df_cate: dataframe
    Return: df
    """
    import pandas as pd
    df = pd.merge(df, df_cate, on='Barcode')
    return df
pass

def ToCsv(df, filename, dir):
    """
    Write dataframe to csv file
    df: dataframe
    filename: the name of csv file
    dir: the directory of csv file
    """
    import pandas as pd 
    import os
    # Read the first line of the file
    output_file = os.path.join( dir , filename + '.csv')

    with open(output_file, 'r') as f:
        first_line = f.readline().strip()
    # Check if the first line contains the expected column names
    has_headers = 'InvoiceID' in first_line
    df.to_csv(output_file ,mode ='a', header = not has_headers, index=False)

if __name__ == 'main':
    output_file_name = 'DataPayment'
    output_file_dir = r'C:\Users\Trieu Pham\OneDrive - BTM Global Consulting\Projects\data csv\outputFile'
    input_file_dir = r'C:\Users\Trieu Pham\OneDrive - BTM Global Consulting\Projects\data'
    cateFileDir = r'C:\Users\Trieu Pham\OneDrive - BTM Global Consulting\Projects\github\python\python\Data Analysis\DataCate.xlsx'
    DataPayment(DataCate(cateFileDir), input_file_dir , output_file_name, output_file_dir)
    pass