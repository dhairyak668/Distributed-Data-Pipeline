from pyspark.sql import SparkSession

# 🔧 Create Spark session with MinIO configs
spark = SparkSession.builder \
    .appName("Read from MinIO") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minio") \
    .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.hadoop.security.authentication", "NOSASL") \
    .config("spark.hadoop.hadoop.security.authorization", "false") \
    .getOrCreate()

#  Set your bucket and file name from MinIO here
bucket = "shared-prosperity-data"
filename = "WB_SHP.csv"  # Replace with actual file name
path = f"s3a://{bucket}/{filename}"

#  Load the CSV into a DataFrame
df = spark.read.option("header", "true").csv(path)

#  Show the first few rows
df.show(n=10, truncate=False)

#  Done
spark.stop()