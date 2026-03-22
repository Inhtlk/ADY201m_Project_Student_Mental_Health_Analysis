import pandas as pd

def load_and_rename(file_path):
    """Đọc file và đổi tên cột cho gọn"""
    # Đọc file
    df = pd.read_csv(file_path)
    # Xóa khoảng trắng thừa ở tên cột
    df.columns = df.columns.str.strip()
    
    mapping = {
        'Timestamp': 'Record_Time',
        '1. What is your year of study?': 'Year',
        '2. What is your gender?': 'Gender',
        '3. How often do you have difficulty falling asleep at night?': 'Difficulty_Falling_Asleep',
        '4. On average, how many hours of sleep do you get on a typical day?': 'Sleep_Hours_Total',
        '5. How often do you wake up during the night and have trouble falling back asleep?': 'Waking_Up_During_Night',
        '6. How would you rate the overall quality of your sleep?': 'Overall_Sleep_Quality',
        '7. How often do you experience difficulty concentrating during lectures or studying due to lack of sleep?': 'Sleep_Impact_on_Concentration',
        '8. How often do you feel fatigued during the day, affecting your ability to study or attend classes?': 'Daytime_Fatigue',
        '9. How often do you miss or skip classes due to sleep-related issues (e.g., insomnia, feeling tired)?': 'Sleep_Impact_on_Attendance',
        '10. How would you describe the impact of insufficient sleep on your ability to complete assignments and meet deadlines?': 'Sleep_Impact_on_Deadlines',
        '11. How often do you use electronic devices (e.g., phone, computer) before going to sleep?': 'Phone_Usage_Before_Sleep',
        '12. How often do you consume caffeine (coffee, energy drinks) to stay awake or alert?': 'Caffeine_Intake',
        '13. How often do you engage in physical activity or exercise?': 'Exercise_Frequency',
        '14. How would you describe your stress levels related to academic workload?': 'Academic_Stress_Level',
        '15. How would you rate your overall academic performance (GPA or grades) in the past semester?': 'GPA_Rating'
    }
    return df.rename(columns=mapping)

def apply_mappings(df):
    """Chuyển đổi các giá trị text sang số"""
    freq_map = {
        'Never': 0, 'Rarely': 1, 'Rarely (1-2 times a month)': 1, 'Rarely (1-2 times a week)': 1,
        'Sometimes': 2, 'Sometimes (1-2 times a week)': 2, 'Sometimes (3-4 times a week)': 2,
        'Often': 3, 'Often (3-4 times a week)': 3, 'Often (5-6 times a week)': 3,
        'Always': 4, 'Every day': 4, 'Every night': 4
    }
    sleep_duration_map = {'Less than 4 hours': 3.5, '4-5 hours': 4.5, '5-6 hours': 5.5, '6-7 hours': 6.5, '7-8 hours': 7.5, 'More than 8 hours': 8.5}
    quality_map = {'Very poor': 1, 'Poor': 2, 'Average': 3, 'Good': 4, 'Very good': 5}
    impact_map = {'No impact': 0, 'Minor impact': 1, 'Moderate impact': 2, 'Major impact': 3, 'Severe impact': 4}
    stress_map = {'No stress': 0, 'Low stress': 1, 'High stress': 2, 'Extremely high stress': 3}
    gpa_map = {'Poor': 1, 'Below Average': 2, 'Average': 3, 'Good': 4, 'Excellent': 5}
    year_map = {'First year': 1, 'Second year': 2, 'Third year': 3, 'Fourth year': 4, 'Graduate student': 4}
    gender_map = {'Male': 0, 'Female': 1}

    # Đảm bảo dữ liệu text không có khoảng trắng thừa trước khi map
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()

    # Áp dụng cho các cột tần suất
    cols_freq = ['Difficulty_Falling_Asleep', 'Waking_Up_During_Night', 'Sleep_Impact_on_Concentration',
                 'Daytime_Fatigue', 'Sleep_Impact_on_Attendance', 'Phone_Usage_Before_Sleep',
                 'Caffeine_Intake', 'Exercise_Frequency']
    
    for col in cols_freq:
        df[col] = df[col].map(freq_map).fillna(0)
        
    df['Sleep_Hours_Total'] = df['Sleep_Hours_Total'].map(sleep_duration_map)
    df['Overall_Sleep_Quality'] = df['Overall_Sleep_Quality'].map(quality_map)
    df['Sleep_Impact_on_Deadlines'] = df['Sleep_Impact_on_Deadlines'].map(impact_map)
    df['Academic_Stress_Level'] = df['Academic_Stress_Level'].map(stress_map)
    df['GPA_Rating'] = df['GPA_Rating'].map(gpa_map)
    df['Year'] = df['Year'].map(year_map)
    df['Gender'] = df['Gender'].map(gender_map)    
    
    return df

def filter_invalid_data(df):
    """Loại bỏ các bản ghi mâu thuẫn logic"""
    # Feature engineering tạm thời để kiểm tra logic
    df['Academic_Burnout_Score'] = df['Sleep_Impact_on_Deadlines'].fillna(0) * df['Sleep_Impact_on_Concentration']
    df['Sleep_Hygiene_Risk'] = df['Phone_Usage_Before_Sleep'] * df['Difficulty_Falling_Asleep']
    
    # Khởi tạo cột đánh dấu lỗi
    df['Invalid_Data_Points'] = 0

    # 1. Khó ngủ do dùng đt nhiều nhưng chất lượng ngủ lại "Rất tốt" -> Vô lý
    df.loc[(df['Sleep_Hygiene_Risk'] >= 16) & (df['Overall_Sleep_Quality'] >= 4), 'Invalid_Data_Points'] += 1

    # 2. Ngủ cực ít (<3.5h) nhưng lại bảo "Không mệt mỏi chút nào" -> Vô lý
    df.loc[(df['Sleep_Hours_Total'] <= 3.5) & (df['Daytime_Fatigue'] <= 1), 'Invalid_Data_Points'] += 1

    # 3. Burnout cực cao nhưng Stress lại bảo "Không có" -> Vô lý
    df.loc[(df['Academic_Burnout_Score'] >= 16) & (df['Academic_Stress_Level'] <= 1), 'Invalid_Data_Points'] += 1

    # Lọc lấy các dòng không có điểm lỗi
    df_clean = df[df['Invalid_Data_Points'] == 0].copy()
    
    # Xóa các cột tạm dùng để check
    df_clean = df_clean.drop(columns=['Invalid_Data_Points'])
    return df_clean

if __name__ == "__main__":
    file_name = 'Student Insomnia and Educational Outcomes Dataset_version-2 (1).csv'
    
    try:
        raw_data = load_and_rename(file_name)
        mapped_data = apply_mappings(raw_data)
        final_data = filter_invalid_data(mapped_data)
        
        print(f"--- Thống kê làm sạch ---")
        print(f"Số dòng ban đầu: {len(raw_data)}")
        print(f"Số dòng bị loại bỏ: {len(raw_data) - len(final_data)}")
        print(f"Số dòng sạch còn lại: {len(final_data)}")
        
        # Lưu file
        final_data.to_csv('Student_Mental_Health_Final.csv', index=False)
        print("\n[OK] Làm sạch dữ liệu hoàn tất! Đã lưu file 'Student_Mental_Health_Final.csv'")
        
    except FileNotFoundError:
        print(f"[Lỗi] Không tìm thấy file: {file_name}. Hãy kiểm tra lại tên file!")
    except Exception as e:
        print(f"[Lỗi hệ thống] {e}")
