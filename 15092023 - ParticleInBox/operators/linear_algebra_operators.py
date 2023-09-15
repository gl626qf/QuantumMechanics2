import numpy as np


def operator_trace(op):
    return np.trace(op)

def conjugate_operator(op):
    return op.dag()
