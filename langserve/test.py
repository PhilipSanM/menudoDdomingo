import requests

print('------------------- Preguntas y Chat -------------------')
print("****Pregunta inicial********")
print('\n')

# URL de tu servidor FastAPI
url = 'http://localhost:8000/generate_info/invoke'

# Cuerpo de la solicitud en formato JSON
data = {
    'input': {'document': 'Si funcionas?'}
}

# Enviar la solicitud POST al servidor con el cuerpo de la solicitud
response = requests.post(url, json=data)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Mostrar la respuesta del chatbot
    print(response.json())
else:
    print(f'Error en la solicitud: {response.status_code}')
