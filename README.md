[weatherDataPipeline-ELT](https://github.com/manasrane/weatherDataPipeline-ELT](https://github.com/manasrane/weatherDataPipeline-ELT-)
# 🌦️ Weather Data Pipeline — ELT Architecture with Airflow, DBT, and Docker

A modular ELT pipeline to collect, transform, and visualize weather data using modern data engineering tools. Built with **Apache Airflow**, **DBT**, **PostgreSQL**, **Docker**, and **Python**, this project demonstrates scalable data orchestration and transformation in a production-ready environment.

---
## 📌 Features

* 🔄 **Automated Scheduling** via **Airflow DAGs**
* 📥 **Data Extraction** from OpenWeatherMap (or similar) API
* 🛠️ **Transformations** using **DBT** (SQL modeling & testing)
* 🗃️ **PostgreSQL** as central data warehouse
* 📊 **Dashboarding** with **Apache Superset** (optional)
* 🐳 Fully containerized with **Docker Compose**

---

## 🏗️ Architecture

```text
[Airflow Scheduler]
        ↓
[Python Scripts] → [Staging Tables in PostgreSQL]
        ↓
     [DBT Models]
        ↓
[Transformed Tables in PostgreSQL] → [Superset Dashboards]
```

---

## ⚙️ Tech Stack

| Tool           | Purpose                            |
| -------------- | ---------------------------------- |
| Python         | API calls, initial data ingestion  |
| Apache Airflow | Task orchestration and scheduling  |
| DBT            | Data transformation (ELT modeling) |
| PostgreSQL     | Data warehouse                     |
| Docker         | Containerized deployment           |
| Superset       | Optional dashboarding              |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/manasrane/weatherDataPipeline-ELT.git
cd weatherDataPipeline-ELT
```

### 2. Set up environment variables

Create a `.env` file with your API keys and DB credentials:

```env
WEATHER_API_KEY=your_api_key
DB_USER=postgres
DB_PASS=postgres
```

### 3. Launch the pipeline

```bash
docker-compose up --build
```

### 4. Access tools

* **Airflow UI**: [http://localhost:8080](http://localhost:8080)
* **PostgreSQL DB**: `localhost:5432`
* **Superset (optional)**: [http://localhost:8088](http://localhost:8088)

---

## 📂 Project Structure

```
├── dags/                # Airflow DAGs
├── dbt/                 # DBT project for transformations
├── scripts/             # Python scripts to fetch/load data
├── docker-compose.yml   # Container orchestration
├── .env                 # Environment config (API keys, etc.)
```

---

## 📈 Sample Dashboard

*<img width="1866" height="1007" alt="image" src="https://github.com/user-attachments/assets/e70a1119-702f-4c42-8467-3ab7ee9da5c6" />*

---

## 📝 Future Improvements

* Add support for multiple cities/regions
* Integrate with a weather alert system (e.g., SMS/email)
* Deploy to cloud (AWS/GCP/Azure)
* Add ML-based forecasting models

---

## 📧 Contact

Created by [**Manas Rane**](https://github.com/manasrane)
For suggestions or collaboration, feel free to open an issue or reach out via [LinkedIn](https://www.linkedin.com/in/manasrane2000/)
