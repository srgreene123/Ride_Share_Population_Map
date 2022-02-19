import math
import pandas
from matplotlib import pyplot
import seaborn
import gmplot


# Find the latitude/longitude coordinates for the area of interest
def get_coordinates():
    file_info = pandas.read_csv('')  # figure out how to get public data
    # parse file based on coordinates only
    refined_results = file_info.parse()

    # select specific sample size to choose from
    refined_results = refined_results.sample(n=2000)

    # plot the coordinate ranges
    coordinate_plot = seaborn.relplot(data=refined_results, kind='scatter', x='latitude', y='longitude')
    return coordinate_plot


# Find optimal distance between clusters
def find_minimum_distance(coordinates):
    print('hi2')
    return 1


# Find the needed clusters
def find_clusters():
    print('hi3')


# Create graphical representation of the busiest zones with people for rideshare drivers
def create_heat_map():
    coordinates_area_rep = get_coordinates()
    optimal_dist = find_minimum_distance(coordinates_area_rep)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_heat_map()
