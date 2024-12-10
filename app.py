import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
from datetime import datetime

# File path
file_path = "silicon_valley_stop_points.csv"

# Streamlit app
st.title("Bus Station Optimization")
st.write("Optimize bus station locations using DBSCAN and KMeans clustering algorithms.")

# Parameter inputs
target_stations = st.slider("Target Stations", min_value=10, max_value=200, step=10, value=50)
eps = st.slider("Eps (DBSCAN Radius)", min_value=0.01, max_value=1.0, step=0.01, value=0.05)
min_samples = st.slider("Min Samples (DBSCAN)", min_value=1, max_value=50, step=1, value=8)

if st.button("Optimize"):
    try:
        # Read data
        df = pd.read_csv(file_path)
        required_columns = ['Latitude', 'Longitude', 'Population Density']
        if not all(col in df.columns for col in required_columns):
            st.error(f"The CSV file must contain the following columns: {required_columns}")
        else:
            # Data standardization
            scaler = StandardScaler()
            df[['Latitude', 'Longitude', 'Population Density']] = scaler.fit_transform(
                df[['Latitude', 'Longitude', 'Population Density']]
            )
            coords = df[['Latitude', 'Longitude', 'Population Density']].values

            # DBSCAN clustering
            db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)
            df['DBSCAN_Cluster'] = db.labels_
            dbscan_clusters = df[df['DBSCAN_Cluster'] != -1].groupby('DBSCAN_Cluster').agg({
                'Latitude': 'mean',
                'Longitude': 'mean',
                'Population Density': 'sum'
            }).reset_index()
            dbscan_top_clusters = dbscan_clusters.nlargest(target_stations, 'Population Density')

            # KMeans clustering
            kmeans = KMeans(n_clusters=target_stations, random_state=42).fit(coords)
            df['KMeans_Cluster'] = kmeans.labels_
            kmeans_clusters = pd.DataFrame(kmeans.cluster_centers_, columns=['Latitude', 'Longitude', 'Population Density'])

            # Visualization
            plt.figure(figsize=(16, 8))
            plt.scatter(df['Longitude'], df['Latitude'], c=df['Population Density'], cmap='Blues', s=5)
            plt.scatter(dbscan_top_clusters['Longitude'], dbscan_top_clusters['Latitude'], c='red', s=100, label='DBSCAN Clusters')
            plt.scatter(kmeans_clusters['Longitude'], kmeans_clusters['Latitude'], c='blue', s=100, label='KMeans Clusters')
            plt.legend()
            plt.title("Bus Station Optimization Results")
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")
            st.pyplot(plt)

            # Download links
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dbscan_csv_path = f'dbscan_optimized_stops_{timestamp}.csv'
            kmeans_csv_path = f'kmeans_optimized_stops_{timestamp}.csv'

            dbscan_top_clusters.to_csv(dbscan_csv_path, index=False)
            kmeans_clusters.to_csv(kmeans_csv_path, index=False)

            st.write("Download Results:")
            st.download_button("Download DBSCAN Results", open(dbscan_csv_path, "rb"), file_name=dbscan_csv_path)
            st.download_button("Download KMeans Results", open(kmeans_csv_path, "rb"), file_name=kmeans_csv_path)
    except FileNotFoundError:
        st.error("Error: CSV file not found. Please check the file path.")
    except Exception as e:
        st.error(f"Error: {str(e)}")