import math
import pandas
from matplotlib import pyplot
import seaborn
import gmplot
from sklearn import preprocessing
from sklearn.cluster import DBSCAN


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
    print(standardized_data[0:2])  # take this out??
    general_area_coordinates.head(n=2)

    find_high_pop_clusters(general_area_coordinates, standardized_data)


# Find the high density clusters (most populous area)
def find_high_pop_clusters(general_area, standardized_data):
    epsilon = 0.5  # max distance between clusters to be considered neighbors (arbitrary value)

    # use DBSCAN algorithm to compare the high density vs low density area in terms of population
    #clusters = DBSCAN(eps=epsilon, min_samples=20).fit(general_area.values)

    predict_clusters = DBSCAN(eps=epsilon, min_samples=25).fit_predict(standardized_data)  # create high density cluster predictions based on normalized data
    created_clusters = pandas.Series(data=predict_clusters)  #
    created_clusters.unique()  # create unique clusters so no duplicates are allowed

    general_area['Populous predictions'] = created_clusters.values

    seaborn.scatterplot(data=general_area, hue='Populous predictions', x='Lat', y='Lon', palette='husl')
    pyplot.show()  # display plot based on high density clusters


# Create graphical representation of the busiest zones with people for ride-share drivers
def create_heat_map():
    return 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    general_region = get_coordinates()
    find_generalized_clusters(general_region)

