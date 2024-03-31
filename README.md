**Airport Dashboard using Streamlit and SQL**

**Project Overview**

This web application is designed to provide users with a convenient and informative interface to explore their flight data. Users can effortlessly search for flights based on source, destination, and date range, while also gaining valuable insights through interactive charts on the analytics page.

**Key Functionalities**

- **Flight Search:**
  - Users can effortlessly specify their desired source, destination, and date range for flight searches.
  - The application leverages SQL queries to retrieve relevant flight data from a connected database.
  - Search results are presented in a user-friendly format, making it easy to find the flights that match their criteria.

- **Analytics Page:**
  - This page delves deeper into flight data by presenting interactive charts.
  - The first chart, "Busy Airports," is an interactive bar chart that visually depicts the airports with the most frequent flights within the specified date range.
  - The second chart, "Flights by Airline (Freq. Distribution)," employs a frequency distribution visualization to reveal the airlines with the most flights during the chosen timeframe.
  - These charts enable users to identify trends and patterns in their flight data, aiding in informed decision-making.

- **About Page:**
  - This page provides additional information about the project, including its purpose, functionalities, and any relevant technical details.

**Technology Stack**

- **Streamlit:** This Python library serves as the foundation for creating the web application's user interface. Its intuitive API streamlines the development of interactive dashboards.
- **SQL:** Structured Query Language is employed to interact with the database containing flight information. SQL queries enable efficient retrieval and filtering of flight data based on user-provided search criteria.

**Code Structure**

The project's code is likely organized into separate Python files for better maintainability:

- `app.py`: This file serves as the entry point for the application. It initializes Streamlit, establishes the database connection, and defines the web app's layout, including the flight search form, analytics page, and about page.
- `dbhelp.py` : This file might handle functions related to processing user input, constructing SQL queries, and retrieving flight data from the database.

**Running the Application**

1. Navigate to the project directory in your terminal.
2. Execute the main Python file (e.g., `streamlit run app.py`).
3. Streamlit will launch the web app in your default browser, typically at `http://localhost:8501`.
