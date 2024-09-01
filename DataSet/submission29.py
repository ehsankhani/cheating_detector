import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate population data
def generate_population_dataset(num_years):
    year_range = np.arange(2000, 2000 + num_years)
    population_values = 300000000 + np.cumsum(np.random.normal(1000000, 500000, num_years))
    return pd.DataFrame({'Year': year_range, 'Population': population_values})

# Function to compute the moving average
def moving_average(data_frame, window):
    return data_frame['Population'].rolling(window=window).mean()

# Function to visualize population trends
def visualize_population(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Year'], data['Population'], label='Population')
    plt.plot(data['Year'], moving_average(data, 5), label='5-Year Moving Avg', linestyle='--')
    plt.title('Population Trends with Moving Average')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()

# Main execution flow
if __name__ == "__main__":
    population_data = generate_population_dataset(20)
    visualize_population(population_data)
