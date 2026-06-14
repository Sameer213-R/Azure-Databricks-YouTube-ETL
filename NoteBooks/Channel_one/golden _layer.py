# Databricks notebook source
# MAGIC %md
# MAGIC # Golden layer 

# COMMAND ----------

# cretifng base path
base_path = "dbfs:/Volumes/youtub_data_catalog/youtube_data_house/soure_file/silver_dataclean_layer"

# COMMAND ----------

# find the file name 
file_list = dbutils.fs.ls(base_path)
for i in file_list:
    file_name = i.name

print(file_name)

# COMMAND ----------

# creating the dataframe of this file
df = spark.read.option("multiline",True).parquet(f"{base_path}/{file_name}")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog youtub_data_catalog;
# MAGIC use database youtube_data_house;
# MAGIC show tables;

# COMMAND ----------

# write the data into fact table
df.write.mode("append").saveAsTable("youtube_data_house.fact_youtube_data")

# COMMAND ----------

# writing data to dim_channel_table
dim_df=df.select(
    "video_id",
    "channel_title",
    "title"
)

dim_df.write.mode("append").saveAsTable("youtube_data_house.dim_channel_table")


# COMMAND ----------

dbutils.fs.rm(base_path,recurse=True)