from scipy.stats import cramervonmises_2samp
import numpy as np

chat_id = 953761952

def solution(x: np.array, y: np.array) -> bool:
    return cramervonmises_2samp(x, y).pvalue < 0.08
