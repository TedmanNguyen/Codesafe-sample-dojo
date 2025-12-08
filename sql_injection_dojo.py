import sqlite3
import time

def setup_database():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE users (
            username TEXT,
            password TEXT
        )
    """)

    users = [
    ("alice", "password123"),
    ("bob", "hunter2"),
    ("admin", "super_secret_admin_password"),
    ("charlie", "letmein"),
    ("diana", "qwerty!@#"),
    ("eve", "correcthorsebatterystaple"),
    ("frank", "p4ssw0rd"),
    ("grace", "sunshine123"),
    ("heidi", "ilovepizza"),
    ("leon", "mysterious_3rd_option"),
    ("stefan", "formattingismypassion"),
    ("emily", "overwatch_gurl"),
    ("theo", "lurkingintheshadows"),
    ("ivan", "dragonfire"),
    ("judy", "monkeyking"),
    ("mallory", "trustno1"),
    ("oscar", "coffee_is_life"),
    ("peggy", "abc12345"),
    ("trent", "securepa55"),
    ("victor", "purpleelephant"),
    ("wendy", "swordfish"),
]
    cursor.executemany("INSERT INTO users VALUES (?, ?)", users)
    conn.commit()
    return conn

def print_database(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM users")
    rows = cursor.fetchall()

    print("\n=== DATABASE CONTENTS ===")
    print("Number, User, Password")
    if rows:
        for row in rows:
            print(row)
    else:
        print("(EMPTY TABLE)")
    print("=================================\n")

def vulnerable_login(conn):
    cursor = conn.cursor()

    print("Try username: ' OR '1'='1 ")
    print("Try password: anything ")

    user = input("Enter username: ")
    pwd = input("Enter password: ")

    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}'"

    print("\n[System] Attempting Login...")
    time.sleep(1)

    # --- NEW: Detect if the input contains SQL injection characters ---
    sql_keywords = ["'", "\"", ";", "--", " OR ", " AND ", "="]

    injection_pattern = any(keyword in user.upper() for keyword in sql_keywords)

    try:
        # executescript tolerates injection
        cursor.executescript(query)
        result = cursor.fetchall()

    except Exception as e:
        print("[SQL ERROR]", e)
        return False, False  # no phase 2

    # --- NEW NORMAL LOGIN BEHAVIOR ---
    # If result contains an actual matching user, log them in
    real_match_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(real_match_query, (user, pwd))
    real_match = cursor.fetchall()

    if real_match:
        print("[System] You are logged in!")
        return True, False  # do NOT treat valid login as injection

    # ----------------------------------------------------------------

    # If SQL ran without error AND input contained SQL syntax → treat as injection
    if injection_pattern:
        print("[System] Log in failed.")
        return True, True  # successful run, but injection detected

    # Normal wrong password scenario
    print("[System] Log in failed.")
    return True, False


def destructive_attack(conn):
    cursor = conn.cursor()

    print("\n=== PHASE 2: DESTRUCTIVE SQL INJECTION ===")
    print("Try username: '; DELETE FROM users; --")
    print("Try password: anything ")

    user = input("Enter username: ")
    pwd = input("Enter password: ")

    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}'"

    print("\n[System] Attempting Login...")
    print(query)

    try:
        cursor.executescript(query)
        time.sleep(5)
    except Exception as e:
        print("[SQL ERROR]", e)

    
#TODO - Implement a safer login method that does not use user and pwd directly.
def safe_login(conn):
    cursor = conn.cursor()

    print("\n=== SAFE LOGIN SYSTEM (PARAMETERIZED QUERY) ===")
    print("Students: Fill in the parameterized query below.\n")

    user = input("Enter username: ")
    pwd = input("Enter password: ")

    # -----------------------------------------
    # Student fills this in:
    query = ""   # They must fix this
    # -----------------------------------------

    print("\n[DEBUG] Executing...")
    time.sleep(1)

    try:
        cursor.execute(query, (user, pwd))
        result = cursor.fetchall()

    except Exception as e:
        print("\nLOGIN IMPLEMENTATION FAILED")
        print("[ERROR]", e)
        return

    if result:
        print("[System] You are logged in!")
        print(result)
    else:
        print("[System] Log in failed.")


def hacker_demo():
    conn = setup_database()

    print("\n--- DATABASE AT START ---")
    print("- HACKER DOES NOT SEE THIS -")
    print_database(conn)

    print("\n--- PHASE 1: TESTING FOR INJECTION ---")
    success, injection_found = vulnerable_login(conn)

    if injection_found:
        print("\n[Attacker] Login failed, but I detected a slight server delay...")
        time.sleep(1)
        print("[Attacker] This system is not santizing SQL queries!")
        time.sleep(1)
        print("[Attacker] Let's delete ALL user records")
        destructive_attack(conn)
    else:
        print("\n[Attacker] No injection indicators detected. Stopping.")
        return

    print("\n--- DATABASE AFTER PHASE 2 (SHOULD BE EMPTY) ---")
    print_database(conn)
    print("[Attacker] Got 'em!")

def test_safe_login():
    conn = setup_database()
    print("\n--- SAFE LOGIN TEST MODE ---")
    safe_login(conn)

def main():
    print("Type 'hacker' to run SQL injection demo")
    print("Type 'test' to test the safe login system\n")

    mode = input("Select mode: ").strip().lower()

    if mode == "hacker":
        hacker_demo()
    elif mode == "test":
        test_safe_login()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
