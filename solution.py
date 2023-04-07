import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Рассчитываем значение K-S статистики и p-значение
    stat, p_value = ks_2samp(x, y)
    # Находим критическое значение для уровня значимости 0.06 и размера выборки
    critical_value = 1.36 / np.sqrt(len(x) + len(y))
    # Сравниваем значение K-S статистики с критическим значением
    return stat < critical_value
