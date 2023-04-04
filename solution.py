import pandas as pd
import numpy as np


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10
    s = np.sum(x)
    teta = s / (len(x) * t)
    
    return teta # Ваш ответ
