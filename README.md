# Web3 Campaign Attribution & On-Chain Analysis

## 📌 Overview
This project bridges the gap between traditional Web2 marketing analytics and Web3 on-chain realities. It analyzes marketing campaigns by tracking user journeys from initial URL clicks (UTM parameters) to actual on-chain conversions (Ethereum smart contract interactions). 

The analysis demonstrates how to move beyond superficial metrics like "clicks" or "page views" to measure true marketing ROI and user quality in the Web3 ecosystem.

## 🚀 Key Features
*   **First-Click Attribution Model:** Built using advanced SQL window functions (`ROW_NUMBER()`) in DuckDB to accurately attribute wallet addresses to their originating campaigns.
*   **On-Chain Verification:** Matches off-chain user events with verified on-chain Ethereum transactions using Web3.py and the Alchemy API.
*   **User Quality Assessment (ENS Resolution):** Performs reverse resolution of Ethereum addresses to ENS domains, establishing the "crypto-nativeness" and quality of the acquired user cohorts.
*   **Data Visualization:** Generates clear, actionable insights using Matplotlib to compare campaign traffic, conversion rates, and user quality.

## 🛠️ Tech Stack
*   **Data Processing & SQL:** DuckDB, Pandas
*   **Web3 & Blockchain:** Web3.py, Alchemy API, Ethereum Name Service (ENS)
*   **Visualization:** Matplotlib
*   **Environment:** Jupyter Notebook / Python

## 📊 Key Insights & Results
*   **Traffic ≠ Conversion:** The `cbwallet` campaign generated the highest volume of raw traffic but resulted in a conversion rate of only ~1.12%[cite: 1].
*   **High-Intent Targeting:** The `bestprice` campaign, despite driving less initial traffic, achieved an outstanding on-chain conversion rate of ~24.49%[cite: 1].
*   **Acquiring High-Quality Users:** Users acquired through the `mev` campaign had the highest rate of owned ENS domains, indicating a more experienced and engaged Web3 user base[cite: 1].

## 🔒 Note on Data Privacy
> **Disclaimer:** The original production datasets contain confidential company and user data. To maintain privacy while demonstrating the code's functionality, all original CSV files have been removed. 
> 
> A `generate_mock_data.py` script is included in this repository. You can run it to generate synthetic mock data with an identical schema, allowing the Jupyter Notebook to run seamlessly.

## ⚙️ How to Run
1. Clone the repository.
2. Install the required dependencies: `pip install duckdb pandas web3 matplotlib`.
3. Run `python generate_mock_data.py` to generate the sample datasets.
4. Open the Jupyter Notebook and execute the cells. *(Note: Ensure you insert your own Alchemy API key where indicated).*

---
**Author:** Daniel
