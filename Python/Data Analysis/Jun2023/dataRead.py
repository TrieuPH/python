# def excel2csv
def DataCate(CateFileDir):
    """
    Read DataCate.xlsx file and return a dataframe
    Parameters
    ----------
    CateFileDir : str
        The directory of DataCate.xlsx file
        Ex: C:\Users\User\DataCate.xlsx
    ----------
    Returns
    df_cate : dataframe
    """
    import pandas as pd
    # check current os
    import os
    if os.name == 'posix':
        # print('posix')
        datacate_dict = r'/Users/trieupham/OneDrive - BTM Global Consulting/Projects/github/python/Python/Data Analysis'
    else:
        # datacate_dict = r'C:\Users\trieu.pham\OneDrive - BTM Global Consulting\Projects\github\python\Python\Data Analysis'
        datacate_dict = r'C:\Users\Trieu Pham\OneDrive - BTM Global Consulting\Projects\github\python\python\Data Analysis'
        
    datacate_filename = r'DataCate.xlsx'
    df_cate = pd.read_excel(CateFileDir,sheet_name='Sheet1', usecols=[0,2,3], skiprows=0)
    return df_cate

def DataPayment(DataPaymentDir):
    """
    Read DataPayment.xlsx file and return a dataframe that contains all the data
    ----------
    Parameters
    DataPaymentDir : str
        The directory of DataPayment.xlsx file
        Ex: C:\Users\User\DataPayment
    ----------
    Returns
    df : dataframe
    """
    import pandas as pd
    import glob
    # Get the list of excel files in the source folder
    excel_files = glob.glob(DataPaymentDir + "/*.xlsx")
    # Loop through the list of excel files
    for file in excel_files:
        # Read the excel file
        df_payment = pd.read_excel(file, 'Sheet2', usecols=[0,2,4,6,7],skiprows=2)
        df = df.append(df_payment)
    return df

def ToCsv(df, filename, dir):
    import pandas as pd # Read the first line of the file
    output_file = dir + '/' + filename + '.csv'
    with open(output_file, 'r') as f:
        first_line = f.readline().strip()
    # Check if the first line contains the expected column names
    has_headers = 'InvoiceID' in first_line
    df.to_csv(output_file ,mode ='a', header = not has_headers, index=False)