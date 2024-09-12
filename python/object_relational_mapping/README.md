# Using databases(docker) with fastapi

## Steps

### Create a Vm in aws and use vscode Remote server extention to connect and work on it 

```vscode
ctrl + shift + p
Remote-SSH-:Connect to Host..
Add New SSH Host..
```

#### config:
```yaml
Host <public-ip>
  HostName <public-ip>
  User <user-name>
  IdentityFile C:\\Users\\<user-name>\\Downloads\\<pem-file>
```

### Creation of Virtual Environment for Python development

```bash
python3 --version
sudo apt update
sudo add-apt-repository universe
sudo apt update
sudo apt install python3-pip
python3 -m venv .venv
source .venv/bin/activate
sudo apt install python3-pip
pip3 install "fastapi[standard]"
```
[Refer here](https://docs.docker.com/engine/install/) for Docker installation commands

#### commands:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
```bash
# for latest version and Verify that the Docker Engine installation is successful running
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world
sudo usermod -aG docker <USER>
```
### docker-compose.yml

* create a docker compose file in the project

```yaml
# sample file

services:
  db:
    image: postgres:13.2  # Use the specified PostgreSQL image
    container_name: postgres  # Name the container
    restart: always  # Restart the container automatically
    environment:
      - POSTGRES_USER=user  # Set the PostgreSQL user
      - POSTGRES_PASSWORD=password  # Set the PostgreSQL password
      - POSTGRES_DB=library  # Set the initial database name
    ports:
      - "5432:5432"  # Map port 5432 on the host to port 5432 in the container
    volumes:
      - postgres_data:/var/lib/postgresql/data  # Persist data in a named volume

  library:
    build:
      context: .  # Build the image from the current directory
      dockerfile: Dockerfile  # Specify the Dockerfile to use
    container_name: fastapi  # Name the container
    restart: always  # Restart the container automatically
    ports:
      - "8000:8000"  # Map port 8000 on the host to port 8000 in the container
    depends_on:
      - db  # Ensure the db service starts before this service
    environment:
      - DATABASE_URL=postgresql://user:password@db/library  # Connection string for the database
    volumes:
      - .:/library  # Mount the current directory to /library in the container
    command: uvicorn src.main:library --reload --workers 1 --host 0.0.0.0 --port 8000  # Command to run the FastAPI app

volumes:
  postgres_data:  # Define a named volume for PostgreSQL data
```

#### command to start the services defined in the Docker Compose file:

```bash
# To Create and Start the Database Service:
docker compose up db -d

# To Stop and Remove Containers on Error:
docker compose down --rmi local -v

# docker logs
docker compose logs library-api

# lists the Docker containers that are running
docker compose ps
```

- docker compose up db -d
    -   This command starts the db service (PostgreSQL) in detached mode (-d), allowing it to run in the background.

-   docker compose down --rmi local -v
    -   `--rmi local`: This removes any images that were built locally.
    -   `-v`: This removes the named volumes declared in the `volumes` section of the Compose file, ensuring that all data is deleted.

### Connecting to Database Service running on Containers through Azure data studio

* install postgres extention
* provide the details and connect (make sure port 5432 open on security group of ec2)

---

### ORM Frameworks (SQLAlchemy)

* ORM Frameworks(object-relational mapping) : Java - Hibernate, dotnet - Entity Framework, Python - SQLAlchemy and there are many more librarys.

-   Generally for interacting with databases, we use SQL [Refer Here](https://www.w3schools.com/postgresql/index.php)

####   Introduction to ORM Frameworks

-   ORM (Object Relational Mapping) Frameworks help map database tables to Python classes. This allows developers to interact with the database using objects rather than writing specific SQL queries for each database type (SQL Server, Oracle, PostgreSQL, MySQL).

##### Key Features of ORM Frameworks

    *   Mappings: We create mappings between database tables and Python classes. This allows us to perform CRUD (Create, Read, Update, Delete) operations using objects instead of SQL queries.
    *   Abstraction: ORM frameworks provide an abstraction layer between the application code and the database, making it easier to work with databases in an object-oriented way.
-   In python, SQLAlchemy is a popular SQL toolkit and Object Relational Mapper, using which classes can be mapped to the database 

### using SQL Alchemy in fast api project

#### File structure
```
.
└── sql_app
    ├── __init__.py # __init__.py is just an empty file, makes folder Package
    ├── crud.py # CRUD comes from: **C**reate, **R**ead, **U**pdate, and **D**elete.
    ├── database.py # Import the SQLAlchemy parts(engine, Session maker, Base Class)
    ├── main.py
    ├── models.py # Create the database models from Base Class
    └── schemas.py
```
[Refer Here](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-base-class) for Setup
[Refer Here](https://www.tutorialspoint.com/sqlalchemy/index.htm) for tutorial

```bash
pip3 install SQLAlchemy
sudo apt install libpq-dev python3-dev
# do this if error on psycopg2 installation on ubuntu, TO Ensure you have the necessary build dependencies
pip3 install psycopg2
# this is specifically needed by SQLAlchemy to communicate with Postgres Database
```

[Refer Here](https://fastapi.tiangolo.com/tutorial/sql-databases/#orms) for documentation and dependences

---

#### Environment variables 

Environment variables are commonly used To:

1. Separating Configuration from Code
    * Environment variables allow you to separate configuration details from your application code. This makes your code more portable and easier to maintain. You can change configuration settings without modifying the code itself

2. Storing Sensitive Information
    * Environment variables are commonly used to store sensitive information like API keys, database credentials, and secret keys.

3. Managing Different Environments, etc..

#### python-dotenv

* python-dotenv is a Python library that allows you to load environment variables from a .env file into your Python project. 
It provides a convenient way to manage sensitive information like API keys, database credentials, and other configuration settings

* To use python-dotenv, you need to install it using pip:

```bash
pip3 install python-dotenv
```
* Create a .env file in the root directory of your project. This file will contain your environment variables in the format KEY=VALUE. For example:

```bash
DEBUG=True
SECRET_KEY=mysecretkey
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
```
* In your Python script, import the load_dotenv function from the dotenv module 
and call it to load the variables from the .env file into your environment

```bash
import os
from dotenv import load_dotenv

load_dotenv()

debug = os.getenv('DEBUG')
secret_key = os.getenv('SECRET_KEY')
database_url = os.getenv('DATABASE_URL')

print(f"Debug: {debug}\nSecret Key: {secret_key}\nDatabase URL: {database_url}")
```

##### Best practices:
    * Provide default values for environment variables using os.getenv('VARIABLE_NAME', 'default_value') in case the variable is not found.
    * Keep the .env file secure by adding it to your .gitignore file to prevent it from being tracked by version control systems
    * Use different .env files for different environments (e.g., .env.dev, .env.prod) and load 
    the appropriate one based on the environment your application is running in

---

#### SQLAlchemy Engine

* The SQLAlchemy engine is the starting point for any SQLAlchemy application. 
It serves as the interface for connecting to a specific database and managing the connection pool.

[Refer here](https://fastapi.tiangolo.com/tutorial/sql-databases/#import-the-sqlalchemy-parts) creating a database URL for SQLAlchemy

*   Engine:
    *   create_engine() creates a connection to the database. It manages connections and allows you to execute SQL commands.
*   Session Factory:
    *   sessionmaker() creates a factory for database sessions. Sessions are used to interact with the database (e.g., adding, querying, and updating records).
*   Base Class:
    *   declarative_base() creates a base class for your SQLAlchemy models. You will define your database tables as classes that inherit from this base class.

[Refer Here](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-database-url-for-sqlalchemy) for more detailed of creating the SQLAlchemy parts

```Python
# Sample Code (sql_app/database.py)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sql_app.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

---

#### Create SQLAlchemy models from the Base class

* sql_app/models.py
    *   Define's the Struture and feilds of the table
    *   __tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models

[Refer here](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-sqlalchemy-models-from-the-base-class) for Process

#### SQLAlchemy style and Pydantic style

*   Notice that SQLAlchemy _models_ define attributes using `=`, and pass the type as a parameter to `Column`, like in:

`name = Column(String)`

*   while Pydantic models declare the types using :, the new type annotation syntax/type hints:

`name: str`

*   Keep these in mind, so you don't get confused when using = and : with them.

---

#### get_db() method for yield database Connection

*   write a get_db method in your database.py file to yield a database connection using SQLAlchemy. 
This method is commonly used in applications, especially with frameworks like FastAPI, to provide a database session for each request.

```Python# Dependency to get a database session

def get_db() -> Session:
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used
    finally:
        db.close()  # Close the session when done
```
---

```Python@app.get("/books", response_model= list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    """function for getting all the books from database"""
    books = db.query(Books).all()  # Query to get all books
    return books
```
* db: Session = Depends(get_db) is a way to inject a database session dependency(from db) into a FastAPI path operation function using the Depends function.

```python
@app.post("/books", response_model= Books)
def create_book(request: BookRequest, db: Session = Depends(get_db)):
    """create book"""
    db_book = Books(**request.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
```

Certainly! Let’s delve deeper into the line of code `db_book = Books(**request.model_dump())` in the context of the `Books` SQLAlchemy model you provided. 

## Breakdown of the Code

### 1. **Understanding `request.model_dump()`**

- **`request`**: In a web application context (like FastAPI or Flask), the `request` object typically represents an incoming HTTP request. It contains data sent by the client, which can include form data, JSON payloads, query parameters, etc.

- **`model_dump()`**: This method is part of a Pydantic model. When called on a Pydantic model instance, it converts the instance's data into a dictionary format. This dictionary contains key-value pairs where the keys correspond to the field names of the model, and the values are the data associated with those fields.

For example, if the `request` object contains the following data:
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780743273565",
  "published_date": "1925-04-10"
}
```
Calling `request.model_dump()` would produce a dictionary like:
```python
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780743273565",
  "published_date": "1925-04-10"
}
```

### 2. **Unpacking the Dictionary with `**`**

- The `**` operator is used to unpack the dictionary returned by `model_dump()`. This means that each key-value pair in the dictionary is passed as a separate keyword argument to the `Books` constructor.

### 3. **Creating the `Books` Instance**

- **`Books(**request.model_dump())`**: This part of the code initializes a new instance of the `Books` model. The unpacked dictionary provides the necessary data to populate the model's fields.

For instance, if the dictionary from `model_dump()` is as shown above, the following call:
```python
db_book = Books(**request.model_dump())
```
is equivalent to:
```python
db_book = Books(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    isbn="9780743273565",
    published_date="1925-04-10"
)
```

### 4. **Resulting Instance**

- After executing this line, `db_book` will be an instance of the `Books` model populated with the data from the request. This instance can then be used to interact with the database, such as saving it to the database or performing further operations.


---

#### Response models

*   Response models in FastAPI are Pydantic models that define the structure of the data returned by an API endpoint. 
They specify what fields are included in the response and their types, ensuring that the API responses are consistent and well-documented.

#### Request models
*   Request models are also Pydantic models that define the structure of the data expected in the request body 
when a client makes a request to an API endpoint. 
*   They specify the required fields and their types for incoming requests.

```Python
@app.get("/books", response_model=list[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """This method gets all the books 
    """
    return db.query(Books).all()


@app.post("/books", response_model= BookResponse)
def create_book(request: BookRequest, db: Session = Depends(get_db)):
    """create book"""
    db_book = Books(**request.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
```
