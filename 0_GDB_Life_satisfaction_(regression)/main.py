import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class LifeSatisfactionAnalyzer:
    """A class to analyze the relationship between 
    GDP per capita and life satisfaction.
    """
    def __init__(self, data_path):
        """
        Precondition: data_path is a valid path to a CSV file
        Postcondition: Initializes the analyzer with data from the CSV file.
        """
        self.data_path = data_path
        self.life_satisfaction = None
        self.x = None
        self.y = None
        self.model = None
    
    def load_data(self):
        """"
        Precondition: self.data_path is a valid path to a CSV file
        Postcondition: Loads data from the CSV file into a DataFrame.
        """
        self.life_satisfaction = pd.read_csv(self.data_path)
        self.x = self.life_satisfaction[["GDP per capita (USD)"]].values
        self.y = self.life_satisfaction[["Life satisfaction"]].values
        print(f"Data successfully loaded. Shape: {self.life_satisfaction.shape}")
        
    def visualize_data(self):
        """
        Precondition: self.life_satisfaction is not None
        Postcondition: Displays a scatter plot of GDP per capita vs Life satisfaction.
        """
        if self.life_satisfaction is None:
            raise ValueError("Data not loaded. Please call load_data() first.")
        self.life_satisfaction.plot(kind="scatter", 
                                    grid=True,
                                    x="GDP per capita (USD)", 
                                    y="Life satisfaction")
        plt.title("Life Satisfaction vs GDP per Capita")
        if self.model is not None:
            x_min = self.x.min()
            x_max = self.x.max()
            x_line = np.linspace(x_min, x_max, 100)
            y_line = self.model.predict(x_line.reshape(-1, 1))
            plt.plot(x_line, y_line, color='red', linewidth=2, label='Fit Line')
            plt.legend()
            
        plt.show()
        
    def select_train_model(self):
        """
        Precondition: self.x and self.y are not None
        Postcondition: Trains a linear regression model on the data.
        """
        if self.x is None or self.y is None:
            raise ValueError("Data not loaded. Please call load_data() first.")
        self.model = LinearRegression()
        self.model.fit(self.x, self.y)
        print("Model trained successfully.")
            
    def predict(self, gdp_per_capita):
        """
        Precondition: self.model is not None and gdp_per_capita is a float
        Postcondition: Returns the predicted life satisfaction for the given GDP per capita.
        """
        if self.model is None:
            raise ValueError("Model not trained. Please call select_train_model() first.")
        prediction = self.model.predict([[gdp_per_capita]])
        return prediction[0][0]

def main():
    data_path = "./Data/lifeSatisfaction.csv"
    analyzer = LifeSatisfactionAnalyzer(data_path)
    analyzer.load_data()
    analyzer.select_train_model()
    analyzer.visualize_data()  
    predict = float(input("Enter a GDP per capita value to predict life satisfaction: "))
    predicted_value = analyzer.predict(predict)
    print(f"Predicted life satisfaction for GDP per capita {predict}: {predicted_value:.2f}")
    
if __name__ == "__main__":
    main()