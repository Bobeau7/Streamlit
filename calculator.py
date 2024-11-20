import streamlit as st

# Titel und Beschreibung
st.title("Taschenrechner")
st.write("Ein einfacher Web-Taschenrechner mit Streamlit.")

# Eingabefelder für Zahlen und Operation
num1 = st.number_input("Erste Zahl", value=0.0)
num2 = st.number_input("Zweite Zahl", value=0.0)
operation = st.selectbox("Operation auswählen", ["Addition", "Subtraktion", "Multiplikation", "Division"])

# Berechnung
result = None
if st.button("Berechnen"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraktion":
        result = num1 - num2
    elif operation == "Multiplikation":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division durch 0 ist nicht erlaubt!")

# Ergebnis anzeigen
if result is not None:
    st.success(f"Das Ergebnis ist: {result}")

#Test1
