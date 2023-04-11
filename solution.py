import pandas as pd
import numpy as np
from scipy import stats

chat_id = 620363988 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    res = stats.ttest_ind(x, y)
    return res.pvalue < 0.06
