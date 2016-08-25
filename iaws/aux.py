# -*- encoding: utf-8 -*-
# Module draw_1D_image
import warnings
import numpy as np

def se2off(Bc):
    Bc2 = Bc.copy()
    center = np.array(Bc.shape)/2
    Bc2[tuple(center)] = 0
    off = np.transpose(Bc2.nonzero()) - center
    return np.ascontiguousarray(off, dtype = np.int32)


