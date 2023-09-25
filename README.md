## Download_Video_TikTok_CMD
Đây là một ứng dụng nhỏ dùng để tải video TikTok không watermark hàng loạt (sử dụng api từ https://rapidapi.com/yi005/api/tiktok-video-no-watermark2), lấy dữ liệu từ file txt, sau khi tải xuống có thể tạo caption cho từng video để đăng lên mạng xã hội khác như reels instagram, facebook,...

## Chi tiết sử dụng
# Bước 1:
Trên điện thoại (chỉ điện thoại mới được), hãy đưa những video bạn muốn tải vào 1 bộ sưu tập, sau đó bấm nút chia sẻ, chọn "Đặt ở chế độ công khai", cuối cùng chọn "Sao chép liên kết".

# Bước 2:
Sau khi "Sao chép liên kết", gửi liên kết đó qua laptop/PC, mở liên kết sau đó F12 vào Console, dán đoạn script trong file "getlink.js" rồi nhấn Enter, một file .txt chứa toàn bộ link video tiktok trong bộ sưu tập sẽ tự động tải về.

# Bước 3:
Di chuyển file .txt đó vào cùng thư mục chứa tệp "download_video_Tiktok.py", đổi tên file .txt đó thành "urls.txt".

# Bước 4: 
Chạy file "download_video_Tiktok.py" bằng câu lệnh "python download_video_Tiktok.py"

# Bước 5:
Những video được tải sẽ lưu ở thư mục "content", cùng thư mục chứa file "download_video_Tiktok.py". Nếu muốn tạo caption thì chạy file "create_caption_to_txt.py" tương tự như bước 4.

## Lưu ý:
API free chỉ được tối đa 150 request/month.