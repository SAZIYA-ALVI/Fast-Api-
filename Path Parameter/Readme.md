
# FastAPI Path Parameter

This folder contains basic examples of **Path Parameters** in FastAPI.

## What is a Path Parameter?

A Path Parameter is a value that is passed directly in the **URL path**.

### Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### How it Works

If we open:

```text
/users/10
```

The value `10` is passed to `user_id`.

**Response:**

```json
{
  "user_id": 10
}
```

## Swagger UI

FastAPI automatically provides Swagger UI to test the API.

```text
http://127.0.0.1:8000/docs
```

## Topics Covered

* Path Parameters
* URL Parameters
* Data Types
* API Testing with Swagger UI

## Technologies

* Python
* FastAPI
* Uvicorn
* Swagger UI

## Purpose

This folder is created for practicing **Path Parameters in FastAPI**.

## Author

**Saziya Alvi**
