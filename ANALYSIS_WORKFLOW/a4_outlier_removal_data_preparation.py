import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.integrate import trapezoid
from functools import reduce

def remove_outliers(df):
    q1 = df['integral'].quantile(0.25)
    q3 = df['integral'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    return df[(df['integral'] >= lower_bound) & (df['integral'] <= upper_bound)]