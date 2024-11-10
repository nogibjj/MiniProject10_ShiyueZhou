import os
from pyspark.sql import SparkSession
from mylib.extract import extract
from mylib.load_spark import load, load_as_pandas, stem_transform

# Initialize Spark session
spark = SparkSession.builder.appName("test_grade_student").getOrCreate()
file_path = "data/grad-students.csv"

# Test if extract function correctly downloads the file
def test_extract():
    file_path = extract()
    assert os.path.exists(file_path), f"File not found at path: {file_path}"


# Test loading the CSV file into Spark DataFrame
def test_load():
    data = load(spark, file_path)
    assert data is not None, "Data is null!"
    assert data.count() > 0, "Data is empty!"  # Ensure the DataFrame is not empty


# Test loading data as Pandas DataFrame
def test_load_as_pandas():
    data = load(spark, file_path)
    df = load_as_pandas(data)
    assert df is not None, "Pandas DataFrame is null!"
    assert len(df) > 0, "Pandas DataFrame is empty!"


# Test STEM transformation
def test_stem_transform():
    data = load(spark, file_path)
    df = stem_transform(data)
    assert df is not None, "Data after transformation is null!"

    # Check if the "STEM_major" column exists and has values
    stem_major_values = df.select("STEM_major").distinct().count()
    assert stem_major_values > 0, "'STEM_major' column is empty!"


if __name__ == "__main__":
    test_extract()  # Test if the file is downloaded
    test_load()  # Test if data is loaded correctly into Spark
    test_load_as_pandas()  # Test conversion to Pandas DataFrame
    test_stem_transform()  # Test STEM transformation

    # Stop Spark session at the end of tests
    spark.stop()
