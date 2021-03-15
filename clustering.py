# clustering try
# from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import style
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import plotly.express as px

token = 'pk.eyJ1IjoicHJpdGh2aWsyMSIsImEiOiJja2g0eHBpamkwYXB5MnNrMDNjaXFvNnRhIn0.6eeLvU-4xuLb8q43RAQGBA'
px.set_mapbox_access_token(token)

df = pd.read_csv("finalMergedBirds/birdsNewLinks.csv")
data = df[['Latitude', 'Longitude']]
geolocator = Nominatim(user_agent="myGeocoder")
k_means = KMeans(n_clusters=5)
labels = k_means.fit_predict(data)


df["Cluster"] = labels
centroids = k_means.cluster_centers_
c = pd.DataFrame(centroids, columns=['Latitude', 'Longitude'])
c['Address'] = c.apply(lambda row: geolocator.reverse((row['Latitude'], row['Longitude'])), axis=1)
#c['Address'] = c.apply(lambda row: row.to_string().split(',')[2] + 'District')
for x in c['Address'].to_list():
    print(x.address.split(',')[2])
#px.scatter_mapbox(c, lat="Latitude", lon="Longitude").show()


# colors = ['g.', 'r.', 'b.', 'c.', 'k.']
# ax = df.plot.scatter(x='Latitude', y='Longitude', c='Cluster', colormap='Set1')
# c.plot.scatter(ax=ax, x='Latitude', y='Longitude', s=1000, c='red', alpha=0.5, marker='h')
# plt.show()

# l = pd.DataFrame(labels).value_counts()
# l.plot.bar()
