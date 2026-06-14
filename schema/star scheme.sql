-- Databricks notebook source
-- MAGIC %md
-- MAGIC ## creating star scheme

-- COMMAND ----------

use catalog youtub_data_catalog;
use database youtube_data_house;

-- COMMAND ----------

-- fact table creation
create or replace table fact_youtube_data(
    sr_no  bigint GENERATED ALWAYS AS IDENTITY,
    channel_title string,
    comment_count int,
    concurrent_viewers int,
    fetched_at timestamp,
    like_count int,
    published_at timestamp,
    title string,
    video_id string,
    view_count int,
    fetched_date date,
    fetched_hours int,
    engagement_rate double
)

-- COMMAND ----------

-- dim_channel_table 
create or replace table dim_channel_table(
    sr_no  bigint generated always as identity ,
    video_id string,
    channel_title string,
    title string
    )