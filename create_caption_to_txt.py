import requests
import re
import pandas as pd
import os
import random

# Đường dẫn đến thư mục chứa tệp video
folder_path = "content"

# Danh sách các tệp video trong thư mục
video_files = [f for f in os.listdir(folder_path) if f.endswith(".mp4")]

# Tạo một danh sách để lưu các dòng văn bản
captions_list = []

# Tạo caption cho từng tệp video và thêm vào danh sách
for video_file in video_files:
    name = os.path.splitext(video_file)[0]
    # Danh sách các mô tả
    descriptions = [
    "Xem video này bạn sẽ cảm thấy hạnh phúc.",
    "Video này giúp bạn yêu đời hơn.",
    "Tôi có 3 bích.",
    "Em gì ơi, em đánh rơi người yêu nè.",
    "Tôi coi hơn chục lần rồi vẫn chưa thấy cuốn chỗ nào."
    ]
    
    # Lấy ngẫu nhiên một mô tả từ danh sách
    random_description = random.choice(descriptions)

    # Sử dụng mô tả ngẫu nhiên cho caption1
    caption1 = random_description
    caption2 = "#reels #thegirlspage #girl #girls #dance #VietnameseGirls #BeautifulGirls"
    caption3 = "cre: {}".format(name)
    caption = "{}\n{}\n{}".format(caption1, caption2, caption3)
    captions_list.append(caption)

# Lưu danh sách các caption vào file .txt
with open("captions.txt", "w", encoding="utf-8") as txt_file:
    for caption in captions_list:
        txt_file.write(caption + "\n")
