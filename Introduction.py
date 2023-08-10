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
This Standard specifies design requirements for bridges with respect to aerodynamic effects, including provisions for wind-tunnel testing.
It supersedes clause 5.3.9 of BS 5400: Part 2(1) and the previous version of this standard BD 49/93. All references to BS 5400: Part 2 are intended to imply the document as implemented by BD 37(2) (DMRB 1.3).
This Standard is applicable to all highway bridges and foot/cycle-track bridges. However its provisions shall only apply to bridges which comply with the constraints outlined herein This Standard specifies design requirements for bridges regarding aerodynamic effects, applicable to highway bridges and foot/cycle-track bridges meeting outlined constraints. Mandatory requirements are highlighted within boxes, while the document also includes advisory content for consideration. Overall, the Standard aims to enhance aerodynamic performance and safety of bridges, ensuring efficiency and reliability.

""")

st.markdown("[DESIGN RULES FOR AERODYNAMIC EFFECTS ON BRIDGES (BD 49/01)](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/bd4901.pdf)")

st.markdown("Files in Jupyter Notebook and Python  are available in GitHub:")
st.markdown("[Calculation notebook (Jupyter Notebook) ](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/Aerodynamic_Excitation-Copy1.ipynb)")
st.markdown("[Aerodynamic effect Python package](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/Aerodynamic_Excitation.py)")

st.markdown(""" :red[The provided Python package, along with the subsequent Streamlit and Jupyter notebook calculation sheets, has been developed to enhance the efficiency of the calculation process.
However, it should be noted that this package may only address certain sections of the document. It is advised to consistently consult the original referenced document and critically evaluate the calculations presented through this package.]""")

st.markdown("""
---
- The program developed by: 		Nam Nguyen & Pedram Manouchehri
- User interface developed by:	Nam Nguyen 
- Independently checked by:		Gonzalo Marinas Sanz
""")
