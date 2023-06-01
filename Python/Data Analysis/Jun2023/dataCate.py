def loadDataCate(directory , dataCateName):

    import pandas as pd
    import os
    import glob

    # check if excel files exist in folder
    if os.path.exists(os.path.join(directory, '*.xlsx')):
        print('Excel files exist in folder')
        excel_files = glob.glob(os.path.join(directory, '*.xlsx'))
    else:
        print('Excel files do not exist in folder')
        #excel_files = glob.glob(os.path.join(directory2, '*.xlsx'))
        pass
    try:
        # use cols 0, Barcode; 2, Category Name
        # use cols 0, Barcode; 3, SubCategory Name
        # use both Category Name and SubCategory Name
        df = pd.read_excel(directory + dataCateName, sheet_name='Sheet1', usecols=[0,2,3])
        pass
    except FileNotFoundError:
        print('File not found')
        pass
