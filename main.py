import math

import numpy
import pandas
from pandas.core.frame import DataFrame
from matplotlib import pyplot
import seaborn
import gmplot
from sklearn import preprocessing
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors


# Find the latitude/longitude coordinates for the area of interest
def get_coordinates():
    # grab public data from https://github.com/fivethirtyeight/uber-tlc-foil-response/tree/master/uber-trip-data
    file_info = pandas.read_csv('uber-raw-data-may14.csv')
    # parse csv file based on longitude/latitude only
    refined_results = file_info.drop(columns=['Date/Time', 'Base'])
    # select specific sample size to choose from since there are many data points
    refined_results = refined_results.sample(n=30000)

    # plot the coordinate ranges
    seaborn.relplot(data=refined_results, kind='scatter', x='Lat', y='Lon')
    pyplot.show()  # display plot of general coordinates of area
    return refined_results


# Find the needed clusters to represent the area
def find_generalized_clusters(general_area_coordinates):
    normalization_prep = preprocessing.StandardScaler()  # prepares standardization on coordinates
    standardized_data = normalization_prep.fit_transform(general_area_coordinates.values)
    return standardized_data


# Find the max distance between clusters to be considered as neighbors
def find_epsilon(general_region):
    # specified num of clusters to compare and computed the nearest neighbors
    values_between = NearestNeighbors(n_neighbors=2).fit(general_region.values)
    distance, index = values_between.kneighbors(general_region.values)
    distance = numpy.sort(distance, axis=0)
    distance = distance[:,1][29500:] # to ensure the curve appears
    pyplot.plot(distance)
    pyplot.show()
    max_value =
    return max_value


# Find the high density clusters (most populous area)
def find_high_pop_clusters(general_area, standardized_data):
    find_epsilon(general_area)  # max distance between clusters to be considered neighbors (arbitrary value)

    # use DBSCAN algorithm to compare the high density vs low density area in terms of population
    # clusters = DBSCAN(eps=epsilon, min_samples=20).fit(general_area.values)


# Create graphical representation of the busiest zones with people for ride-share drivers
def create_heat_map():
    general_region = get_coordinates()
    standardized_data = find_generalized_clusters(general_region)
    general_area = pandas.DataFrame(general_region)
    general_area.head(n=2)
    general_area = find_high_pop_clusters(general_area, standardized_data)

    longitude_list = list(general_area.Lon.values)
    latitude_list = list(general_area.Lat.values)

    # visualize as a heat map through Google Maps
    google_map = gmplot.GoogleMapPlotter.from_geocode('Manhattan, New York')
    google_map.apikey = 'hackathonSecretKey'
    google_map.heatmap(latitude_list, longitude_list)
    google_map.draw('~/Users/Sarah/Desktop/map1.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_heat_map()

