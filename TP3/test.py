import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('penguins.csv')

# Drop rows with missing values
df = df.dropna()

# Define colors for each species
species_colors = {'Adelie': 'blue', 'Chinstrap': 'orange', 'Gentoo': 'green'}

# Define marker styles for each sex
sex_markers = {'MALE': '+', 'FEMALE': 'o'}

# Create a 4x4 grid of scatterplots
fig, axes = plt.subplots(4, 4, figsize=(12, 12))

# Define the column names for each line
column_names = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

# Loop through each row (line) and column
for i, y_column in enumerate(column_names):
    for j, x_column in enumerate(column_names):
        # Set the current axis
        ax = axes[i, j]

        # Loop through each species
        for species, color in species_colors.items():
            # Filter data for the current species
            species_data = df[df['species'] == species]

            # Loop through each sex
            for sex, marker in sex_markers.items():
                # Filter data for the current sex
                sex_data = species_data[species_data['sex'] == sex]

                # Plot the scatterplot
                ax.scatter(x=sex_data[x_column], y=sex_data[y_column], label=f'{sex} - {species}', color=color, marker=marker)

        # Set axis labels
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)

# Add legend to the first subplot
axes[0, 0].legend(loc='upper right')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
