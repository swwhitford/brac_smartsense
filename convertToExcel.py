import datetime

import pandas as pd
import xlsxwriter
from matplotlib import lines

from digi_login import dlpoints


def createXLSX(response, outputFileName: str):

    # outputFileName = "output.xlsx"

    lines = {}
    for l in response.text.splitlines():
        sName2 = l.split(",")[0]
        if (sName2!="Sensor Name"):
            if sName2 not in lines:
                lines[sName2] = []
            lines[sName2].append(l.split(","))

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(outputFileName, engine="xlsxwriter")
    
    for eachLines in lines:
        df = pd.DataFrame(
            lines[eachLines],
            columns=["Sensor Name", "Date & Time (UTC-5)", "Reading", "Reading Type"],
        )

        df.drop(index=0, inplace=True)
        df.rename(columns={"Date & Time (UTC-5)": "Date"}, inplace=True)

        df = df.sort_values(by="Date")

        chartTitle = getChartTitle(df)

        # Set Column types
        df["Date"] = pd.to_datetime(df["Date"])
        df["Reading"] = pd.to_numeric(df["Reading"])

        sName = df["Sensor Name"].iloc[0]
        #or df._get_value(1, "Sensor Name")

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name=sName)

        workbook = writer.book
        worksheet = writer.sheets[sName]

        # Adjust the width of the first column to make the date values clearer.
        worksheet.set_column("A:A", 20)

        # Create a chart object.
        chart = workbook.add_chart({"type": "line"})
        # chart = workbook.add_chart({"type": "scatter"})

        # Configure the series of the chart from the dataframe data.
        max_row = len(df) + 1

        chart.add_series(
            {
                "name": [sName, 0, 5],
                "categories": [sName, 1, 2, max_row, 2],
                "values": [sName, 1, 3, max_row, 3],
            }
        )

        chart.set_title({"name": chartTitle})
        chart.set_x_axis({"name": "Date"})
        chart.set_x_axis(
            {"date_axis": True, "num_format": "mm/dd/yyyy", "major_unit": 1,}
        )

        chart.set_y_axis({"name": "Temperature"})
        chart.set_legend({"none": True})

        chartsheet = workbook.add_chartsheet()
        chartsheet.set_chart(chart)

        chartsheet.set_first_sheet()  # First visible worksheet tab.
        chartsheet.activate()  # First visible worksheet.

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def getChartTitle(df) -> list:
    # get Month/year for chart title
    datetime2 = df._get_value(1, "Date")
    dtObj = datetime.datetime.strptime(datetime2, "%m/%d/%Y %H:%M:%S")
    month = dtObj.strftime("%B")
    year = dtObj.strftime("%Y")

    # get Freezer name for chart title
    freezerName = df._get_value(1, "Sensor Name")
    chartTitle = freezerName + "\n" + month + " " + year
    return chartTitle


if __name__ == "__main__":
    # startTS = "1644382800000"
    startTS = "1641013200000"
    # endTS   = "1644469199999"
    endTS = "1643691599999"
    asset = "156354"
    outputFile = "OutputXLSX.xlsx"
    response = dlpoints(asset, startTS, endTS)
    createXLSX(response, outputFile)
