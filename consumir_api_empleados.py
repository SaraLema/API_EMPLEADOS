import requests

# Realizar solicitud a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
respuesta = requests.get(url).json()['data']  # Hacer solicitud GET a la URL


# Inicializar variables para cálculos
numero_de_empleados = len(respuesta)  # Obtener la cantidad de empleados
salarios = [float(emp['employee_salary']) for emp in respuesta]  # Crear una lista de salarios
edades = [int(emp['employee_age']) for emp in respuesta]  # Crear una lista de edades

# Calcular el promedio de salarios
promedio_salario = sum(salarios) / numero_de_empleados 
# Calcular el promedio de edades
promedio_edad = sum(edades) / numero_de_empleados 
# Encontrar el salario mínimo 
salario_minimo = min(salarios)  
# Encontrar el salario máximo
salario_maximo = max(salarios)  
# Encontrar la edad mínima
edad_minima = min(edades)  
# Encontrar la edad máxima
edad_maxima = max(edades)  

# Resultados
print(f"Cantidad total de empleados: {numero_de_empleados}")
print(f"Promedio de salario: {promedio_salario}")
print(f"Promedio de edad: {promedio_edad}")
print(f"Salario mínimo: {salario_minimo}")
print(f"Salario máximo: {salario_maximo}")
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")