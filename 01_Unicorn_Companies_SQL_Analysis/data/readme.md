# 🦄 Strategic Analysis of Unicorn Companies (SQL)

## 🎯 Objetivo del Proyecto
Analizar un dataset global de empresas "Unicornio" para identificar qué industrias han tenido el mayor crecimiento entre 2019 y 2021. Este análisis sirve para orientar decisiones de inversión basadas en datos históricos de valuación y tracción de mercado.

## 📊 Metodología (Método STAR)
- **Situación:** Una firma de capital de riesgo necesita identificar los sectores más prometedores para invertir.
- **Tarea:** Extraer las 3 industrias con más empresas unicornio nuevas en los últimos 3 años y calcular su valuación promedio.
- **Acción:** Desarrollé consultas SQL avanzadas utilizando **CTEs** para organizar la lógica, **Joins** para conectar datos de valuación e industria, y **funciones de fecha** para filtrar el periodo crítico.
- **Resultado:** Identificación de Fintech, Internet Software y E-commerce como los motores de crecimiento, permitiendo una visión clara de dónde se está concentrando la riqueza tecnológica.

## 📂 Estructura del Repositorio
- `analisis_unicornios.sql`: Script con la lógica de negocio y consultas SQL.
- `/datos`: Carpeta que contiene los archivos CSV originales (`unicorns.csv`, `dates.csv`, `funding.csv`, `industries.csv`).
- `README.md`: Documentación del proyecto.

## 🛠️ Requisitos Técnicos
Para replicar este análisis, puedes importar los archivos CSV de la carpeta `/datos` en cualquier motor de base de datos SQL (PostgreSQL, MySQL, SQLite). El código está optimizado para sintaxis estándar de SQL.

---
*Proyecto desarrollado por el Ing. Jorge Carlos Cuevas Noriega como parte  de su portafolio de Análisis de Datos.*