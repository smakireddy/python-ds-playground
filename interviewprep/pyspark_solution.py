from pyspark.sql import SparkSession
import pyspark.sql.functions as func


class ChargePointsETLJob:
    input_path = 'data/input/electric-chargepoints-2017.csv'
    output_path = 'data/output/chargepoints-2017-analysis'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                              .master("local[*]")
                              .appName("ElectricChargePointsETLJob")
                              .getOrCreate())

    def extract(self):
        input_df = self.spark_session.read.option("header", "true").option("inferSchema", "true").csv(self.input_path)
        return input_df

    def transform(self, df):
        agg_df = df.groupBy("CPID").agg(max("PluginDuration").alias("max_duration"),
                                        avg("PluginDuration").alias("avg_duration"))
        return agg_df

    def load(self, df):
        final_df = df.select(df["CPID"].alias("chargepoint_id"),
                             func.round(df["max_duration"], 2).alias("max_duration"),
                             func.round(df["avg_duration"], 2).alias("avg_duration"))
        final_df.write.mode("overwrite").parquet(output_path)

    def run(self):
        self.load(self.transform(self.extract()))
