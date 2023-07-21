#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:06:38 2023

@author: namnguyen
"""
import streamlit as st 
import pandas as pd
import numpy as np
from sympy import *
from sympy import symbols, Eq, Function,UnevaluatedExpr, Mul
init_printing()
import Aerodynamic_Excitation as AF


#Parameters in the sidebar

st.sidebar.header("Parameters")

bridge_types = ["1", "1A", "2", "3", "3A", "4", "4A", "5", "6"]

bridge_type=st.sidebar.selectbox("bridge_type", options=bridge_types)

motions=["Vertical", "Torsional"]

motion=st.sidebar.selectbox("motion", options=motions)

rho=st.sidebar.number_input('Density of  air rho=', value= 1.226, min_value=0.0, step=0.01, format="%.3f")

b=st.sidebar.number_input("Overall width of the bridge deck $b=$",value= 12.6, min_value=0.0, step=0.2, format="%.2f")

m=st.sidebar.number_input('Mass per unit length of the bridge m=', value= 6306., min_value=0.0, step=1., format="%.2f")

L=st.sidebar.number_input('Length of the relevant maximum spanvof the bridge L=', value= 96.673, min_value=0.0, step=0.1, format="%.3f")


b_0=st.sidebar.number_input('Effective width of the bridge $b^*=$', value=b/2,min_value=0.0, max_value=b, step=0.2, format="%.2f")

d_4=st.sidebar.number_input('Depth of the bridge $d_4$=', value= 3.8, min_value=0.0, step=0.01, format="%.3f")

f_B=st.sidebar.number_input('Natural frequency in bending $f_B$=', value= 1.17, min_value=0.0, step=0.01, format="%.3f")

f_T=st.sidebar.number_input("natural frequency in torsion $f_T=$", value=1.30, min_value=0.0, step=0.1, format="%.2f")

f=st.sidebar.selectbox('$f$ either $f_B$ or $f_T$', options=[f_B,f_T])

V_s=st.sidebar.number_input(' site hourly mean wind speed (10m above ground level) $V_s$=',  min_value=37.0, max_value=40., step=1., format="%.2f")

V_r=st.sidebar.number_input('hourly mean wind speed $V_r$=',  min_value=20.0, max_value=40., step=1., format="%.2f")

V_d=st.sidebar.number_input('the maximum wind gust speed $V_d=$',min_value=V_r, value=50., step=1., format="%.2f")

r=st.sidebar.number_input('polar radius $r=$', value=5.985, min_value=0.0, step=0.5, format="%.3f")

sigma_flm=st.sidebar.number_input("peak stress in the structure per unit $\sigma_{flm}=$",value= 600., min_value=0.0, step=10., format="%.2f")

sigma_c=st.sidebar.number_input(" reference stress $\sigma_{c}=$",value= 80., min_value=0.0, step=2., format="%.2f")


delta_s=st.sidebar.number_input("logarithmic decrement of damping $\delta_s=$", value=0.04, min_value=0.02,max_value=1.0, step=0.01, format="%.3f")

K_1A=st.sidebar.number_input("coefficient $K_{1A}=$",value=1.25, max_value=4.0, step=0.1, format="%.2f")


st.header("Vortex excitation effects")

st.subheader("Amplitudes")

st.markdown(f""" 
			The maximum amplitudes of flexural and torsional vibrations, ymax, shall be obtained for each mode of vibration for each corresponding critical wind speed less than Vr as defined in 2.1.1.3(b).
			The formulae below provide an approximate value to the amplitudes. However if the consequences of such values in the design are significant then wind tunnel tests shall be considered.
			""")
			
text, y_max=AF.y_max_func(bridge_type=bridge_type, motion=motion)
st.write(text)
st.latex(latex(y_max))






