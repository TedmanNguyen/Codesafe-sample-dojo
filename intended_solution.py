def safe_login(conn):
    cursor = conn.cursor()

    print("\n=== SAFE LOGIN SYSTEM (PARAMETERIZED QUERY) ===")
    print("Students: Fill in the parameterized query below.\n")

    user = input("Enter username: ")
    pwd = input("Enter password: ")

    # -----------------------------------------
    # Intended solution:
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
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