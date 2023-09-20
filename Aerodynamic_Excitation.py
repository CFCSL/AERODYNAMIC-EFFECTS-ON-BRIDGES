#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:08:46 2023

@author: namnguyen
"""
from sympy import symbols, Eq, Function,UnevaluatedExpr, Mul
from sympy import *
from sympy import N
init_printing()
from sympy import Piecewise, nan
import numpy as np
import streamlit as st
import os

current_path= os.getcwd()

def custom_header():
	t1, t2 = st.columns((1, 1))
	
	#logo_path = "figures/cfc_logo.png"
	#logo_path = "figures/CFC_LOGO_20220510_blanco.png"
	logo_path = "figures/CFC_LOGO_20220510_Negro_jpeg.jpg"

	# Display the image from the URL with a specified width
	t1.image(logo_path, width=300)
	t2.markdown("")
	t2.markdown("")
	t2.markdown("")

	t1.markdown(f"[https://www.cfcsl.com/](https://www.cfcsl.com)")








def round_expr(expr, num_digits=3):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(Number)})

def round_equation(eq, num_digits=3):
    lhs = eq.lhs
    rhs = eq.rhs
    rounded_rhs = round_expr(rhs, num_digits)
    return Eq(lhs, rounded_rhs)


def Geo_Constraints():
	text="""
		2.3 Geometric constraints
	
		For applicability of the reduced velocities for
		divergent amplitude response (2.1.3.2) and the
		vortex shedding maximum amplitude derivation
		(3.1), the following constraints shall be satisfied:
			
		(i)  Solid edge members, such as fascia beams
		and solid parapets shall have a total depth
		less than $0.2d_4$ unless positioned closer than
		$0.5d_4$ from the outer girder when they shall
		not protrude above the deck by more than
		$0.2d_4$ nor below the deck by more than
		$0.5d_4$. In defining such edge members, edge
		stiffening of the slab to a depth of $0.5$ times
		the slab thickness may be ignored.
		
		(ii)  Other edge members such as parapets,
		barriers, etc., shall have a height above deck
		level, $h$, and a solidity ratio, $\phi$, such that $\phi$ is
		less than $0.5$ and the product $h\phi$ is less than
		$0.35d_4$ for the effective edge member. The
		value of $\phi$ may exceed $0.5$ over short
		lengths of parapet, provided that the total
		length projected onto the bridge centre-line
		of both the upwind and downwind portions
		of parapet whose solidity ratio exceeds $0.5$
		does not exceed 30% of the bridge span.
		
		(iii)  Any central median barrier shall have a
		shadow area in elevation per metre length
		less than $0.5m^2$. Kerbs or upstands greater
		than $100mm$ deep shall be considered as
		part of this constraint by treating as a solid
		bluff depth; where less than $100mm$ the
		depth shall be neglected, see Figure 2.
		
		In the above, $d_4$ is the reference depth of the bridge
		deck (see Figures 1 and 2). Where the depth is
		variable over the span, $d_4$ shall be taken as the
		average value over the middle third of the longest
		span.
			"""
	return text
	
	




#%%
## 2.1 Criteria for applicability and consideration of aerodynamic effects
# Define the symbols
b = symbols('b')
m = symbols('m')
rho = symbols('rho')
V_r = symbols('V_r')
L = symbols('L')
f_B = symbols('f_B')

P = symbols('P', cls=Function)(b)
def P_func(b=b,rho=rho, m=m, V_r=V_r,L=L,f_B=f_B):
	b=UnevaluatedExpr(b)
	rho=UnevaluatedExpr(rho)
	m=UnevaluatedExpr(m)  
	V_r=UnevaluatedExpr(V_r)
	L=UnevaluatedExpr(L)
	f_B=UnevaluatedExpr(f_B)    


	#return Eq(P, ((rho * b**2 / m)) * (16 * V_r**2 / (b * L * f_b**2)))
	return Eq(P,Mul(  ((rho * b**2) / m) , (16 * V_r**2) / (b * L * f_B**2),evaluate=False))

#%%

#### 2.1.1.2 Criticalwindspeedsforvortex excitation

# Calculate V_cr

# Define the bridge types:
bridge_types = ["1", "1A","2", "3", "3A", "4", "4A", "5", "6"]

# Define the symbols
V_cr = symbols('V_cr')
f_T = symbols('f_T')
b_0 = symbols('b_0')
d_4 = symbols('d_4')
f = symbols('f')
r = symbols('r')
bt = symbols('bt')

def V_cr_func(bridge_type, b_0=b_0, d_4=d_4, f=f):
# =============================================================================
#     b_0=UnevaluatedExpr(b_0)
#     d_4=UnevaluatedExpr(d_4)
#     f=UnevaluatedExpr(f)
#     
# =============================================================================
    r = N(b_0 / d_4,3)
    r=UnevaluatedExpr(r)
    val = Piecewise(
        (N(6.5 * f * d_4,4), (r <= 5) & (bridge_type in bridge_types)),
        (N(f * d_4 * (1.1 * b_0 / d_4 + 1),4), (r > 5) & (r < 10) & (bridge_type in ["1", "1A", "3", "3A", "4", "4A"])),
        (N(f * d_4 * (0.7 * b_0 / d_4 + 3),4), (r > 5) & (r < 10) & (bridge_type in ["2", "5", "6"])),
        (N(12 * f * d_4,4), (r >= 10) & (bridge_type in ["1", "1A", "3", "3A", "4", "4A"])),
        (N(10 * f * d_4,4), (r >= 10) & (bridge_type in ["2", "5", "6"])),
        (0, True)  # default value when none of the conditions are met
    )

    return Eq(V_cr, val)


#%%
#### 2.1.1.3 Limiting criteria
# define the symbols 
V_vs= symbols('V_vs')
def V_vs_func(V_r=V_r):
    V_r=UnevaluatedExpr(V_r)
    #V_vs=UnevaluatedExpr(V_vs)
    val=1.25*V_r
    return Eq(V_vs, val, evaluate=False)

#%%
### 2.1.2 Limited amplitude response - turbulence

# Define the symbols
V_s = symbols('V_s')
sigma_flm=symbols('sigma_flm')
sigma_c=symbols('sigma_c')
P_T = symbols('P_T', cls=Function)(b)

# Define the equation

def P_T_func(b=b,rho=rho, m=m, V_s=V_s,f_B=f_B, sigma_flm=sigma_flm, sigma_c=sigma_c):

    # Make x an UnevaluatedExpr
    b=UnevaluatedExpr(b)
    rho=UnevaluatedExpr(rho)
    m=UnevaluatedExpr(m)  
    V_s=UnevaluatedExpr(V_s)
    sigma_flm=UnevaluatedExpr(sigma_flm)
    sigma_c=UnevaluatedExpr(sigma_c)    
    

    return round_equation(Eq(P_T,Mul( Mul(((rho * b**2) / m) , (V_s / (N(f_B,2)*b))**2, evaluate=False),((sigma_flm*b)/sigma_c),evaluate=False)),3)







from sympy import Piecewise, Eq, symbols, Min

C_g,V_g, V_Rg, f_B, f_T, b, d_4 , delta_s,rho,b_0 = symbols('C_g V_g V_Rg f_B f_T b d_4 delta_s rho b_0')




#%%


def V_g_Vertical_func(bridge_type, motion="Vertical",V_Rg=V_Rg, f_B=f_B, d_4=d_4):
	V_Rg=UnevaluatedExpr(V_Rg)
	f_B=UnevaluatedExpr(f_B)
	d_4=UnevaluatedExpr(d_4)
	if bridge_type in ["3", "3A", "4", "4A"]:
		val=V_Rg*f_B*d_4
	else:
		val= float('nan')
	return Eq(V_g,val, evaluate= False)



def V_Rg_func(C_g=C_g, m=m, delta_s=delta_s, rho=rho, d_4=d_4):

	C_g = UnevaluatedExpr(C_g)
	delta_s = UnevaluatedExpr(delta_s)
	rho=UnevaluatedExpr(rho)
	d_4 = UnevaluatedExpr(d_4)
	result=(C_g*m*delta_s)/(rho*d_4**2)

	return  Eq(V_Rg, result, evaluate=False)



def C_g_func(bridge_type, b=b, b_0=b_0, d_4=d_4):
	b=float(b)
	b_0=float(b)
	overhang = (b - b_0) / 2
	if bridge_type in ["3", "4"] and overhang >= 0.7 * d_4:
		val=2.0
	if bridge_type in ["3", "3A", "4", "4A"] and overhang < 0.7 * d_4:
		val=1.0
	return  val#Eq(C_g, val, evaluate=False)


#%%

def V_g_func_0(bridge_type,motion, V_Rg=V_Rg, f_B=f_B, f_T=f_T,b=b, d_4=d_4):
    
    V_Rg=UnevaluatedExpr(V_Rg)
    f_B=UnevaluatedExpr(f_B)
    f_T=UnevaluatedExpr(f_T)
    b=UnevaluatedExpr(b)
    d_4=UnevaluatedExpr(d_4)
    if bridge_type in ["1","1A","2","5","6"]:
        if motion=="Torsional":
            val=3.3*f_T
        if motion=="Vertical":
            val=float("nan")
    else:
        if motion=="Vertical":
            
            val=V_Rg * f_B * d_4
        else:
            val3=Min(5.5*f_T*b, 12*f_T*d_4)
            val4=5.5*f_T*b
            
            cond3=(b<4*d_4)
            cond4=(b>=4*d_4)
            
            val=Piecewise((val3,cond3), (val4, cond4))
    
    return Eq(V_g,val, evaluate=False)

#%%
def V_g_func(bridge_type, motion, b=b, b_0=b_0, m=m, rho=rho, d_4=d_4, f_B=f_B, f_T=f_T, delta_s=delta_s):


    b = float(b)
    b_0 = float(b_0)

    if bridge_type in ["1", "1A", "2", "5", "6"]:
        if motion == "Torsional":
            val = 3.3 * f_T
        if motion == "Vertical":
            val = float("nan")
    if bridge_type in ["3", "3A", "4", "4A"]:
        if motion == "Vertical":
            C_g=C_g_func(bridge_type, b=b, b_0=b_0, d_4=d_4)
      
            V_Rg=V_Rg_func(C_g=C_g, m=m, delta_s=delta_s, rho=rho, d_4=d_4).doit().rhs
            val=V_Rg * f_B * d_4


        if motion == "Torsional":
            val3 = Min(5.5 * f_T * b, 12 * f_T * d_4)
            val4 = 5.5 * f_T * b
            
            cond3 = (b < 4 * d_4)
            cond4 = (b >= 4 * d_4)
            
            val = Piecewise((val3, cond3), (val4, cond4))

    return Eq(V_g, val, evaluate=False)



#%%
#### 2.1.3.3 Classical flutter

# define the symbols:

V_Rf =symbols('V_Rf')
V_f=symbols('V_f')
r=symbols('r')



def V_f_func(V_Rf=V_Rf,f_T=f_T,b=b):
    V_Rf=UnevaluatedExpr(V_Rf)
    val=round_expr(V_Rf*f_T*b,2)
    return Eq(V_f,val)


def V_Rf_func(f_B=f_B, f_T=f_T, m=m, r=r, rho=rho,b=b):
    f_B=UnevaluatedExpr(f_B)
    f_T=UnevaluatedExpr(f_T)
    f_B=UnevaluatedExpr(f_B)
    m=UnevaluatedExpr(m)
    r=UnevaluatedExpr(r)
    rho=UnevaluatedExpr(rho)
    b=UnevaluatedExpr(b)
    
    a1=(1-1.1*(f_B/f_T)**2)#**(1/2)
    a2=Pow(a1,(1/2), evaluate=False)
    val=round_expr(1.8*a2*((m*r)/(rho*b**3))**(1/2),2)
   
    return Eq(V_Rf,val)
    
##2.1.3.4 Limiting criteria

# define the symbols
V_WO= symbols('V_WO')
V_d=symbols('V_d')
K_1A=symbols('K_1A')

def V_WO_func(V_r=V_r, V_d=V_d, K_1A=K_1A):
    V_r=UnevaluatedExpr(V_r)
    V_d=UnevaluatedExpr(V_d)
    K_1A=UnevaluatedExpr(K_1A)
    
    val= round_expr((1.1/3)*(V_r+2*V_d)*K_1A,2)
    return Eq(V_WO,val,evaluate=False)


#%%


from sympy import symbols, Eq

# Define the symbols
c = symbols("c")
r = symbols("r")
y_max = symbols("y_max")
k, h, phi, d_4 = symbols('k h phi d_4')

def c_func(k=k, h=h, phi=phi, d_4=d_4):
    return 3 * (k + h * phi) / d_4

def y_max_func(bridge_type, motion, c=c, b=b, d_4=d_4, rho=rho, m=m, delta_s=delta_s, r=r):
    c=UnevaluatedExpr(c)
    b=UnevaluatedExpr(b)
    d_4=UnevaluatedExpr(d_4)
    rho=UnevaluatedExpr(rho)
    m=UnevaluatedExpr(m)  
    delta_s=UnevaluatedExpr(delta_s)
    r=UnevaluatedExpr(r)

	
    bridge_types = ["1", "1A", "2", "3", "3A", "4", "4A", "5", "6"]
	
    text1 = "For vertical flexural vibrations and for bridge types 1 to 6"
    text3 = "y_max may be ignored for torsional vibrations for bridge types 2, 5 and 6"
    text2 = "For torsional vibrations and for bridge types 1, 1A, 3, 3A, 4 and 4A"
	
    val1 = (c * b**0.5 * d_4**2.5 * rho) / (4 * m * delta_s)
    val2 = (c * b**1.5 * d_4**3.5 * rho) / (8 * m * r**2 * delta_s)
    val3 = None

    cond1 = (bridge_type in bridge_types) and (motion == "Vertical")
    cond2 = (bridge_type in ["1", "1A", "3", "3A", "4", "4A"]) and (motion == "Torsional")
    cond3 = (bridge_type in ["2", "5", "6"]) and (motion == "Torsional")
    
    # Calculate c based on the provided values or the function c_func if c is a symbol
    if c == symbols('c'):
        if cond1:
            val = val1
            text_message = text1
        elif cond2:
            val = val2
            text_message = text2
        elif cond3:
            return text3
        return text_message, Eq(y_max, val, evaluate=False)
    else:
        c = c_func(k, h, phi, d_4)
        if cond1:
            val = val1
            text_message = text1
        elif cond2:
            val = val2
            text_message = text2
        elif cond3:
            return text3
        return text_message, Eq(y_max, val, evaluate=False)



K_D=symbols('K_D')

def K_D_func(y_max=y_max, f=f):
	y_max=UnevaluatedExpr(y_max)
	f=UnevaluatedExpr(f)
	val=y_max*f**2
	return Eq(K_D,val, evaluate=False)

















