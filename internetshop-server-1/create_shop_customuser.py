import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Создание таблицы shop_customuser
cursor.execute('''
CREATE TABLE IF NOT EXISTS shop_customuser (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP NULL,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    is_approved BOOLEAN NOT NULL,
    UNIQUE(username)
)
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Таблица shop_customuser успешно создана.")
