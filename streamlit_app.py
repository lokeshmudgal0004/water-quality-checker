import streamlit as st
import numpy as np
from WaterQualitySystem import wqi_simulation
from MF_and_Visualization import pH, do, bod, nitrate, temp
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fuzzy Water Quality Checker", layout="centered")
st.title("💧 Fuzzy Logic-Based Water Quality Assessment")

st.markdown("""
This app evaluates **Water Quality Index (WQI)** using a fuzzy logic system based on:
- Temperature
- Dissolved Oxygen (DO)
- pH
- Biochemical Oxygen Demand (BOD)
- Nitrate
""")

# Input sliders (with safe ranges based on MF definitions)
col1, col2 = st.columns(2)

with col1:
    input_temp = st.slider("Temperature (°C)", 2.0, 38.0, 20.0, 0.1)
    input_ph = st.slider("pH", 6.0, 9.9, 7.5, 0.1)
    input_bod = st.slider("BOD (mg/L)", 0.1, 105.0, 5.0, 0.1)

with col2:
    input_do = st.slider("Dissolved Oxygen (mg/L)", 0.4, 13.6, 7.0, 0.1)
    input_nitrate = st.slider("Nitrate (mg/L)", 0.03, 11.9, 2.0, 0.01)

if st.button("Evaluate Water Quality"):
    # Pass inputs to fuzzy system
    wqi_simulation.input['pH'] = input_ph
    wqi_simulation.input['DO'] = input_do
    wqi_simulation.input['BOD'] = input_bod
    wqi_simulation.input['Nitrate'] = input_nitrate
    wqi_simulation.input['Temperature'] = input_temp
    wqi_simulation.compute()
    
    result = wqi_simulation.output['WQI']
    st.success(f"Predicted Water Quality Index (WQI): **{result:.2f}**")

    if result >= 70:
        st.markdown("✅ **Good Water Quality**")
    elif result >= 40:
        st.markdown("⚠️ **Moderate Water Quality**")
    else:
        st.markdown("❌ **Poor Water Quality**")

# Optional: Show membership functions
with st.expander("📊 Show Membership Function Plots"):
    def plot_membership(var, title):
        fig, ax = plt.subplots(figsize=(6, 2.5))
        for label in var.terms:
            ax.plot(var.universe, var[label].mf, label=label)
        ax.set_title(title)
        ax.set_xlabel("Value")
        ax.set_ylabel("Membership")
        ax.legend()
        st.pyplot(fig)

    plot_membership(pH, "pH Membership")
    plot_membership(do, "Dissolved Oxygen Membership")
    plot_membership(bod, "BOD Membership")
    plot_membership(nitrate, "Nitrate Membership")
    plot_membership(temp, "Temperature Membership")
