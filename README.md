# 🛠️ Modular Data Cleaning System (Enterprise Grade)

An efficient, modular Python framework for data sanitization, normalization, and statistical transformation. Originally designed for logistics telemetry, its architecture is highly adaptable to any industry dataset.

---

## 🚀 Guía de Inicio Rápido / Quick Start Guide

Para aplicar este sistema a un nuevo dataset, sigue estos 3 pasos:

1.  **Load:** Import your raw dataset into a Pandas DataFrame.
2.  **Configure:** Define your `master_list` (ground truth values) and target columns.
3.  **Execute:** Chain the specialized kits (`structure`, `uniqueness`, `statistical`) to generate "Gold Standard" data.

---

## 📦 Arquitectura del Sistema (System Architecture)

El framework se compone de tres módulos core que puedes ver en el repositorio:

* **`structure_cleaning.py`**: Text standardization (title case, stripping) and datetime parsing.
* **`uniqueness_handler.py`**: **Fuzzy Matching** logic (thefuzz) to fix typos in names and deduplicate records.
* **`statistical_transformation.py`**: **Outlier detection (IQR)** and missing value imputation (mean/median).

## 📊 Impacto en el Negocio (Business Impact)

* **Reliability:** Automated GPS/Sensor error removal (Outliers).
* **Consistency:** Unified node names (e.g., "Nvo Laredo" -> "Nuevo Laredo").
* **Efficiency:** Drastic reduction in manual cleaning time.

---

## 🌐 Contacto / Contact
**Jorge Carlos Cuevas Noriega** *Especialista en Análisis de Datos & Ingeniería de Procesos*

* **LinkedIn:** [linkedin.com/in/jorge-carlos-cuevas-noriega](https://www.linkedin.com/in/jorge-carlos-cuevas-noriega)
* **Email:** [jorge.carloscuevasnoriega@gmail.com](mailto:jorge.carloscuevasnoriega@gmail.com)
* **Portfolio:** [GitHub Repository](https://github.com/12jorgec/Data_Analytics_Portfolio_JC)