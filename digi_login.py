import ast
from os.path import exists, splitext

from requests import Session

# from login import data


def main():

    startTS = "1644382800000"
    endTS = "1644469199999"
    outFileName = "test.csv"
    asset = "156354"
    response = dlpoints(asset, startTS, endTS)
    responseToFile(response, outFileName)
    print("Success")


def checkHTMLResponse(response):
    if str(response.status_code) == "401":
        return "Code: 401 - Unauthorized"
    elif str(response.status_code) == "405":
        return "Code: 405 Method Not Allowed"
    elif str(response.status_code) == "400":
        return "Code: 400 - Bad Request"
    elif str(response.status_code) == "200":
        return "Code: 200 - IT WORKED"
    else:
        return response


def dlpoints(asset, startTS, endTS):
    from login import data

    headers = {
        "authority": "app.smartsense.co",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://app.smartsense.co",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.smartsense.co/",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "amplitude_id_e2080f9fca8687e8157fc49bf3135a41smartsense.co=eyJkZXZpY2VJZCI6IjU1Y2YyN2VlLTE5MWMtNDU1Yi04NGEzLWFkMzU4MTU4OTE5Y1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0NDEyMzE3MDQ3NSwibGFzdEV2ZW50VGltZSI6MTY0NDEyMzE3MDQ3NSwiZXZlbnRJZCI6MTQsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjoxNH0=",
    }

    with Session() as s:
        response = s.post(
            "https://app.smartsense.co/api/Login", headers=headers, data=data
        )

    # print(checkHTMLResponse(response))

    tokendict = ast.literal_eval(response.text)
    token = str(tokendict["token"])

    headers = {
        "authority": "app.smartsense.co",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer " + token,
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "amplitude_id_e2080f9fca8687e8157fc49bf3135a41smartsense.co=eyJkZXZpY2VJZCI6IjU1Y2YyN2VlLTE5MWMtNDU1Yi04NGEzLWFkMzU4MTU4OTE5Y1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0NDEyMzE3MDQ3NSwibGFzdEV2ZW50VGltZSI6MTY0NDEyMzE3MDQ3NSwiZXZlbnRJZCI6MTQsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjoxNH0=",
    }

    params = (
        ("start", startTS),
        ("end", endTS),
        ("includeDeletedSensorPoints", "false"),
        ("utcOffset", "0"),
    )

    with Session() as s2:
        response = s2.get(
            "https://app.smartsense.co/api/Asset/" + str(asset) + "/ChartData/Download",
            headers=headers,
            params=params,
        )

    # print(checkHTMLResponse(response))
    return response


def responseToFile(response, outFileName):
    filename_base = splitext(outFileName)[0]
    ext = splitext(outFileName)[1]
    j = 1
    file_exists = exists(filename_base + ext)
    if file_exists:
        while exists(filename_base + "(" + str(j) + ")" + ext):
            j += 1
        file_to_write = filename_base + "(" + str(j) + ")" + ext
    else:
        file_to_write = filename_base + ext

    with open(file_to_write, "w") as file:
        file.write(response.text)


if __name__ == "__main__":
    main()
