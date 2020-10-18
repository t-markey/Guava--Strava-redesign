import gmplot
import notapp.gps.auth as auth


# selects the location of the map to be started at in the window


def findMiddleMap(mapCenter):
    index = int(len(mapCenter)/2)
    print(index)
    print(mapCenter[index])
    return mapCenter[index]


def make_a_map(inputCoords, center=[40.694475, -73.988954]):

    # Create the map plotter, Hide this KEY*************
    apikey = goog_key
    # this defines center of map and how much to zoom in
    gmap = gmplot.GoogleMapPlotter(center[0], center[1], 13, apikey=apikey)

    # Outline the run:
    coording = zip(*inputCoords)

    print(coording)
    print(type(coording))
    gmap.plot(*coording, color='pink', edge_width=8)

    # marker at start:
    startlong = [x[1] for x in inputCoords]
    startlat = [x[0] for x in inputCoords]
    gmap.text(startlat[0], startlong[0], 'Start', color='green')
    gmap.marker(startlat[0], startlong[0], color='green')
    # marker at finish
    gmap.marker(startlat[-1], startlong[-1], color='red')
    gmap.text(startlat[-1], startlong[-1], 'Finish', color='red')

    # Draw the map:
    gmap.draw('map.html')
    htmltext = gmap.get()
    return htmltext
