import requests
import json
import sys
import io
import os
from tqdm import tqdm

# Thiết lập môi trường mã hóa mặc định là UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Đọc danh sách các URL từ tệp urls.txt
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# Khởi tạo biến đếm
count = 0

# Lặp qua từng URL trong danh sách
for url_tt in urls:
    count += 1  # Tăng số thứ tự đếm lên 1
    url_tt = url_tt.strip()  # Loại bỏ khoảng trắng và ký tự xuống dòng

    # Kiểm tra xem URL có hợp lệ không
    if not url_tt.startswith("https://www.tiktok.com/"):
        print(f"URL không hợp lệ ({count}): {url_tt}")
        continue

    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

    querystring = {"url": url_tt, "hd": "1"}

    headers = {
        "X-RapidAPI-Key": "your-key",
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    response_data = response.json()

    # Kiểm tra xem có dữ liệu video hay không
    if "data" in response_data and "play" in response_data["data"]:
        video_url = response_data["data"]["play"]

        # Tạo thư mục "content" nếu chưa tồn tại
        os.makedirs("content", exist_ok=True)

        # Tạo tên tệp tin từ unique_id và title
        unique_id = response_data["data"]["author"]["unique_id"]
        title = response_data["data"]["title"]
        clean_unique_id = "".join(c for c in unique_id if c.isalnum())
        clean_title = "".join(c for c in title if c.isalnum() or c.isspace())
        file_name = f"{count}_@{clean_unique_id}%{clean_title}.mp4"
        file_path = os.path.join("content", file_name)

        # Tải xuống và lưu video với sự theo dõi của tqdm
        video_response = requests.get(video_url, stream=True)
        if video_response.status_code == 200:
            total_size = int(video_response.headers.get("content-length", 0))
            with open(file_path, "wb") as f, tqdm(
                total=total_size,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                desc=f"Downloading ({count})",
            ) as progress_bar:
                for data in video_response.iter_content(chunk_size=1024):
                    f.write(data)
                    progress_bar.update(len(data))
            print(f"Video ({count}) đã được tải xuống và lưu vào thư mục 'content' thành công.")
        else:
            print(f"Có lỗi xảy ra khi tải xuống video từ URL ({count}): {url_tt}")
    else:
        print(f"Không có dữ liệu video cho URL ({count}): {url_tt}")
