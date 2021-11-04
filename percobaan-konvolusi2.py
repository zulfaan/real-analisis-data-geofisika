# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:58:27 2021

@author: 5_kewajiban
"""
import numpy as np
import matplotlib.pyplot as plt


def ricker(f, length=0.128, dt=0.001):
    t = np.arange(-length / 2, (length - dt) / 2, dt)
    y = (1.0 - 2.0 * (np.pi ** 2) * (f ** 2) * (t ** 2)) * np.exp(-(np.pi ** 2) * (f ** 2) * (t ** 2))
    return t, y

f = 25
t, w = ricker(f)

c = np.convolve(t,w)
plt.plot(c)
plt.show()