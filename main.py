import numpy
import pandas
from matplotlib import pyplot
import seaborn
from sklearn import preprocessing
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import gmplot

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
    distance = distance[:,1][29500:]  # to ensure the curve appears, based on the sample indicated with refined results
    pyplot.title('Epsilon finder')
    pyplot.plot(distance)
    pyplot.show()


# Find the high density clusters (most populous areas)
def get_high_pop_areas(general_area, standardized_data):
    find_epsilon(general_area)  # max distance between clusters to be considered neighbors (arbitrary value)
    epsilon = 0.05  # look at 'Epsilon finder' plot created and the max of the function (deepest curvature) is about 0.05
    # use DBSCAN algorithm to compare the high density vs low density area in terms of population
    predict_clusters = DBSCAN(eps=epsilon, min_samples=100).fit_predict(standardized_data)  # create high density cluster predictions based on normalized data
    created_clusters = pandas.Series(data=predict_clusters)
    created_clusters.unique()  # create unique clusters so no duplicates are allowed

    general_area['Populous_predictions'] = created_clusters.values

    pyplot.title('Predicted high density clusters')
    seaborn.scatterplot(data=general_area, hue='Populous_predictions', x='Lat', y='Lon', palette='Set2')
    pyplot.legend()
    pyplot.show()  # display plot based on high density clusters

    pyplot.title('Highest density area in New York City')
    seaborn.scatterplot(data=general_area[general_area.Populous_predictions == 0], hue='Populous_predictions', x='Lat', y='Lon', palette='Set2')
    pyplot.show()  # display plot that do not include any variance in neighboring distance


# Create graphical representation of the busiest zone with people for ride-share drivers
def find_densest_area():
    general_region = get_coordinates()
    standardized_data = find_generalized_clusters(general_region)
    general_area = pandas.DataFrame(general_region)
    general_area.head(n=2)
    get_high_pop_areas(general_area, standardized_data)

    # create heat map using google api resources
    # latitude_list = list(general_area.Lat.values)
    # longitude_list = list(general_area.Lon.values)
    # google_map = gmplot.GoogleMapPlotter(40.7831, -73.9712, 10)
    # google_map.heatmap(latitude_list, longitude_list)
    # google_map.apikey = 'hackathonsecretkey'
    # google_map.draw('~/Users/Desktop/Sarah/map1.html')


if __name__ == '__main__':
    find_densest_area()

