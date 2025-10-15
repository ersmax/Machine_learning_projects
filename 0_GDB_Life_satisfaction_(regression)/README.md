# Life Satisfaction vs GDP per Capita - Linear Regression Analysis

## Overview
This project analyzes the relationship between GDP per capita and life satisfaction across different countries using linear regression.

## Data Source
The dataset is downloaded from the following repository:
https://github.com/ageron/data/raw/main/

The author (Aurélien Geron) proceeded with the data cleansing.
All the efforts for the data collection and pre-processing are attributed to him.

## Project Structure
- `main.py` - Main script containing the LifeSatisfactionAnalyzer class
- `Data/lifeSatisfaction.csv` - Dataset containing GDP per capita and life satisfaction data
- `README.md` - Project documentation

## Features
The `LifeSatisfactionAnalyzer` class provides:
- Data loading from CSV files
- Data visualization with scatter plots
- Linear regression model training
- Life satisfaction predictions based on GDP per capita

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn

## Usage
```python
python main.py
```

The program will:
1. Load the life satisfaction data
2. Train a linear regression model
3. Display a visualization with the fitted line
4. Prompt for GDP per capita input to predict life satisfaction

## Results
The linear regression model shows a positive correlation between GDP per capita and life satisfaction:

![Life Satisfaction vs GDP per Capita](results.png)

The red line represents the fitted linear regression model, showing that as GDP per capita increases, life satisfaction tends to increase as well.

## Model Performance
The model uses a simple linear regression approach to establish the relationship between:
- **X (Independent Variable)**: GDP per capita (USD)
- **Y (Dependent Variable)**: Life satisfaction score

## License
Dataset and preprocessing credits go to Aurélien Geron.

