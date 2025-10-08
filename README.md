# Rapido-Ride-Insights-An-Analytical-Deep-Dive
## Project Overview
The analysis is structured around a three-page performance dashboard, which translates raw data (sourced and cleaned using Python) into prioritized, actionable business intelligence.
Key Objectives:
Quantify Financial Loss: Calculate and prioritize the estimated $2.48 Million in lost revenue due to cancellations.
Identify High-Impact Services: Pinpoint which service lines (e.g., Bike, Auto) pose the greatest financial and operational risk (using a Control-Impact Matrix).
Determine Intervention Timing: Isolate the precise hours and days (using a Cancellation Risk Matrix) that require aggressive operational fixes, such as driver incentives.
The project leverages Python's pandas for feature engineering and seaborn for initial exploratory data analysis, ensuring the final dashboard is built on robust, derived metrics. The ultimate output is a clear roadmap to recover efficiency and optimize resource allocation.

## Role of Python in the Project

Python was the foundational tool used for preparing, cleaning, and engineering the raw data before it was fed into the Looker Studio visualization layer.

### `data_loading.py`
This script handled the initial intake of the raw dataset (`rides_data.csv`), performing crucial checks on data integrity and structure.
* **Key Function:** Initial data load, displaying the first few rows, and outputting general DataFrame information (`.info()`) and a statistical summary (`.describe()`) to identify data types and potential outliers.

### `data_cleaning_and_feature_engineering.py`
This is the core data preparation script responsible for transforming raw logs into enriched, analysis-ready features.
* **Key Functions:**
    * **Datetime Conversion:** Combining separate `date` and `time` columns into a single `datetime` object for time-series analysis.
    * **Missing Value Handling:** Filling missing fare values for cancelled rides with 0 to maintain accurate aggregates.
    * **Feature Creation:** Creating essential categorical and numerical features used in the dashboard, including:
        * `day_of_week`, `hour_of_day`, and `daypart`.
        * **`trip_type`** (Bike, Auto, Cab, Parcel).
        * **`fare_per_km`** (Revenue efficiency metric).
        * **`is_rush_hour`** (A boolean flag for peak demand periods: 7-10 AM and 5-8 PM).

### `EDA.py`
This script was used for Exploratory Data Analysis, generating initial plots and visualizations to guide the dashboard design and confirm key data patterns.
* **Key Functions:** Generated plots to analyze hourly demand by service type, distribution of `fare_per_km`, cancellation rates by day of the week, and the relationship between ride duration and distance.

---
## Interactive Dashboard Link
The full interactive dashboard can be viewed here:
[Google Looker Studio Report Link](https://lookerstudio.google.com/s/gmD_JjNSJ40))

## Insights from the Report
### Page 1: Executive Summary

This page establishes the scale and daily rhythm of the business operations.

* **Busiest vs. Riskiest Day:**
    * **Busiest Day:** **Monday**, with $\mathbf{6,679}$ completed rides.
    * **Riskiest Day (by Volume):** **Thursday**, with the highest absolute number of cancellations at **767**.
* **Operational Consistency:** The average speed is highly consistent across all services, ranging narrowly from **35.01 km/hr (Auto) to 35.66 km/hr (Parcel)**. This uniformity suggests that **driver supply and acceptance behavior**, not network congestion or routing, are the primary levers for performance improvement.

### Page 2: Financial Efficiency and Demand Structure
This page focuses on the characteristics of **completed rides** to guide pricing and market strategy.

* **Core Demand is Long-Haul:** The business is heavily reliant on long trips. Over **$\mathbf{67\%}$ of completed ride volume** comes from trips lasting **45 minutes or longer**.
    * Long (45-90 min): $\mathbf{40.7\%}$ (18,300 rides).
    * Very Long (>90 min): $\mathbf{26.3\%}$ (11,840 rides).
* **Most Price-Efficient Service:** The **Auto** service is the most profitable per distance unit, with the highest **fare per km ($\mathbf{39.82}$)**.
* **Transaction Stability:** Payment processing is not a cause of cancellations. All digital methods show high completion rates ($\mathbf{\ge 98.59\%}$), with **Paytm achieving 100% stability**.

### Page 3: Risk Management & Operational Intervention

This page identifies the highest-impact service lines and time windows for immediate operational intervention, using the **$10.07\%$** overall rate as the benchmark.

#### Strategic Risk Prioritization (Control-Impact Matrix)
| Service | Volume (Rides) | Cancellation Rate | Estimated Lost Revenue | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **Bike** | $\mathbf{20,012}$ | $\mathbf{10.28\%}$ | $\mathbf{\$1,009,431}$ | **P1: Must Fix (High Volume/High Risk)** |
| **Cab** | $10,202$ | $\mathbf{10.33\%}$ | $\$517,208$ | **P2: Investigate (Highest Rate/Process Failure)** |
| Auto | $12,327$ | $9.84\%$ | $\$600,229$ | P3: Stable (Monitor) |
| Parcel | $7,459$ | $9.55\%$ | $\$351,899$ | P3: Stable (Monitor) |

#### Tactical Time Intervention (Cancellation Risk Matrix)
* **Absolute Peak Failure Time:** The network is most fragile on **Friday at 7 AM**, which records a peak cancellation rate of **$\mathbf{14.19\%}$**. This hour requires the maximum level of dynamic incentives.
* **Systemic Off-Peak Instability:** High volatility (rates $\ge 12\%$) is consistently seen in the **early morning hours (1 AM to 4 AM)**. This points to a need for non-surge incentives to stabilize the 24/7 driver base.
