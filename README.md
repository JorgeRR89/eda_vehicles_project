# eda_vehicles_project
Proyecto-Sprint 7
# 🚗 Análisis Exploratorio de Datos — *Vehicles EDA App*

## 📘 Contexto del Proyecto
Este proyecto forma parte del módulo de análisis de datos del programa **TripleTen**.  
El objetivo es desarrollar una aplicación web interactiva que permita realizar un **análisis exploratorio de datos (EDA)** sobre 
anuncios de vehículos usados.  

El desarrollo combina análisis con **Pandas y Plotly**, y la creación de una interfaz web con **Streamlit**, desplegada en 
**Render**.

---

## 🎯 Objetivo
Analizar y visualizar los datos del conjunto `vehicles_us.csv`, comprendiendo patrones en variables como:
- Precio del vehículo  
- Kilometraje (`odometer`)  
- Año de fabricación  
- Condición y tipo de transmisión  

Además, ofrecer al usuario una interfaz sencilla para visualizar histogramas y gráficos de dispersión de manera interactiva.

---

## ⚙️ Tecnologías y Librerías Utilizadas
- **Python 3**
- **Pandas** — análisis y manipulación de datos
- **Plotly** — visualizaciones interactivas
- **Streamlit** — interfaz web de la aplicación
- **Render** — despliegue de la aplicación

---

## 🧠 Pasos del Proyecto

### 1️⃣ Preparación del entorno
- Creación del entorno virtual `vehicles_env`.
- Instalación de librerías requeridas:  
  ```
  pip install pandas plotly streamlit
  ```

### 2️⃣ Análisis exploratorio (EDA)
- Se desarrolló un notebook `EDA.ipynb` en el directorio `notebooks/`.
- Se analizaron distribuciones y relaciones entre variables principales usando **Plotly**.

### 3️⃣ Desarrollo de la aplicación
- Se creó el archivo `app.py` en la raíz del proyecto.  
- Incluye:
  - Encabezado con `st.header()`.
  - Botón para construir **un histograma** de la variable `odometer`.
  - Botón para construir **un gráfico de dispersión** entre `price` y `odometer`.
  - Visualización de resultados con `st.plotly_chart()`.

### 4️⃣ Despliegue
- Se creó un archivo `requirements.txt` con las dependencias del entorno.
- Se vinculó el repositorio GitHub con **Render.com**.
- Comandos de despliegue configurados en Render:
  - **Build command:** `pip install --upgrade pip && pip install -r requirements.txt`
  - **Start command:** `streamlit run app.py`

---

## 📊 Visualizaciones Principales
1. **Histograma del odómetro** — muestra la distribución del kilometraje de los vehículos.  
2. **Gráfico de dispersión (price vs odometer)** — visualiza la relación entre el precio y el kilometraje.  
3. **Interactividad** — el usuario puede generar gráficos con solo un clic.

---

## 📂 Estructura del Proyecto
```bash
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

---

## 🖥️ Ejecución Local
Si deseas ejecutar la app localmente:

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/JorgeRR89/eda_vehicles_project.git
cd eda_vehicles_project

# 2️⃣ Crea un entorno virtual
python3 -m venv vehicles_env
source vehicles_env/bin/activate

# 3️⃣ Instala dependencias
pip install -r requirements.txt

# 4️⃣ Ejecuta la app
streamlit run app.py
```

La aplicación se abrirá en tu navegador en:  
👉 http://localhost:8501

---

## 🌐 Versión Desplegada
Accede a la aplicación online aquí:  
🔗 **[https://eda-vehicles-project.onrender.com](https://eda-vehicles-project.onrender.com)**

---

## 📈 Conclusiones
- El dataset permitió observar tendencias en los precios según kilometraje y año.  
- Se desarrolló una aplicación funcional y ligera, con visualizaciones interactivas y un flujo claro de análisis.  
- El despliegue en Render facilita compartir resultados de forma accesible y profesional.

---

## 👨‍💻 Autor
**Jorge Reyes Rodríguez**  
📧 reyesrod.jorge@gmail.com  
💼 [GitHub: JorgeRR89](https://github.com/JorgeRR89)

---

## ✅ Criterios de Evaluación Cubiertos
- [x] Aplicación accesible vía navegador  
- [x] Encabezado visible  
- [x] Histograma funcional  
- [x] Gráfico de dispersión funcional  
- [x] Botones o casillas interactivas  
- [x] Estructura de proyecto completa  
- [x] README claro, completo y profesional
