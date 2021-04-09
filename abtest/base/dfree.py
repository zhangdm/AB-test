# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def dfree(stda,stdb,stdab,na,nb):
    free = np.power(stdab, 4) / (np.power(stda / np.sqrt(na), 4) / (na - 1) + np.power(stdb / np.sqrt(nb), 4) / (nb - 1))
    return free

