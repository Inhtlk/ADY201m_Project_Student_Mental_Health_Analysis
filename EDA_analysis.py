import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cấu hình chung cho biểu đồ
sns.set_theme(style="whitegrid")

def plot_correlation(df):
    """1. Vẽ ma trận tương quan"""
    plt.figure(figsize=(12, 10))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix of Academic & Sleep Factors", fontsize=15, fontweight='bold')
    plt.show()

def plot_distributions(df):
    """2. Vẽ biểu đồ phân phối Risk và Burnout"""
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df['Sleep_Hygiene_Risk'], kde=True, color='teal')
    plt.title('Distribution of Sleep Hygiene Risk')
    plt.subplot(1, 2, 2)
    sns.histplot(df['Academic_Burnout_Score'], kde=True, color='coral')
    plt.title('Distribution of Academic Burnout Score')
    plt.tight_layout()
    plt.show()

def plot_stress_pie(df):
    """3. Vẽ biểu đồ tròn thể hiện tỷ trọng stress"""
    plt.figure(figsize=(8, 8))
    stress_counts = df['Academic_Stress_Level'].value_counts().sort_index()
    labels = ['No Stress (0)', 'Low (1)', 'High (2)', 'Extremely High (3)']
    colors = ['#8fd9b6', '#f2c46d', '#f29c38', '#e65539']
    plt.pie(stress_counts, labels=labels, autopct='%1.1f%%', startangle=140,
            colors=colors, textprops={'fontsize': 12, 'fontweight': 'bold'},
            explode=(0.05, 0.05, 0.05, 0.05)) 
    plt.title('Total Stress Distribution', fontsize=15, fontweight='bold')
    plt.show()

def plot_hygiene_vs_stress(df):
    """4. Mối quan hệ giữa Vệ sinh giấc ngủ và Stress"""
    plt.figure(figsize=(9, 6))
    ax = sns.barplot(x='Academic_Stress_Level', y='Sleep_Hygiene_Risk', data=df,
                     hue='Academic_Stress_Level', palette='Blues_r', legend=False, errorbar=None)
    plt.title('Sleep Hygiene Risk vs Stress Level', fontsize=14, fontweight='bold')
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=11, fontweight='bold')
    plt.show()

def plot_gpa_stress_relationship(df):
    """5. Mối quan hệ giữa Stress và GPA"""
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='GPA_Rating', y='Academic_Stress_Level', data=df,
                     palette='viridis', hue='GPA_Rating', legend=False, errorbar=None)
    plt.title('Average Academic Stress Level across GPA Ratings', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('GPA Rating (1=Poor to 5=Excellent)')
    plt.ylabel('Mean Academic Stress Level (0-3)')
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=11, fontweight='bold')
    plt.show()

# --- KHỐI THỰC THI ---
if __name__ == "__main__":
    try:
        df = pd.read_csv('Student_Mental_Health_Final.csv')
        
        # Tạo lại các cột tính toán nếu chưa có
        if 'Sleep_Hygiene_Risk' not in df.columns:
            df['Sleep_Hygiene_Risk'] = df['Phone_Usage_Before_Sleep'] * df['Difficulty_Falling_Asleep']
        if 'Academic_Burnout_Score' not in df.columns:
            df['Academic_Burnout_Score'] = df['Sleep_Impact_on_Deadlines'] * df['Sleep_Impact_on_Concentration']

        # GỌI HÀM (Đã sửa tên hàm ở đây)
        plot_correlation(df)
        plot_distributions(df)
        plot_stress_pie(df)
        plot_hygiene_vs_stress(df)
        plot_gpa_stress_relationship(df) # <-- Đã sửa từ plot_gpa_vs_stress thành tên này
        
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'Student_Mental_Health_Final.csv'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")