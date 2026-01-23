# 🐧 Antarctic Penguin Species: Machine Learning Clustering

### Project Overview
This project applies **Unsupervised Machine Learning** to classify penguin populations in Antarctica based on morphological measurements (culmen length, flipper length, and body mass). The objective was to identify natural biological groupings using high-dimensional data.

### Tech Stack
* **Language:** Python (Scikit-Learn, Pandas).
* **Machine Learning:** Unsupervised Learning (K-Means, PCA) — *Validated by Stanford University & DataCamp Career Tracks*.
* **Methodology:** Feature Scaling and Dimensionality Reduction for optimal cluster separation.

### Machine Learning Framework (Stanford Standards)
Following the rigorous analytical framework from my **Stanford University** training, I implemented:
* **Data Preprocessing:** Standardizing biological features to ensure model convergence.
* **Optimal K Selection:** Utilizing the Elbow Method and Silhouette Analysis to determine the true number of species clusters.
* **Principal Component Analysis (PCA):** Reducing complexity to visualize 3D biological clusters in a 2D plane for executive interpretation.

### Key Results
* **Cluster Validation:** Successfully identified three distinct biological clusters corresponding to different species.
* **Morphological Predictors:** Determined that flipper length is the most significant indicator for species differentiation.

### Project Structure
* `data/`: `penguins.csv` — Raw observational data.
* `images/`: Cluster visualizations and PCA distribution plots.
* `notebooks/`: `penguin_clustering_model.ipynb` — Full ML pipeline.
* `reports/`: [Antarctic_Penguin_ML_Report.pdf](./Antarctic_Penguin_ML_Report.pdf) — Technical scientific report.