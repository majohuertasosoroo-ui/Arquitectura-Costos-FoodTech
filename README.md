# 🥗 Food-Tech Monitor - MVP Frontend & Backend

Solución tecnológica diseñada para la auditoría de precios de insumos gastronómicos y monitoreo de inflación, desarrollada para la Clase 11: Interfaces Gráficas, Eventos y Excepciones.

## 🏗️ Arquitectura del Proyecto
El software utiliza un diseño modular para garantizar la integridad de los datos financieros:

* **Frontend/ (`app_costos.py`):** Interfaz desarrollada en `Tkinter`. Integra procesamiento de imágenes con `Pillow` y manejo avanzado de excepciones para evitar errores en el ingreso de precios.
* **Backend/ (`gastronomia.py` & `database.py`):** Capa lógica que calcula variaciones porcentuales y dispara alertas automáticas cuando la inflación supera el umbral crítico del 20%.
* **Base de Datos (`foodtech_costos.db`):** Base de datos `SQLite` que registra el histórico de costos y estados de alerta.
* **Orquestador (`main.py`):** Archivo central encargado de la conexión entre el frontend y el motor de datos.

## 👥 Integrantes del Grupo
* **Maria Jose Huertas** (Líder de Proyecto)
* **Alessandro Di-Mauro Correa**
* **Gabriela Ruiz Perez**

## 🚀 Instalación y Uso
1. Instalar la librería de procesamiento de imágenes: `pip install Pillow`.
2. Iniciar el monitor de costos: `python main.py`.

---
*Proyecto académico para el Tercer Corte - Universidad de La Sabana (2026).*
