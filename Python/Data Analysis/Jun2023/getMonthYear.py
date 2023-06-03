# Get month and year from file name 230117 Payment Summary - 2023-01-18T085845.454.xlsx
def getMonthYear(filename):
    """
    Extract the month and year from the file name
    Parameters:
        filename: file name
    Returns:
        new_file_name: new file name
    """

    import re
    import pandas as pd
    
    # Extract the month and year from the file name
    match = re.search(r'(\d{4})-(\d{2})', filename)
    year = match.group(1)
    month = match.group(2)

    # Create the new CSV file name
    new_file_name = f"data{month}{year}.csv"
    print(new_file_name)
    pass

# def main
if __name__ == '__main__':
    # dataHandle(sourcefolder, destfolder, cate_dir)
    pass