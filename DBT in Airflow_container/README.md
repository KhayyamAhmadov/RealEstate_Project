# DBT in Airflow Container

This project demonstrates how to run a DBT project inside an Apache Airflow Docker container.

## 📁 Project Structure

```
project-root/
├── .env                      # Environment variables
├── config/                   # Airflow configuration files
├── dags/                     # Airflow DAGs
├── dbt_profiles/             # DBT profiles directory (profiles.yml)
├── dbt_project/              # Actual DBT project (models, etc.)
├── logs/                     # Airflow logs
├── plugins/                  # Custom Airflow plugins
├── docker-compose.yml        # Docker Compose setup
├── Dockerfile                # Custom Airflow image with dbt installed
├── entrypoint.sh             # Entrypoint script for Airflow
└── setup.sh                  # Initialization helper script
```

## 🚀 How to Run

1. **Build Docker containers**

```bash
docker-compose build
```

2. **Initialize Airflow metadata database**

```bash
docker-compose up airflow-init
```

3. **Start Airflow services**

```bash
docker-compose up
```

4. **Access Airflow UI**

Go to [http://localhost:8080](http://localhost:8080)  
Username: `airflow`  
Password: `airflow`

## 🧱 DBT Execution

- DBT is installed inside the Airflow container via `Dockerfile`.
- The `dbt_project/` directory is mounted inside the container at `/opt/airflow/dbt_project/`.
- The `dbt_profiles/` directory is mounted to provide the necessary `profiles.yml`.
