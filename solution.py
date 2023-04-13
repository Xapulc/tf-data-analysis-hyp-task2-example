import pandas as pd
import numpy as np


chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    crit = 0.05
    t, p = ttest_ind(x,y)
    return (not(p < crit))
