# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a simple REST API using Python and FastAPI that exposes endpoints for working with a collection of items and demonstrates common API patterns such as reading, creating, and updating data.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a basic FastAPI application and define the main app instance and a simple in-memory data model for your API.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Define a resource such as `items`, `tasks`, or `books`
- Use a simple in-memory list or dictionary to store data while the app is running
- Start the app with a local development server command
- Confirm the app loads successfully and the root endpoint responds

### 🛠️ Build CRUD Endpoints

#### Description
Implement the main REST endpoints for creating, reading, and updating records in your API.

#### Requirements
Completed program should:

- Add a `GET` endpoint to list all records
- Add a `GET` endpoint to fetch one record by ID
- Add a `POST` endpoint to create a new record
- Add a `PUT` endpoint to update an existing record
- Return JSON data in a clear, consistent format
- Handle invalid or missing IDs gracefully with appropriate HTTP responses
- Use FastAPI request and response models to structure the API input and output
