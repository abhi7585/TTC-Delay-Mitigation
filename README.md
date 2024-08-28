# TTC Delay Mitigation Project

## Executive Summary

The TTC Delay Mitigation Project, initiated by the Toronto City Council, is a strategic initiative designed to tackle operational challenges within the Toronto Transit Commission (TTC), focusing specifically on bus delays. By leveraging advanced data analysis techniques, this project aims to identify underlying causes of delays and implement targeted solutions. Utilizing a decade of historical bus delay data (2014-2023), the project seeks to enhance transit efficiency, optimize routes, and improve commuter experience. Tools used include Excel, Python, and Power BI for data analysis and visualization.

## Introduction

The Toronto Transit Commission (TTC) is crucial for approximately 1.7 million daily commuters in Toronto and its surrounding areas. However, challenges such as delays in bus services impact both efficiency and public perception of the transit system. The TTC Delay Mitigation Project addresses these challenges using advanced data analytics to improve service delivery and operational effectiveness. The project not only aims to enhance current operations but also provides valuable insights for long-term improvements and sets a precedent for other transit agencies.

## Business Problem Overview

The TTC faces significant operational issues with delays in bus services, which affect commuter experience and system performance. A report by the Toronto Region Board of Trade (TRBOT) indicates an average delay time of 16 minutes, leading to an 18-minute longer waiting time and an on-time percentage of only 57.98%. The project aims to identify and address the root causes of these delays to improve reliability and efficiency.

## Analytics Questions

### a. What are the most frequently occurring incidents in the TTC system?

**Answer:** Descriptive analytics reveal that common incidents include signal failures, inefficiencies within the bus network, emergency services, mechanical issues, and road incidents. This analysis helps in understanding incident patterns and informs decision-making to improve service reliability.

**Problem it will solve:** Identifying patterns in incident occurrences aids in resource allocation, incident management, and enhancing overall system performance.

### b. Why are certain incidents more frequent in specific directions within the TTC system, and what factors contribute to the variation in incident occurrence across different directions?

**Answer:** Diagnostic analytics show that aging infrastructure, higher passenger volumes, and environmental factors contribute to directional variations in incident frequency.

**Problem it will solve:** This analysis helps in reducing risks, improving service performance, and making informed decisions to enhance transportation efficiency.

### c. Why are certain incidents more frequent in specific directions (eastbound, westbound, northbound, southbound) within the TTC system, and how does the delay time associated with these incidents vary across different directions?

**Answer:** Diagnostic analytics identify that vehicle conditions, passenger load, and environmental variables affect the frequency of incidents and delay times in different directions.

**Problem it will solve:** Understanding these variations helps in addressing the underlying causes of directional differences in incidents and delays, leading to more effective strategies for reducing delays and improving system efficiency.

## Scope Statement

### Project Objectives

The TTC Delay Mitigation Project aims to:

- Reduce bus service delays within the TTC by identifying and addressing core causes of delays.
- Optimize bus routes and infrastructure to improve overall network efficiency.
- Enhance the reliability and effectiveness of the bus network, leading to better commuter satisfaction.

## Technologies Used

- **Excel:** For data processing and initial analysis.
- **Python:** For advanced data analysis and automation of data pipelines.
- **Power BI:** For data visualization and dashboard creation.

## Brief Overview of Data Manipulation Process and Data Output

### Data Manipulation Process

1. **Data Import:**
   - Libraries like Pandas, datetime, Seaborn, and Matplotlib were imported for data manipulation and visualization.

2. **Data Acquisition:**
   - Data was sourced from a combined TTC bus delay dataset, created by merging several CSV files downloaded through an official source's API.

3. **Data Cleaning:**
   - **General Cleaning:**
     - Trimmed whitespaces from each cell.
     - Renamed column names for better readability.
     - Converted "Report_Date" to datetime format and created new date, month, and year columns.
     - Removed rows with non-numeric route numbers.
   - **Time-Related Cleaning:**
     - Converted the "Time" column to 24-hour format and extracted hours and minutes.
   - **Location Cleaning:**
     - Cleaned location names (e.g., converting to lowercase, removing special characters).
     - Removed rows with missing location data.
   - **Delay-Related Cleaning:**
     - Removed rows with missing or invalid values in the "Min_Delay" and "Min_Gap" columns.
     - Created a new "Delay_Category" column based on delay duration quartiles.
   - **Incident-Related Cleaning:**
     - Standardized direction codes (North, South, East, West, etc.).
     - Mapped incident descriptions to broader categories using a dictionary.
     - Filled in missing values in "Incident" with "Unknown".
   - **Vehicle Column Removal:**
     - Dropped the "Vehicle" column due to a significant number of missing entries.

4. **Exploratory Data Analysis (EDA):**
   - Generated descriptive statistics from the data.
   - Visualized trends in delays over time using line plots.
   - Analyzed the distribution of delay categories.
   - Examined average delays by day of the week.
   - Created a heatmap to explore average delays by month and year.
   - Identified the most frequent incident types causing delays.
   - Calculated average delay per route and plotted the top 10 routes with the highest average delays.
   - Counted delays by location and visualized the top 10 locations with the most frequent delays.

### Data Output

The data manipulation process resulted in a cleaned and transformed dataset suitable for further analysis. The key outputs include:

- Descriptive statistics summarizing the data.
- Various visualizations, such as time series plots, bar charts, heatmaps, and count plots, revealing patterns and trends in bus delays.
- Identification of common delay causes and locations.
- Insights into routes experiencing the most significant delays.


