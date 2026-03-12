import numpy as np 
from uncertainties import ufloat
from uncertainties import unumpy as unp
from IPython.display import Latex, HTML, Math, display
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
import pandas as pd
from scipy import constants as c
from matplotlib.patches import Rectangle
from matplotlib.ticker import MaxNLocator
from sklearn.metrics import r2_score



def r2_curve_fit(popt, x, y, model_f):
    """
    gives you an r^2 for a given func.

    Input
    popt: parameter from curvefit
    x: x-cord (NDArray)
    y: y-cord (NDArray)
    model_f: function 

    Output
    r2: float
    """
    y_pred = model_f(x, *popt)
    r2 = r2_score(y, y_pred)
    return r2

def linfit(x,a,b):
    return a*x+b