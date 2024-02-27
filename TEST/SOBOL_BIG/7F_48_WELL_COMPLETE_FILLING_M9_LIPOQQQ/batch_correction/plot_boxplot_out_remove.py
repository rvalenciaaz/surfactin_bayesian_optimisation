import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('0_batch_corrected.csv', usecols=['Sample', 'SurfactinC'])

# Extract batch, sample type, and replicate information
data[['Batch', 'SampleType', 'Replicate']] = data['Sample'].str.split('_', expand=True)
data['Batch_SampleType'] = data['Batch'] + '_' + data['SampleType']

# Define color palette
palette = {
    '0': '#0000FF',  # Blue
    '1': '#FF0000',  # Red
    '2': '#77DD77',  # Pastel Green
    '3': '#FDFD96',  # Pastel Yellow
    '4': '#800080',  # Purple
    '5': '#ADD8E6',  # Light Blue
}

# Map each unique batch to a color
data['Color'] = data['Batch'].map(lambda x: palette[x])

# Function to remove one outlier per box if needed
def remove_one_outlier_per_box(group):
    q1 = group['SurfactinC'].quantile(0.25)
    q3 = group['SurfactinC'].quantile(0.75)
    iqr = q3 - q1
    outlier_threshold_upper = q3 + 1.5 * iqr
    outlier_threshold_lower = q1 - 1.5 * iqr
    outliers = group[(group['SurfactinC'] > outlier_threshold_upper) | (group['SurfactinC'] < outlier_threshold_lower)]
    if not outliers.empty:
        outlier_to_remove = outliers.sample(n=1)
        return group.drop(outlier_to_remove.index)
    return group

# Apply function to remove one outlier per box if needed
data = data.groupby('Batch_SampleType', group_keys=False).apply(remove_one_outlier_per_box)

# Plotting
plt.figure(figsize=(14, 8))
sns.boxplot(x='Batch_SampleType', y='SurfactinC', data=data,
            palette=data.set_index('Batch_SampleType')['Color'].to_dict())

plt.xticks(rotation=90)
plt.xlabel('Batch_SampleType')
plt.ylabel('SurfactinC Concentration')
plt.title('SurfactinC Concentration by Batch and Sample Type')
plt.tight_layout()

# Save the plot
file_path = 'surfactinc_concentration_boxplot_out_remove.png'
plt.savefig(file_path, dpi=600, transparent=True)
plt.close()  # Close the plot

print(f'Plot saved to {file_path}')
