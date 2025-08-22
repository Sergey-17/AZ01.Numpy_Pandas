import pandas as pd
import io

# Создаем тестовые данные
test_data = {
    'Name': ['Аня', 'Боб', 'Чарли'],
    'City': ['Томск', 'Москва', 'Москва'],
    'Salary': [200000, 350000, 270000]
}

df = pd.DataFrame(test_data)

print("Тестовые данные:")
print(df)

print("\nИнформация о данных:")
print(df.info())

# Записываем в файл
with open('test_output.txt', 'w', encoding='utf-8') as f:
    f.write("ТЕСТОВЫЕ ДАННЫЕ\n")
    f.write("=" * 30 + "\n\n")
    
    f.write("Данные:\n")
    f.write(df.to_string() + "\n\n")
    
    f.write("Информация о данных:\n")
    buffer = io.StringIO()
    df.info(buf=buffer)
    f.write(buffer.getvalue() + "\n")

print("\nРезультат записан в test_output.txt")
