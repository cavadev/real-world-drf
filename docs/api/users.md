# Users
Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `/api/v1/rest-auth/registration/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
email      | string | No       | The user's email address.
first_name | string | No       | The user's given name.
last_name  | string | No       | The user's family name.
password1  | string | Yes      | The password for the new user account.
password2  | string | Yes      | The password for the new user account.


*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "user": {
        "id": 48,
        "username": "john",
        "email": "johndoe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "about": null,
        "account_verified": true
    }
}
```

The `token` returned with this response should be stored by the client for
authenticating future requests to the API. See [Authentication](authentication.md).

## Verify Email
Description

**Request**:

`POST` `/api/v1/rest-auth/registration/verify-email/`

Parameters:

Name   | Type   | Description
-------|--------|------------
key    | string | The user's key send by email


**Response**:
```json
{
  "detail": "ok"
}
```

## Get current user's profile information
We can get the current user profile with the JSON Web Token header (this endpoint support PUT, PATCH methods as well)

**Request**:

`GET` `/api/v1/rest-auth/user/`

Parameters:

(none)

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```json
{
  "id": 48,
  "username": "john",
  "email": "johndoe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "about": "About me...",
  "account_verified": true
}
```

## Get a user's profile information

**Request**:

`GET` `/users/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 48,
  "username": "john",
  "email": "johndoe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "about": "About me...",
  "account_verified": true
}
```


## Update profile information

**Request**:

`PUT/PATCH` `/users/:id`

Parameters:

Name       | Type   | Description
-----------|--------|---
first_name | string | The first_name of the user object.
last_name  | string | The last_name of the user object.
email      | string | The user's email address.
about      | string | The user's description.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 48,
  "username": "john",
  "email": "johndoe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "about": "New info...",
  "account_verified": true
}
```
