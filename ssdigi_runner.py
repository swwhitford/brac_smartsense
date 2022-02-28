from convertToExcel import createXLSX
from TempScraper import eachAssetXL, eachAssetXL, my_StringtoDatetime

import pandas as pd
import xlsxwriter
from matplotlib import lines

from digi_login import dlpoints

if __name__ == "__main__":
    # Do something here
    #print("Hello World")
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

    startDate = my_StringtoDatetime("1/1/2022")
    endDate = my_StringtoDatetime("2/1/2022 23:59:59")

    eachAssetXL(assets, startDate, endDate)


def csvtoexcel():
    print("hello World")


def listtoexcel():
    print("list to Excel")


def filesInDirToList():
    print("files in dir")
