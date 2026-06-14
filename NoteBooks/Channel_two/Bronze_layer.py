# Databricks notebook source
# MAGIC %md
# MAGIC %md
# MAGIC # Collecting live Stream Sourse Data

# COMMAND ----------

# MAGIC %md
# MAGIC **Brozen_layer 2**

# COMMAND ----------

import requests
import json
import time
from datetime import datetime
import os


# ---- CONFIG ----
API_KEY = ""  # Your YouTube API key
JSON_DIR = "/Volumes/youtub_data_catalog/youtube_data_house/soure_file/"
JSON_FILE = "Channel_two_live_data.json"
JSON_PATH = os.path.join(JSON_DIR, JSON_FILE)
CHANNEL_ID = "UCVbsFo8aCgvIRIO9RYwsQMA"

FETCH_INTERVAL = 900   
RUN_DURATION = 3600    

# Ensure folder exists
if not os.path.exists(JSON_DIR):
    os.makedirs(JSON_DIR)

# ---- 1. FETCH YOUTUBE LIVE DATA ----
def get_live_video_details():
    search_url = (
        f"https://www.googleapis.com/youtube/v3/search?"
        f"part=snippet&channelId={CHANNEL_ID}&eventType=live&type=video&key={API_KEY}"
    )
    search_response = requests.get(search_url).json()
    if "items" not in search_response or len(search_response["items"]) == 0:
        return None

    video_id = search_response["items"][0]["id"]["videoId"]

    stats_url = (
        f"https://www.googleapis.com/youtube/v3/videos?"
        f"part=snippet,liveStreamingDetails,statistics&id={video_id}&key={API_KEY}"
    )
    stats_response = requests.get(stats_url).json()
    if "items" not in stats_response:
        return None

    video = stats_response["items"][0]
    snippet = video["snippet"]
    stats = video.get("statistics", {})
    live_details = video.get("liveStreamingDetails", {})

    data = {
        "video_id": video_id,
        "title": snippet.get("title"),
        "channel_title": snippet.get("channelTitle"),
        "published_at": snippet.get("publishedAt"),
        "concurrent_viewers": live_details.get("concurrentViewers"),
        "like_count": stats.get("likeCount"),
        "view_count": stats.get("viewCount"),
        "comment_count": stats.get("commentCount"),
        "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

# ---- 2. SAVE TO JSON ----
def save_to_json(data):
    try:
        # If file doesn't exist → create it
        if not os.path.exists(JSON_PATH):
            with open(JSON_PATH, "w") as f:
                json.dump([data], f, indent=4)
        else:
            # Append to existing JSON array
            with open(JSON_PATH, "r+") as f:
                existing_data = json.load(f)
                existing_data.append(data)
                f.seek(0)
                json.dump(existing_data, f, indent=4)
        print(f"✅ Saved: {data['title']} at {data['fetched_at']}")
    except Exception as e:
        print(f"❌ Error writing JSON: {e}")

# ---- 3. MAIN LOOP ----
start_time = time.time()
while time.time() - start_time < RUN_DURATION:
    try:
        video_data = get_live_video_details()
        if video_data:
            save_to_json(video_data)
        else:
            print("⚠️ No live video currently.")
        time.sleep(FETCH_INTERVAL)
    except Exception as e:
        print(f"❌ Main loop error: {e}")
        time.sleep(10)
