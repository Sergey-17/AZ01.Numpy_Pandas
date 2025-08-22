import pandas as pd
import numpy as np
import io

def analyze_automobile_data():
    """
    Анализ данных из Automobile_data.csv
    """
    print("=" * 60)
    print("АНАЛИЗ ДАННЫХ ИЗ AUTOMOBILE_DATA.CSV")
    print("=" * 60)
    
    try:
        # Загружаем данные из Automobile_data.csv
        df_auto = pd.read_csv('Automobile_data.csv')
        
        print("\n1. Первые 5 строк данных:")
        print(df_auto.head())
        
        print("\n2. Информация о данных:")
        print(df_auto.info())
        
        print("\n3. Статистическое описание:")
        print(df_auto.describe())
        
        # Сохраняем результаты анализа в файл
        with open('Automobile_data.txt', 'w', encoding='utf-8') as f:
            f.write("АНАЛИЗ ДАННЫХ ИЗ AUTOMOBILE_DATA.CSV\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("1. Первые 5 строк данных:\n")
            f.write(df_auto.head().to_string() + "\n\n")
            
            f.write("2. Информация о данных:\n")
            # Захватываем вывод .info() в строку
            buffer = io.StringIO()
            df_auto.info(buf=buffer, max_cols=None)
            f.write(buffer.getvalue() + "\n\n")
            
            f.write("3. Статистическое описание:\n")
            f.write(df_auto.describe().to_string() + "\n\n")
            
            f.write(f"Размер данных: {df_auto.shape}\n")
        
        print(f"\nРезультаты анализа сохранены в файл: Automobile_data.txt")
        
        return df_auto
        
    except FileNotFoundError:
        print("Ошибка: Файл Automobile_data.csv не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла Automobile_data.csv: {e}")
        return None

def analyze_dz_data():
    """
    Анализ данных из dz.csv с обработкой пропусков
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ ДАННЫХ ИЗ DZ.CSV")
    print("=" * 60)
    
    try:
        # Загружаем данные из dz.csv
        df_dz = pd.read_csv('dz.csv')
        
        print("\n1. Все строки данных:")
        print(df_dz.to_string())
        
        print("\n2. Информация о данных:")
        print(df_dz.info())
        
        print("\n3. Количество пропусков:")
        print(df_dz.isnull().sum())
        
        # Обработка пропусков по зарплате
        print("\n4. Обработка пропусков по зарплате...")
        
        # Создаем копию для безопасной работы
        df_processed = df_dz.copy()
        
        # Заполняем пропуски по зарплате медианой по городу
        # Если город не заполнен - зарплата = 0
        for city in df_processed['City'].dropna().unique():
            city_mask = df_processed['City'] == city
            city_salary_median = df_processed.loc[city_mask, 'Salary'].median()
            
            # Заполняем пропуски по зарплате для данного города
            salary_mask = city_mask & df_processed['Salary'].isnull()
            df_processed.loc[salary_mask, 'Salary'] = city_salary_median
        
        # Для строк без города устанавливаем зарплату = 0
        no_city_mask = df_processed['City'].isnull() & df_processed['Salary'].isnull()
        df_processed.loc[no_city_mask, 'Salary'] = 0
        
        print("Пропуски по зарплате обработаны!")
        
        print("\n5. Количество пропусков после обработки:")
        print(df_processed.isnull().sum())
        
        print("\n6. Все скорректированные строки данных:")
        print(df_processed.to_string())
        
        # Определяем среднюю зарплату по городам
        print("\n7. Средняя зарплата по городам:")
        city_salary_avg = df_processed.groupby('City')['Salary'].agg(['mean', 'count']).round(2)
        city_salary_avg.columns = ['Средняя зарплата', 'Количество записей']
        print(city_salary_avg)
        
        # Медианная зарплата по городам
        print("\n8. Медианная зарплата по городам:")
        city_salary_median = df_processed.groupby('City')['Salary'].agg(['median', 'count']).round(2)
        city_salary_median.columns = ['Медианная зарплата', 'Количество записей']
        print(city_salary_median)
        
        # Общая статистика по зарплате
        print("\n9. Общая статистика по зарплате:")
        print(f"Общая средняя зарплата: {df_processed['Salary'].mean():.2f}")
        print(f"Медианная зарплата: {df_processed['Salary'].median():.2f}")
        print(f"Минимальная зарплата: {df_processed['Salary'].min():.2f}")
        print(f"Максимальная зарплата: {df_processed['Salary'].max():.2f}")
        
        # Сохраняем результаты анализа в файл
        with open('dz.txt', 'w', encoding='utf-8') as f:
            f.write("АНАЛИЗ ДАННЫХ ИЗ DZ.CSV\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("1. Все строки данных:\n")
            f.write(df_dz.to_string() + "\n\n")
            
            f.write("2. Информация о данных:\n")
            # Захватываем вывод .info() в строку
            buffer = io.StringIO()
            df_dz.info(buf=buffer, max_cols=None)
            f.write(buffer.getvalue() + "\n\n")
            
            f.write("3. Количество пропусков:\n")
            f.write(df_dz.isnull().sum().to_string() + "\n\n")
            
            f.write("4. Обработка пропусков по зарплате:\n")
            f.write("- Заполнение медианой по городу\n")
            f.write("- Установка зарплаты = 0 для строк без города\n\n")
            
            f.write("5. Количество пропусков после обработки:\n")
            f.write(df_processed.isnull().sum().to_string() + "\n\n")
            
            f.write("6. Все скорректированные строки данные:\n")
            f.write(df_processed.to_string() + "\n\n")
            
            f.write("7. Средняя зарплата по городам:\n")
            f.write(city_salary_avg.to_string() + "\n\n")
            
            f.write("8. Медианная зарплата по городам:\n")
            f.write(city_salary_median.to_string() + "\n\n")
            
            f.write("9. Общая статистика по зарплате:\n")
            f.write(f"Общая средняя зарплата: {df_processed['Salary'].mean():.2f}\n")
            f.write(f"Медианная зарплата: {df_processed['Salary'].median():.2f}\n")
            f.write(f"Минимальная зарплата: {df_processed['Salary'].min():.2f}\n")
            f.write(f"Максимальная зарплата: {df_processed['Salary'].max():.2f}\n\n")
            
            f.write(f"Размер данных: {df_processed.shape}\n")
        
        print(f"\nРезультаты анализа сохранены в файл: dz.txt")
        
        return df_processed
        
    except FileNotFoundError:
        print("Ошибка: Файл dz.csv не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла dz.csv: {e}")
        return None

def main():
    """
    Основная функция для последовательного анализа данных
    """
    print("НАЧАЛО АНАЛИЗА ДАННЫХ")
    print("=" * 60)
    
    # Анализ данных из Automobile_data.csv
    df_auto = analyze_automobile_data()
    
    # Анализ данных из dz.csv
    df_dz = analyze_dz_data()
    
    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЕН")
    print("=" * 60)
    
    if df_auto is not None:
        print(f"Данные из Automobile_data.csv успешно загружены. Размер: {df_auto.shape}")
    
    if df_dz is not None:
        print(f"Данные из dz.csv успешно загружены и обработаны. Размер: {df_dz.shape}")
    
    print("\nРезультаты анализа сохранены в файлы:")
    print("- Automobile_data.txt")
    print("- dz.txt")

if __name__ == "__main__":
    main()
