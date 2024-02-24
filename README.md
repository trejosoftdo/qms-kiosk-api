# QMS Kiosk API
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
![Build Status](https://github.com/trejosoftdo/qms-kiosk-api/actions/workflows/build.yml/badge.svg)


## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Linting](#linting)
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

5. Run the setup file:
```
./setup.sh
```

## Environment Variables

In order to run this project, you need to set up the following environment variables. Create a `.env` file under the /app directory of your project and add the necessary values:

### `AUTH_API_BASE_URL`

- **Description:** Base url of the API for authentication.
- **Example:** 
  ```plaintext
  AUTH_API_BASE_URL=http://localhost:1234
  ```

### `APP_CLIENT_ID`

- **Description:** Client ID of the APP for authentication.
- **Example:** 
  ```plaintext
  APP_CLIENT_ID=test-client-id
  ```

### `APP_CLIENT_SECRET`

- **Description:** Client Secret of the APP for authentication.
- **Example:** 
  ```plaintext
  APP_CLIENT_SECRET=test-client-secret
  ```

### `IAM_API_KEY`

- **Description:** API key to be able to consume the IAM API
- **Example:** 
  ```plaintext
  IAM_API_KEY=test-iam-api-key
  ```

### `CORE_API_KEY`

- **Description:** API key to be able to consume the Core API
- **Example:** 
  ```plaintext
  CORE_API_KEY=test-core-api-key
  ```

### `CORE_API_BASE_URL`

- **Description:** Base url of the core API.
- **Example:** 
  ```plaintext
  CORE_API_BASE_URL=http://localhost:5432
  ```

### `TEST_AUTH_APPLICATION`

- **Description:** Auth API application for testing
- **Example:** 
  ```plaintext
  TEST_AUTH_APPLICATION=test-auth-application
  ```

### `TEST_AUTH_USERNAME`

- **Description:** Auth API user name for testing
- **Example:** 
  ```plaintext
  TEST_AUTH_USERNAME=test-auth-username
  ```

### `TEST_AUTH_PASSWORD`

- **Description:** Auth API user password for testing
- **Example:** 
  ```plaintext
  TEST_AUTH_PASSWORD=test-auth-password
  ```

## Running the Application
Run the FastAPI application:
```bash
make start
```

The API will be accessible at http://localhost:5000.

## API Documentation
Swagger UI: http://127.0.0.1:5000/docs

## Linting
Run the linting on the code using:

```bash
make lint
```

## Testing
Run the unit tests using:

```bash
make unit-tests
```

Run the integration tests using:

```bash
make integration-tests
```
