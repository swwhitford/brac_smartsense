from TempScraper import eachAssetXL, eachAssetXL, my_StringtoDatetime, dlMonthChart, responseToFile
import convertToExcel

from digi_login import dlpoints

if __name__ == "__main__":
    
    assets = {
        #156368,
        #156370,
        #156375,
        156376,
        #156377,
        #156452,
        #156453,
        #156454,
        #445018
    }

    startDate = my_StringtoDatetime("05/1/2025")
    endDate = my_StringtoDatetime("09/30/2025 23:59:59")

    eachAssetXL(assets, startDate, endDate)

def singleMonthToCSV():
    """create a CSV file for a single month"""
    asset = "156368"
    month = 5
    year = 2021

    response = dlMonthChart(asset, month, year)
    responseToFile(response, asset+"-"+str(month)+"-"+str(year)+".csv")

def singleMonthToXLS():
    """convert a CSV file for a single month to XLSX"""
    asset = "156368"
    month = 5
    year = 2021

    response = dlMonthChart(asset, month, year)
    convertToExcel.createXLSX(response, asset+"-"+str(month)+"-"+str(year)+".csv")
    