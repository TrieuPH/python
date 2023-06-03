import pandas as pd
import os
import glob

def loadDataExcel(directory , dataCateName, sheet_name, usecols, skiprows):
    """
    Load data from excel file
    Parameters:
        directory: directory of excel file
        dataCateName: excel DataCate file name, not include extension
    Returns:
        df: dataframe
    """

    # check if excel files exist in folder
    file_path = os.path.join(directory , dataCateName)
    print(f"file_path: ", file_path)
    if os.path.exists(file_path):
        print('Excel files exist in folder')
        excel_files = glob.glob(file_path)
    else:
        print(f'Excel files do not exist in folder {file_path}')
        #excel_files = glob.glob(os.path.join(directory2, '*.xlsx'))
        pass
    try:
        # use cols 0, Barcode; 2, Category Name
        # use cols 0, Barcode; 3, SubCategory Name
        # use both Category Name and SubCategory Name
        df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=usecols, skiprows=skiprows)
        return df
        pass
    except FileNotFoundError:
        print('File not found')
        pass

if __name__ == '__main__':
    # dataHandle(sourcefolder, destfolder, cate_dir)
    datacate_dict = r'C:\Users\trieu.pham\OneDrive - BTM Global Consulting\Projects\github\python\Python\Data Analysis'
    datacate_filename = r'DataCate'
    df_cate = loadDataExcel(datacate_dict, datacate_filename)
    print(df_cate)
    # print("TESTING")
    # print(os.path.join(datacate_dict , datacate_filename + '.xlsx'))

    pass