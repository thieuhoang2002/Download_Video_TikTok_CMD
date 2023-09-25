// Tìm tất cả các thẻ div có class "tiktok-x6y88p-DivItemContainerV2 e19c29qe8"
const divs = document.querySelectorAll('.tiktok-x6y88p-DivItemContainerV2.e19c29qe8');

// Tạo một mảng để lưu trữ các href
const hrefArray = [];

// Lặp qua từng div để lấy href từ thẻ a
divs.forEach(div => {
  const aTag = div.querySelector('a');
  if (aTag) {
    const href = aTag.getAttribute('href');
    hrefArray.push(href);
  }
});

// Tạo nội dung txt từ danh sách href
const txtContent = hrefArray.join('\n');

// Tạo một đối tượng Blob để lưu trữ nội dung
const blob = new Blob([txtContent], { type: 'text/plain' });

// Tạo một URL tạm thời để tải xuống
const url = URL.createObjectURL(blob);

// Tạo một thẻ a để tải xuống
const downloadLink = document.createElement('a');
downloadLink.href = url;
downloadLink.download = 'href_list.txt';
downloadLink.textContent = 'Tải xuống danh sách href';

// Thêm thẻ a vào body và kích hoạt sự kiện click để tải xuống
document.body.appendChild(downloadLink);
downloadLink.click();

// Giải phóng URL tạm thời
URL.revokeObjectURL(url);

// Gỡ bỏ thẻ a khỏi body sau khi đã hoàn thành tải xuống
document.body.removeChild(downloadLink);

//chay file nay trong console trinh duyet