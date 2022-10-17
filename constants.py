"""Constant values for the project"""

# A dictionary of the 48 contiguous states in the US with the latitude and longitude of their center
# Source: https://www.latlong.net/category/states-236-14.html
# Accessed: 2019-10-15
STATE_COORDINATES = {
    "00": {"state": "AL", "lat": 32.318231, "lon": -86.902298},
    "01": {"state": "AK", "lat": 61.370716, "lon": -152.404419},
    "02": {"state": "AZ", "lat": 33.729759, "lon": -111.431221},
    "03": {"state": "AR", "lat": 34.969704, "lon": -92.373123},
    "04": {"state": "CA", "lat": 36.116203, "lon": -119.681564},
    "05": {"state": "CO", "lat": 39.059811, "lon": -105.311104},
    "06": {"state": "CT", "lat": 41.597782, "lon": -72.755371},
    "07": {"state": "DE", "lat": 39.318523, "lon": -75.507141},
    "08": {"state": "FL", "lat": 27.766279, "lon": -81.686783},
    "09": {"state": "GA", "lat": 33.040619, "lon": -83.643074},
    "10": {"state": "HI", "lat": 21.094318, "lon": -157.498337},
    "11": {"state": "ID", "lat": 44.240459, "lon": -114.478828},
    "12": {"state": "IL", "lat": 40.349457, "lon": -88.986137},
    "13": {"state": "IN", "lat": 39.849426, "lon": -86.258278},
    "14": {"state": "IA", "lat": 42.011539, "lon": -93.210526},
    "15": {"state": "KS", "lat": 38.526600, "lon": -96.726486},
    "16": {"state": "KY", "lat": 37.668140, "lon": -84.670067},
    "17": {"state": "LA", "lat": 31.169546, "lon": -91.867805},
    "18": {"state": "ME", "lat": 44.693947, "lon": -69.381927},
    "19": {"state": "MD", "lat": 39.063946, "lon": -76.802101},
    "20": {"state": "MA", "lat": 42.230171, "lon": -71.530106},
    "21": {"state": "MI", "lat": 43.326618, "lon": -84.536095},
    "22": {"state": "MN", "lat": 45.694454, "lon": -93.900192},
    "23": {"state": "MS", "lat": 32.741646, "lon": -89.678696},
    "24": {"state": "MO", "lat": 38.456085, "lon": -92.288368},
    "25": {"state": "MT", "lat": 46.921925, "lon": -110.454353},
    "26": {"state": "NE", "lat": 41.125370, "lon": -98.268082},
    "27": {"state": "NV", "lat": 38.313515, "lon": -117.055374},
    "28": {"state": "NH", "lat": 43.452492, "lon": -71.563896},
    "29": {"state": "NJ", "lat": 40.298904, "lon": -74.521011},
    "30": {"state": "NM", "lat": 34.840515, "lon": -106.248482},
    "31": {"state": "NY", "lat": 42.165726, "lon": -74.948051},
    "32": {"state": "NC", "lat": 35.630066, "lon": -79.806419},
    "33": {"state": "ND", "lat": 47.528912, "lon": -99.784012},
    "34": {"state": "OH", "lat": 40.388783, "lon": -82.764915},
    "35": {"state": "OK", "lat": 35.565342, "lon": -96.928917},
    "36": {"state": "OR", "lat": 44.572021, "lon": -122.070938},
    "37": {"state": "PA", "lat": 40.590752, "lon": -77.209755},
    "38": {"state": "RI", "lat": 41.680893, "lon": -71.511780},
    "39": {"state": "SC", "lat": 33.856892, "lon": -80.945007},
    "40": {"state": "SD", "lat": 44.299782, "lon": -99.438828},
    "41": {"state": "TN", "lat": 35.747845, "lon": -86.692345},
    "42": {"state": "TX", "lat": 31.054487, "lon": -97.563461},
    "43": {"state": "UT", "lat": 40.150032, "lon": -111.862434},
    "44": {"state": "VT", "lat": 44.045876, "lon": -72.710686},
    "45": {"state": "VA", "lat": 37.769337, "lon": -78.169968},
    "46": {"state": "WA", "lat": 47.400902, "lon": -121.490494},
    "47": {"state": "WV", "lat": 38.491226, "lon": -80.954453},
    "48": {"state": "WI", "lat": 44.268543, "lon": -89.616508},
    "49": {"state": "WY", "lat": 42.755966, "lon": -107.302490},
}


STATES = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


COLOR_RANGE = [
    [65, 182, 196],
    [127, 205, 187],
    [199, 233, 180],
    [237, 248, 177],
    [255, 255, 204],
    [255, 237, 160],
    [254, 217, 118],
    [254, 178, 76],
    [253, 141, 60],
    [252, 78, 42],
    [227, 26, 28],
]

COLOR_VALUES = [
    [13, 59, 102],
    [238, 150, 75],
    [249, 87, 56],
    [0, 0, 128],
    [210, 105, 30],
    [220, 20, 60],
    [250, 128, 114],
    [0, 100, 0],
    [255, 215, 0],
    [50, 205, 50],
    [47, 79, 79],
    [0, 255, 255],
    [0, 0, 255],
    [75, 0, 130],
    [255, 0, 255],
    [255, 192, 203],
]

BREAKS = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# make a bar chart of the COLOR_VALUES using matplotlib


def make_color_bar():
    fig = plt.figure(figsize=(10, 1))
    ax = fig.add_axes([0.05, 0.80, 0.9, 0.15])
    cmap = mpl.colors.ListedColormap(COLOR_VALUES)
    norm = mpl.colors.BoundaryNorm(BREAKS, cmap.N)
    cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation="horizontal")
    cb.set_ticks([])
    fig.savefig("colorbar.png", dpi=300, bbox_inches="tight")
