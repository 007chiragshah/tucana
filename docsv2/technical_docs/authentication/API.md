---
title: Authentication v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="authentication">Authentication v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

The purpose of this service is to provide secure and easy-to-use authentication for any web or mobile application.

# Authentication

* API Key (cookieAuth)
    - Parameter Name: **sessionid**, in: cookie. 

- HTTP Authentication, scheme: bearer 

<h1 id="authentication-api">api</h1>

## api_auth_change_password_create

<a id="opIdapi_auth_change_password_create"></a>

`POST /api/auth/change-password`

> Body parameter

```json
{
  "current_password": "string",
  "new_password": "string"
}
```

```yaml
current_password: string
new_password: string

```

<h3 id="api_auth_change_password_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PasswordUpdate](#schemapasswordupdate)|true|none|

> Example responses

> 201 Response

```json
{
  "current_password": "string",
  "new_password": "string"
}
```

<h3 id="api_auth_change_password_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[PasswordUpdate](#schemapasswordupdate)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_configuration_list

<a id="opIdapi_configuration_list"></a>

`GET /api/configuration/`

<h3 id="api_configuration_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "key": "string",
      "value": "string"
    }
  ]
}
```

<h3 id="api_configuration_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedAppSettingList](#schemapaginatedappsettinglist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_configuration_create

<a id="opIdapi_configuration_create"></a>

`POST /api/configuration/`

> Body parameter

```json
{
  "key": "string",
  "value": "string"
}
```

```yaml
key: string
value: string

```

<h3 id="api_configuration_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AppSetting](#schemaappsetting)|true|none|

> Example responses

> 201 Response

```json
{
  "key": "string",
  "value": "string"
}
```

<h3 id="api_configuration_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[AppSetting](#schemaappsetting)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_list

<a id="opIdapi_groups_list"></a>

`GET /api/groups/`

<h3 id="api_groups_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}
```

<h3 id="api_groups_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedPrivilegeList](#schemapaginatedprivilegelist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_create

<a id="opIdapi_groups_create"></a>

`POST /api/groups/`

> Body parameter

```json
{
  "name": "string"
}
```

```yaml
name: string

```

<h3 id="api_groups_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Privilege](#schemaprivilege)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}
```

<h3 id="api_groups_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Privilege](#schemaprivilege)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_members_list

<a id="opIdapi_groups_members_list"></a>

`GET /api/groups/{group_pk}/members/`

<h3 id="api_groups_members_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|group_pk|path|string|true|none|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "username": "string",
      "tenant_id": "string",
      "email": "user@example.com",
      "first_name": "string",
      "last_name": "string"
    }
  ]
}
```

<h3 id="api_groups_members_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedUserList](#schemapaginateduserlist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_members_create

<a id="opIdapi_groups_members_create"></a>

`POST /api/groups/{group_pk}/members/`

> Body parameter

```json
{
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

```yaml
tenant_id: string
email: user@example.com
first_name: string
last_name: string

```

<h3 id="api_groups_members_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|group_pk|path|string|true|none|
|body|body|[User](#schemauser)|false|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

<h3 id="api_groups_members_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_members_destroy

<a id="opIdapi_groups_members_destroy"></a>

`DELETE /api/groups/{group_pk}/members/{id}/`

<h3 id="api_groups_members_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|group_pk|path|string|true|none|
|id|path|string(uuid)|true|A UUID string identifying this user.|

<h3 id="api_groups_members_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_retrieve

<a id="opIdapi_groups_retrieve"></a>

`GET /api/groups/{id}/`

<h3 id="api_groups_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this privilege.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}
```

<h3 id="api_groups_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Privilege](#schemaprivilege)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_update

<a id="opIdapi_groups_update"></a>

`PUT /api/groups/{id}/`

> Body parameter

```json
{
  "name": "string"
}
```

```yaml
name: string

```

<h3 id="api_groups_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this privilege.|
|body|body|[Privilege](#schemaprivilege)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}
```

<h3 id="api_groups_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Privilege](#schemaprivilege)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_partial_update

<a id="opIdapi_groups_partial_update"></a>

`PATCH /api/groups/{id}/`

> Body parameter

```json
{
  "name": "string"
}
```

```yaml
name: string

```

<h3 id="api_groups_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this privilege.|
|body|body|[PatchedPrivilege](#schemapatchedprivilege)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}
```

<h3 id="api_groups_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Privilege](#schemaprivilege)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_groups_destroy

<a id="opIdapi_groups_destroy"></a>

`DELETE /api/groups/{id}/`

<h3 id="api_groups_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this privilege.|

<h3 id="api_groups_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_token_create

<a id="opIdapi_token_create"></a>

`POST /api/token`

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

> Body parameter

```json
{
  "username": "string",
  "password": "string"
}
```

```yaml
username: string
password: string

```

<h3 id="api_token_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TokenObtainPairDetail](#schematokenobtainpairdetail)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="api_token_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TokenObtainPairDetail](#schematokenobtainpairdetail)|

<aside class="success">
This operation does not require authentication
</aside>

## api_token_logout_create

<a id="opIdapi_token_logout_create"></a>

`POST /api/token/logout`

Logs out a users.

<h3 id="api_token_logout_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_token_refresh_create

<a id="opIdapi_token_refresh_create"></a>

`POST /api/token/refresh`

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

> Body parameter

```json
{
  "refresh": "string"
}
```

```yaml
refresh: string

```

<h3 id="api_token_refresh_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TokenRefresh](#schematokenrefresh)|true|none|

> Example responses

> 200 Response

```json
{
  "access": "string"
}
```

<h3 id="api_token_refresh_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TokenRefresh](#schematokenrefresh)|

<aside class="success">
This operation does not require authentication
</aside>

## api_users_list

<a id="opIdapi_users_list"></a>

`GET /api/users/`

Lists, creates, updates and retrieves user accounts

<h3 id="api_users_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "username": "string",
      "tenant_id": "string",
      "email": "user@example.com",
      "first_name": "string",
      "last_name": "string"
    }
  ]
}
```

<h3 id="api_users_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedUserList](#schemapaginateduserlist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_users_create

<a id="opIdapi_users_create"></a>

`POST /api/users/`

Lists, creates, updates and retrieves user accounts

> Body parameter

```json
{
  "username": "string",
  "password": "string",
  "tenant_id": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com"
}
```

```yaml
username: string
password: string
tenant_id: string
first_name: string
last_name: string
email: user@example.com

```

<h3 id="api_users_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateUser](#schemacreateuser)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com"
}
```

<h3 id="api_users_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[CreateUser](#schemacreateuser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_users_retrieve

<a id="opIdapi_users_retrieve"></a>

`GET /api/users/{id}/`

Lists, creates, updates and retrieves user accounts

<h3 id="api_users_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this user.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

<h3 id="api_users_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_users_update

<a id="opIdapi_users_update"></a>

`PUT /api/users/{id}/`

Lists, creates, updates and retrieves user accounts

> Body parameter

```json
{
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

```yaml
tenant_id: string
email: user@example.com
first_name: string
last_name: string

```

<h3 id="api_users_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this user.|
|body|body|[User](#schemauser)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

<h3 id="api_users_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_users_partial_update

<a id="opIdapi_users_partial_update"></a>

`PATCH /api/users/{id}/`

Lists, creates, updates and retrieves user accounts

> Body parameter

```json
{
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

```yaml
tenant_id: string
email: user@example.com
first_name: string
last_name: string

```

<h3 id="api_users_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this user.|
|body|body|[PatchedUser](#schemapatcheduser)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}
```

<h3 id="api_users_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

## api_users_destroy

<a id="opIdapi_users_destroy"></a>

`DELETE /api/users/{id}/`

Lists, creates, updates and retrieves user accounts

<h3 id="api_users_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this user.|

<h3 id="api_users_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, jwtAuth
</aside>

# Schemas

<h2 id="tocS_AppSetting">AppSetting</h2>
<!-- backwards compatibility -->
<a id="schemaappsetting"></a>
<a id="schema_AppSetting"></a>
<a id="tocSappsetting"></a>
<a id="tocsappsetting"></a>

```json
{
  "key": "string",
  "value": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|key|string|true|none|none|
|value|string|true|none|none|

<h2 id="tocS_CreateUser">CreateUser</h2>
<!-- backwards compatibility -->
<a id="schemacreateuser"></a>
<a id="schema_CreateUser"></a>
<a id="tocScreateuser"></a>
<a id="tocscreateuser"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "password": "string",
  "tenant_id": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|username|string|true|none|Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.|
|password|string|true|write-only|none|
|tenant_id|string|false|none|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|
|email|string(email)|false|none|none|

<h2 id="tocS_PaginatedAppSettingList">PaginatedAppSettingList</h2>
<!-- backwards compatibility -->
<a id="schemapaginatedappsettinglist"></a>
<a id="schema_PaginatedAppSettingList"></a>
<a id="tocSpaginatedappsettinglist"></a>
<a id="tocspaginatedappsettinglist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "key": "string",
      "value": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|resources|[[AppSetting](#schemaappsetting)]|false|none|none|

<h2 id="tocS_PaginatedPrivilegeList">PaginatedPrivilegeList</h2>
<!-- backwards compatibility -->
<a id="schemapaginatedprivilegelist"></a>
<a id="schema_PaginatedPrivilegeList"></a>
<a id="tocSpaginatedprivilegelist"></a>
<a id="tocspaginatedprivilegelist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|resources|[[Privilege](#schemaprivilege)]|false|none|none|

<h2 id="tocS_PaginatedUserList">PaginatedUserList</h2>
<!-- backwards compatibility -->
<a id="schemapaginateduserlist"></a>
<a id="schema_PaginatedUserList"></a>
<a id="tocSpaginateduserlist"></a>
<a id="tocspaginateduserlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "username": "string",
      "tenant_id": "string",
      "email": "user@example.com",
      "first_name": "string",
      "last_name": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|resources|[[User](#schemauser)]|false|none|none|

<h2 id="tocS_PasswordUpdate">PasswordUpdate</h2>
<!-- backwards compatibility -->
<a id="schemapasswordupdate"></a>
<a id="schema_PasswordUpdate"></a>
<a id="tocSpasswordupdate"></a>
<a id="tocspasswordupdate"></a>

```json
{
  "current_password": "string",
  "new_password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|current_password|string|true|none|none|
|new_password|string|true|none|none|

<h2 id="tocS_PatchedPrivilege">PatchedPrivilege</h2>
<!-- backwards compatibility -->
<a id="schemapatchedprivilege"></a>
<a id="schema_PatchedPrivilege"></a>
<a id="tocSpatchedprivilege"></a>
<a id="tocspatchedprivilege"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|name|string|false|none|none|

<h2 id="tocS_PatchedUser">PatchedUser</h2>
<!-- backwards compatibility -->
<a id="schemapatcheduser"></a>
<a id="schema_PatchedUser"></a>
<a id="tocSpatcheduser"></a>
<a id="tocspatcheduser"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|username|string|false|read-only|Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.|
|tenant_id|string|false|none|none|
|email|string(email)|false|none|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|

<h2 id="tocS_Privilege">Privilege</h2>
<!-- backwards compatibility -->
<a id="schemaprivilege"></a>
<a id="schema_Privilege"></a>
<a id="tocSprivilege"></a>
<a id="tocsprivilege"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|name|string|true|none|none|

<h2 id="tocS_TokenObtainPairDetail">TokenObtainPairDetail</h2>
<!-- backwards compatibility -->
<a id="schematokenobtainpairdetail"></a>
<a id="schema_TokenObtainPairDetail"></a>
<a id="tocStokenobtainpairdetail"></a>
<a id="tocstokenobtainpairdetail"></a>

```json
{
  "username": "string",
  "password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|write-only|none|
|password|string|true|write-only|none|

<h2 id="tocS_TokenRefresh">TokenRefresh</h2>
<!-- backwards compatibility -->
<a id="schematokenrefresh"></a>
<a id="schema_TokenRefresh"></a>
<a id="tocStokenrefresh"></a>
<a id="tocstokenrefresh"></a>

```json
{
  "access": "string",
  "refresh": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access|string|true|read-only|none|
|refresh|string|true|write-only|none|

<h2 id="tocS_User">User</h2>
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "tenant_id": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|username|string|true|read-only|Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.|
|tenant_id|string|false|none|none|
|email|string(email)|false|none|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|

