import sqlite3

PATH = "../database/expense_manager.db"

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, username, role
        FROM users
        WHERE username = ? AND password = ?
    """, (username, password))
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        print(f"\nLogin successful. Welcome, {user[1]}!")
        print(f"Role: {user[2]}")
        return user
    else:
        print("Invalid username or password.")
        return None

def main():
    print("===== Revature Expense Manager =====")
    
    user = login()
    
    if user:
        user_id = user[0]
        username = user[1]
        role = user[2]
    
        if role == "employee":
            print("\nEmployee menu goes here.")
        elif role == "manager":
            print("\nManager menu goes here.")
        else:
            print("\nUnknown role.")
        
if __name__ == "__main__":
    main()
