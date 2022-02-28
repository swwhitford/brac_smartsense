
#TODELETE
#  Create an excel file with condensed data on one sheet and a chart on the second

import datetime

import pandas as pd
import xlsxwriter

# pip install XlsxWriter
# pip install xlrd
# pip install pandas
# https://www.geeksforgeeks.org/reading-excel-file-using-python/
# https://xlsxwriter.readthedocs.io/working_with_pandas.html

inputFileName = 'smartsense/asset_156375_readings_1-2022.csv'


outputFileName = 'output2.xlsx'

# how often to copy the line to another file (how many lines to skip)
# TODO: Implement frequency
frequency = 100

df = pd.read_csv(inputFileName, sep=',', parse_dates=[
                 'Date & Time (UTC-5)'], index_col='Date & Time (UTC-5)')
df = df.sort_values(by="Date & Time (UTC-5)")

# get Month/year for chart title
datetime2 = pd.read_csv(inputFileName)['Date & Time (UTC-5)'][2]
dtObj = datetime.datetime.strptime(datetime2, '%m/%d/%Y %H:%M:%S')
month = dtObj.strftime("%B")
year = dtObj.strftime("%Y")

# get Freezer name for chart title
freezerName = pd.read_csv(inputFileName)['Sensor Name'][2]
freezerName = freezerName.split('on port')[0]

chartTitle = freezerName + "\n" + month + " " + year


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(outputFileName, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')


workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Adjust the width of the first column to make the date values clearer.
worksheet.set_column('A:A', 20)


# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
max_row = len(df) + 1

format2 = workbook.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})
worksheet.conditional_format('G2:G' + str(max_row), {'type':     'cell',
                                                     'criteria': 'equal to',
                                                     'value':    '"Y"',
                                                     'format':   format2})


for i in range(len(['ReadingDate'])):
    col = i + 1
    #     [sheetname, first_row, first_col, last_row, last_col]
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 1, 0, max_row, 0],
        'values':     ['Sheet1', 1, 2, max_row, 2],
    })

chart.set_title({'name': chartTitle})
chart.set_x_axis({'name': 'Date'})
chart.set_x_axis({
    'date_axis':  True,
    'num_format': 'mm/dd/yyyy',
    'major_unit':      1,
})
chart.set_y_axis({'name': 'Reading'})
chart.set_legend({'none': True})

chartsheet = workbook.add_chartsheet()
chartsheet.set_chart(chart)

chartsheet.set_first_sheet()  # First visible worksheet tab.
chartsheet.activate()         # First visible worksheet.

# Close the Pandas Excel writer and output the Excel file.
writer.save()
