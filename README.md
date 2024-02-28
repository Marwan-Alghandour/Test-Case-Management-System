# Test Case Management System

## Technology Stack

- Python (Flask)
- flask-smorest
- python-dotenv
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

### Database Schema

- The application uses a SQLite database with the following schema:

  ![image](https://github.com/Marwan-Alghandour/Test-Case-Management-System/assets/73784274/0092a25d-b79e-4a71-b0b1-b0ce6c773049)

  - **subjects**: Contains information about test subjects.
  - **subjects_testcases**: Contains information about test executions.
  - **testcases**: Contains information about testcases.
  - **testcase_steps**: Contains information about testcase steps.
