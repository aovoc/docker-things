#
# /opt/spark/spark/bin/spark-submit --master spark://spark-master:$SPARK_MASTER_PORT test_main.py
# ==============================================================================
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("appName").getOrCreate()
sc = spark.sparkContext

for i in range(10):
  print("="*50+"{}".format(i))
  rdd = sc.parallelize([1,2,3,4,5,6,7])
  print(rdd.count())
