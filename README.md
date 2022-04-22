# Miare

### Table of Contents

- [General info](#general-info)
- [Technologies](#technologies)
- [How To Use](#how-to-use)
- [API Reference](#api-reference)

## General Info

A project for Courier Income Report

## Technologies

- Python
- Django
- DRF
- Sqlite

## How To Use

### Installation

Install requirements:\
`pip install -r requirements.txt`

Migrate database:
```
python manage.py makemigrations
python manage.py migrate
```

Run Server:\
`python manage.py runserver`

## API Reference

Get Couriers:

```http
GET   /api/couriers/{courier_id}
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `courier_id` | `int` | **Optional** |

200 status code return one, or a list of Courier:

```json
{
  "id": int,
  "name": string
}
```

---

ADD Courier:

```http
POST   /api/couriers/
```

The request should be a JSON in the form of

```json
{
  "name": string
}
```

200 status code return one, or a list of Courier:

```json
{
  "id": int,
  "name": string
}
```

---

Get Courier Income:

```http
GET   /api/couriers/{courier_id}/income/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `courier_id` | `int` | **Required** |

200 status code return a list of Courier_Income:

```json
{
  "id": int,
  "mission_id": int,
  "income_type_id": int,
  "amount": int,
  "created_at": str,
  "courier": int
}
```

---

ADD Courier Income:

```http
POST   /api/couriers/{courier_id}/income/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `courier_id` | `int` | **Required** |

The request should be a JSON in the form of

```json
{
  "mission_id": int,
  "income_type_id": int,
  "amount": int
}
```

200 status code return one, or a list of Courier:

```json
{
  "id": int,
  "mission_id": int,
  "income_type_id": int,
  "amount": int,
  "created_at": str,
  "courier": int
}
```

---


GET Daily Report:

```http
GET   /api/api/reports/daily/couriers/{courier_id}/
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `courier_id` | `int` | **Optional** |

200 status code return a list of Daily Income Report:

```json
{
    "courier_id": int,
    "income": int,
    "date": str
}
```

---

GET Weekly Report:

```http
GET   /api/api/reports/weekly/couriers/{courier_id}/?from_date={from_date}&to_date={to_date}
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `courier_id` | `int` | **Optional** |
| `from_date` | `str` | **Required** |
| `to_date` | `str` | **Required** |


200 status code return a list of Weekly Income Report:

```json
{
    "courier_id": int,
    "income": int,
    "date": str
}
```

---
