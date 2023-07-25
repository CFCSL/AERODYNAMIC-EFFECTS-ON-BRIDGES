#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:30:58 2023

@author: namnguyen
"""
import streamlit as st 
import pandas as pd
import numpy as np
from sympy import *
from sympy import symbols, Eq, Function,UnevaluatedExpr, Mul
init_printing()
import Aerodynamic_Excitation as AF


options = [
    "2.1.1 Limited amplitude response - vortex excitation",
    "2.1.2 Limited amplitude response - turbulence",
    "2.1.3 Divergent amplitude response"
]

default_options = [
    "2.1.1 Limited amplitude response - vortex excitation",
    "2.1.2 Limited amplitude response - turbulence",
    "2.1.3 Divergent amplitude response"
]

selected_options = st.sidebar.checkbox("Select options:", options, default=default_options)


#Parameters in the sidebar

st.sidebar.header("Global parameters")

bridge_types = ["1", "1A", "2", "3", "3A", "4", "4A", "5", "6"]

bridge_type=st.sidebar.selectbox("bridge_type", options=bridge_types)

motions=["Vertical", "Torsional"]

motion=st.sidebar.selectbox("motion", options=motions)





# Show the calculations
	
st.header("2.1 Criteria for applicability and consideration of aerodynamic effects")

st.write("The aerodynamic susceptibility parameter, $P_b$")

rho=st.sidebar.number_input('Density of  air rho=', value= 1.226, min_value=0.0, step=0.01, format="%.3f")

b=st.number_input("Overall width of the bridge deck $b=$",value= 12.6, min_value=0.0, step=0.2, format="%.2f")

m=st.number_input('Mass per unit length of the bridge m=', value= 6306., min_value=0.0, step=1., format="%.2f")

L=st.number_input('Length of the relevant maximum spanvof the bridge L=', value= 96.673, min_value=0.0, step=0.1, format="%.3f")

V_r=st.number_input('hourly mean wind speed $V_r$=',  min_value=20.0, max_value=40., step=1., format="%.2f")

f_B=st.number_input('Natural frequency in bending $f_B$=', value= 1.17, min_value=0.0, step=0.01, format="%.3f")



# Calculate P_b using P_func() from All_functions module and display in LaTeX format
P_b1 = AF.P_func()
st.latex(latex(P_b1))

# Calculate P_b using P_func() with specific values and display in LaTeX format
P_b2 = AF.P_func(b=b, rho=rho, m=m, V_r=V_r, L=L, f_B=f_B)
st.latex(latex(P_b2))

# Calculate P_b_value and display it as an equation
P_b = N(P_b2.doit(),3)
st.latex(latex(P_b))



P_b=round(AF.P_func(b=b,rho=rho, m=m, V_r=V_r,L=L,f_B=f_B).doit().rhs,3)

#if P_b<=0.04:
st.write("(a) Bridges designed to carry the loadings specified in BD 37 (DMRB 1.3), built of normal construction, are considered to be subject to insignificant effects in respect of all forms of aerodynamic excitation when $P_b < 0.04.$ However the Rules can still be applied if required, provided the constraints of 2.3 are satisfied.")
	#st.write(AF.Geo_constraints())

#if P_b>0.04 and P_b<1.00:
st.write("(b) Bridges having $0.04 \leq P_b \leq 1.00$ shall be considered to be within the scope of these rules, provided the geometric constraints of 2.3 are satisfied, and shall be considered adequate with regard to each potential type of excitation if they satisfy the relevant criteria given in 2.1.1, 2.1.2 and 2.1.3.")
#st.write(AF.Geo_constraints())
st.write("(c) Bridges with $P_b > 1.00$ shall be considered to be potentially very susceptible to aerodynamic excitation: see 2.2.")






		
if default_options[0] in selected_options :
	st.subheader("2.1.1 Limited amplitude response - vortex excitation")
	st.write("2.1.1.2 Critical wind speeds for vortex excitation")

	b_0=st.number_input('Effective width of the bridge $b^*=$', value=b/2,min_value=0.0, max_value=b, step=0.2, format="%.2f")

	d_4=st.number_input('Depth of the bridge $d_4$=', value= 3.8, min_value=0.0, step=0.01, format="%.3f")



	f_T=st.number_input("natural frequency in torsion $f_T=$", value=1.30, min_value=0.0, step=0.1, format="%.2f")

	f=st.selectbox('$f$ either $f_B$ or $f_T$', options=[f_B,f_T])

	V_cr=latex(AF.V_cr_func(bridge_type=bridge_type))
	st.latex(V_cr)
	V_cr=latex(AF.V_cr_func(bridge_type=bridge_type, b_0=b_0, d_4=d_4, f=f))
	st.latex(V_cr)

	#V_cr=round(AF.V_cr_func(bridge_type=bridge_type, b_0=b_0, d_4=d_4, f=f).doit().rhs,3)
	V_cr=AF.V_cr_func(bridge_type=bridge_type, b_0=b_0, d_4=d_4, f=f).doit()
	st.latex(latex(V_cr))
	V_cr=round(AF.V_cr_func(bridge_type=bridge_type, b_0=b_0, d_4=d_4, f=f).doit().rhs,3)
	
	

	st.write("2.1.1.3 Limiting criteria")

	#if max(f_B,f_T)>5:
	st.write("(a) Any bridge whose fundamental frequency is greater than $5Hz$ shall be considered stable with respect to vortex excitation.")

	V_vs=latex(AF.V_vs_func())
	st.latex(V_vs)
	V_vs=latex(AF.V_vs_func(V_r=V_r))
	st.latex(V_vs)
	V_vs=latex(AF.V_vs_func(V_r=V_r).doit())
	st.latex(V_vs)
	V_vs=round(AF.V_vs_func(V_r=V_r).doit().rhs,3)

	if V_cr>=V_vs:
		st.write(" $V_{cr} \geq V_{vs}$ the bridge is considered stable.")
	else:
		st.warning("Unstable bridge")
		
if default_options[1] in selected_options :
	st.subheader("2.1.2 Limited amplitude response - turbulence")
	#if f>1: 
	st.write("Provided the fundamental frequencies in both bending and torsion calculated in accordance with 2.1.1.2 are greater than 1Hz, the dynamic magnification effects of turbulence may be ignored.")
	#else: 
		
	V_s=st.number_input(' site hourly mean wind speed (10m above ground level) $V_s$=',  min_value=37.0, max_value=40., step=1., format="%.2f")
	sigma_flm=st.number_input("peak stress in the structure per unit $\sigma_{flm}=$",value= 600., min_value=0.0, step=10., format="%.2f")
	sigma_c=st.number_input(" reference stress $\sigma_{c}=$",value= 80., min_value=0.0, step=2., format="%.2f")

		

	P_T=latex(AF.P_T_func())
	st.latex(P_T)
	P_T=latex(AF.P_T_func(b=b,rho=rho, m=m, V_s=V_s,f_B=f_B, sigma_flm=sigma_flm, sigma_c=sigma_c))
	st.latex(P_T)
	P_T=AF.round_equation( AF.P_T_func(b=b,rho=rho, m=m, V_s=V_s,f_B=f_B, sigma_flm=sigma_flm, sigma_c=sigma_c).doit(),3)
	st.latex(latex(P_T))
	P_T_value=AF.P_T_func(b=b,rho=rho, m=m, V_s=V_s,f_B=f_B, sigma_flm=sigma_flm, sigma_c=sigma_c).doit().rhs
	#if P_T_value<=1.0:
	st.write("The dynamic magnification effects of turbulence may also be neglected for $P_T \leq 1.0$")
	

		
if default_options[0] in selected_options :
	st.subheader("2.1.3 Divergent amplitude response")
	st.write("2.1.3.2 Galloping and stall flutter")
	st.markdown(f"""
			 (a) Vertical motion
			 Vertical motion need be considered only for bridges of types 3, 3A, 4 and 4A as shown in Figure 1, and only if b < 4d4.
			 Provided the constraints (i) to (iii) in 2.3 are satisfied Vg shall be calculated from the reduced velocity, VRg, using the formula below:
				 
			 (b) Torsional motion
			 Torsional motion shall be considered for all bridge types. Provided the fascia beams and parapets comply with the constraints given in 2.3, then Vg shall be taken as:
			 
			 
			 """)

	V_g_0=latex(AF.V_g_func_0(bridge_type,motion))
	st.latex(V_g_0)
	
	delta_s=st.number_input("logarithmic decrement of damping $\delta_s=$", value=0.04, min_value=0.02,max_value=1.0, step=0.01, format="%.3f")

	V_g=AF.round_equation(AF.V_g_func(bridge_type, motion, b=b, b_0=b_0, m=m, rho=rho, d_4=d_4, f_B=f_B, f_T=f_T, delta_s=delta_s),2)
	st.latex(latex(V_g))

	st.write("2.1.3.3 Classical flutter")
	V_f=latex(AF.V_f_func())
	st.latex(V_f)
	st.write("Where")
	r=st.number_input('polar radius $r=$', value=5.985, min_value=0.0, step=0.5, format="%.3f")
	V_Rf=latex(AF.V_Rf_func())
	st.latex(V_Rf)
	V_Rf=latex(AF.V_Rf_func(f_B=f_B, f_T=f_T, m=m, r=r, rho=rho,b=b))
	st.latex(V_Rf)
	V_Rf=AF.round_equation((AF.V_Rf_func(f_B=f_B, f_T=f_T, m=m, r=r, rho=rho,b=b).doit()),2)
	st.latex(latex(V_Rf))
	V_Rf_value=AF.V_Rf_func(f_B=f_B, f_T=f_T, m=m, r=r, rho=rho,b=b).doit().rhs
	if V_Rf_value<2.5:
		st.write("$V_{Rf}$ is not less than $2.5$. If $V_{Rf} \leq 2.5$ then the value  $2.5$ is taken")
		V_Rf_value=2.5
		V_f=latex(AF.V_f_func(V_Rf=V_Rf_value,f_T=f_T,b=b))
		st.latex(V_f)
		V_f=latex(AF.V_f_func(V_Rf=V_Rf_value,f_T=f_T,b=b).doit())
		st.latex(V_f)
		
	else:
		V_f=latex(AF.V_f_func(V_Rf=V_Rf_value,f_T=f_T,b=b))
		st.latex(V_f)
		V_f=latex(AF.V_f_func(V_Rf=V_Rf_value,f_T=f_T,b=b).doit())
		st.latex(V_f)
		
		st.write('2.1.3.4 Limiting criteria')
		
		st.write("The bridge shall be shown to be stable with respect to divergent amplitude response in wind storms up to wind speed $V_{WO}$, given by:")

		
		K_1A=st.sidebar.number_input("coefficient $K_{1A}=$",value=1.25, max_value=4.0, step=0.1, format="%.2f")

		V_d=st.sidebar.number_input('the maximum wind gust speed $V_d=$',min_value=V_r, value=50., step=1., format="%.2f")
		
		
		
		
		V_WO=latex(AF.V_WO_func())
		st.latex(V_WO)
		V_WO=latex(AF.V_WO_func(V_r=V_r, V_d=V_d, K_1A=K_1A))
		st.latex(V_WO)
		V_WO=AF.round_equation((AF.V_WO_func(V_r=V_r, V_d=V_d, K_1A=K_1A).doit()),2)
		st.latex(latex(V_WO))
	





