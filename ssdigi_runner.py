from TempScraper import eachAssetXL, eachAssetXL, my_StringtoDatetime, dlMonthChart, responseToFile
import convertToExcel
import freezer_name_lookup_table

from digi_login import dlpoints

if __name__ == "__main__":
    
    assets = freezer_name_lookup_table.getFreezerIDs()

    startDate = my_StringtoDatetime("03/1/2026")
    endDate = my_StringtoDatetime("03/31/2026 23:59:59")

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
    convertToExcel.createXLSX(response, asset+"-"+str(month)+"-"+str(year)+".csv", asset)
    