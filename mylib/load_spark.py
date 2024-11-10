
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

def start_spark(appName="grade_student"):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    try:
        spark.stop()
        return "Spark session stopped successfully."
    except Exception as e:
        return f"Error stopping Spark session: {e}"

def load(spark, file_path="data/grad-students.csv"):
    # Start Spark session
    try:
        # Load the CSV data
        spark_data = spark.read.csv(file_path, inferSchema=True, header=True)
        return spark_data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def load_as_pandas(spark_data):
    """
    Convert a Spark DataFrame into a Pandas DataFrame.
    :param spark_data: The Spark DataFrame to convert.
    :return: Pandas DataFrame.
    """
    try:
        df = spark_data.toPandas()
        return df
    except Exception as e:
        print(f"Error converting to Pandas DataFrame: {e}")
        return None
    
    

def stem_transform(df):
    """Applies an example transformation to classify majors into STEM categories"""
    
    # Define core and other STEM categories
    core_STEM = [
        'Engineering',
        'Computers & Mathematics',
        'Biology & Life Science',
        'Physical Sciences'
    ]

    other_STEM = [
        'Agriculture & Natural Resources',
        'Health',
        'Interdisciplinary'
    ]
    
    # Define the conditions
    df = df.withColumn(
        "STEM_major",
        when(col("Major_category").isin(core_STEM), "core_STEM")
        .when(col("Major_category").isin(other_STEM), "other_STEM")
        .otherwise("Other")
    )
    
    return df