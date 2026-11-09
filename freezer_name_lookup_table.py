#Lookup disctionary of Freezer ID: Name, Mean
import sys
#TODO: Possibly chage to a freezer class with an ID.port, Reading Type, Name, Setvalue

lookup2 = {
    (156368,1,"temperature (C)"): ["RF476 -20C Walk-in Freezer",-20],
    (156370,1,"temperature (C)"): ["RF460 4C Walk-in Refrigerator",4],
    (156375,1,"temperature (C)"): ["RF479 -80C Stirling Freezer",-80],
    (156376,1,"temperature (C)"): ["RF482 -80C Thermo Freezer",-80],
    (156377,1,"temperature (C)"): ["RF480 -20C SoLo Freezer",-20],
    (156452,0,"temperature (C)"): ["RF479 Room Temperature (Stirling)",21],
    (156453,2,"temperature (C)"): ["RF482 Room Temperature (SoLo NIST)",21],
    (156454,0,"temperature (C)"): ["RF480 Room Temperature",21],
    (445018,1,"temperature (C)"): ["RF479 -20C SoLo Freezer (NIST)",-20],
    (655236,1,"temperature (C)"): ["RF479 4C Metabolics Refrigerator",4],
    (544675,0,"temperature (C)"): ["RF479 -20C SoLo Freezer BACKUP",-20], #Non-NIST Temperature redundant
    (156453,2,"humidity (%RH)"): ["RF482 Room Humidity(SoLo NIST)",21],
    (156453,0,"temperature (C)"): ["RF482 Room Temperature(SoLo) BACKUP",21], #Non-NIST Temperature redundant
    (156452,2,"humidity (%RH)"): ["RF479 Room Humidity (Stirling NIST)",21],
    (156452,2,"temperature (C)"): ["RF479 Room Temperature (Stirling NIST)",21],
    (156454,2,"humidity (%RH)"): ["RF480 Room Humidity (NIST)",21],
    (156454,2,"temperature (C)"): ["RF480 Room Temp (NIST)",21]
 }

#class freezer:
    
def getFreezerName(asset, port=1, reading="temperature (C)") :
    x=0
    try:
        x = lookup2[asset][0]
    except KeyError:
        print("Unknown Freezer Name: ")
        print(str(asset[0]) + " - Port: "+str(asset[1]) + " - " + asset[2])
        sys.exit("Exception")
    return x

def getFreezerMean(asset) :

    try:
        x = lookup2[asset][1]
    except KeyError:
        print("Unknown Freezer")
    return x

def getFreezerIDs():
    numbers2 = []
    numbers = list(set(lookup2.keys()))
    for num in numbers:
            numbers2.append(num[0])
    return numbers2