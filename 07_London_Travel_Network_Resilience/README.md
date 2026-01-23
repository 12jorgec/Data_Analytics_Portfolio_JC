# 🚇 London Travel: Transport Network Resilience Analysis

### Project Overview
This project evaluates the resilience of London's underground transport network. By modeling the system as a complex network, I analyzed how the failure of specific stations or lines impacts the overall connectivity and efficiency of urban mobility.

### Tech Stack
* **Language:** Python
* **Libraries:** NetworkX (Graph Theory), Pandas (Data Management), Matplotlib (Visualization)
* **Concepts:** Graph Theory, Centrality Measures, Network Topology

### Engineering Analysis (Systems Thinking)
Leveraging my background as an **Industrial and Systems Engineer (ITESM)**, the analysis includes:
* **Network Mapping:** Modeling stations as nodes and tracks as edges to visualize the TFL (Transport for London) infrastructure.
* **Critical Node Identification:** Using Closeness and Betweenness Centrality to find the most vital hubs in the city.
* **Resilience Testing:** Simulating disruptions to measure the system's "robustness" and identifying potential bottlenecks for urban planning.

### Key Results
* Identified the top 5 most critical stations whose closure would cause the highest network-wide delay.
* Proposed data-driven recommendations for infrastructure reinforcement based on network topology.

### Project Structure
* `data/`: Graph-structured datasets of the London Underground network.
* `images/`: Network visualizations and centrality distribution plots.
* `notebooks/`: `london_network_resilience.ipynb` — Full graph analysis script.
* `reports/`: [London_Transport_Network_Analysis.pdf](./London_Transport_Network_Analysis.pdf) — Full technical analysis.