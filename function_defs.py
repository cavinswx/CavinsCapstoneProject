import numpy as np
from matplotlib import pyplot as plt
import metpy
import scipy
import xarray as xr

def jet_occurrence_Oliviera(wind_u, wind_v):
    if wind_u>3:
        return True
    elif len(np.where(abs(wind_v) > abs(wind_u))) > 0:
        return False
    else:
        return False
    
def jet_occurence_Sasaki(wind_u, wind_v):
    if wind_u>3:
        return True
    else:
        return False


