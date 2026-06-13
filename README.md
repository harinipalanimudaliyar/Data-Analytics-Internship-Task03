# WEB TRAFFIC ANALYTICS & FUNNEL EXPLORATION

## OVERVIEW
The goal of this assignment is to examine granular website data stream logs, evaluate user behavior metrics, map conversion paths, and isolate drop-off friction boundaries using standard Google Analytics 4 (GA4) structural patterns.

## VISUAL DATA INSIGHTS
### 1. GA4 E-commerce Funnel: Conversion Performance & Friction Points
![Funnel Dropoff Chart](funnel_dropoff_chart.png)

## CORE ACTIONS TAKEN
* **Data Stream Integration**: Formatted anonymized hit logs into structured tracking dimensions (`session_id`, `page_url`, `event_name`) to mimic live tag collection pipelines.
* **Milestone Event Aggregation**: Filtered user interactions via SQL into distinct conversion steps: `view_item`, `add_to_cart`, `begin_checkout`, and `purchase`.
* **Friction Points Mapping**: Evaluated baseline conversion volumes and step attrition drop-off rates simultaneously to localize interface elements causing user leaks.
* **Funnel Exploration Deployment**: Constructed an automated Python visualization script using Matplotlib and Seaborn to map user trends across product paths.

## OPERATIONAL MATRIX

| Data Element / Tool | Functional Purpose | Technical Implementation |
| :--- | :--- | :--- |
| **User De-duplication** | Tracks unique customer journeys | `df['user_id'].nunique()` |
| **Event Filtering** | Pinpoints exact interaction steps | `df['event_name'] == 'add_to_cart'` |
| **Dual-Axis Visualizer** | Plots conversion rates & leak lines | Matplotlib dual-axis pipeline engine |

## PROJECT ASSETS
* `dataset.csv`: Anonymized raw website event logs spreadsheet dataset.
* `funnel_query.sql`: Structural SQL query file calculating event count aggregations.
* `traffic_analysis.py`: Main Python event-filtering and visual-plotting engine script.
* `funnel_dropoff_chart.png`: Visual conversion funnel path chart image asset.
* `README.md`: Project documentation blueprint and status file.

**Project Completed By:** HARINI P  
**Role:** Data Analytics Intern  
**Project Track:** Task 3 Evaluation
