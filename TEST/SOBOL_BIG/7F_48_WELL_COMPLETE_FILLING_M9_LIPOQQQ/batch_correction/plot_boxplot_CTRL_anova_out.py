import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Load the data
data = pd.read_csv('0_batch_corrected.csv', usecols=['Sample', 'SurfactinC'])
data[['Batch', 'SampleType', 'Replicate']] = data['Sample'].str.split('_', expand=True)
data['Batch_SampleType'] = data['Batch'] + '_' + data['SampleType']
data['Color'] = data['Batch'].map(lambda x: {
    '0': '#0000FF',  # Blue
    '1': '#FF0000',  # Red
    '2': '#77DD77',  # Pastel Green
    '3': '#FDFD96',  # Pastel Yellow
    '4': '#800080',  # Purple
    '5': '#ADD8E6',  # Light Blue
}[x])

# Filtering for CTRL sample type
ctrl_data = data[data['SampleType'] == 'CTRL']

# Remove outliers in 5_CTRL
def remove_outliers(df, group, threshold=1.5):
    group_data = df[df['Batch_SampleType'] == group]
    Q1 = group_data['SurfactinC'].quantile(0.25)
    Q3 = group_data['SurfactinC'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    filtered_df = df.drop(group_data[(group_data['SurfactinC'] < lower_bound) | (group_data['SurfactinC'] > upper_bound)].index)
    return filtered_df

ctrl_data_filtered = remove_outliers(ctrl_data, '5_CTRL')

# ANOVA on filtered data
anova_groups_filtered = ctrl_data_filtered.groupby('Batch_SampleType')['SurfactinC'].apply(list)
anova_result_filtered = f_oneway(*anova_groups_filtered)
p_value_filtered = anova_result_filtered.pvalue

# Plotting
plt.figure(figsize=(14, 8))
sns.boxplot(x='Batch_SampleType', y='SurfactinC', data=ctrl_data_filtered,
            palette=ctrl_data_filtered.set_index('Batch_SampleType')['Color'].to_dict())

plt.xticks(rotation=90, fontsize=12)  # Increase tick label size
plt.xlabel('Batch_SampleType', fontsize=14)  # Increase label size
plt.ylabel('SurfactinC Concentration', fontsize=14)  # Increase label size
plt.title('SurfactinC Concentration by Batch and Sample Type (CTRL Only, Outliers Removed in 5_CTRL)\nANOVA p-value: {:.3f}'.format(p_value_filtered), fontsize=16)

plt.tight_layout()

# Save the plot
plt.savefig('surfactinc_concentration_ctrl_boxplot_filtered.png', dpi=600, transparent=True)
plt.show()  # Show the plot in the output
