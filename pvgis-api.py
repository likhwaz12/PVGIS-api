import requests

def main(lat, lon, peakPower, losses):
    response = requests.get("https://re.jrc.ec.europa.eu/api/PVcalc?",
    params={"lat":lat, 
            "lon": lon,
#            "usehorizon": horizon,
#            "userhorizon": horizonValue,
#            "raddatabase": radiationDatabase,
            "peakpower": peakPower,
#            "pvtechchoice": pvTech,
#            "mountingplace": mounting,
             "loss": losses,
             "outputformat": "json",
             "browser": 0
            # "fixed": fixed,
            # "angle": inclinationAngle,
            # "aspect": azimuth,
            # "optimalinclination": optimalInclination,
            # "optimalangles": optimalAngles,
            # "inclined_axis": inclinedAxis,
            # "inclined_optimum": inclinedOptimum,
            # "inclinedaxisangle": inclinedAxisAngle,
            # "vertical_axis": verticalAxisAngle,
            # "vertical_optimum": verticalOptimum,
            # "verticalaxisangle": verticalAxisAngle,
            # "twoaxis": twoAxis,
            # "pvprice": pvPrice,
            # "systemcost": systemCost,
            # "interest": interest,
            # "lifetime": lifetime,
            # "outputformat": outputformat,
            # "browser": browser
            })

#    if response.code != 200:
#        raise Exception (f"{response.code} Error - API request unsuccessful. {response.text}")
#    else:
#        pvgis_data= response.json()
#        return(pvgis_data)
    return(response)

if __name__ == '__main__':
    lat = input("Latitude (-) for South: ")
    lon = input("Longitude: (-) for West: ")
#    horizon = input("Account for shadows from the horizon? 1 - yes, 0 - no: ")
#    horizonValue = input("Height of the horizon in degress from PV location starting at North moving anti-clockwise. [unknown]: ")
#    radiationDatabase = input("Name of the radiation database to be used. Leave blank for default value: ")
    peakPower = input("Enter system peak power in kW: ")
#    pvTech = input("Select PV technology. Choices are: 'crystSi', 'CIS', 'CdTe' and 'Unknown'. [crystSi]: ")
#    mounting = input("Mounting type - 'free' for freestanding and 'building' for BIPV. [free]: ")
    losses = input("Enter total system losses as a percentage. Recommend 12: ")
    

    pvgis_data = main(lat, lon, peakPower, losses)
    print(pvgis_data)
