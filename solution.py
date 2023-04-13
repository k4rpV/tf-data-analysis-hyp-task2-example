from scipy.stats import anderson_ksamp
import numpy as np

chat_id = 953761952

def solution(x: np.array, y: np.array) -> bool:
    return anderson_ksamp([x, y]).pvalue > 0.08
