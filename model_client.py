import streamlit as st
import requests
import json 

SERVER_URL = 'https://linear-model-service-yoloogroth.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(hours_worked):
    # Hacer una solicitud al servidor externo para predecir la métrica
    payload = {'instances': [hours_worked]}
    response = requests.post(SERVER_URL, json=payload)
    response.raise_for_status()
    prediction = response.json()
    return prediction['predictions'][0][0]

def calculate_efficiency(hours_worked):
    # Usar la fórmula Y=4X+7 para calcular una métrica relacionada con la eficiencia del programador
    efficiency_metric = 4 * hours_worked + 7

    # Lógica para horas extras en caso de fallas del sistema o red wifi
    if efficiency_metric < 0:
        efficiency_metric = 0

    return efficiency_metric

def main():
    st.title('Calculadora de atrasos de un Programador')

    hours_worked = st.number_input('Ingrese el número de horas de un proyecto:', min_value=0.0, step=1.0)

    if st.button('Calcular'):
        # Hacer la llamada al servidor externo para predecir la métrica
        predicted_efficiency = make_prediction(hours_worked)
        
        # Calcular la métrica relacionada con la eficiencia del programador
        efficiency_result = calculate_efficiency(hours_worked)
        
        st.title('Resultados:')
        st.write(f'Métrica de eficiencia del programador para {hours_worked} horas trabajadas: {efficiency_result}')
        st.write(f'Métrica predicha por el servidor externo: {predicted_efficiency}')

if _name_ == '_main_':
    main()



        
    
