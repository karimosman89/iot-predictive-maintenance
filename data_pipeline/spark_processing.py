# data_pipeline/spark_processing.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SensorDataProcessing").getOrCreate()

def process_sensor_data():
    # Load data from Kafka or another source
    data = spark.read.json("data/raw_data.json")  # Replace with actual data source
    processed_data = data.filter(col("temperature") > 50)  # Example filter

    processed_data.write.format("csv").save("data/processed/sensor_data.csv")

if __name__ == "__main__":
    process_sensor_data()

