# Databricks notebook source
# MAGIC %md
# MAGIC # Transformation Operations

# COMMAND ----------

# impoting lib
from pyspark.sql import functions as f
from pyspark.sql.functions import from_utc_timestamp
from pyspark.sql.functions import to_date

# COMMAND ----------

# creating variable
base_path = "dbfs:/Volumes/youtub_data_catalog/youtube_data_house/soure_file/Channel_one_live_data.json"

save_path = "dbfs:/Volumes/youtub_data_catalog/youtube_data_house/soure_file/silver_dataclean_layer"

# COMMAND ----------

# making json file to dataframe
data = spark.read.option("multiline",True).json(base_path)

# COMMAND ----------

# MAGIC %sql 
# MAGIC use catalog youtub_data_catalog;
# MAGIC use database youtube_data_house;

# COMMAND ----------

# creating temp viw  and than table
# Work directly with the DataFrame - no temp view needed
data_frame = data

# COMMAND ----------

# Tranforamtion 1  type casting of all column
data_frame = data_frame.\
    withColumn("comment_count",f.col("comment_count").cast("int")).\
    withColumn("concurrent_viewers",f.col("concurrent_viewers").cast("int")).\
    withColumn("fetched_at",f.col("fetched_at").cast("timestamp")).\
    withColumn("like_count",f.col("like_count").cast("int")).\
    withColumn("published_at",f.col("published_at").cast("timestamp")).\
    withColumn("view_count",f.col("view_count").cast("int"))


# COMMAND ----------

# transformation `2 
data_frame = data_frame.withColumn(
    "fetched_at",
    from_utc_timestamp(f.col("fetched_at"), "Asia/Kolkata")
)

# COMMAND ----------

# tranformation 3 
data_frame = data_frame.withColumn("channel_title",f.initcap(f.col("channel_title"))).\
    withColumn("title",f.initcap(f.col("title")))

# COMMAND ----------

# tanfromation 4 add column day and hours
data_frame = data_frame.withColumn("fetched_date",to_date(f.col("fetched_at"))).\
    withColumn("fetched_hours",f.hour(f.col("fetched_at")))




# COMMAND ----------

# tanformation 5 add column engagement rate
data_frame = data_frame.withColumn("engagement_rate",f.round((f.col("comment_count")+f.col("like_count"))/f.col("view_count"),2))

# COMMAND ----------

data_frame.write.mode("overwrite").format("parquet").save(save_path)

# COMMAND ----------

dbutils.fs.rm(base_path,recurse=True)