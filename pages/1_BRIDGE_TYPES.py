#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:26:38 2023

@author: namnguyen
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import base64
from io import BytesIO
from Aerodynamic_Excitation import *


custom_header()
st.title("Bridge types")
st.image("figures/fig1a.jpeg")
st.image("figures/fig1b.jpeg")