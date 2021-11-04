# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:09:17 2021

@author: Zulfa Nurfajar
"""
import numpy as np
import matplotlib.pyplot as plt


#membaca data gempa
data_read = np.genfromtxt('Data-gempa-padang.txt', skip_header=1, delimiter=',')


#menghitung ricker
def ricker(f, length=0.128, dt=0.001):
    t = np.arange(-length / 2, (length - dt) / 2, dt)
    y = (1.0 - 2.0 * (np.pi ** 2) * (f ** 2) * (t ** 2)) * np.exp(-(np.pi ** 2) * (f ** 2) * (t ** 2))
    return t, y

f = 25
b = np.ravel(ricker(f))

c = np.convolve(data_read,b)
plt.plot(c)
plt.show()