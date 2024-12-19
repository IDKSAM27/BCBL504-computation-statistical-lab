# Program to measure central tendency and measures of dispersion: Mean, Median, Mode, Standard Deviattion, Variance, Mean deviation and Quartile deviation for a frequency distribution/data

import numpy as np
import pandas as pd

def calculate_statistics(data, frequencies):
    df = pd.DataFrame({'Value': data, 'Frequency': frequencies})

    total = df['Frequency'].sum()

    df['Weighted_Value'] = df['Value'] * df['Frequency']
    mean = df['Weighted_Value'].sum() / total

    cumulative_frequency = df['Frequency'].cumsum()
    median_index = cumulative_frequency.searchsorted(total / 2)
    median = df['Value'][median_index]

    mode = df['Value'][df['Frequency'].idxmax()]

    variance = np.averag