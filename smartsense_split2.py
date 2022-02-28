#TODELETE?
#  split the input file by date, adding the month at the end of the new filename (data.csv becomes data.csv01.csv for January data)
from datetime import datetime
from os.path import exists, splitext


filename = "smartsense/asset_156375_readings.csv"

filename_base = splitext(filename)[0]

lastmonth = 13
with open(filename) as f:
    lines = f.readlines()

header = lines.pop(0)

da = [[] for y in range(1, 13)]

for line in lines:
    # Split at comma
    inputFields = line.split(",")

    date_time = datetime.strptime(inputFields[1], "%m/%d/%Y %H:%M:%S")

    year = date_time.strftime("%Y")
    month = date_time.strftime("%m")

    data = line
    da[date_time.month - 1].append(data)

    lastmonth = month
for i in range(12):
    if da[i]:
        file_to_write = filename_base + "_" + str(i + 1) + "-" + year
        j = 1

        file_exists = exists(file_to_write + ".csv")
        if file_exists:
            while exists(file_to_write + "(" + str(j) + ")" + ".csv"):
                j += 1
            file_to_write = file_to_write + "(" + str(j) + ")"

        # open the input file in write mode-
        with open(file_to_write + ".csv", "at") as fin:
            fin.write(header)
            for xyz in da[i]:
                fin.write(str(xyz))
