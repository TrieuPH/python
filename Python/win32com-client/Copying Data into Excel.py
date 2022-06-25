import win32com.client as win32
import pandas as pd
from pathlib import Path

# Read in the remote data file
df = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sample-sales-tax.csv?raw=True")

# Define the full path for the data file file
data_file = Path.cwd() / "sales_summary.xlsx"

# Define the full path for the final output file
save_file = Path.cwd() / "sales_dashboard.xlsx"

# Define the template file
template_file = Path.cwd() / "sample_dashboard_template.xlsx"

# Do some summary calcs
# In the real world, this would likely be much more involved
df_summary = df.groupby('category')['quantity', 'ext price', 'Tax amount'].sum()

# Save the file as Excel
df_summary.to_excel(data_file, sheet_name="Data")

# Use com to copy the files around
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False

# Template file
wb_template = excel.Workbooks.Open(template_file)

# Open up the data file
wb_data = excel.Workbooks.Open(data_file)

# Copy from the data file (select all data in A:D columns)
wb_data.Worksheets("Data").Range("A:D").Select()

# Paste into the template file
excel.Selection.Copy(Destination=wb_template.Worksheets("Data").Range("A1"))

# Must convert the path file object to a string for the save to work
wb_template.SaveAs(str(save_file))