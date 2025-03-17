# Chat with Database App

This project is a Streamlit-based AI-powered SQL query application that allows users to interact with a MySQL database using natural language. The app uses LangChain, OpenAI, and DeepSeek API to generate and execute SQL queries dynamically.

## Features

Natural Language to SQL Conversion: Users can ask database-related questions in natural language, and the app will generate SQL queries.

AI-Powered Query Explanation: The app provides human-readable explanations for SQL query results.

Streamlit UI: Interactive web-based UI for user queries.

Docker Support: Fully containerized using Docker and docker-compose.

MySQL Integration: Works with a MySQL database for querying and data retrieval.


## Installation & Setup

### Clone the Repository

git clone https://github.com/ShohelAlMahmudDev/ChatWithDatabase.git
cd ChatWithDatabase

### Setup Environment Variables

Create a .env file in the root directory and set up the following:

MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_HOST=db  # Use 'db' when running in Docker, 'localhost' otherwise
MYSQL_DB=my_database
DEEPSEEK_API_KEY=your_deepseek_api_key

### Install Dependencies

If running locally (without Docker):

pip install -r requirements.txt

## Running with Docker

The project is fully containerized. To run it using Docker:

### Build and Start Containers

docker-compose up --build

### Access the App

Once running, open your browser and go to:

http://localhost:8501

### Stopping the App

To stop and remove containers, run:

docker-compose down

## Development & Testing

Running Locally (Without Docker)

If you prefer running the app without Docker, ensure MySQL is running, and then execute:

streamlit run app/main.py

## Functionality

Key Functions

Database Connection (``)

Establishes a connection with MySQL using SQLAlchemy.

Query Execution (``)

Converts user queries into SQL using LangChain & DeepSeek.

Executes SQL queries and retrieves results.

Utility Functions (``)

Extracts and cleans SQL queries.

Formats responses for better readability.

### Technologies Used

Python (Streamlit, LangChain, SQLAlchemy, OpenAI, DeepSeek)

MySQL (for database storage and querying)

Docker & Docker Compose (for containerization)

### Troubleshooting

### MySQL Connection Issues

If you see an error connecting to MySQL inside Docker:

Ensure docker-compose is running: docker-compose ps

Check MySQL logs: docker logs mysql-db

Restart the database container: docker-compose restart db

### Environment Variables Not Loading

Make sure you have created the .env file correctly and run:

source .env  # On Linux/macOS
set -o allexport; source .env; set +o allexport  # On Windows (Git Bash)

## License

This project is MIT licensed. Feel free to use and modify it as needed.

## Future Improvements

* Add support for PostgreSQL and other databases 
* Implement authentication for secure API access 
* Enhance query optimization and result visualization

### Contributing

We welcome contributions! Feel free to fork this repo and submit PRs.

