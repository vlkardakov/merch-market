import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Удаление таблиц, если они существуют
cursor.execute('DROP TABLE IF EXISTS shop_customuser_groups')
cursor.execute('DROP TABLE IF EXISTS shop_customuser')

# Создание таблицы shop_customuser
cursor.execute('''
CREATE TABLE shop_customuser (
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
    birth_date DATE NOT NULL,
    is_approved BOOLEAN NOT NULL,
    UNIQUE(username)
)
''')

# Создание таблицы shop_customuser_groups
cursor.execute('''
CREATE TABLE shop_customuser_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customuser_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (customuser_id) REFERENCES shop_customuser(id),
    FOREIGN KEY (group_id) REFERENCES auth_group(id)
)
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Таблицы shop_customuser и shop_customuser_groups успешно пересозданы.")
