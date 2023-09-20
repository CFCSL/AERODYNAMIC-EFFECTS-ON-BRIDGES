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
from Aerodynamic_Excitation import *

custom_header()

#Parameters in the sidebar

st.sidebar.header("Global parameters")

bridge_types = ["1", "1A", "2", "3", "3A", "4", "4A", "5", "6"]

bridge_type=st.sidebar.selectbox("Bridge type", options=bridge_types)

rho=st.sidebar.number_input('Density of  air $\\rho [kg/m^3]$ =', value= 1.225, min_value=0.0, step=0.01, format="%.3f")

b=st.sidebar.number_input("Overall width of the bridge deck $b [m] = $",value= 12.6, min_value=0.0, step=0.2, format="%.2f")

m=st.sidebar.number_input('Mass per unit length of the bridge $m [kg/m]= $', value= 6306., min_value=0.0, step=1., format="%.2f")

L=st.sidebar.number_input('Length of the relevant maximum spanvof the bridge $L [m] =$', value= 96.673, min_value=0.0, step=0.1, format="%.3f")

V_r=st.sidebar.number_input('Hourly mean wind speed $V_r [m/s]=$',  min_value=20.0, max_value=40., step=1., format="%.2f")

b_0=st.sidebar.number_input('Effective width of the bridge $b^* [m]= $', value=b/2,min_value=0.0, max_value=b, step=0.2, format="%.2f")

d_4=st.sidebar.number_input('Depth of the bridge $d_4 [m] =$', value= 3.8, min_value=0.0, step=0.01, format="%.3f")

f_B=st.sidebar.number_input('Natural frequency in bending $f_B [Hz]=$', value= 1.17, min_value=0.0, step=0.01, format="%.3f")

f_T=st.sidebar.number_input("Natural frequency in torsion $f_T [Hz]=$", value=1.30, min_value=0.0, step=0.1, format="%.2f")

# =============================================================================
# 
# motions=["Vertical", "Torsional"]
# 
# motion=st.sidebar.selectbox("motion", options=motions)
# 
# rho=st.sidebar.number_input('Density of  air rho=', value= 1.226, min_value=0.0, step=0.01, format="%.3f")
# 
# b=st.sidebar.number_input("Overall width of the bridge deck $b=$",value= 12.6, min_value=0.0, step=0.2, format="%.2f")
# 
# m=st.sidebar.number_input('Mass per unit length of the bridge m=', value= 6306., min_value=0.0, step=1., format="%.2f")
# 
# L=st.sidebar.number_input('Length of the relevant maximum spanvof the bridge L=', value= 96.673, min_value=0.0, step=0.1, format="%.3f")
# 
# V_r=st.sidebar.number_input('hourly mean wind speed $V_r$=',  min_value=20.0, max_value=40., step=1., format="%.2f")
# 
# b_0=st.sidebar.number_input('Effective width of the bridge $b^*=$', value=b/2,min_value=0.0, max_value=b, step=0.2, format="%.2f")
# 
# d_4=st.sidebar.number_input('Depth of the bridge $d_4$=', value= 3.8, min_value=0.0, step=0.01, format="%.3f")
# 
# f_B=st.sidebar.number_input('Natural frequency in bending $f_B$=', value= 1.17, min_value=0.0, step=0.01, format="%.3f")
# 
# f_T=st.sidebar.number_input("natural frequency in torsion $f_T=$", value=1.30, min_value=0.0, step=0.1, format="%.2f")
# 
# =============================================================================


st.header("3.1 Vortex excitation effects")

st.write("If the bridge is found to be susceptible to aerodynamic excitation in accordance with the criteria in 2.1, then the following additional requirements shall be considered (see also 4).")

st.subheader("3.1.1 General")

st.markdown(f"""
Where the bridge cannot be assumed to be aerodynamically stable against vortex excitation in accordance with 2.1.1 above, consideration shall be given to:

(i) the effects of maximum oscillations of any one of the motions considered singly, calculated in accordance with 3.1.2 together with the effects of other coincident loading (see 4);

(ii) fatigue damage, assessed in accordance with 5 summated with damage from other loading.

""")



# =============================================================================
# section_312=st.sidebar.checkbox(f"**3.1.2 Amplitudes**")
# if section_312:
# =============================================================================
st.subheader("3.1.2 Amplitudes")
st.write("The maximum amplitudes of flexural and torsional vibrations, $y_{max}$, shall be obtained for each mode of vibration for each corresponding critical wind speed less than $V_r$ as defined in 2.1.1.3(b). The formulae below provide an approximate value to the amplitudes. However if the consequences of such values in the design are significant then wind tunnel tests shall be considered.")

k=st.sidebar.number_input("The depth of fascia beam or edge slab $k[m]=$",value =1.0,min_value=0.0, step=0.1, format="%.2f")
h=st.sidebar.number_input("Height of bridge parapet or edge member above deck level $h[m]=$",value =5.0,min_value=0.0, step=0.5, format="%.2f")
phi=st.sidebar.number_input("Solidity ratio of parapet $\phi[rad]=$",value =1.0,min_value=0.0, step=0.1, format="%.2f")
delta_s=st.sidebar.number_input("Structural damping expressed as logarithmic decrement $\delta_s=$", value=0.04, min_value=0.02,max_value=1.0, step=0.01, format="%.3f")
r=st.sidebar.number_input('Polar radius of gyration of the effective bridge cross section $r[m]=$', value=5.985, min_value=0.0, step=0.5, format="%.3f")
#delta_s=st.sidebar.number_input("logarithmic decrement of damping $\delta_s=$", value=0.04, min_value=0.02,max_value=1.0, step=0.01, format="%.3f")
#r=st.sidebar.number_input('polar radius $r=$', value=5.985, min_value=0.0, step=0.5, format="%.3f")


motions=["Vertical", "Torsional"]
# 
motion=st.radio("Motion", options=motions)
result =AF.y_max_func(bridge_type=bridge_type, motion=motion)

if isinstance(result, str):
	 # Display the text message
    st.markdown(f"**{result}**")


else:
    # Unpack the tuple and display the equation and text message
    text_message,equation  = result
    st.markdown(f"**{text_message}**")
    st.latex(latex(equation))

st.write("$c$ is amplitude correction factor")	

result =AF.y_max_func(bridge_type=bridge_type, motion=motion, c=AF.c_func())

if isinstance(result, str):

	pass

else:
    # Unpack the tuple and display the equation and text message
    text_message,equation  = result
   # st.markdown(f"**{text_message}**")
    st.latex(latex(equation))
	
result =AF.y_max_func(bridge_type=bridge_type, motion=motion, c=AF.c_func(k=k, h=h, phi=phi, d_4=d_4),b=b, d_4=d_4, rho=rho, m=m, delta_s=delta_s, r=r)
if isinstance(result, str):
	 # Display the text message
    #st.markdown(f"**{result}**")
	pass

else:
    # Unpack the tuple and display the equation and text message
    text_message,equation  = result
   # st.markdown(f"**{text_message}**")
    st.latex(latex(AF.round_equation(equation)))
    st.latex(latex(AF.round_equation(equation.doit()))+f"(m)")
    y_max_val=round(equation.doit().rhs,3)

#%%	
# =============================================================================
# section_313=st.sidebar.checkbox(f"**3.1.3 Assessment of vortex excitation effects**")
# if section_313:
# =============================================================================

st.subheader("3.1.3 Assessment of vortex excitation effects")

st.write("A dynamic sensitivity parameter, $K_D$, shall be derived, as given by:")

K_D=AF.K_D_func(motion=motion)

st.latex(latex(K_D))

# Initialize the options dictionary
#f_options = {f"$f=f_B={f_B}$": f_B, f"$f=f_T={f_T}$": f_T}
f_options = {
   f"In This case, the motion is ${motion}$ and $f =f_B={f_B}$. Therefore the dynamic sensitivity parameter, $K_D$": f_B,
   f"n This case, the motion is ${motion}$ and $ f=f_T={f_T}$. Therefore the dynamic sensitivity parameter, $K_D$": f_T}


#selected_f_key = st.radio( " ",options=list(f_options.keys()))
#selected_f_value = f_options[selected_f_key]

f_B_selected=list(f_options.keys())[0]
f_T_selected=list(f_options.keys())[1]





if motion=="Vertical" and f_B_selected:
	st.write(f_B_selected)
	f = f_B

	try:
		K_D=AF.K_D_func(motion=motion,y_max=y_max_val, f=f)
		
		st.latex(latex(K_D))
		st.latex(latex(AF.round_equation(K_D.doit()))+f"(m/s^2)")
		#st.latex(f"K_D = {K_D:.2f} (m/s^2)")
	
	except:
		st.markdown(f"y_max value is not defined for **bridge types 2, 5 and 6**")






if motion=="Torsional" and f_T_selected:
	st.write(f_T_selected)
	f = f_T

	try:
		K_D=AF.K_D_func(motion=motion,y_max=y_max_val, f=f)
		
		st.latex(latex(K_D))
		st.latex(latex(AF.round_equation(K_D.doit()))+f"(m/s^2)")
		#st.latex(f"K_D = {K_D:.2f} (m/s^2)")
	
	except:
		st.markdown(f"y_max value is not defined for **bridge types 2, 5 and 6**")


