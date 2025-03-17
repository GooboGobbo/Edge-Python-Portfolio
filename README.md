# 🐍 Python Projects Portfolio

Welcome to my Python projects repository! Here, I showcase interactive applications and data analysis projects built using **Streamlit**, **Pandas**, and other tools. My goal is to turn raw data into meaningful insights while improving my coding skills.

---
# 🏅 2008 Olympic Medalists - Tidy Data Project

## Overview
This project focuses on tidying and visualizing data from the 2008 Olympic Games. The raw dataset contains messy information, requiring data cleaning before meaningful insights can be drawn.

## Data Cleaning Process
- **Melting Data**: Transformed the dataset so each row represents a single athlete's medal in a specific event.
- **Removing Duplicates and Null Values**: Used `.drop_duplicates()` and `.dropna()` to clean missing or redundant data.
- **Data Structuring**: Split the `Event` column into `Gender` and `Event` to separate participation details.
- **Capitalization**: Used `.str.capitalize()` to ensure uniform formatting.

## Visualizations
### 🏆 Medal Count by Event & Gender
- Bar chart displaying medal counts per event, separated by gender.

### ⭐ Athlete Achievements
- Dropdown selection allows users to view an athlete’s medals.

### 🏅 Medalists by Event & Gender
- Users can filter by event and gender to see the top medalists, sorted by medal type.

## Technologies Used
- **Python** (pandas, Streamlit)
- **Data Cleaning & Manipulation**
- **Interactive Visualization**

---

# 🐧 Palmer's Penguins Interactive App

## Overview
This Streamlit app provides an interactive interface for exploring the **Palmer's Penguins** dataset.

## Features
- **Filter by Species**: Select a penguin species to view relevant data.
- **Body Mass Filter**: Use a slider to filter penguins by body mass.

## Technologies Used
- **Python** (pandas, Streamlit)
- **Data Filtering & Display**

## Usage
Simply run the Streamlit app to interactively explore the dataset, filtering by species and body mass.

