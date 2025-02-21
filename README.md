# 📊 Customer Analytics Pipeline with dbt & Airflow

![Airflow](https://img.shields.io/badge/Airflow-2.6-blue?style=flat&logo=apache-airflow) 
![dbt](https://img.shields.io/badge/dbt-1.9-orange?style=flat&logo=dbt) 
![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=flat&logo=docker) 
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)

## 🚀 Project Overview
This project implements a **customer analytics pipeline** using **dbt (Data Build Tool)** and **Apache Airflow**. The pipeline orchestrates dbt models to transform raw data into meaningful insights, ensuring smooth **data transformations, scheduling, and execution tracking**.

## 🏗️ Tech Stack
- **Apache Airflow** 🏗️ - Workflow orchestration and scheduling
- **dbt (Data Build Tool)** 🔧 - Data transformation and modeling
- **PostgreSQL** 🗄️ - Database for data storage and transformation
- **Docker & Docker Compose** 🐳 - Containerization
- **Python** 🐍 - Core programming language

---

## ⚙️ Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/oguzhangoktas/customer_analytics_project.git
cd customer_analytics_project
```

### 2️⃣ Set Up Environment
Ensure you have **Docker & Docker Compose** installed:
```sh
docker --version  # Ensure Docker is installed
docker compose version  # Ensure Docker Compose is installed
```

### 3️⃣ Start Airflow & dbt in Docker
```sh
docker compose up -d  # Start all services in detached mode
```

### 4️⃣ Verify Airflow & dbt Installation
Check if services are running:
```sh
docker ps  # Verify running containers
docker exec -it airflow_webserver airflow dags list  # Check if DAGs are registered
docker exec -it airflow_webserver dbt --version  # Verify dbt installation
```

---

## 🛠️ How the Pipeline Works
### 🏗 **Pipeline Workflow:**
1. **Raw Data** 🏗 → Stored in PostgreSQL database
2. **dbt Models** 🔧 → Transform the raw data using SQL-based models
3. **Apache Airflow DAG** 📊 → Schedules & orchestrates dbt runs
4. **Refined Data** ✅ → Ready for analytics & reporting

### 📌 **DAG Definition:**
The Airflow DAG `dbt_pipeline.py` executes the following:
```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 1),
    'retries': 1
}

dag = DAG(
    dag_id='dbt_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

dbt_run = BashOperator(
    task_id='run_dbt',
    bash_command='/home/airflow/.local/bin/dbt run --profiles-dir /opt/airflow/dbt',
    dag=dag
)

dbt_run
```

---

## 🚀 Running the Pipeline
### ✅ **Trigger DAG Execution in Airflow**
Run the pipeline manually:
```sh
docker exec -it airflow_webserver airflow dags trigger dbt_pipeline
```

### ✅ **Check Task Logs**
```sh
docker exec -it airflow_webserver airflow tasks logs dbt_pipeline run_dbt $(date +'%Y-%m-%d')
```

### ✅ **Monitor Execution in Airflow UI**
Access the Airflow web UI:
```sh
http://localhost:8080
```
(Default user: `airflow`, password: `airflow`)

---

## 📌 Troubleshooting
### ❌ **dbt Command Not Found in Airflow Container**
If `dbt` is not recognized inside the Airflow container, install it manually:
```sh
docker exec -it --user airflow airflow_webserver pip install --user dbt-core dbt-postgres
```

### ❌ **DAG Not Appearing in UI**
If the DAG does not show up, restart Airflow services:
```sh
docker restart airflow_webserver airflow_scheduler
```

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Feel free to fork this repository, submit issues, and contribute improvements!

---

### 📩 **Author**
📌 **[Oğuzhan Göktaş](https://github.com/oguzhangoktas)**

