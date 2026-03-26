-- =======================================================
-- PROJECT: STUDENT MENTAL HEALTH ANALYSIS
-- GIAI ĐOẠN 2: PHÂN TÍCH DỮ LIỆU (EXPLORATORY DATA ANALYSIS)
-- =======================================================
Use mental_health_student
Go 
---------------------------------------------------------
-- 1. TỔNG QUAN VỀ GIẤC NGỦ VÀ HỌC TẬP (OVERALL VIEW)
---------------------------------------------------------
-- Xem trung bình các chỉ số theo Năm học (Year)
SELECT 
    Year,
    COUNT(*) AS Total_Students,
    ROUND(AVG(Sleep_Hours_Total), 2) AS Avg_Sleep_Hours,
    ROUND(AVG(Academic_Stress_Level * 1.0), 2) AS Avg_Stress_Level,
    ROUND(AVG(GPA_Rating * 1.0), 2) AS Avg_GPA
FROM student_data_cleaned
GROUP BY Year
ORDER BY Year;

---------------------------------------------------------
-- 2. PHÂN TÍCH MỐI QUAN HỆ GIỮA GIỜ NGỦ VÀ GPA
---------------------------------------------------------
-- Sinh viên ngủ ít có GPA thấp hơn sinh viên ngủ đủ không?
SELECT 
    CASE 
        WHEN Sleep_Hours_Total < 5 THEN 'Extremely Low (<5h)'
        WHEN Sleep_Hours_Total BETWEEN 5 AND 7 THEN 'Moderate (5-7h)'
        ELSE 'Healthy (>7h)'
    END AS Sleep_Group,
    COUNT(*) AS Student_Count,
    ROUND(AVG(GPA_Rating * 1.0), 2) AS Avg_GPA,
    ROUND(AVG(Academic_Stress_Level * 1.0), 2) AS Avg_Stress
FROM student_data_cleaned
GROUP BY 
    CASE 
        WHEN Sleep_Hours_Total < 5 THEN 'Extremely Low (<5h)'
        WHEN Sleep_Hours_Total BETWEEN 5 AND 7 THEN 'Moderate (5-7h)'
        ELSE 'Healthy (>7h)'
    END
ORDER BY Avg_GPA DESC;

---------------------------------------------------------
-- 3. TÁC ĐỘNG CỦA THÓI QUEN DÙNG ĐIỆN THOẠI (SLEEP HYGIENE)
---------------------------------------------------------
-- Rủi ro từ thói quen dùng điện thoại ảnh hưởng thế nào đến chất lượng giấc ngủ
SELECT 
    Sleep_Hygiene_Risk,
    ROUND(AVG(Overall_Sleep_Quality * 1.0), 2) AS Avg_Sleep_Quality,
    ROUND(AVG(Difficulty_Falling_Asleep * 1.0), 2) AS Avg_Difficulty_Falling_Asleep,
    COUNT(*) AS Student_Count
FROM student_data_cleaned
GROUP BY Sleep_Hygiene_Risk
HAVING COUNT(*) > 5 -- Chỉ lấy các nhóm có số lượng mẫu đáng kể
ORDER BY Sleep_Hygiene_Risk DESC;

---------------------------------------------------------
-- 4. PHÂN TÍCH CHI TIẾT VỀ SỰ KIỆT SỨC (ACADEMIC BURNOUT)
---------------------------------------------------------
-- Mối liên hệ giữa Burnout Score và việc nghỉ học (Attendance)
SELECT 
    Academic_Burnout_Score,
    ROUND(AVG(Sleep_Impact_on_Attendance * 1.0), 2) AS Avg_Absence_Rate,
    ROUND(AVG(GPA_Rating * 1.0), 2) AS Avg_GPA
FROM student_data_cleaned
WHERE Academic_Burnout_Score > 0
GROUP BY Academic_Burnout_Score
ORDER BY Academic_Burnout_Score;

---------------------------------------------------------
-- 5. TÌM KIẾM CÁC "OUTLIERS" (TRƯỜNG HỢP ĐẶC BIỆT)
---------------------------------------------------------
-- Những sinh viên có GPA cao (Good/Excellent) nhưng mức stress cực cao
SELECT 
    Record_Time,
    Year,
    Sleep_Hours_Total,
    Academic_Stress_Level,
    GPA_Rating,
    Academic_Burnout_Score
FROM student_data_cleaned
WHERE GPA_Rating >= 4 AND Academic_Stress_Level >= 3
ORDER BY Academic_Burnout_Score DESC;
GO
