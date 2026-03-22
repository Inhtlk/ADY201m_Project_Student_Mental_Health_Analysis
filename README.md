# ADY201m_Project_Student_Mental_Health_Analysis
# Student Mental Health and Educational Outcomes Analysis 🎓📊
> Dự án phân tích mối tương quan giữa áp lực học tập, thói quen ngủ và sức khỏe tâm thần ở sinh viên bậc Đại học.

##  Giới thiệu (Overview)
Nghiên cứu này nhằm khám phá cách thức các yếu tố môi trường học đường và thói quen sinh hoạt ảnh hưởng đến tâm lý sinh viên. Dự án sử dụng các kỹ thuật phân tích dữ liệu chuyên sâu để tìm ra các mẫu (patterns) và đề xuất các giải pháp cải thiện sức khỏe tinh thần trong môi trường giáo dục.

## Dashboard trực tuyến
Bạn có thể xem các biểu đồ tương tác tại đây:
👉 [**Link Streamlit Dashboard**](https://student-stress-dashboard-ady-apffo852xwebh7rsrq4uyf.streamlit.app/)

## Cấu trúc thư mục (Project Structure)
Dự án được tổ chức khoa học để dễ dàng quản lý và theo dõi:
* **`data/`**: Chứa các file dữ liệu gốc (.csv) về mất ngủ và sức khỏe tâm thần.
* **`sql/`**: Các script SQL (`data_cleaning.sql`) dùng để truy vấn và làm sạch dữ liệu.
* **`scripts/`**: Mã nguồn Python (`Model_training.py`) phục vụ việc huấn luyện mô hình và chạy Dashboard.
* **`README.md`**: Hướng dẫn và giới thiệu tổng quan về dự án.

## Câu hỏi nghiên cứu (Research Questions)
1. **RQ1:** Thói quen ngủ và hậu quả trực tiếp của chúng ảnh hưởng như thế nào đến kết quả học tập, mức độ căng thẳng học tập của sinh viên và kết quả giáo dục nói chung?
2. **RQ2:** Các mô hình học máy có thể dự đoán mức độ căng thẳng học tập của sinh viên dựa trên hành vi ngủ và các đặc điểm về kết quả học tập của họ hiệu quả đến mức nào?
  

## Công cụ & Kỹ thuật (Tech Stack)
* **Ngôn ngữ:** SQL (Làm sạch dữ liệu), Python (Phân tích & Dashboard).
* **Thư viện:** Pandas, Plotly/Matplotlib, Streamlit.
* **Định dạng báo cáo:** LaTeX (Overleaf).

## Cách sử dụng
Để chạy dự án này ở máy cục bộ (Local):
1. Clone repository:
   ```bash
   git clone [https://github.com/Inhtlk/ADY201m_Project_Student_Mental_Health_Analysis.git](https://github.com/Inhtlk/ADY201m_Project_Student_Mental_Health_Analysis.git)
2. Cài đặt thư viện:
    pip install -r requirements.txt

3. Chạy dashboard:
    streamlit run scripts/app.py
