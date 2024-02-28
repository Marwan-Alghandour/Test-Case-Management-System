# Test Case Management System

## Technology Stack

- Python (Flask)
- Flask-smorest
- Python-dotenv
- Flask-SQLAlchemy (ORM for interacting with the database)
- SQLite (Database)

## Prerequisites

- Python and pip (package installer for Python) installed on your system.
- A code editor (e.g., Visual Studio Code).
- Postman or a similar tool for API testing.

## Getting Started

1. **Clone the repository:**
   ```bash
   https://github.com/Marwan-Alghandour/Test-Case-Management-System.git
   
2. **Navigate to the project directory:**

   ```bash
   cd Test-Case-Management-System

3. **Create an environment:**

   ```bash
   py -3 -m venv .venv

4. **Activate the environment:**

   ```bash
   .venv\Scripts\activate

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

6. **Start the server:**

   ```bash
   flask run

The server should now be running on http://localhost:5000.

## API Reference

### Base URL

- Base URL: `http://localhost:5000`

### Error Handling

- The API follows standard HTTP status codes for error handling.
- In case of an error, you will receive a JSON response with an error message that describes it.

### Endpoints

#### Subject

#### POST /subject

**Description:** Create a new test subject.

**Input:**
- name: name of the subject (required and must be unique).

```json
{
    "name": "login form"
}
```

**Output:**

```json
{
    "created_at": "2024-02-28T19:53:24",
    "id": "1",
    "name": "login form",
    "testcases": [],
    "updated_at": "2024-02-28T19:53:24"
}
```

#### GET /subject

**Description:** Retrieve a list of subject(s).

**No Input**

**Output:**

```json
[
    {
        "created_at": "2024-02-28T19:53:24",
        "id": "1",
        "name": "login form",
        "testcases": [],
        "updated_at": "2024-02-28T19:53:24"
    },
    {
        "created_at": "2024-02-28T20:27:37",
        "id": "2",
        "name": "create user",
        "testcases": [],
        "updated_at": "2024-02-28T20:27:37"
    },
]
```

#### GET /subject/<id>

**Description:** Retrieve information about a specific subject.

**Input:** Subject ID (e.g., /subject/1)

**Output:**

```json
{
    "created_at": "2024-02-28T19:53:24",
    "id": "1",
    "name": "login form",
    "testcases": [],
    "updated_at": "2024-02-28T19:53:24"
}
```

#### PUT /subject/<id>

**Description:** Update information for a specific subject.

**Input:**
- Subject ID (e.g., /subject/1)
- name: name of the subject (required and must be unique).

```json
{
    "name": "Login form"
}
```

**Output:**

```json
{
    "created_at": "2024-02-28T19:53:24",
    "id": "1",
    "name": "Login form",
    "testcases": [],
    "updated_at": "2024-02-28T19:53:24"
}
```

#### DELETE /subject/<id>

**Description:** Delete a specific subject.

**Input:** Subject ID (e.g., /subject/1)

**Output:**

```json
{
    "message": "Subject deleted"
}
```

-------------------------------------------------------------------------------------------------------------

#### Testcase

#### POST /testcase

**Description:** Create a new testcase.

**Input:**
- title: title of the testcase (required and must be unique).
- description: description of the testcase (required).
- expected_output: the expected output of the testcase (required).
- testcase_steps: a list containing the steps to be executed (required).

```json
{
    "title": "Login",
    "description": "Test login functionality",
    "expected_output": "Login successful",
    "testcase_steps": [
        {
            "input": "m@y.com",
            "type": "email"
        },
        {
            "input": "123",
            "type": "password"
        }
    ]
}
```

**Output:**

```json
{
    "created_at": "2024-02-28T19:42:47",
    "description": "Test login functionality",
    "expected_output": "Login successful",
    "id": "1",
    "subjects": [],
    "testcase_steps": [
        {
            "created_at": "2024-02-28T19:42:47",
            "id": "1",
            "input": "m@y.com",
            "type": "email"
        },
        {
            "created_at": "2024-02-28T19:42:47",
            "id": "2",
            "input": "123",
            "type": "password"
        }
    ],
    "title": "Login",
    "updated_at": "2024-02-28T19:42:47"
}
```

#### GET /testcase

**Description:** Retrieve a list of testcase(s).

**No Input**

**Output:**

```json
[
     {
        "created_at": "2024-02-28T19:42:47",
        "description": "Test login functionality",
        "expected_output": "Login successful",
        "id": "1",
        "subjects": [],
        "testcase_steps": [
            {
                "created_at": "2024-02-28T19:42:47",
                "id": "1",
                "input": "m@y.com",
                "type": "email"
            },
            {
                "created_at": "2024-02-28T19:42:47",
                "id": "2",
                "input": "123",
                "type": "password"
            }
        ],
        "title": "Login",
        "updated_at": "2024-02-28T19:42:47"
    },
    {
        "created_at": "2024-02-28T20:27:41",
        "description": "Test creating user functionality",
        "expected_output": "User created successfully",
        "id": "2",
        "subjects": [],
        "testcase_steps": [
            {
                "created_at": "2024-02-28T20:57:05",
                "id": "3",
                "input": "Jack",
                "type": "username"
            },
            {
                "created_at": "2024-02-28T20:57:05",
                "id": "4",
                "input": "5236548",
                "type": "password"
            }
        ],
        "title": "Create User",
        "updated_at": "2024-02-28T20:27:41"
    }
]
```

#### GET /testcase/<id>

**Description:** Retrieve information about a specific testcase.

**Input:** Testcase ID (e.g., /testcase/1)

**Output:**

```json
{
    "created_at": "2024-02-28T19:42:47",
    "description": "Test login functionality",
    "expected_output": "Login successful",
    "id": "1",
    "subjects": [],
    "testcase_steps": [
        {
            "created_at": "2024-02-28T19:42:47",
            "id": "1",
            "input": "m@y.com",
            "type": "email"
        },
        {
            "created_at": "2024-02-28T19:42:47",
            "id": "2",
            "input": "123",
            "type": "password"
        }
    ],
    "title": "Login",
    "updated_at": "2024-02-28T19:42:47"
}
```

#### PUT /testcase/<id>

**Description:** Update information for a specific testcase.

**Input:**
- Testcase ID (e.g., /testcase/1)
- title (optional): title of the testcase (must be unique).
- description (optional): description of the testcase.
- expected_output (optional): the expected output of the testcase.
- testcase_steps (optional): a list containing the steps to be executed.

```json
{
    "testcase_steps": [
        {
            "input": "jack@g.com",
            "type": "email"
        },
        {
            "input": "jack123",
            "type": "password"
        }
    ]
}
```

**Output:**

```json
{
    "created_at": "2024-02-28T19:42:47",
    "description": "Test login functionality",
    "expected_output": "Login successful",
    "id": "1",
    "subjects": [],
    "testcase_steps": [
        {
            "created_at": "2024-02-28T20:26:17",
            "id": "1",
            "input": "jack@g.com",
            "type": "email"
        },
        {
            "created_at": "2024-02-28T20:26:17",
            "id": "2",
            "input": "jack123",
            "type": "password"
        }
    ],
    "title": "Login",
    "updated_at": "2024-02-28T19:42:47"
}
```

#### DELETE /testcase/<id>

**Description:** Delete a specific testcase.

**Input:** Testcase ID (e.g., /testcase/1)

**Output:**

```json
{
    "message": "Testcase deleted"
}
```

-------------------------------------------------------------------------------------------------------------

#### Execution Result

#### POST /subject/<subject_id>/testcase/<testcase_id>

**Description:** Create a new execution result.

**Input:**
- Subject ID (e.g., /subject/1/testcase/1)
- Testcase ID (e.g., /subject/1/testcase/1)
- status: status of the result [succeed or failed] (required).
- actual_output: output resulted from execution (required).
- comment: comment on the execution result (required).

```json
{
    "status": true,
    "actual_output": "login successful",
    "comment": "laggy"
}
```

**Output:**

```json
{
    "actual_output": "login successful",
    "comment": "laggy",
    "created_at": "2024-02-28T20:22:34",
    "id": "1",
    "status": true
}
```

#### GET /subject/<subject_id>/testcase/<testcase_id>

**Description:** Retrieve a list of execution result(s).

**Input:**
- Subject ID (e.g., /subject/1/testcase/1)
- Testcase ID (e.g., /subject/1/testcase/1)

**Output:**

```json
[
    {
        "actual_output": "login successful",
        "comment": "laggy",
        "created_at": "2024-02-28T20:22:34",
        "id": "1",
        "status": true
    },
    {
        "actual_output": "login failed",
        "comment": "problem with server",
        "created_at": "2024-02-28T20:25:34",
        "id": "2",
        "status": false
    }
]
```

### Database Schema

- The application uses a SQLite database with the following schema:

  ![image](https://github.com/Marwan-Alghandour/Test-Case-Management-System/assets/73784274/0092a25d-b79e-4a71-b0b1-b0ce6c773049)

  - **subjects**: Contains information about test subjects.
  - **subjects_testcases**: Contains information about test executions.
  - **testcases**: Contains information about testcases.
  - **testcase_steps**: Contains information about testcase steps.
