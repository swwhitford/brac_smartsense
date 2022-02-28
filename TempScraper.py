# Python code to convert SmartSense timestamp to actual date

import calendar
import datetime
#from datetime import timezone
from urllib import response

import convertToExcel

# from smartsense.digi_login import *
from digi_login import *


def my_StringtoDatetime(str: str) -> datetime:
    # convert date string to date object

    # if str contains a space, assume it includes a time
    if " " in str:
        return datetime.datetime.strptime(str, "%m/%d/%Y %H:%M:%S")
    else:
        return datetime.datetime.strptime(str, "%m/%d/%Y")


def main():
    assetList = (156376, 156377)

    endStr = "12/31/2000 23:59:59"
    startDate = my_StringtoDatetime(startStr)
    endDate = my_StringtoDatetime(endStr)
    eachAssetCSV(assetList, startDate, endDate)


def dlMonthChart(asset: str, month: int, year: int) -> response:
    # Take a month and year, and download a chart for it

    # get last day of month
    lastDay = calendar.monthrange(year, month)[1]

    # create date string
    fullfirst = f'{month}{"/1/"}{year}{" 00:00:00"}'
    fulllast = f'{month}{"/"}{lastDay}{"/"}{year}{" 23:59:59"}'

    # convert to timestamp
    startTS = dateToTimestamp(my_StringtoDatetime(fullfirst))
    endTS = dateToTimestamp(my_StringtoDatetime(fulllast))

    rsp = dlpoints(asset, startTS, endTS)
    return rsp
    # https://app.smartsense.co/api/Asset/156376/ChartData/Download?start=1638334800000&end=1639285199999&includeDeletedSensorPoints=false


def eachAssetXL(assetList: list, start: datetime, end: datetime):
    for monthYr in getMonthYearRange(start, end):
        for asset in assetList:
            strAsset = str(asset) 
            strMonthYr = str(monthYr[0]) + "-" + str(monthYr[1])
            
            resp = dlMonthChart(asset, monthYr[0], monthYr[1])
            #If resp is empty (only one row for title), then skip
            if (resp.text.count('\n') != 1):
                print("Generating file for Asset: " + strAsset + ", " + strMonthYr)
                filename = (
                    "Temp_"
                    + str(asset)
                    + "_"
                    + str(monthYr[0])
                    + "-"
                    + str(monthYr[1])
                    + ".xlsx"
                )
                #print (filename)
                convertToExcel.createXLSX(resp, filename)
            else:
                print("No Data for Asset: " + strAsset + ", " + strMonthYr + ".  SmartSense only stores data for 2 years.")


def eachAssetCSV(assetList: list, start: datetime, end: datetime):
    for monthYr in getMonthYearRange(start, end):
        for asset in assetList:
            resp = dlMonthChart(asset, monthYr[0], monthYr[1])
            filename = (
                "out/Temp_Log_"
                + str(asset)
                + str(monthYr[0])
                + "-"
                + str(monthYr[1])
                + ".csv"
            )
            responseToFile(resp, filename)


def dateToTimestamp(d: datetime) -> int:
    # convert date obj to timestamp
    # 1638334800000 = 12/1/21 at 5 am)

    my_timestamp = int(d.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)
    return my_timestamp


def getMonthYearRange(startDate: datetime, endDate: datetime) -> tuple:
    # input: datetime objs
    # Get month and return all month/year tuples in range (month,year)
    """
    eg: 04/01/2021 & 07/01/2021 = (04,2021), (05,2021), (06,2021), (07,2021)

    x = my_StringtoDatetime(startDate)
    ed = my_StringtoDatetime(endDate)
    """

    monthYear = []

    while startDate < endDate:
        # Add x's month and year to tuple, increment x by 1 month
        monthYear.append((startDate.month, startDate.year))
        startDate = startDate + datetime.timedelta(days=31)
    return monthYear


""" Convert timestamp to datetime
from datetime import datetime
dt = datetime.fromtimestamp(1638334800000 // 1000)
print(dt) """


if __name__ == "__main__":
    assetList = ("156376", "156377")
    startStr = "1/1/2000 00:00:00"
    endStr = "2/28/2000 23:59:59"
    eachAssetXL(assetList, startStr, endStr)
