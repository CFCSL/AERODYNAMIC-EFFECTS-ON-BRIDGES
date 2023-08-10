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

st.markdown("""The calculation notebook, founded upon the British Standard (DESIGN MANUAL FOR ROADS AND BRIDGES - BD 49/01), serves the purpose of evaluating the aerodynamic impact on bridges and determining the bridge's vulnerability to wind-induced vibrations.
The provided Python package, coupled with the subsequent Streamlit and Jupyter notebook calculation resources, has been devised to simplify the calculation procedure. :red[Nonetheless, it is important to acknowledge that this package may solely address specific sections of the document. It is strongly recommended to consistently consult the original referenced document and critically assess the calculations presented by means of this package.]""")

st.markdown("""
the package is based on :
['DESIGN RULES FOR AERODYNAMIC EFFECTS ON BRIDGES (BD 49/01)'](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/bd4901.pdf)""")

st.markdown("""---
:bold[you can access the following to run your calculation in a more relaxed format by directly running the package locally]""")

st.markdown("Files in Jupyter Notebook and Python  are available in GitHub:")
st.markdown("[Calculation notebook (Jupyter Notebook) ](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/Aerodynamic_Excitation-Copy1.ipynb)")
st.markdown("[Aerodynamic effect Python package](https://github.com/CFCSL/AERODYNAMIC-EFFECTS-ON-BRIDGES/blob/main/Aerodynamic_Excitation.py)")

st.markdown("""---
:red[The provided Python package, along with the subsequent Streamlit and Jupyter Notebook calculation sheets, has been developed to enhance the efficiency of the calculation process.
However, it should be noted that this package may only address certain sections of the document. It is advised to consistently consult the original referenced document and critically evaluate the calculations presented through this package.]""")

st.markdown("""
---
- The program developed by: 		Nam Nguyen & Pedram Manouchehri
- User interface developed by:	Nam Nguyen 
- Independently checked by:		Gonzalo Marinas Sanz
""")
