import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('0_batch_corrected.csv', usecols=['Sample', 'SurfactinC'])
data[['Batch', 'SampleType', 'Replicate']] = data['Sample'].str.split('_', expand=True)
data['Batch_SampleType'] = data['Batch'] + '_' + data['SampleType']
data['Color'] = data['Batch'].map(lambda x: {
    '0': '#0000FF', # Blue
    '1': '#FF0000', # Red
    '2': '#77DD77', # Pastel Green
    '3': '#FDFD96', # Pastel Yellow
    '4': '#800080', # Purple
    '5': '#ADD8E6', # Light Blue
}[x])

# Filtering for CTRL sample type
ctrl_data = data[data['SampleType'] == 'CTRL']

# Plotting
plt.figure(figsize=(14, 8))
sns.boxplot(x='Batch_SampleType', y='SurfactinC', data=ctrl_data,
            palette=ctrl_data.set_index('Batch_SampleType')['Color'].to_dict())

plt.xticks(rotation=90)
plt.xlabel('Batch_SampleType')
plt.ylabel('SurfactinC Concentration')
plt.title('SurfactinC Concentration by Batch and Sample Type (CTRL Only)')
plt.tight_layout()

# Save the plot
plt.savefig('surfactinc_concentration_ctrl_boxplot.png', dpi=600, transparent=True)
plt.close()
