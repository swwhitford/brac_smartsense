#Lookup disctionary of Freezer ID: Name, Mean
lookup = {
    156368: ["RF476 -20C Walk-in Freezer",-20],
    156370: ["RF460 4C Walk-in Refrigerator",4],
    156375: ["RF479 -80C Stirling Freezer",-80],
    156376: ["RF482 -80C Thermo Freezer",-80],
    156377: ["RF480 -20C SoLo Freezer",-20],
    156452: ["RF479 Room Temperature (Stirling)",21],
    156453: ["RF480 Room Temperature (SoLo)",21],
    156454: ["RF480 Room Temperature",21],
    445018: ["RF479 -20C SoLo Freezer",-20],
    655236: ["RF479 4C Metabolics Refrigerator",4],
    544675: ["RF479 -20C SoLo Freezer",-20]
 }

def getFreezerName(asset) :
    try:
        x = lookup[asset][0]
    except KeyError:
        print("Unknown Freezer Name")

    return x
def getFreezerMean(asset) :

    try:
        x = lookup[asset][1]
    except KeyError:
        print("Unknown Freezer")
    return x

def getFreezerIDs():
    return list(lookup.keys())