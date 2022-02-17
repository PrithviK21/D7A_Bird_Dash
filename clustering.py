# HOW TO USE: import clustering -> new_df = clustering.clusterset(df) -> use new_df for map/graph
# where clustering is needed, and df for other
from geopy.geocoders import Photon, MapBox
from matplotlib import style
from sklearn.cluster import KMeans
import pandas as pd
style.use('ggplot')


def clusterset(df):
    data = df[['Latitude', 'Longitude']]
    geolocator = MapBox(api_key='pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA')  # geopy module used to retrieve address based on lat/long
    k_means = KMeans(n_clusters=5)
    labels = k_means.fit_predict(data)               # this function fits data to model, and returns labels of centroids for each element
    df["Cluster"] = labels                      # adding each entry's label to the dataset
    centroids = k_means.cluster_centers_
    c = pd.DataFrame(centroids, columns=['Latitude', 'Longitude'])
    c['Address'] = c.apply(lambda row: geolocator.reverse((row['Latitude'], row['Longitude'])), axis=1) # adding column of address
    # print(geolocator.reverse((19.178992  ,72.991496)))
    address_table = dict()
    i = 0
    for x in c['Address'].to_list():  # creating a dictionary that maps integer value of label to address of label
        hm = x.address.split(',')
        hm = hm[1]+', '+ hm[2]
        address_table[i] = hm
        i += 1

    df['Cluster'] = df['Cluster'].apply(lambda row: address_table[row]) # replaces integer label with address stored in dictionary
    return df


if __name__ == '__main__':
    dtf = pd.read_csv("finalMergedBirds/birdsNewLinks.csv")
    dtf = clusterset(dtf)


"""px.scatter_mapbox(c, lat="Latitude", lon="Longitude").show()


colors = ['g.', 'r.', 'b.', 'c.', 'k.']
ax = df.plot.scatter(x='Latitude', y='Longitude', c='Cluster', colormap='Set1')
c.plot.scatter(ax=ax, x='Latitude', y='Longitude', s=1000, c='red', alpha=0.5, marker='h')
plt.show()

l = pd.DataFrame(labels).value_counts()
l.plot.bar()"""
