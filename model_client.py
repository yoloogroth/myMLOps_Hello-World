import streamlit as st
import requests

SERVER_URL = 'https://linear-model-service-yoloogroth.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(hours_worked):
    # Hacer una solicitud al servidor externo para predecir la métrica
    payload = {'instances': [limitaciones]}
    response = requests.post(SERVER_URL, json=payload)
    response.raise_for_status()
    prediction = response.json()
    return prediction['predictions'][0][0]

def calculate_efficiency(hours_worked):
    # Usar la fórmula Y=3X+2 para calcular una métrica relacionada con la eficiencia del programador
    efficiency_metric = -4 * hours_worked + 7
    return efficiency_metric

def main():
    st.title('Calculadora de Eficiencia del Programador')

    limitaciones = st.number_input('Ingrese el número de limitaciones:', min_value=0.0, step=1.0)

    if st.button('Calcular'):
        # Hacer la llamada al servidor externo para predecir la métrica
        predicted_efficiency = make_prediction(limitaciones)
        
        # Calcular la métrica relacionada con la eficiencia del programador
        efficiency_result = calculate_efficiency(limitaciones)
        
        st.write(f'Métrica de eficiencia del programador para {limitaciones} limitaciones al trabajar: {efficiency_result}')
        st.write(f'Métrica predicha por el servidor externo: {predicted_efficiency}')

if __name__ == '__main__':
    main()
