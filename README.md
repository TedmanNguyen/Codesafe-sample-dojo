# Homework 6 - Proof of Concept Challenge

## User Story:

**Author:** Theo

**ID:** US-SEC-01

As a student in Codesafe, I want to complete a SQL Injection challenge that shows how insecure login code can be exploited and how to fix it, So that I can learn what insecure code looks like in practice and understand how to write safer login logic.

**Source:** HW6 Challenge Requirement; Team Meeting Transcript (12/02); SQL Injection Starter Code

**Acceptance Criteria:**
- The challenge gives me starter code that intentionally contains an unsafe login function.
- Students observe how SQL injection allows login bypass
- Students implement a secure parameterized SQL query using placeholder syntax Valid username/password combinations successfully authenticate.
- Logging in with correct credentials should still work normally.
- Wrong passwords should fail as expected.
- SQL injection attempts should no longer work after my fix.
- The database should remain intact after my changes.
-The solution must pass all provided test cases.

**Rationale:**
This story helps students gain real experience with a common security flaw. Instead of just reading about SQL injection, they get to see it happen and learn how to stop it, which fits directly with Codesafe’s learning goals.

## Use Case:

`CompleteSQLInjectionChallenge` written by Theo

**Priority:** High

**Source:** HW6 Challenge Requirements; Team Meeting 12/02/2025; SQL Injection Starter Code; Updated HW3 (US-SEC-01)

**Short Description**

A student completes a security challenge in Codesafe that demonstrates how SQL injection works and fixes the vulnerable login code by implementing a parameterized SQL query.

**Goals**

This use case teaches students how insecure SQL queries can be exploited and how to apply a secure fix. 
It supports Codesafe’s goal of providing hands-on cybersecurity learning experiences.

**Primary Actor:** Student

**Secondary Actors: Instructor, Researcher**

**Preconditions**
- The student is logged into Codesafe.
- The SQL Injection challenge is available and loads successfully.
- The starter file (sql_injection_dojo.py) is accessible within the environment.

**Postconditions**
- The student successfully implements a secure login function.
- SQL injection attempts fail.
- All automated test cases pass.

**Main Flow**
1. The student selects the SQL Injection challenge from their Codesafe dashboard.
2. Codesafe loads the starter code, including:
   - a vulnerable login function,
   - a destructive SQL injection example,
   - an incomplete safe_login() function.
3. The student runs the vulnerable login and sees how SQL injection can let someone bypass the login or mess with the database.
4. The student edits safe_login() to use a parameterized SQL query instead of string formatting.
5. The student tests their updated code:
   - valid credentials work,
   - invalid credentials fail,
   - injection attempts no longer succeed.
6. The student submits their solution.
7. Codesafe automatically runs the unit tests to verify correctness.
8. If all tests pass, the challenge is marked complete.

**Alternative Flows**

A1 – The student uses incorrect SQL syntax and encounters an error.  
     The tests fail, and the student revises their code.

A2 – The student removes required output or logic.  
     The automated tests detect this, and the student makes corrections.

**Exceptions**

- Errors caused by using the SQL parameters incorrectly.
- Using unsafe functions (e.g., executescript()) results in test failure.

**Rationale**

This use case provides students with a practical exercise to understand SQL injection and implement secure coding practices in a realistic scenario, reinforcing Codesafe’s educational objectives.

## Scenario Description:

**Scenario: “Quick Fix Login” (SQL injection Dojo)**
You’re a junior developer assisting with administering an internal learning site named CodeSafe. Students learn about software security as they solve challenges. The Dojo staff gets complaints about an unusual login system. Sometimes, it seems as if it executes unexpected commands on the database even for failed login attempts. Your teacher guesses that there might be an SQL injection issue with its login script.

To analyze, you execute the given Python code and choose the hacker option, which mimics an attacker exploiting the system. As you analyze the result, you see that the login functionality builds an SQL query by directly appending user input into an SQL query string. As a result, without user input verification, an attacker attacks an exe uted database query. To demonstrate the attack, an attacker begins with a boolean query like ‘ OR ‘1’ = ‘1, then moves on to a destructive query which deletes all user data from a database.

You assignment is to remediate this issue as realistically and securely as possible. You have a function named safe_login() that is intentionally incomplete. You will complete a parameterized SQL query in the “TO DO” section of the code, so that user input is treated as strictly as data instead of as an executable query.

**Files Provided:**
sql_injection_dojo.py
sql_injection_dojo_tests.py

**Instructions:**
Look at the vulnerable_login function and analyze it carefully to learn more about what unsound sql query construction represents.
Use parameterized SQL queries with placeholders for user data within a function named safe_login(conn)
Execute these unit tests to check your solution, all tests should pass when “TO DO” is complete and correct.

This should take approximately 30-60 minutes to solve this challenge, good luck!


## Starter Code:

`sql_injection_dojo.py` written by Tedman


## Test Cases:

`sql_injection_dojo_tests` written by Emily


## Intended Solution:

`intended_solution.py` written by Leon
