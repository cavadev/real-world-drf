# Authentication

For this functionality we use [`django-rest-auth`](https://github.com/Tivix/django-rest-auth), [`djangorestframework-jwt`](https://github.com/GetBlimp/django-rest-framework-jwt) and [`django-allauth`](https://github.com/pennersr/django-allautht).

For clients to authenticate, the JSON Web Token (JWT) should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Bearer", with whitespace separating the two strings (see JWT_AUTH_HEADER_PREFIX configuration). For example:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Unauthenticated responses that are denied permission will result in an HTTP `401 Unauthorized` response with an appropriate `WWW-Authenticate` header. For example:

```
WWW-Authenticate: Bearer
```

The curl command line tool may be useful for testing token authenticated APIs. For example:

```bash
curl -X GET http://127.0.0.1:8000/api/v1/users/ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```

## Retrieving Tokens (Login)
Authorization tokens are issued and returned when a user registers (/api/v1/rest-auth/registration/). A registered user can also retrieve their token with the following request:

**Request**:

`POST` `/api/v1/rest-auth/login/`

Parameters:

Name     | Type   | Description
---------|--------|------------
email    | string | The user's email
password | string | The user's password

**Response**:
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "user": {
        "id": 48,
        "username": "john",
        "email": "johndoe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "about": "About me...",
        "account_verified": true
    }
}
```

## Delete Tokens (Logout)
This method does not work well.
Ref: https://bit.ly/2QyNXtm & https://bit.ly/2Keyeib

**Request**:

`POST` `/api/v1/rest-auth/logout/`

Parameters:

Name   | Type   | Description
-------|--------|------------
key    | string | The user's JSON Web Token

**Response**:
```json
{
  "detail": "Successfully logged out."
}
```

## Reset Password
Description

**Request**:

`POST` `/api/v1/rest-auth/password/reset/`

Parameters:

Name     | Type   | Description
---------|--------|------------
email    | string | The user's email

**Response**:
```json
{
    "detail": "Password reset e-mail has been sent."
}
```

## Reset Password (confirmation)
Description

**Request**:

`POST` `/api/v1/rest-auth/password/reset/confirm/`

Parameters:

Name          | Type   | Description
--------------|--------|------------
new_password1 | string | The user's new password
new_password2 | string | The user's new password (confirmation)
uid           | string | uid send by email
token         | string | token send by email


**Response**:
```json
{
    "detail": "Password has been reset with the new password."
}
```

## Change Password
Description

**Request**:

`POST` `/api/v1/rest-auth/password/change/`

Parameters:

Name          | Type   | Description
--------------|--------|------------
new_password1 | string | The user's new password
new_password2 | string | The user's new password (confirmation)
old_password  | string | The user's old password

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```json
{
  "detail": "New password has been saved."
}
```

## Facebook Login
Description

**Request**:

`POST` `/api/v1/rest-auth/facebook/`

Parameters:

Name         | Type   | Description
-------------|--------|---
access_token | string | access token.
code         | string | code.


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "user": {
        "id": 48,
        "username": "john",
        "email": "johndoe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "about": "About me...",
        "account_verified": true
    }
}
```
