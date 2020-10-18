import pandas as pd
import numpy
import notapp.gps.maps as maps
import notapp.gps.start as start


# inputs string of file name


def outputHtml(fitFileUpload):
    # this converts the file and stores its new name
    inputFile = start.main(fitFileUpload)
    # reads file and puts lat, long in dataFrame
    # This location will need to be FIXED
    datamaps = pd.read_csv('./' + inputFile)
    coords = datamaps[["position_lat", "position_long"]]
    # outputs all rows for debugging makes new dataFrame without null values
    pd.set_option('display.max_rows', None)
    # dumps all the rows missing long/lat data
    coords2 = coords.dropna(axis=0, subset=["position_lat", "position_long"])
    # convert to numpy array
    coords3 = coords2.to_numpy()
    # convert numpy array to tuple object
    coordTup = map(tuple, coords3)
    # convert to list of tuples
    coordFinal = list(coordTup)
    orienting_map = maps.findMiddleMap(coordFinal)
    mapping_code = maps.make_a_map(coordFinal, center=orienting_map)
    print(mapping_code)


# for testing
# outputHtml('AA2F0532.FIT')
