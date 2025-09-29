# Distributed Data Pipeline

A distributed data processing pipeline built with Apache Spark and MinIO for analyzing World Bank Shared Prosperity data. This project demonstrates scalable data processing using containerized Spark clusters and S3-compatible object storage.

## Architecture

This project implements a distributed data pipeline with the following components:

- **Apache Spark**: Distributed computing framework for large-scale data processing
- **MinIO**: S3-compatible object storage for data lake functionality
- **Docker Compose**: Container orchestration for easy deployment
- **PySpark**: Python API for Spark for data analysis and processing

## Dataset

The pipeline processes the **World Bank Shared Prosperity (WB_SHP)** dataset, which contains:
- Mean consumption/income per capita of bottom 40% population
- Data across multiple countries and time periods
- Economic indicators in 2017 PPP USD per day
- Structured data with comprehensive metadata

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.8+ (for local development)
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd distributed-data-pipeline
   ```

2. **Start the services**
   ```bash
   docker-compose up -d
   ```

3. **Verify services are running**
   - Spark Master UI: http://localhost:8080
   - MinIO Console: http://localhost:9001
   - MinIO API: http://localhost:9000

### Default Credentials

- **MinIO Console**: `minio` / `minio123`
- **MinIO API**: `minio` / `minio123`

## Project Structure

```
distributed-data-pipeline/
├── datasets/                 # Raw data files
│   └── WB_SHP.csv           # World Bank Shared Prosperity dataset
├── spark-jobs/              # PySpark job scripts
│   ├── basic_job.py         # Basic Spark job template
│   └── read_minio.py        # MinIO data reading job
├── notebooks/               # Jupyter notebooks for analysis
│   └── analysis.ipynb       # Data analysis notebook
├── jars/                    # Custom JAR files
│   ├── aws-java-sdk-bundle-1.12.215.jar
│   └── hadoop-aws-3.3.2.jar
├── results/                 # Output files and results
├── docker-compose.yml       # Service orchestration
├── requirements.txt         # Python dependencies
├── setup_env.sh            # Environment setup script
└── README.md               # This file
```

## Services

### Spark Cluster
- **Master**: Manages job scheduling and resource allocation
- **Worker**: Executes tasks and processes data
- **UI**: Web interface for monitoring jobs and cluster status

### MinIO Object Storage
- **S3 API**: Compatible with AWS S3 for data storage
- **Console**: Web-based management interface
- **Buckets**: Organized data storage containers

## Usage

### Running Spark Jobs

1. **Submit a job to the Spark cluster**
   ```bash
   docker exec spark-master spark-submit \
     --master spark://spark-master:7077 \
     /app/spark-jobs/read_minio.py
   ```

2. **Monitor job execution**
   - Visit http://localhost:8080 to view the Spark UI
   - Check job status, stages, and performance metrics

### Data Processing

The `read_minio.py` script demonstrates:
- Connecting to MinIO using S3A filesystem
- Reading CSV data from object storage
- Basic data exploration and display

### Local Development

1. **Set up Python environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run setup script**
   ```bash
   chmod +x setup_env.sh
   ./setup_env.sh
   ```

## Data Analysis

The project includes Jupyter notebooks for interactive data analysis:

- **analysis.ipynb**: Comprehensive data exploration and visualization
- Statistical analysis of shared prosperity indicators
- Country-wise comparisons and trends
- Time series analysis of economic indicators

## Configuration

### Spark Configuration
- Master URL: `spark://spark-master:7077`
- UI Port: `8080`
- Custom JARs loaded from `/custom-jars`

### MinIO Configuration
- API Endpoint: `http://minio:9000`
- Console: `http://minio:9001`
- Default bucket: `shared-prosperity-data`

### Environment Variables
Key environment variables can be modified in `docker-compose.yml`:
- `SPARK_MODE`: Master or Worker mode
- `MINIO_ROOT_USER`: MinIO access key
- `MINIO_ROOT_PASSWORD`: MinIO secret key

## Development

### Adding New Spark Jobs

1. Create Python scripts in `spark-jobs/`
2. Use the provided templates for MinIO connectivity
3. Submit jobs using `spark-submit` command

### Custom JARs

Place additional JAR files in the `jars/` directory:
- AWS SDK for S3 connectivity
- Hadoop AWS integration
- Custom Spark extensions

## Monitoring

- **Spark UI**: Real-time job monitoring and performance metrics
- **MinIO Console**: Storage usage and bucket management
- **Docker Logs**: Service logs and debugging information

## Security Notes

- Default credentials are for development only
- Change MinIO credentials for production deployments
- Consider network security for external access

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is part of CPRE 450 coursework at Iowa State University.

## Troubleshooting

### Common Issues

1. **Services not starting**
   - Check Docker daemon is running
   - Verify ports 8080, 9000, 9001 are available

2. **Spark job failures**
   - Check MinIO connectivity
   - Verify data file exists in bucket
   - Review Spark UI for error details

3. **Permission issues**
   - Ensure proper file permissions on scripts
   - Check Docker volume mounts

### Getting Help

- Check Docker logs: `docker-compose logs <service-name>`
- Review Spark UI for job details
- Consult MinIO console for storage issues