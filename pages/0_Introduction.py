import streamlit as st
from Aerodynamic_Excitation import *


add_logo()
custom_header()

st.header("1.Scope")
st.markdown("""This Standard specifies design requirements for bridges with respect to aerodynamic effects,
including provisions for wind-tunnel testing. It supersedes clause 5.3.9 of BS 5400: Part 2(1) and the previous version of this standard BD 49/93.
All references to BS 5400: Part 2 are intended to imply the document as implemented by BD 37(2) (DMRB 1.3). This Standard is applicable to all highway bridges and foot/cycle-track bridges. However its provisions shall only apply to bridges which comply with the constraints outlined herein.""")

st.subheader("1.2 Design requirements")
st.markdown("""The aerodynamic aspects of bridge design shall be carried out in accordance with the rules including associated annexes when applicable.
The requirements, in the form of design rules, are given in the following sections. Proximity effects are covered in Annex A. Formulae for the prediction of fundamental frequencies in bending and in torsion are given in Annex B, and further requirements for wind tunnel testing are given in Annex C.""")
