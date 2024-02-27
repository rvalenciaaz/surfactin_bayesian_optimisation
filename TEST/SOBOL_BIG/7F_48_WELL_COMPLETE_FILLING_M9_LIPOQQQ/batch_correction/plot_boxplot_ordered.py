import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = '0_batch_corrected.csv'
data = pd.read_csv(file_path, usecols=['Sample', 'SurfactinC'])

# Extract batch, sample type, and replicate information
data[['Batch', 'SampleType', 'Replicate']] = data['Sample'].str.split('_', expand=True)

# Add a 'Batch_SampleType' column for grouping
data['Batch_SampleType'] = data['Batch'] + '_' + data['SampleType']

# Calculate mean SurfactinC concentration for each 'Batch_SampleType' and sort
mean_concentration = data.groupby('Batch_SampleType')['SurfactinC'].mean().reset_index()
mean_concentration_sorted = mean_concentration.sort_values(by='SurfactinC')['Batch_SampleType']

# Define the color palette
palette = {
    '0': '#0000FF',  # Blue
    '1': '#FF0000',  # Red
    '2': '#77DD77',  # Pastel Green
    '3': '#FDFD96',  # Pastel Yellow
    '4': '#800080',  # Purple
    '5': '#ADD8E6',  # Light Blue
}

# Map each batch to its corresponding color
data['Color'] = data['Batch'].map(lambda x: palette[x])

# Create and adjust the figure for plotting
plt.figure(figsize=(14, 8))
# Plot using the order specified by 'mean_concentration_sorted'
sns.boxplot(x='Batch_SampleType', y='SurfactinC', data=data,
            palette=data.set_index('Batch_SampleType')['Color'].to_dict(),
            order=mean_concentration_sorted)

plt.xticks(rotation=90,fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('Batch_SampleType',fontsize=20)
plt.ylabel('SurfactinC Concentration',fontsize=20)
plt.title('SurfactinC Concentration by Batch and Sample Type Ordered by Mean Concentration',fontsize=20)
plt.tight_layout()

# Saving the plot
save_path = 'surfactinc_concentration_boxplot_ordered.png'
plt.savefig(save_path, dpi=600, transparent=True)
plt.close()  # Close the plot
