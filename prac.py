import numpy as np 
import pandas as pd

def calculate_statistics(data, frequencies):
    df = pd.DataFrame({'Value': data, 'Frequency': frequencies})

    