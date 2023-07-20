#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:27:34 2023

@author: namnguyen
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import base64
from io import BytesIO
import Aerodynamic_Excitation as AF

st.header(" DESIGN RULES FOR AERODYNAMIC EFFECTS ON BRIDGES")


st.markdown("""

This Standard specifies design requirements for bridges regarding aerodynamic effects, applicable to highway bridges and foot/cycle-track bridges meeting outlined constraints. Mandatory requirements are highlighted within boxes, while the document also includes advisory content for consideration. Overall, the Standard aims to enhance aerodynamic performance and safety of bridges, ensuring efficiency and reliability.

""")

st.markdown("[Click here to see PDF document](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/bd4901.pdf)")


st.image("figures/fig1a.jpeg")
st.image("figures/fig1b.jpeg")



st.markdown("""
---
- The program developed by: 		Pedram Manouchehri & Nam Nguyen 
- User interface developed by:	Nam Nguyen 
- Independently Checked by:		
""")