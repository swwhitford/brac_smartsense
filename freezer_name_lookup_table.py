
def getFreezerName(asset) :
    lookup = {
    156368: "RF476 -20C Walk-in Freezer",
    156370: "RF460 4C Walk-in Refrigerator",
    156375: "RF479 -80C Stirling Freezer",
    156376: "RF482 -80C Thermo Freezer",
    156377: "RF480 -20C SoLo Freezer",
    156452: "RF479 Room Temperature (Stirling)",
    156453: "RF480 Room Temperature (SoLo)",
    156454: "RF480 Room Temperature",
    445018: "RF479 -20C SoLo Freezer",
    655236: "RF479 4C Metabolics Refrigerator",
    544675: "RF479 -20C SoLo Freezer"
 }
    try:
        x = lookup[asset]
    except KeyError:
        print("Unknown Freezer Name")

    return x