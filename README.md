# QMS Kiosk API

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Overview

The API for the QMS Kiosk Application.

## Requirements

- Python 3.7+
- Install dependencies using `pip install -r requirements.txt`

## Installation

1. Clone the repository

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
- On Windows:
```bash
venv\Scripts\activate
```
- On Unix or MacOS:
```
source venv/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```


## Environment Variables

In order to run this project, you need to set up the following environment variables. Create a `.env` file under the /app directory of your project and add the necessary values:

### `AUTH_API_BASE_URL`

- **Description:** Base url of the API for authentication.
- **Example:** 
  ```plaintext
  AUTH_API_BASE_URL=http://localhost:1234
  ```

### `AUTH_API_CLIENT_ID`

- **Description:** Client ID of the API for authentication.
- **Example:** 
  ```plaintext
  AUTH_API_CLIENT_ID=test-client-id
  ```

### `AUTH_API_CLIENT_SECRET`

- **Description:** Client Secret of the API for authentication.
- **Example:** 
  ```plaintext
  AUTH_API_CLIENT_SECRET=test-client-secret
  ```

## Running the Application
Run the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```

The API will be accessible at http://localhost:5000.

## API Documentation
Swagger UI: http://127.0.0.1:5000/docs

## Testing
Run the test suite using:

```bash
pytest
```