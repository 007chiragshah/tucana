# 1. Workflow and algorithms

The following section presents all non-trivial workflows of the authentication microservice as activity diagrams. The workflows for "get" endpoints are omitted, as their algorithms are straightforward, involving only retrieving and filtering the returned information.

In all cases, the diagrams focus solely on business logic validations, excluding input sanitization checks or database integrity error handling. This omission enhances readability, as such validations are expected to be performed for every endpoint or event by default.

## 1.1. API Workflows

All these workflows are triggered by requests from the web microservice.

### 1.1.1. Login

![User login](<../images/activity_diagrams/authentication/api/login.svg>)

### 1.1.2. Logout

![Logout](<../images/activity_diagrams/authentication/api/logout.svg>)

### 1.1.3. Change Password

![Change password](<../images/activity_diagrams/authentication/api/change_password.svg>)

### 1.1.4. User CRUD

![User CRUD](<../images/activity_diagrams/authentication/api/user_crud.svg>)

### 1.1.5. Privilege CRUD

![Privilege CRUD](<../images/activity_diagrams/authentication/api/privilege_crud.svg>)

### 1.1.6. Group CRUD

![Group CRUD](<../images/activity_diagrams/authentication/api/group_crud.svg>)

### 1.1.7. App setting CRUD

![App setting CRUD](<../images/activity_diagrams/authentication/api/app_setting_crud.svg>)

### 1.1.23. Trivial workflows (Get workflows)

As mentioned before there is a list of workflows that are trivial and do not have a diagram since it would be a single node. They still have validation and parsing done by the framework used, but have no business logic other than retrieving the data from the database.

Here is the list of workflows:

- Get user
- Get user list
- Get privilege list
- Get group list

Since all this workflows retrieve information they are triggered by the user when displaying anything on the frontend.
