
# Bus Station Optimization

This project optimizes bus station locations using clustering algorithms (DBSCAN and KMeans). The application is built with Streamlit and provides an interactive UI for parameter tuning, visualization, and downloading results.

## Features
- **Clustering Algorithms**:
  - **DBSCAN**: Density-based clustering to identify natural clusters.
  - **KMeans**: Partition-based clustering for targeted station placement.
- **Interactive Visualization**:
  - Display the clustering results on a 2D scatter plot.
- **Download Results**:
  - Optimized bus station locations can be downloaded as CSV files.

---

## Prerequisites
- Python 3.11 or higher
- Streamlit installed
- A CSV file named `silicon_valley_stop_points.csv` with the following columns:
  - `Latitude`
  - `Longitude`
  - `Population Density`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/bus-station-optimization.git
   cd bus-station-optimization
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the data file (`silicon_valley_stop_points.csv`) in the root directory.

---

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. Adjust the following parameters:
   - **Target Stations**: Number of bus stations to optimize.
   - **Eps (DBSCAN Radius)**: Radius for DBSCAN clustering.
   - **Min Samples (DBSCAN)**: Minimum samples per cluster in DBSCAN.

4. Click "Optimize" to:
   - Visualize the clustering results.
   - Download optimized bus station locations as CSV files.

---

## Deployment with Docker

1. Build the Docker image:
   ```bash
   docker build -t bus-station-optimization .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 bus-station-optimization
   ```

3. Access the application at:
   ```
   http://localhost:8080
   ```

---

## CSV File Format
Ensure your CSV file (`silicon_valley_stop_points.csv`) has the following columns:
```csv
Latitude,Longitude,Population Density
37.7749,-122.4194,1000
37.7849,-122.4094,2000
...
```

---

## Outputs
- **DBSCAN Results**: CSV file with clustered stations based on population density.
- **KMeans Results**: CSV file with optimized station placements.

---


## Acknowledgments
This project uses:
- [Streamlit](https://streamlit.io/) for interactive UI.
- [Scikit-learn](https://scikit-learn.org/) for clustering algorithms.
- [Matplotlib](https://matplotlib.org/) for visualization.

--- 

Enjoy optimizing your bus stations! 🚍
