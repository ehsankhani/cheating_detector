import pandas as pd
import matplotlib.pyplot as plt


# Function to read CSV file into DataFrame
def read_csv_data(filename):
    data = pd.read_csv(filename)
    return data


# Function to compute growth percentage
def compute_growth(dataframe):
    dataframe['GrowthRate'] = dataframe['Population'].pct_change() * 100
    return dataframe


# Function to create plots
def create_plots(dataframe):
    plt.figure(figsize=(10, 6))

    # Plotting the Population data
    plt.subplot(2, 1, 1)
    plt.plot(dataframe['Year'], dataframe['Population'], marker='o', linestyle='-')
    plt.title('Yearly Population')
    plt.xlabel('Year')
    plt.ylabel('Population')

    # Plotting the Growth Rate
    plt.subplot(2, 1, 2)
    plt.plot(dataframe['Year'], dataframe['GrowthRate'], marker='o', linestyle='-', color='orange')
    plt.title('Yearly Population Growth Rate')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')

    plt.tight_layout()
    plt.show()


# Main execution function
def run():
    filename = "population_data.csv"
    dataframe = read_csv_data(filename)
    dataframe = compute_growth(dataframe)
    create_plots(dataframe)


if __name__ == "__main__":
    run()
