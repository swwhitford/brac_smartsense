import datetime
import unittest

from digi_login import checkHTMLResponse, dlpoints
from TempScraper import (
    dateToTimestamp,
    dlMonthChart,
    eachAssetXL,
    eachAssetCSV,
    getMonthYearRange,
    my_StringtoDatetime,
)

asset = "156354"

class smartSenseTests(unittest.TestCase):
    print("Running Test")
    def test_checkHTMLResponse(self):
        from requests import Session

        with Session() as s:
            response = s.post("http://google.com")
        expected = "Code: 405 Method Not Allowed"
        actual = checkHTMLResponse(response)
        self.assertEqual(actual, expected)


    def test_dlpoints(self):
        startTS = "1644382800000"
        endTS = "1644469199999"

        actualResponse = dlpoints(asset, startTS, endTS)
        bytesResponse = len(actualResponse.text.encode("utf-8"))
        actual = str(bytesResponse)

        expected = "5895"
        self.assertEqual(actual, expected)

    # def responseToFile(self):
    #    #unable to test

    def test_myStringtoDatetime(self):
        str = "10/22/2021 00:00:00"
        actual = my_StringtoDatetime(str)
        expected = datetime.datetime(2021, 10, 22, 0, 0, 0)
        self.assertEqual(actual, expected)

    #     def test_dlMonthChalrt(self):
    #         #unable to test (doesn't return anything)
    #         month = 2
    #         year = 2021
    #         dlMonthChart(asset, month, year)
    #         self.assertEqual(1, 2)

    #     def test_eachAsset(self):
    #         #unable to test (doesn't return anything)
    #         assetList  = (156376, 156377)
    #         start = datetime.datetime(2021,1,5,5,6,7)
    #         end = datetime.datetime(2021,12,5,5,6,7)

    #         eachAsset(assetList, start, end)
    #         self.assertEqual(1, 2)

    def test_dateToTimestamp(self):

        date = datetime.datetime(2021, 12, 1, 17)
        actual = dateToTimestamp(date)
        expected = 1638378000000
        self.assertEqual(actual, expected)

    def test_getMonthDateRange(self):
        import datetime

        startStr = "1/1/2000 00:00:00"
        endStr = "12/31/2000 23:59:59"
        startDT = datetime.datetime.strptime(startStr, "%m/%d/%Y %H:%M:%S")
        endDT = datetime.datetime.strptime(endStr, "%m/%d/%Y %H:%M:%S")
        actual = getMonthYearRange(startDT, endDT)
        expected = [
            (1, 2000),
            (2, 2000),
            (3, 2000),
            (4, 2000),
            (5, 2000),
            (6, 2000),
            (7, 2000),
            (8, 2000),
            (9, 2000),
            (10, 2000),
            (11, 2000),
            (12, 2000),
        ]
        self.assertEqual(expected, actual)
        # print (t.getMonthYearRange(startDT, endDT))

    def test_FirstDate(self):
        import datetime;
        import time
        now = datetime.datetime.now().date()
        nowStr = str(now)
        ts = int(time.mktime(time.strptime(nowStr,"%Y-%m-%d"))) - time.timezone
        response = dlMonthChart(asset,now.month, now.year)

        l = response.text.splitlines()[1]
        datet = l.split(",")[1]

        self.assertEqual(int(datet[0:2]), now.month)

    def test_LastDate(self):
        import datetime;
        import time
        now = datetime.datetime.now().date()
        nowStr = str(now)
        ts = int(time.mktime(time.strptime(nowStr,"%Y-%m-%d"))) - time.timezone
        response = dlMonthChart(asset,now.month, now.year)

        l = response.text.splitlines()[-1]
        datet = l.split(",")[1]

        self.assertEqual(int(datet[0:2]), now.month)

    def test_dlpoints(self):
        import datetime;
        import time
        now = datetime.datetime.now().date()
        nowStr = str(now)
        ts = int(time.mktime(time.strptime(nowStr,"%Y-%m-%d"))) - time.timezone
        #rsp = dlpoints(asset, startTS, endTS)
        #TODO: Finish
        #self.assertEquals(0,1)
        self.fail()



if __name__ == "__main__":
    unittest.main()
    
