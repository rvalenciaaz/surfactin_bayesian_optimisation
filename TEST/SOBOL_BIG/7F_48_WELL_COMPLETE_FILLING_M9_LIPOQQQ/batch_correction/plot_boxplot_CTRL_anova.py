import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

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

# Performing ANOVA
anova_result = stats.f_oneway(*(ctrl_data[ctrl_data['Batch_SampleType'] == bs]['SurfactinC']
                                for bs in ctrl_data['Batch_SampleType'].unique()))

# ANOVA p-value as decimal format
p_value_decimal = "{:.3f}".format(anova_result.pvalue)

# Plotting
plt.figure(figsize=(14, 8))
sns.boxplot(x='Batch_SampleType', y='SurfactinC', data=ctrl_data,
            palette=ctrl_data.set_index('Batch_SampleType')['Color'].to_dict())

plt.xticks(rotation=90, fontsize=12) # Increase tick label size
plt.xlabel('Batch_SampleType', fontsize=14) # Increase label size
plt.ylabel('SurfactinC Concentration', fontsize=14) # Increase label size
plt.title(f'SurfactinC Concentration by Batch and Sample Type (CTRL Only) - ANOVA p-value: {p_value_decimal}', fontsize=16)
plt.tight_layout()

# Optionally, add p-value as text annotation
#plt.text(0.5, max(ctrl_data['SurfactinC']), f'ANOVA p-value: {p_value_decimal}', fontsize=12, ha='center')

# Save the plot
plt.savefig('surfactinc_concentration_ctrl_boxplot.png', dpi=600, transparent=True)
plt.close()
