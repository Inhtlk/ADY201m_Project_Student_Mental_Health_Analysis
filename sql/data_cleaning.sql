-- =======================================================
-- PROJECT: STUDENT MENTAL HEALTH ANALYSIS
-- GIAI ĐOẠN 2: DATA CLEANING & OUTLIER DETECTION
-- =======================================================

Use cleaned_student_data
Go

-- Kiểm tra số lượng dòng bị thiếu dữ liệu
SELECT 
    COUNT(*) - COUNT(year_study) AS missing_year,
    COUNT(*) - COUNT(sleep_hours) AS missing_sleep,
    COUNT(*) - COUNT(stress_level) AS missing_stress
FROM cleaned_student_data;

-- Xóa các dòng có quá nhiều dữ liệu trống (Ví dụ: thiếu cả stress và gpa)
DELETE FROM cleaned_student_data 
WHERE stress_level IS NULL AND gpa_rating IS NULL;

--Kiểm tra giá trị nằm ngoài phạm vi (Range Check)
--Ví dụ: Số giờ ngủ không thể âm hoặc lớn hơn 24 giờ.
SELECT * FROM cleaned_student_data
WHERE sleep_hours < 0 OR sleep_hours > 24;

-- Tìm các bản ghi mâu thuẫn logic
SELECT * FROM cleaned_student_data
WHERE sleep_hours <= 3.5 
  AND sleep_quality IN ('Good', 'Very good');

-- Tạo view hoặc bảng mới với dữ liệu đã map số
CREATE VIEW student_numeric_view AS
SELECT 
    *,
    CASE 
        WHEN sleep_quality = 'Very poor' THEN 1
        WHEN sleep_quality = 'Poor' THEN 2
        WHEN sleep_quality = 'Average' THEN 3
        WHEN sleep_quality = 'Good' THEN 4
        WHEN sleep_quality = 'Very good' THEN 5
        ELSE 0 
    END AS sleep_quality_score,
    CASE 
        WHEN stress_level = 'No stress' THEN 0
        WHEN stress_level = 'Low stress' THEN 1
        WHEN stress_level = 'High stress' THEN 2
        WHEN stress_level = 'Extremely high stress' THEN 3
        ELSE 1 -- Giá trị mặc định
    END AS academic_stress_score
FROM cleaned_student_data;

-- Tính toán Academic Burnout Score
-- Giả sử các cột đã được chuyển sang dạng số
SELECT 
    record_time,
    (sleep_impact_on_deadlines_score * sleep_impact_on_concentration_score) AS academic_burnout_score,
    (phone_usage_score * diff_falling_asleep_score) AS sleep_hygiene_risk
FROM student_numeric_view;
