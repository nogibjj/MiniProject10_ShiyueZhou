# MiniProject10_ShiyueZhou
[![CI](https://github.com/nogibjj/MiniProject10_ShiyueZhou/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/MiniProject10_ShiyueZhou/actions/workflows/ci.yml)


# Project Summary
PySpark Data Processing
## 1. Setup

### Spark Setup:
- Spark is initialized using the `start_spark()` function, which starts a Spark session with the app name `"grade_student"`. It uses PySpark to handle large datasets and execute SQL queries on Spark DataFrames.

### File Extraction:
- The `extract()` function downloads the "grad-students.csv" file from a remote URL (GitHub), ensuring the file is saved locally.
- Data Source: https://github.com/fivethirtyeight/data/blob/master/college-majors/grad-students.csv


## 2. PySpark Data Processing

### Loading Data:
- The `load()` function loads the "grad-students.csv" file into a Spark DataFrame using PySpark's `.read.csv()` method with `inferSchema=True` for automatic type detection. It ensures the data is ready for further analysis.

### Data Transformation:
- The `stem_transform()` function classifies each college major into STEM categories. It uses PySpark's `when()` and `isin()` functions to categorize the data into `core_STEM`, `other_STEM`, or `Other`.

## 3. Spark SQL Query

### SQL Transformation:
- The `Spark_SQL()` function uses Spark SQL to filter and aggregate data. It creates a temporary view of the loaded data, and then uses a SQL query to filter categories with a total employment count above 10,000, while also summing up employment statistics (`Grad_employed`, `Nongrad_employed`, etc.) per major category.

## 4. Transformations & Output Data (Markdown) 

### Data Output:
- After transforming the data with `stem_transform()`, the results are saved as a Markdown file using `pandas.DataFrame.to_markdown()`. This allows the generated data to be presented in an easily readable format.

## 5. Visualization

### Visualization:
- The transformed data is visualized using a Seaborn barplot, comparing the average `Grad_unemployment_rate` across different `STEM_major` categories. This step helps visualize trends in unemployment rates based on the major category classification.

## 6. Code Flow:
1. **Data Extraction**: `extract()` downloads the file.
2. **Data Loading**: `load()` loads the CSV into Spark DataFrame.
3. **Data Transformation**: `stem_transform()` classifies the majors into STEM categories.
4. **SQL Query**: `Spark_SQL()` applies an SQL query to filter categories with total employment over 10,000.
5. **Output Generation**: The data is saved as a Markdown file and visualized.

## 7. Key Functions:
- `start_spark(appName)`: Initializes the Spark session.
- `end_spark(spark)`: Stops the Spark session.
- `load(spark, file_path)`: Loads the CSV data into a Spark DataFrame.
- `stem_transform(df)`: Classifies college majors into STEM categories.
- `Spark_SQL(data)`: Runs a SQL query to filter and aggregate data.

## 8. File Saved:
- The transformation results are saved as `df_transform.md` in Markdown format, which is generated automatically after the data transformation step.
- The transformed column `STEM_major` is showed in the last column of `df_transform.md`.
- [Output data after transform](df_transform.md)

## 9. Example Visualization:
- A bar plot displaying the average graduation unemployment rate by STEM major, which helps to analyze trends in the job market across various fields of study.

