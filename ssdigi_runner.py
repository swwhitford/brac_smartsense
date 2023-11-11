from TempScraper import eachAssetXL, eachAssetXL, my_StringtoDatetime, dlMonthChart, responseToFile
import convertToExcel

from digi_login import dlpoints

if __name__ == "__main__":
    assets = {
        156368,
        156370,
        156375,
        156376,
        156377,
        #156378,
        156452,
        156453,
        156454,
        160840,
    }

    startDate = my_StringtoDatetime("10/1/2023")
    endDate = my_StringtoDatetime("10/31/2023 23:59:59")

    eachAssetXL(assets, startDate, endDate)


def singleMonthToCSV():
    asset = "156368"
    month = 5
    year = 2021

    response = dlMonthChart(asset, month, year)
    responseToFile(response, asset+"-"+str(month)+"-"+str(year)+".csv")

def singleMonthToXLS():
    asset = "156368"
    month = 5
    year = 2021

    response = dlMonthChart(asset, month, year)
    convertToExcel.createXLSX(response, asset+"-"+str(month)+"-"+str(year)+".csv")
    