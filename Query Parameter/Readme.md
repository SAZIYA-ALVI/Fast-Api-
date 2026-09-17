# FastAPI Query Parameters


## What is a Query Parameter?

A Query Parameter is a value passed in the URL after the `?` symbol.

### Example

```text
/items?name=phone
```

Here:

* `name` is the query parameter
* `phone` is its value

Multiple query parameters can be passed using `&`.

```text
/items?name=phone&price=500
```

## Basic Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items(name: str):
    return {"name": name}
```

Example request:

```text
/items?name=phone
```

Response:

```json
{
  "name": "phone"
}
```

## Optional Query Parameter

A query parameter can have a default value.

```python
@app.get("/items")
def get_items(name: str = "Laptop"):
    return {"name": name}
```

If no value is provided, the default value is used.

## Multiple Query Parameters

```python
@app.get("/products")
def get_products(
    category: str = "Electronics",
    limit: int = 10
):
    return {
        "category": category,
        "limit": limit
    }
```

Example:

```text
/products?category=Mobile&limit=5
```

## Using Query()

FastAPI provides `Query()` for adding validation and metadata to query parameters.

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
def search(
    q: str = Query(..., min_length=3)
):
    return {"query": q}
```

Here, the query must contain at least **3 characters**.

## Query Parameter vs Path Parameter

| Query Parameter              | Path Parameter              |
| ---------------------------- | --------------------------- |
| Comes after `?`              | Comes inside the URL path   |
| Used for filtering/searching | Used to identify a resource |
| `/items?id=10`               | `/items/10`                 |
| Usually optional             | Often required              |

## Swagger UI

FastAPI automatically provides interactive API documentation through **Swagger UI**.

Run the application and open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to enter query parameters and test the API directly.

## Topics Covered

* Query Parameters
* Required Query Parameters
* Optional Query Parameters
* Default Values
* Multiple Query Parameters
* `Query()`
* Query Parameter Validation
* Swagger UI

## Technologies

* Python
* FastAPI
* Uvicorn
* Swagger UI

## Purpose

The purpose of this folder is to practice **Query Parameters in FastAPI** and understand how values can be passed through URLs to an API.

## Author

**Saziya Alvi**

