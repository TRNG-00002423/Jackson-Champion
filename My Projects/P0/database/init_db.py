import sqlite3

conn = sqlite3.connect("expense_manager.db")
cursor = conn.cursor()

#Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

cursor.execute("""
INSERT OR IGNORE INTO users
(username, password, role)
VALUES
('employee1', 'password123', 'employee')
""")

cursor.execute("""
INSERT OR IGNORE INTO users
(username, password, role)
VALUES
('manager1', 'admin123', 'manager')
""")

#Expenses Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    description TEXT,
    date_submitted TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

#approvals Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS approvals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    reviewer INTEGER,
    comment TEXT,
    review_date TEXT,
    FOREIGN KEY (expense_id) REFERENCES expenses(id),
    FOREIGN KEY (reviewer) REFERENCES users(id)
)
""")




conn.commit()
conn.close()

print("Database initialized")
