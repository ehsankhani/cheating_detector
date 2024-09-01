import pandas as pd
import matplotlib.pyplot as plt


# Load CSV data
def load_data(file_name):
    df = pd.read_csv(file_name)
    return df


# Calculate the population growth rate
def calculate_growth(df):
    df['Growth'] = df['Population'].pct_change() * 100
    return df


# Plot the population data and growth rate
def plot_data(df):
    plt.figure(figsize=(10, 6))

    # Plot Population
    plt.subplot(2, 1, 1)
    plt.plot(df['Year'], df['Population'], marker='o', linestyle='-')
    plt.title('Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population')

    # Plot Growth Rate
    plt.subplot(2, 1, 2)
    plt.plot(df['Year'], df['Growth'], marker='o', linestyle='-', color='orange')
    plt.title('Population Growth Rate')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')

    plt.tight_layout()
    plt.show()


# Main function to run the steps
def main():
    file_name = "population_data.csv"
    df = load_data(file_name)
    df = calculate_growth(df)
    plot_data(df)


if __name__ == "__main__":
    main()
