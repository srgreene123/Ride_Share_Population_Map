import math
import pandas
from matplotlib import pyplot
import seaborn
import gmplot
from sklearn import preprocessing


# Find the latitude/longitude coordinates for the area of interest
def get_coordinates():
    # grab public data from https://github.com/fivethirtyeight/uber-tlc-foil-response
    file_info = pandas.read_csv('uber-raw-data-may14.csv')
    # parse csv file based on longitude/latitude only
    refined_results = file_info.drop(columns=['Date/Time', 'Base'])
    # select specific sample size to choose from since there are many data points
    refined_results = refined_results.sample(n=30000)
    # plot the coordinate ranges
    coordinate_plot = seaborn.relplot(data=refined_results, kind='scatter', x='Lat', y='Lon')
    return coordinate_plot


# Find optimal distance between clusters
def find_minimum_distance(coordinates):
    return 1


# Find the needed clusters
def find_clusters():
    coordinates = get_coordinates()


# Create graphical representation of the busiest zones with people for ride-share drivers
def create_heat_map():
    return 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_heat_map()

