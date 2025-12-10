# Homework 6 - Proof of Concept Challenge

## User Story:

Author: Theo
ID: US-SEC-01

As a student in Codesafe, I want to complete a SQL Injection challenge that shows how insecure login code can be exploited and how to fix it, So that I can learn what insecure code looks like in practice and understand how to write safer login logic.

Source: HW6 Challenge Requirement; Team Meeting Transcript (12/02); SQL Injection Starter Code

Acceptance Criteria:
- The challenge gives me starter code that intentionally contains an unsafe login function.
- Students observe how SQL injection allows login bypass
- Students implement a secure parameterized SQL query using placeholder syntax Valid username/password combinations successfully authenticate.
- Logging in with correct credentials should still work normally.
- Wrong passwords should fail as expected.
- SQL injection attempts should no longer work after my fix.
- The database should remain intact after my changes.
-The solution must pass all provided test cases.

Rationale:
This story helps students gain real experience with a common security flaw. Instead of just reading about SQL injection, they get to see it happen and learn how to stop it, which fits directly with Codesafe’s learning goals.

## Use Case:

`CompleteSQLInjectionChallenge` written by Theo

Priority
High

Source
HW6 Challenge Requirements; Team Meeting 12/02/2025; SQL Injection Starter Code; Updated HW3 (US-SEC-01)

Short Description
A student completes a security challenge in Codesafe that demonstrates how SQL injection works and fixes the vulnerable login code by implementing a parameterized SQL query.

Goals
This use case teaches students how insecure SQL queries can be exploited and how to apply a secure fix. 
It supports Codesafe’s goal of providing hands-on cybersecurity learning experiences.

Primary Actor
Student

Secondary Actors
Instructor, Researcher

Preconditions
- The student is logged into Codesafe.
- The SQL Injection challenge is available and loads successfully.
- The starter file (sql_injection_dojo.py) is accessible within the environment.

Postconditions
- The student successfully implements a secure login function.
- SQL injection attempts fail.
- All automated test cases pass.

Main Flow
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

Alternative Flows
A1 – The student uses incorrect SQL syntax and encounters an error.  
     The tests fail, and the student revises their code.

A2 – The student removes required output or logic.  
     The automated tests detect this, and the student makes corrections.

Exceptions
- Errors caused by using the SQL parameters incorrectly.
- Using unsafe functions (e.g., executescript()) results in test failure.

Rationale
This use case provides students with a practical exercise to understand SQL injection and implement secure coding practices in a realistic scenario, reinforcing Codesafe’s educational objectives.

## Scenario Description:

`DESCRIPTION.md` written by Stefan

## Starter Code:

`sql_injection_dojo.py` written by Tedman


## Test Cases:

`sql_injection_dojo_tests` written by Emily


## Intended Solution:

`intended_solution.py` written by Leon
