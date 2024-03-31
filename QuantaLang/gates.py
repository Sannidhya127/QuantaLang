import math
from qubit import *


def hadamard(qubit_obj):
    sqrt2 = math.sqrt(2)
    alpha = (qubit_obj.alpha + qubit_obj.beta) / sqrt2
    beta = (qubit_obj.alpha - qubit_obj.beta) / sqrt2
    return Qubit(alpha, beta)
