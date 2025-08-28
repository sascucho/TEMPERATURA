# app.py
import streamlit as st

st.set_page_config(page_title="Celsius → Fahrenheit", page_icon="🌡️", layout="centered")

def c_to_f(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 9 / 5 + 32

st.title("Conversor: °C → °F")
st.write("Introduce una temperatura en grados Celsius y presiona Convertir.")

# Entrada
c = st.number_input("Temperatura (°C)", value=25.0, step=0.1, format="%.2f", help="Ej: 36.6")

# Conversión instantánea (sin botón) — más UX-friendly
f = c_to_f(c)
st.metric(label="Resultado", value=f"{f:.2f} °F")

# Opcional: botón para recalcular si prefieres control explícito
# if st.button("Convertir"):
#     st.success(f"{c:.2f} °C = {f:.2f} °F")

with st.expander("Fórmula"):
    st.latex(r"F = C \times \frac{9}{5} + 32")
    st.write("- 0 °C → 32 °F\n- 100 °C → 212 °F\n- -40 °C → -40 °F")

st.caption("Hecho con Streamlit. Sencillo, rápido y funcional.")
