# ADY201m_Project_Student_Mental_Health_Analysis
# Student Mental Health Analysis: Academic Stress Among Undergraduate Students

---

##  Giới thiệu (Overview)
Nghiên cứu này tập trung vào việc đánh giá tác động đa chiều của thói quen sinh hoạt và áp lực học đường đối với sức khỏe tâm thần của sinh viên đại học. Dự án kết hợp giữa phân tích thống kê truyền thống để làm rõ các mối liên hệ nhân quả và áp dụng một số mô hình học máy (Machine Learning) để dự báo sớm mức độ căng thẳng.

Thông qua việc khai thác dữ liệu về giấc ngủ và kết quả học tập, dự án hướng tới cung cấp các góc nhìn thực chứng, giúp hỗ trợ việc ra quyết định và đề xuất các giải pháp can thiệp tâm lý kịp thời trong môi trường giáo dục đại học.

---

## Dashboard trực tuyến
Bạn có thể xem các biểu đồ tương tác tại đây:
👉 [**Link Streamlit Dashboard**]([https://student-stress-dashboard-ady-apffo852xwebh7rsrq4uyf.streamlit.app/](https://student-stress-dashboard-ady-apffo852xwebh7rsrq4uyf.streamlit.app/#academic-stress-level-across-gpa-ratings))

---

## Cấu trúc thư mục (Project Structure)

 ```text
ADY201m_Project_Student_Mental_Health_Analysis/
├── data/                                  # Chứa các tệp dữ liệu gốc và dữ liệu dự báo
│   ├── Student Insomnia and Education...csv
│   ├── Student_Mental_Health_Final.csv
│   └── Student_Mental_Health_Predicti...csv
├── scripts/                               # Chứa mã nguồn xử lý và mô hình Python
│   ├── Clean_data.py                      # Code làm sạch và tiền xử lý dữ liệu
│   ├── EDA_analysis.py                    # Code phân tích khám phá dữ liệu (biểu đồ)
│   └── Model_training.py                  # Code huấn luyện mô hình và giao diện Streamlit
├── sql/                                   # Chứa các truy vấn dữ liệu bằng SQL
│   └── data_cleaning.sql                  # Script làm sạch dữ liệu trên database
├── README.md                              # Giới thiệu tổng quan và hướng dẫn dự án
 ```
---

## Câu hỏi nghiên cứu (Research Questions)
1. **RQ1:** Thói quen ngủ và hậu quả trực tiếp của chúng ảnh hưởng như thế nào đến kết quả học tập, mức độ căng thẳng học tập của sinh viên và kết quả giáo dục nói chung?
2. **RQ2:** Các mô hình học máy có thể dự đoán mức độ căng thẳng học tập của sinh viên dựa trên hành vi ngủ và các đặc điểm về kết quả học tập của họ hiệu quả đến mức nào?
  
---

## Công cụ & Kỹ thuật (Tech Stack)
* **Ngôn ngữ:** SQL (Làm sạch dữ liệu), Python (Làm sạch dữ liệu & Phân tích ).
* **Thư viện:** Pandas, Plotly/Matplotlib, Streamlit.
* **Định dạng báo cáo:** LaTeX (Overleaf).
  
---

## Cách sử dụng
Để chạy dự án này ở máy cục bộ (Local):
1. Clone kho lưu trữ:
   ```bash
   git clone [https://github.com/Inhtlk/ADY201m_Project_Student_Mental_Health_Analysis.git](https://github.com/Inhtlk/ADY201m_Project_Student_Mental_Health_Analysis.git)
   ```
2. Cài đặt thư viện:
 ```bash
   git clone [ip install -r requirements.txt]
 ```
3. Khởi chạy dashboard:
   ```bash
   git clone [ip install -r requirements.txt]
   ```
---

## Kết quả thực nghiệm (Experimental Results)

Dự án đã thực hiện phân tích trên tập dữ liệu gồm **875 mẫu** sinh viên sau khi đã làm sạch và loại bỏ các bản ghi không nhất quán. Dưới đây là các kết quả chính từ mô hình thực nghiệm:

### 1. Các yếu tố dự báo chính (Key Predictors)
* **Burnout Composite Score:** Là yếu tố dự báo mạnh nhất đối với áp lực học tập (Academic Stress).
* **Sleep Hygiene Risk Score:** Có mối tương quan thuận với mức độ căng thẳng (càng thiếu ngủ/vệ sinh giấc ngủ kém, áp lực càng tăng).
* **GPA:** Có mối tương quan nghịch với áp lực (GPA càng cao, mức độ áp lực ghi nhận có xu hướng giảm).

### 2. Hiệu suất mô hình (Model Performance)
Chúng tôi đã thử nghiệm và so sánh các mô hình hồi quy để dự đoán mức độ áp lực:

| Mô hình | Chỉ số R² (Test set) | Chỉ số MAE | Ghi chú |
| :--- | :---: | :---: | :--- |
| **OLS Regression** | **0.246** | **0.528** | Giải thích được 22.8% phương sai toàn mẫu. |
| **Random Forest** | **0.241** | **0.531** | Mô hình đạt độ ổn định cao sau khi tinh chỉnh (tuned). |


### 3. Kết luận thực nghiệm
Kết quả cho thấy áp lực học tập của sinh viên trong mẫu nghiên cứu có liên quan chặt chẽ đến các khó khăn trong học tập do **kiệt sức (burnout)** và **thói quen ngủ kém**. Mô hình Random Forest cho thấy khả năng dự báo triển vọng, hỗ trợ việc nhận diện sớm các sinh viên có nguy cơ gặp vấn đề về sức khỏe tâm thần.

---
## Nhóm Tác giả (Authors)
* **Trần Ngọc Thúy Hiền (SA170191)** - *Trưởng nhóm *
* **Đoàn Đức Nguyên (SE201711)** - *Thành viên*
* **Đồng Bảo Hân (SE203683)** - *Thành viên*
* **Trần Lợi Kiều Nhi (SE203044)** - *Thành viên*
  
**Đơn vị:** Đại học FPT TP.HCM | Ngành Trí tuệ Nhân tạo (AI).
