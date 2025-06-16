# Fullstack Consumption Module

Este proyecto es un módulo fullstack para visualizar datos de consumo por usuario, usando:

- 🐍 Flask (backend)
- 🐬 MySQL (base de datos)
- 🐳 Docker + Docker Compose

## 🚀 Cómo ejecutar

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/consumption-module.git
cd consumption-module


Para ejecuta docker
docker-compose up --build

Prueba de api de consumo desde postman 
GET http://localhost:5000/consumption/1


Datos iniciales
El sistema crea automáticamente:
La base de datos database_dev
La tabla consumption
Registros de ejemplo para pruebas
