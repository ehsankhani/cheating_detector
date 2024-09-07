import pandas as pd
import matplotlib.pyplot as plt


# Function to load the CSV dataset
def import_data(file_path):
    data_frame = pd.read_csv(file_path)
    return data_frame


# Function to compute the population growth rate
def compute_growth_rate(data_frame):
    data_frame['GrowthRate'] = data_frame['Population'].pct_change() * 100
    return data_frame


# Function to visualize the population data and growth rate
def visualize_data(data_frame):
    plt.figure(figsize=(10, 6))

    # Plot Population
    plt.subplot(2, 1, 1)
    plt.plot(data_frame['Year'], data_frame['Population'], marker='o', linestyle='-')
    plt.title('Population Trend Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population')

    # Plot Growth Rate
    plt.subplot(2, 1, 2)
    plt.plot(data_frame['Year'], data_frame['GrowthRate'], marker='o', linestyle='-', color='orange')
    plt.title('Population Growth Rate Over Time')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')

    plt.tight_layout()
    plt.show()


# Primary function to execute the process
def execute():
    file_path = "population_data.csv"
    data_frame = import_data(file_path)
    data_frame = compute_growth_rate(data_frame)
    visualize_data(data_frame)


if __name__ == "__main__":
    execute()
