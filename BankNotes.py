# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:46:17 2023

@author: pc
"""

from pydantic import BaseModel
class BankNote(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float