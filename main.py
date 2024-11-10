# import pyspark
from mylib.extract import extract
from mylib.load_spark import (
    start_spark,
    end_spark,
    load,
    load_as_pandas,
    stem_transform,
)
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    extract()
    spark = start_spark(appName="grade_student")
    spark_df = load(spark, "data/grad-students.csv")
    # show the data
    spark_df.show(5)
    # summary the data
    spark_df.printSchema()

    # transform and get new column
    df_transform = stem_transform(spark_df)
    # show the new column
    df_transform.select("STEM_major").show()

    # describe data

    # transform as pandas dataframe
    pandas_df = load_as_pandas(df_transform)

    # visualization
    # Creating a bar plot for the average 'Grad_unemployment_rate' by 'STEM_major'
    plt.figure(figsize=(10, 6))
    # Using Seaborn's barplot to calculate
    # and display the average unemployment rate by STEM major
    sns.barplot(
        x="STEM_major",
        y="Grad_unemployment_rate",
        data=pandas_df,
        estimator="mean",
        ci=None,
    )
    plt.title("Average Grad_unemployment_rate by STEM Major")
    plt.xlabel("STEM Major")
    plt.ylabel("Average Grad_unemployment_rate")
    plt.tight_layout()
    plt.show()

    # end spark
    end_spark(spark)


if __name__ == "__main__":
    main()
    # print(pyspark.__version__) #check pyspark install
