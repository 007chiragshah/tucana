---
title: FastAPI v0.1.0
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

<h1 id="fastapi">FastAPI v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

- HTTP Authentication, scheme: bearer 

<h1 id="fastapi-patient">Patient</h1>

This tag encompasses all endpoints related to managing patient information and resources. These APIs allow for the creation, retrieval, updating, and deletion of patient records, as well as other patient-related operations. Authentication is required for all endpoints under this tag to ensure secure access.

## get-patient-list

<a id="opIdget-patient-list"></a>

`GET /web/patient`

*Get Patient List*

Retrieve a list of all patients.

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primaryIdentifier": "string",
      "active": true,
      "gender": "male",
      "birthDate": "2019-08-24"
    }
  ]
}
```

<h3 id="get-patient-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebPatientResources](#schemawebpatientresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## upsert-patient

<a id="opIdupsert-patient"></a>

`PUT /web/patient`

*Upsert Patient Api*

Create or update patient information.

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primaryIdentifier": "string",
  "active": true,
  "givenName": "pa$$word",
  "familyName": "pa$$word",
  "gender": "male",
  "birthDate": "2019-08-24"
}
```

<h3 id="upsert-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpsertPatientSchema](#schemaupsertpatientschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="upsert-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="upsert-patient-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## create-patient

<a id="opIdcreate-patient"></a>

`POST /web/patient`

*Create Patient Api*

Onboarding new patients into the system with their initial details. This endpoint is not usually needed since patients are added by startinga monitoring session.

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primaryIdentifier": "string",
  "active": true,
  "givenName": "pa$$word",
  "familyName": "pa$$word",
  "gender": "male",
  "birthDate": "2019-08-24"
}
```

<h3 id="create-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreatePatientSchema](#schemacreatepatientschema)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "active": true,
  "gender": "male",
  "birth_date": "2019-08-24"
}
```

<h3 id="create-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PlatformPatient](#schemaplatformpatient)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-patient

<a id="opIdget-patient"></a>

`GET /web/patient/{patient_id}`

*Get Patient*

Fetch detailed information about a specific patient by their unique internal ID.

<h3 id="get-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patient_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primaryIdentifier": "string",
  "active": true,
  "gender": "male",
  "birthDate": "2019-08-24"
}
```

<h3 id="get-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebPatient](#schemawebpatient)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## delete-patient

<a id="opIddelete-patient"></a>

`DELETE /web/patient/{patient_id}`

*Delete Patient*

Remove a specific patient record.

<h3 id="delete-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patient_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="delete-patient-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-session-alerts

<a id="opIdget-session-alerts"></a>

`GET /web/patient/{patient_id}/session/alerts`

*Get Session Alerts*

Retrieve alerts associated with a specific patient session.

<h3 id="get-session-alerts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patient_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "code": "string",
      "startDeterminationTime": "2019-08-24T14:15:22Z",
      "endDeterminationTime": "2019-08-24T14:15:22Z",
      "valueText": "string",
      "devicePrimaryIdentifier": "string",
      "deviceCode": "string",
      "triggerLowerLimit": 0,
      "triggerUpperLimit": 0
    }
  ]
}
```

<h3 id="get-session-alerts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebSessionAlertResources](#schemawebsessionalertresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-ehr-patients

<a id="opIdget-ehr-patients"></a>

`GET /web/patient/ehr`

*Get Ehr Patients*

Retrieve patient information from the integrated EHR. Requires EHR integration enabled to be enabled.

<h3 id="get-ehr-patients-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patientIdentifier|query|string|false|none|
|givenName|query|string|false|none|
|familyName|query|string|false|none|
|birthDate|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "resources": []
}
```

<h3 id="get-ehr-patients-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PlatformEHRPatientResources](#schemaplatformehrpatientresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## patient-ehr-admission

<a id="opIdpatient-ehr-admission"></a>

`POST /web/patient/admission`

*Patient Ehr Admission*

Admit a patient into the system. There are two possible operation flows,`quick admit` and `ehr admit`. Choosing `quick admit` means that the informationpassed to the system will be used to start a patient monitoring session. On the other side `ehr admit` will search for patient information in the integrated EHR and upon confirmation pass that information along to the patient monitor. If the admission succeeds this only means that the admission was requested, as still needs to be confirmed from bed side.

> Body parameter

```json
{
  "bedId": "f67e1026-328f-4d18-9ce4-e0f3bfea83d2",
  "payload": {
    "type": "quick-admit",
    "givenName": "string",
    "familyName": "string",
    "birthDate": "2019-08-24",
    "gender": "unknown"
  }
}
```

<h3 id="patient-ehr-admission-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebPatientAdmission](#schemawebpatientadmission)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="patient-ehr-admission-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="patient-ehr-admission-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## delete-patient-admission

<a id="opIddelete-patient-admission"></a>

`DELETE /web/patient/{patient_id}/admission`

*Delete Patient Admission*

In case of rejection of the patient admission from bed side, this API allows removing the admission request.

<h3 id="delete-patient-admission-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patient_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-patient-admission-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="delete-patient-admission-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-bed">Bed</h1>

This tag groups all endpoints related to the management of bed resources. These APIs are designed to handle individual and bulk operations on beds. Authentication is enforced to ensure secure and authorized access.

## get-bed-list

<a id="opIdget-bed-list"></a>

`GET /web/bed`

*Get Bed List*

Retrieve a list of beds or detailed information about individual beds. This endpoint is useful for querying available beds or fetching specific bed data for reporting or operational purposes.

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primaryIdentifier": "string",
        "active": true,
        "gender": "male",
        "birthDate": "2019-08-24"
      },
      "encounter": {
        "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
        "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
        "createdAt": "2019-08-24T14:15:22Z",
        "status": "string",
        "startTime": "2019-08-24T14:15:22Z",
        "endTime": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="get-bed-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebBedResources-Input](#schemawebbedresources-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-create-or-update-beds

<a id="opIdbatch-create-or-update-beds"></a>

`PUT /web/bed/batch`

*Batch Create Or Update Beds*

Creates or updates multiple bed resources in a single request. If a bed resource already exists, it will be updated; otherwise, a new bed will be created.

> Body parameter

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}
```

<h3 id="batch-create-or-update-beds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBatchCreateOrUpdateBeds](#schemawebbatchcreateorupdatebeds)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-create-or-update-beds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-create-or-update-beds-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-create-beds

<a id="opIdbatch-create-beds"></a>

`POST /web/bed/batch`

*Batch Create Beds*

Create multiple bed resources in a single request. Ideal for batch onboarding of new beds, allowing for streamlined and efficient resource setup.

> Body parameter

```json
{
  "resources": [
    {
      "name": "string"
    }
  ]
}
```

<h3 id="batch-create-beds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBatchCreateBeds](#schemawebbatchcreatebeds)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primaryIdentifier": "string",
        "active": true,
        "gender": "male",
        "birthDate": "2019-08-24"
      },
      "encounter": {
        "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
        "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
        "createdAt": "2019-08-24T14:15:22Z",
        "status": "string",
        "startTime": "2019-08-24T14:15:22Z",
        "endTime": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="batch-create-beds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebBedResources-Input](#schemawebbedresources-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-delete-beds

<a id="opIdbatch-delete-beds"></a>

`DELETE /web/bed/batch`

*Batch Delete Beds*

Remove multiple bed resources in a single request. This is useful for batch cleanup or decommissioning of unused or outdated bed records.

> Body parameter

```json
{
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}
```

<h3 id="batch-delete-beds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBatchDeleteBeds](#schemawebbatchdeletebeds)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-delete-beds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-delete-beds-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-bedgroup">BedGroup</h1>

This tag encompasses all endpoints related to managing bed groups, which are collections of bed resources that can be grouped based on shared characteristics, purposes, or locations. These APIs allow for the creation, updating, deletion, and retrieval of bed groups, as well as operations to manage beds within these groups. Authentication is required for all endpoints under this tag to ensure secure and authorized access.

## batch-create-or-update-bed-groups

<a id="opIdbatch-create-or-update-bed-groups"></a>

`PUT /web/bed-group/batch`

*Batch Create Or Update Bed Groups*

Create or update multiple bed groups in a single operation. Use this endpoint to either add new bed groups or update existing ones in bulk, ensuring the groupings are up-to-date.

> Body parameter

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string"
    }
  ]
}
```

<h3 id="batch-create-or-update-bed-groups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBatchCreateOrUpdateBedGroup](#schemawebbatchcreateorupdatebedgroup)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-create-or-update-bed-groups-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-create-or-update-bed-groups-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-create-bed-groups

<a id="opIdbatch-create-bed-groups"></a>

`POST /web/bed-group/batch`

*Batch Create Bed Groups*

Create multiple bed groups in a single request. This is ideal for bulk creation when establishing new bed groupings for different use cases or locations.

> Body parameter

```json
{
  "resources": [
    {
      "name": "string",
      "description": "string"
    }
  ]
}
```

<h3 id="batch-create-bed-groups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBedGroupCreateResources](#schemawebbedgroupcreateresources)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string",
      "beds": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string"
        }
      ]
    }
  ]
}
```

<h3 id="batch-create-bed-groups-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebBedGroupResources](#schemawebbedgroupresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-delete-bed-groups

<a id="opIdbatch-delete-bed-groups"></a>

`DELETE /web/bed-group/batch`

*Batch Delete Bed Groups*

Remove multiple bed groups in a single request. This operation is useful for batch deletions when bed groups are no longer required or are being restructured.

> Body parameter

```json
{
  "group_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}
```

<h3 id="batch-delete-bed-groups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBedGroupBatchDelete](#schemawebbedgroupbatchdelete)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-delete-bed-groups-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-delete-bed-groups-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-bed-group-list

<a id="opIdget-bed-group-list"></a>

`GET /web/bed-group`

*Get Bed Group List*

Retrieve a list of all bed groups. This can be used to get an overview of existing bed groups, their configurations, and related data.

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string",
      "beds": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string"
        }
      ]
    }
  ]
}
```

<h3 id="get-bed-group-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebBedGroupResources](#schemawebbedgroupresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## assign-bed-to-a-group

<a id="opIdassign-bed-to-a-group"></a>

`PUT /web/bed-group/{group_id}/beds`

*Assign Beds To A Group*

Add or update beds within an existing bed group. This allows administrators to modify the bed assignments in a specific group by associating or updating beds based on their group ID.

> Body parameter

```json
{
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}
```

<h3 id="assign-bed-to-a-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|group_id|path|string(uuid)|true|none|
|body|body|[WebAssignBedsToGroup](#schemawebassignbedstogroup)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="assign-bed-to-a-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="assign-bed-to-a-group-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-assign-bed-to-a-group

<a id="opIdbatch-assign-bed-to-a-group"></a>

`PUT /web/bed-group/beds/batch`

*Batch Assign Beds*

Assign beds across one or more bed groups in a single batch request.

> Body parameter

```json
{
  "resources": [
    {
      "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f",
      "bed_ids": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ]
    }
  ]
}
```

<h3 id="batch-assign-bed-to-a-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBatchAssignBeds](#schemawebbatchassignbeds)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-assign-bed-to-a-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-assign-bed-to-a-group-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-assigned-bed-for-group

<a id="opIdget-assigned-bed-for-group"></a>

`GET /web/bed-group/{bed_group_id}/beds`

*Get Bed Group Beds*

Retrieve the list of beds associated with a specific bed group. This endpoint is helpful for viewing which beds belong to which group.

<h3 id="get-assigned-bed-for-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bed_group_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primaryIdentifier": "string",
        "active": true,
        "gender": "male",
        "birthDate": "2019-08-24"
      },
      "encounter": {
        "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
        "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
        "createdAt": "2019-08-24T14:15:22Z",
        "status": "string",
        "startTime": "2019-08-24T14:15:22Z",
        "endTime": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="get-assigned-bed-for-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebBedResources-Input](#schemawebbedresources-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-bed-group-observations

<a id="opIdget-bed-group-observations"></a>

`GET /web/bed-group/{bed_group_id}/alerts`

*Get Bed Group Observations*

Get patient alerts for patients assigned to a bed in the requested bed group.

<h3 id="get-bed-group-observations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bed_group_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "patientId": "460a6d87-689c-4661-a526-a52450bbe2d7",
      "primaryIdentifier": "string",
      "alerts": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "category": "string",
          "code": "string",
          "effectiveDt": "2019-08-24T14:15:22Z",
          "valueNumber": 0,
          "valueText": "string",
          "devicePrimaryIdentifier": "string",
          "deviceCode": "string"
        }
      ]
    }
  ]
}
```

<h3 id="get-bed-group-observations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebBedGroupAlertResources](#schemawebbedgroupalertresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-audittrail">AuditTrail</h1>

This tag groups endpoints related to tracking and retrieving audit trails. Audit trails are records of actions or changes made to specific entities, providing a detailed log for accountability, debugging, and compliance purposes. Authentication is enforced to ensure secure access.

## get-audit-list

<a id="opIdget-audit-list"></a>

`GET /web/audit/{entity_id}`

*Get Audit List*

Retrieve the audit trail for a specific entity identified by its unique ID. This includes a detailed history of changes or actions performed on the entity, such as creation, updates, deletions, or other operational events.

<h3 id="get-audit-list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entity_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "entity_id": "8161163a-f227-466f-bc01-090a01e80165",
      "event_name": "string",
      "timestamp": "2019-08-24T14:15:22Z",
      "data": {}
    }
  ]
}
```

<h3 id="get-audit-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebAuditResources](#schemawebauditresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-device">Device</h1>

This tag includes endpoints for managing and interacting with devices. Devices may represent hardware or software components that are associated with beds in the system. These APIs allow for retrieving, updating, and performing batch operations on devices, as well as fetching specific details like operational ranges. Authentication is required to ensure secure access. There are two types of devices, patient monitors (PM) and sensors. They can be tell apart by checking the `gatewayId` property. If it's `null` is a PM if not it's a sensors.

## get-device-list

<a id="opIdget-device-list"></a>

`GET /web/device`

*Get Device List*

Retrieve a list of all devices or detailed information about specific devices.

<h3 id="get-device-list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bedId|query|array[string]|false|none|
|gatewayId|query|string(uuid)|false|none|
|isGateway|query|boolean|false|none|
|deviceCode|query|string|false|none|
|bedGroup|query|string(uuid)|false|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "config": {
        "audio_pause_enabled": true,
        "audio_enabled": true
      },
      "device_code": "string",
      "vital_ranges": [],
      "alerts": []
    }
  ]
}
```

<h3 id="get-device-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebDeviceResources](#schemawebdeviceresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## create-or-update-device

<a id="opIdcreate-or-update-device"></a>

`PUT /web/device`

*Create Or Update Device*

Associate or update multiple devices linked to beds in a single operation. Ideal for batch assigning or reconfiguring devices in bulk.

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "primary_identifier": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "device_code": "string"
}
```

<h3 id="create-or-update-device-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebCreateOrUpdateDevice](#schemawebcreateorupdatedevice)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="create-or-update-device-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="create-or-update-device-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-assign-device-bed

<a id="opIdbatch-assign-device-bed"></a>

`PUT /web/device/bed/batch`

*Batch Assign Beds*

> Body parameter

```json
{
  "associations": [
    {
      "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
      "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
    }
  ]
}
```

<h3 id="batch-assign-device-bed-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebBatchAssignBedsSchema](#schemawebbatchassignbedsschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-assign-device-bed-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-assign-device-bed-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-device-vital-ranges

<a id="opIdget-device-vital-ranges"></a>

`GET /web/device/{device_id}/range`

*Get Device Vital Ranges*

Retrieve the operational range or configuration details of a specific device identified by its unique ID.

<h3 id="get-device-vital-ranges-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|device_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "code": "string",
      "upper_limit": 0,
      "lower_limit": 0,
      "alert_condition_enabled": true
    }
  ]
}
```

<h3 id="get-device-vital-ranges-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebDeviceRangesResources](#schemawebdevicerangesresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-configuration">Configuration</h1>

This tag encompasses endpoints for retrieving and updating configuration settings within the system. Configurations may define system-wide parameters, operational preferences, or entity-specific settings. These APIs provide a centralized way to manage configurations, ensuring consistency and control. Authentication is required to secure access.

## get-config-list

<a id="opIdget-config-list"></a>

`GET /web/config`

*Get Config List*

Retrieve the current configuration settings. This endpoint is useful for reviewing the active configurations, understanding the system's current state, and ensuring that the settings align with expected values.

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "key": "string",
      "value": "string"
    }
  ]
}
```

<h3 id="get-config-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[WebConfigResources](#schemawebconfigresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-create-or-update-configs

<a id="opIdbatch-create-or-update-configs"></a>

`PUT /web/config`

*Batch Create Or Update Configs*

Update configuration settings. This endpoint allows modifications to system parameters, enabling customization or realignment of settings to meet evolving requirements. Some configurations might require additional validation (eg: setting an invalid MLLP_HOST/PORT might result in EHR integration issues, so additional steps need to be taken to validate integration after configuration is applied).

> Body parameter

```json
{
  "password": "pa$$word",
  "config": {
    "MLLP_HOST": "string",
    "MLLP_PORT": 65535,
    "MLLP_EXPORT_INTERVAL_MINUTES": 100
  }
}
```

<h3 id="batch-create-or-update-configs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebUpdateOrCreateConfigPayload](#schemawebupdateorcreateconfigpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-create-or-update-configs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorSchema](#schemaerrorschema)|

<h3 id="batch-create-or-update-configs-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-authentication">Authentication</h1>

This tag includes all endpoints related to user authentication and session management. These APIs provide tools for secure login, token management, and password updates, ensuring robust access control within the system. They are essential for managing user sessions and enforcing security protocols.

## post-web-auth-api

<a id="opIdpost-web-auth-api"></a>

`POST /web/auth/token`

*Get Internal Token Api*

This endpoint authenticates a user by validating the provided credentials and, upon successful verification, returns an authentication token. The token can be used to access other secure endpoints within the application.If username is not provided, it will use the system default.The response will include the token and refresh tokenThe validity of each token can be found in the `ttl` field contained in the token payload (please note the token is base64 encoded).

> Body parameter

```json
{
  "username": "admin@sibelhealth.com",
  "password": "pa$$word"
}
```

<h3 id="post-web-auth-api-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[LoginCredential](#schemalogincredential)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post-web-auth-api-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[InternalToken](#schemainternaltoken)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## post-web-auth-refresh-api

<a id="opIdpost-web-auth-refresh-api"></a>

`POST /web/auth/token/refresh`

*Refresh Token Api*

This endpoint allows a user to refresh their authentication token, extending access without requiring a full re-authentication. The client provides a refresh token, which the server verifies and, if valid, issues a new authentication token.

> Body parameter

```json
{
  "refresh": "pa$$word"
}
```

<h3 id="post-web-auth-refresh-api-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RefreshToken](#schemarefreshtoken)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post-web-auth-refresh-api-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[RefreshedInternalToken](#schemarefreshedinternaltoken)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## post-web-auth-logout-api

<a id="opIdpost-web-auth-logout-api"></a>

`POST /web/auth/token/logout`

*Logout Api*

This endpoint closes the user session.

> Body parameter

```json
{
  "password": "pa$$word"
}
```

<h3 id="post-web-auth-logout-api-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[LogoutSchema](#schemalogoutschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="post-web-auth-logout-api-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="post-web-auth-logout-api-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## post-web-auth-change-password-api

<a id="opIdpost-web-auth-change-password-api"></a>

`POST /web/auth/change-password`

*Change Password*

This endpoint allows an authenticated user to change their password. The user must provide the necessary information in the payload to verify their current password and specify a new password.

> Body parameter

```json
{
  "current": "pa$$word",
  "new": "pa$$word"
}
```

<h3 id="post-web-auth-change-password-api-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebChangePasswordPayload](#schemawebchangepasswordpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="post-web-auth-change-password-api-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="post-web-auth-change-password-api-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## post-web-auth-technical-api

<a id="opIdpost-web-auth-technical-api"></a>

`POST /web/auth/technical/token`

*Get Technical Internal Token Api*

This endpoint generates an authentication token specifically for technical users or services, allowing them to interact with internal APIs securely. If username is not provided, it will use the system default.

> Body parameter

```json
{
  "username": "tech@sibelhealth.com",
  "password": "pa$$word"
}
```

<h3 id="post-web-auth-technical-api-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TechnicalLoginCredential](#schematechnicallogincredential)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post-web-auth-technical-api-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[InternalToken](#schemainternaltoken)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-system">System</h1>

## get_health_check_api_health_get

<a id="opIdget_health_check_api_health_get"></a>

`GET /health`

*Get Health Check Api*

> Example responses

> 200 Response

```json
{
  "status": "Healthy"
}
```

<h3 id="get_health_check_api_health_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[HealthCheck](#schemahealthcheck)|

<aside class="success">
This operation does not require authentication
</aside>

## get_health_check_api_web_health_get

<a id="opIdget_health_check_api_web_health_get"></a>

`GET /web/health`

*Get Health Check Api*

> Example responses

> 200 Response

```json
{
  "status": "Healthy"
}
```

<h3 id="get_health_check_api_web_health_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[HealthCheck](#schemahealthcheck)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_CreatePatientSchema">CreatePatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemacreatepatientschema"></a>
<a id="schema_CreatePatientSchema"></a>
<a id="tocScreatepatientschema"></a>
<a id="tocscreatepatientschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primaryIdentifier": "string",
  "active": true,
  "givenName": "pa$$word",
  "familyName": "pa$$word",
  "gender": "male",
  "birthDate": "2019-08-24"
}

```

CreatePatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primaryIdentifier|string|true|none|none|
|active|boolean|true|none|none|
|givenName|string(password)|true|write-only|none|
|familyName|string(password)|true|write-only|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|none|
|birthDate|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DeviceConfig">DeviceConfig</h2>
<!-- backwards compatibility -->
<a id="schemadeviceconfig"></a>
<a id="schema_DeviceConfig"></a>
<a id="tocSdeviceconfig"></a>
<a id="tocsdeviceconfig"></a>

```json
{
  "audio_pause_enabled": true,
  "audio_enabled": true
}

```

DeviceConfig

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_pause_enabled|boolean|true|none|none|
|audio_enabled|boolean|true|none|none|

<h2 id="tocS_EHRPatient">EHRPatient</h2>
<!-- backwards compatibility -->
<a id="schemaehrpatient"></a>
<a id="schema_EHRPatient"></a>
<a id="tocSehrpatient"></a>
<a id="tocsehrpatient"></a>

```json
{
  "patientIdentifiers": [],
  "givenName": "string",
  "familyName": "string",
  "birthDate": "2019-08-24",
  "gender": "string"
}

```

EHRPatient

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patientIdentifiers|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|givenName|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|familyName|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|birthDate|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ErrorSchema">ErrorSchema</h2>
<!-- backwards compatibility -->
<a id="schemaerrorschema"></a>
<a id="schema_ErrorSchema"></a>
<a id="tocSerrorschema"></a>
<a id="tocserrorschema"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string",
  "ctx": {}
}

```

ErrorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[string]|true|none|none|
|msg|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|none|
|ctx|object|false|none|none|

<h2 id="tocS_GenderEnum">GenderEnum</h2>
<!-- backwards compatibility -->
<a id="schemagenderenum"></a>
<a id="schema_GenderEnum"></a>
<a id="tocSgenderenum"></a>
<a id="tocsgenderenum"></a>

```json
"male"

```

GenderEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|GenderEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|GenderEnum|male|
|GenderEnum|female|
|GenderEnum|other|
|GenderEnum|unknown|

<h2 id="tocS_HL7GenderEnum">HL7GenderEnum</h2>
<!-- backwards compatibility -->
<a id="schemahl7genderenum"></a>
<a id="schema_HL7GenderEnum"></a>
<a id="tocShl7genderenum"></a>
<a id="tocshl7genderenum"></a>

```json
"M"

```

HL7GenderEnum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|HL7GenderEnum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|HL7GenderEnum|M|
|HL7GenderEnum|F|
|HL7GenderEnum|A|
|HL7GenderEnum|N|
|HL7GenderEnum|O|
|HL7GenderEnum|U|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_HealthCheck">HealthCheck</h2>
<!-- backwards compatibility -->
<a id="schemahealthcheck"></a>
<a id="schema_HealthCheck"></a>
<a id="tocShealthcheck"></a>
<a id="tocshealthcheck"></a>

```json
{
  "status": "Healthy"
}

```

HealthCheck

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|[HealthCheckStatus](#schemahealthcheckstatus)|true|none|none|

<h2 id="tocS_HealthCheckStatus">HealthCheckStatus</h2>
<!-- backwards compatibility -->
<a id="schemahealthcheckstatus"></a>
<a id="schema_HealthCheckStatus"></a>
<a id="tocShealthcheckstatus"></a>
<a id="tocshealthcheckstatus"></a>

```json
"Healthy"

```

HealthCheckStatus

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|HealthCheckStatus|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|HealthCheckStatus|Healthy|
|HealthCheckStatus|Error|

<h2 id="tocS_InternalToken">InternalToken</h2>
<!-- backwards compatibility -->
<a id="schemainternaltoken"></a>
<a id="schema_InternalToken"></a>
<a id="tocSinternaltoken"></a>
<a id="tocsinternaltoken"></a>

```json
{
  "access": "pa$$word",
  "refresh": "pa$$word"
}

```

InternalToken

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access|string(password)|true|write-only|none|
|refresh|string(password)|true|write-only|none|

<h2 id="tocS_LoginCredential">LoginCredential</h2>
<!-- backwards compatibility -->
<a id="schemalogincredential"></a>
<a id="schema_LoginCredential"></a>
<a id="tocSlogincredential"></a>
<a id="tocslogincredential"></a>

```json
{
  "username": "admin@sibelhealth.com",
  "password": "pa$$word"
}

```

LoginCredential

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|false|none|none|
|password|string(password)|true|write-only|none|

<h2 id="tocS_LogoutSchema">LogoutSchema</h2>
<!-- backwards compatibility -->
<a id="schemalogoutschema"></a>
<a id="schema_LogoutSchema"></a>
<a id="tocSlogoutschema"></a>
<a id="tocslogoutschema"></a>

```json
{
  "password": "pa$$word"
}

```

LogoutSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|password|string(password)|true|write-only|none|

<h2 id="tocS_PlatformEHRPatientResources">PlatformEHRPatientResources</h2>
<!-- backwards compatibility -->
<a id="schemaplatformehrpatientresources"></a>
<a id="schema_PlatformEHRPatientResources"></a>
<a id="tocSplatformehrpatientresources"></a>
<a id="tocsplatformehrpatientresources"></a>

```json
{
  "resources": []
}

```

PlatformEHRPatientResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[EHRPatient](#schemaehrpatient)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PlatformPatient">PlatformPatient</h2>
<!-- backwards compatibility -->
<a id="schemaplatformpatient"></a>
<a id="schema_PlatformPatient"></a>
<a id="tocSplatformpatient"></a>
<a id="tocsplatformpatient"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "active": true,
  "given_name": "pa$$word",
  "family_name": "pa$$word",
  "gender": "male",
  "birth_date": "2019-08-24"
}

```

PlatformPatient

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|active|boolean|true|none|none|
|given_name|string(password)|true|write-only|none|
|family_name|string(password)|true|write-only|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|none|
|birth_date|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_RefreshToken">RefreshToken</h2>
<!-- backwards compatibility -->
<a id="schemarefreshtoken"></a>
<a id="schema_RefreshToken"></a>
<a id="tocSrefreshtoken"></a>
<a id="tocsrefreshtoken"></a>

```json
{
  "refresh": "pa$$word"
}

```

RefreshToken

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|refresh|string(password)|true|write-only|none|

<h2 id="tocS_RefreshedInternalToken">RefreshedInternalToken</h2>
<!-- backwards compatibility -->
<a id="schemarefreshedinternaltoken"></a>
<a id="schema_RefreshedInternalToken"></a>
<a id="tocSrefreshedinternaltoken"></a>
<a id="tocsrefreshedinternaltoken"></a>

```json
{
  "access": "pa$$word"
}

```

RefreshedInternalToken

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access|string(password)|true|write-only|none|

<h2 id="tocS_TechnicalLoginCredential">TechnicalLoginCredential</h2>
<!-- backwards compatibility -->
<a id="schematechnicallogincredential"></a>
<a id="schema_TechnicalLoginCredential"></a>
<a id="tocStechnicallogincredential"></a>
<a id="tocstechnicallogincredential"></a>

```json
{
  "username": "tech@sibelhealth.com",
  "password": "pa$$word"
}

```

TechnicalLoginCredential

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|false|none|none|
|password|string(password)|true|write-only|none|

<h2 id="tocS_UpsertPatientSchema">UpsertPatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemaupsertpatientschema"></a>
<a id="schema_UpsertPatientSchema"></a>
<a id="tocSupsertpatientschema"></a>
<a id="tocsupsertpatientschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primaryIdentifier": "string",
  "active": true,
  "givenName": "pa$$word",
  "familyName": "pa$$word",
  "gender": "male",
  "birthDate": "2019-08-24"
}

```

UpsertPatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primaryIdentifier|string|true|none|none|
|active|boolean|true|none|none|
|givenName|string(password)|true|write-only|none|
|familyName|string(password)|true|write-only|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|none|
|birthDate|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_WebAlert">WebAlert</h2>
<!-- backwards compatibility -->
<a id="schemawebalert"></a>
<a id="schema_WebAlert"></a>
<a id="tocSwebalert"></a>
<a id="tocswebalert"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "category": "string",
  "code": "string",
  "effectiveDt": "2019-08-24T14:15:22Z",
  "valueNumber": 0,
  "valueText": "string",
  "devicePrimaryIdentifier": "string",
  "deviceCode": "string"
}

```

WebAlert

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|category|string|true|none|none|
|code|string|true|none|none|
|effectiveDt|string(date-time)|true|none|none|
|valueNumber|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|valueText|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|devicePrimaryIdentifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|deviceCode|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebAssignBedSchema">WebAssignBedSchema</h2>
<!-- backwards compatibility -->
<a id="schemawebassignbedschema"></a>
<a id="schema_WebAssignBedSchema"></a>
<a id="tocSwebassignbedschema"></a>
<a id="tocswebassignbedschema"></a>

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
}

```

WebAssignBedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uuid)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|device_id|string(uuid)|true|none|none|

<h2 id="tocS_WebAssignBeds">WebAssignBeds</h2>
<!-- backwards compatibility -->
<a id="schemawebassignbeds"></a>
<a id="schema_WebAssignBeds"></a>
<a id="tocSwebassignbeds"></a>
<a id="tocswebassignbeds"></a>

```json
{
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f",
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

WebAssignBeds

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group_id|string(uuid)|true|none|none|
|bed_ids|[string]|true|none|none|

<h2 id="tocS_WebAssignBedsToGroup">WebAssignBedsToGroup</h2>
<!-- backwards compatibility -->
<a id="schemawebassignbedstogroup"></a>
<a id="schema_WebAssignBedsToGroup"></a>
<a id="tocSwebassignbedstogroup"></a>
<a id="tocswebassignbedstogroup"></a>

```json
{
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

WebAssignBedsToGroup

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_ids|[string]|true|none|none|

<h2 id="tocS_WebAuditEvent">WebAuditEvent</h2>
<!-- backwards compatibility -->
<a id="schemawebauditevent"></a>
<a id="schema_WebAuditEvent"></a>
<a id="tocSwebauditevent"></a>
<a id="tocswebauditevent"></a>

```json
{
  "entity_id": "8161163a-f227-466f-bc01-090a01e80165",
  "event_name": "string",
  "timestamp": "2019-08-24T14:15:22Z",
  "data": {}
}

```

WebAuditEvent

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|entity_id|string(uuid)|true|none|none|
|event_name|string|true|none|none|
|timestamp|string(date-time)|true|none|none|
|data|object|true|none|none|

<h2 id="tocS_WebAuditResources">WebAuditResources</h2>
<!-- backwards compatibility -->
<a id="schemawebauditresources"></a>
<a id="schema_WebAuditResources"></a>
<a id="tocSwebauditresources"></a>
<a id="tocswebauditresources"></a>

```json
{
  "resources": [
    {
      "entity_id": "8161163a-f227-466f-bc01-090a01e80165",
      "event_name": "string",
      "timestamp": "2019-08-24T14:15:22Z",
      "data": {}
    }
  ]
}

```

WebAuditResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebAuditEvent](#schemawebauditevent)]|true|none|none|

<h2 id="tocS_WebBatchAssignBeds">WebBatchAssignBeds</h2>
<!-- backwards compatibility -->
<a id="schemawebbatchassignbeds"></a>
<a id="schema_WebBatchAssignBeds"></a>
<a id="tocSwebbatchassignbeds"></a>
<a id="tocswebbatchassignbeds"></a>

```json
{
  "resources": [
    {
      "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f",
      "bed_ids": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ]
    }
  ]
}

```

WebBatchAssignBeds

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebAssignBeds](#schemawebassignbeds)]|true|none|none|

<h2 id="tocS_WebBatchAssignBedsSchema">WebBatchAssignBedsSchema</h2>
<!-- backwards compatibility -->
<a id="schemawebbatchassignbedsschema"></a>
<a id="schema_WebBatchAssignBedsSchema"></a>
<a id="tocSwebbatchassignbedsschema"></a>
<a id="tocswebbatchassignbedsschema"></a>

```json
{
  "associations": [
    {
      "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
      "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
    }
  ]
}

```

WebBatchAssignBedsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|associations|[[WebAssignBedSchema](#schemawebassignbedschema)]|true|none|none|

<h2 id="tocS_WebBatchCreateBeds">WebBatchCreateBeds</h2>
<!-- backwards compatibility -->
<a id="schemawebbatchcreatebeds"></a>
<a id="schema_WebBatchCreateBeds"></a>
<a id="tocSwebbatchcreatebeds"></a>
<a id="tocswebbatchcreatebeds"></a>

```json
{
  "resources": [
    {
      "name": "string"
    }
  ]
}

```

WebBatchCreateBeds

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebCreateBed](#schemawebcreatebed)]|true|none|none|

<h2 id="tocS_WebBatchCreateOrUpdateBedGroup">WebBatchCreateOrUpdateBedGroup</h2>
<!-- backwards compatibility -->
<a id="schemawebbatchcreateorupdatebedgroup"></a>
<a id="schema_WebBatchCreateOrUpdateBedGroup"></a>
<a id="tocSwebbatchcreateorupdatebedgroup"></a>
<a id="tocswebbatchcreateorupdatebedgroup"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string"
    }
  ]
}

```

WebBatchCreateOrUpdateBedGroup

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebCreateOrUpdateBedGroup](#schemawebcreateorupdatebedgroup)]|true|none|none|

<h2 id="tocS_WebBatchCreateOrUpdateBeds">WebBatchCreateOrUpdateBeds</h2>
<!-- backwards compatibility -->
<a id="schemawebbatchcreateorupdatebeds"></a>
<a id="schema_WebBatchCreateOrUpdateBeds"></a>
<a id="tocSwebbatchcreateorupdatebeds"></a>
<a id="tocswebbatchcreateorupdatebeds"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}

```

WebBatchCreateOrUpdateBeds

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebUpdateOrCreateBed](#schemawebupdateorcreatebed)]|true|none|none|

<h2 id="tocS_WebBatchDeleteBeds">WebBatchDeleteBeds</h2>
<!-- backwards compatibility -->
<a id="schemawebbatchdeletebeds"></a>
<a id="schema_WebBatchDeleteBeds"></a>
<a id="tocSwebbatchdeletebeds"></a>
<a id="tocswebbatchdeletebeds"></a>

```json
{
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

WebBatchDeleteBeds

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_ids|[string]|true|none|none|

<h2 id="tocS_WebBed-Input">WebBed-Input</h2>
<!-- backwards compatibility -->
<a id="schemawebbed-input"></a>
<a id="schema_WebBed-Input"></a>
<a id="tocSwebbed-input"></a>
<a id="tocswebbed-input"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "patient": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primaryIdentifier": "string",
    "active": true,
    "givenName": "pa$$word",
    "familyName": "pa$$word",
    "gender": "male",
    "birthDate": "2019-08-24"
  },
  "encounter": {
    "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
    "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
    "createdAt": "2019-08-24T14:15:22Z",
    "status": "string",
    "startTime": "2019-08-24T14:15:22Z",
    "endTime": "2019-08-24T14:15:22Z"
  }
}

```

WebBed

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|
|patient|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[WebPatient](#schemawebpatient)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|encounter|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[WebEncounter](#schemawebencounter)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebBed-Output">WebBed-Output</h2>
<!-- backwards compatibility -->
<a id="schemawebbed-output"></a>
<a id="schema_WebBed-Output"></a>
<a id="tocSwebbed-output"></a>
<a id="tocswebbed-output"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "patient": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primaryIdentifier": "string",
    "active": true,
    "givenName": "pa$$word",
    "familyName": "pa$$word",
    "gender": "male",
    "birthDate": "2019-08-24"
  },
  "encounter": {
    "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
    "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
    "createdAt": "2019-08-24T14:15:22Z",
    "status": "string",
    "startTime": "2019-08-24T14:15:22Z",
    "endTime": "2019-08-24T14:15:22Z"
  }
}

```

WebBed

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|
|patient|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[WebPatient](#schemawebpatient)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|encounter|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[WebEncounter](#schemawebencounter)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebBedGroup">WebBedGroup</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroup"></a>
<a id="schema_WebBedGroup"></a>
<a id="tocSwebbedgroup"></a>
<a id="tocswebbedgroup"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "description": "string",
  "beds": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}

```

WebBedGroup

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|beds|[[WebBedGroupBed](#schemawebbedgroupbed)]|true|none|none|

<h2 id="tocS_WebBedGroupAlertResources">WebBedGroupAlertResources</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroupalertresources"></a>
<a id="schema_WebBedGroupAlertResources"></a>
<a id="tocSwebbedgroupalertresources"></a>
<a id="tocswebbedgroupalertresources"></a>

```json
{
  "resources": [
    {
      "patientId": "460a6d87-689c-4661-a526-a52450bbe2d7",
      "primaryIdentifier": "string",
      "alerts": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "category": "string",
          "code": "string",
          "effectiveDt": "2019-08-24T14:15:22Z",
          "valueNumber": 0,
          "valueText": "string",
          "devicePrimaryIdentifier": "string",
          "deviceCode": "string"
        }
      ]
    }
  ]
}

```

WebBedGroupAlertResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebPatientAlert](#schemawebpatientalert)]|true|none|none|

<h2 id="tocS_WebBedGroupBatchDelete">WebBedGroupBatchDelete</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroupbatchdelete"></a>
<a id="schema_WebBedGroupBatchDelete"></a>
<a id="tocSwebbedgroupbatchdelete"></a>
<a id="tocswebbedgroupbatchdelete"></a>

```json
{
  "group_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

WebBedGroupBatchDelete

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group_ids|[string]|true|none|none|

<h2 id="tocS_WebBedGroupBed">WebBedGroupBed</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroupbed"></a>
<a id="schema_WebBedGroupBed"></a>
<a id="tocSwebbedgroupbed"></a>
<a id="tocswebbedgroupbed"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

WebBedGroupBed

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|

<h2 id="tocS_WebBedGroupCreate">WebBedGroupCreate</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroupcreate"></a>
<a id="schema_WebBedGroupCreate"></a>
<a id="tocSwebbedgroupcreate"></a>
<a id="tocswebbedgroupcreate"></a>

```json
{
  "name": "string",
  "description": "string"
}

```

WebBedGroupCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebBedGroupCreateResources">WebBedGroupCreateResources</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroupcreateresources"></a>
<a id="schema_WebBedGroupCreateResources"></a>
<a id="tocSwebbedgroupcreateresources"></a>
<a id="tocswebbedgroupcreateresources"></a>

```json
{
  "resources": [
    {
      "name": "string",
      "description": "string"
    }
  ]
}

```

WebBedGroupCreateResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebBedGroupCreate](#schemawebbedgroupcreate)]|true|none|none|

<h2 id="tocS_WebBedGroupResources">WebBedGroupResources</h2>
<!-- backwards compatibility -->
<a id="schemawebbedgroupresources"></a>
<a id="schema_WebBedGroupResources"></a>
<a id="tocSwebbedgroupresources"></a>
<a id="tocswebbedgroupresources"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string",
      "beds": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string"
        }
      ]
    }
  ]
}

```

WebBedGroupResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebBedGroup](#schemawebbedgroup)]|true|none|none|

<h2 id="tocS_WebBedResources-Input">WebBedResources-Input</h2>
<!-- backwards compatibility -->
<a id="schemawebbedresources-input"></a>
<a id="schema_WebBedResources-Input"></a>
<a id="tocSwebbedresources-input"></a>
<a id="tocswebbedresources-input"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primaryIdentifier": "string",
        "active": true,
        "givenName": "pa$$word",
        "familyName": "pa$$word",
        "gender": "male",
        "birthDate": "2019-08-24"
      },
      "encounter": {
        "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
        "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
        "createdAt": "2019-08-24T14:15:22Z",
        "status": "string",
        "startTime": "2019-08-24T14:15:22Z",
        "endTime": "2019-08-24T14:15:22Z"
      }
    }
  ]
}

```

WebBedResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebBed-Input](#schemawebbed-input)]|true|none|none|

<h2 id="tocS_WebBedResources-Output">WebBedResources-Output</h2>
<!-- backwards compatibility -->
<a id="schemawebbedresources-output"></a>
<a id="schema_WebBedResources-Output"></a>
<a id="tocSwebbedresources-output"></a>
<a id="tocswebbedresources-output"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primaryIdentifier": "string",
        "active": true,
        "givenName": "pa$$word",
        "familyName": "pa$$word",
        "gender": "male",
        "birthDate": "2019-08-24"
      },
      "encounter": {
        "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
        "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
        "createdAt": "2019-08-24T14:15:22Z",
        "status": "string",
        "startTime": "2019-08-24T14:15:22Z",
        "endTime": "2019-08-24T14:15:22Z"
      }
    }
  ]
}

```

WebBedResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebBed-Output](#schemawebbed-output)]|true|none|none|

<h2 id="tocS_WebChangePasswordPayload">WebChangePasswordPayload</h2>
<!-- backwards compatibility -->
<a id="schemawebchangepasswordpayload"></a>
<a id="schema_WebChangePasswordPayload"></a>
<a id="tocSwebchangepasswordpayload"></a>
<a id="tocswebchangepasswordpayload"></a>

```json
{
  "current": "pa$$word",
  "new": "pa$$word"
}

```

WebChangePasswordPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|current|string(password)|true|write-only|none|
|new|string(password)|true|write-only|none|

<h2 id="tocS_WebConfig">WebConfig</h2>
<!-- backwards compatibility -->
<a id="schemawebconfig"></a>
<a id="schema_WebConfig"></a>
<a id="tocSwebconfig"></a>
<a id="tocswebconfig"></a>

```json
{
  "key": "string",
  "value": "string"
}

```

WebConfig

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|key|string|true|none|none|
|value|string|true|none|none|

<h2 id="tocS_WebConfigResources">WebConfigResources</h2>
<!-- backwards compatibility -->
<a id="schemawebconfigresources"></a>
<a id="schema_WebConfigResources"></a>
<a id="tocSwebconfigresources"></a>
<a id="tocswebconfigresources"></a>

```json
{
  "resources": [
    {
      "key": "string",
      "value": "string"
    }
  ]
}

```

WebConfigResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebConfig](#schemawebconfig)]|true|none|none|

<h2 id="tocS_WebCreateBed">WebCreateBed</h2>
<!-- backwards compatibility -->
<a id="schemawebcreatebed"></a>
<a id="schema_WebCreateBed"></a>
<a id="tocSwebcreatebed"></a>
<a id="tocswebcreatebed"></a>

```json
{
  "name": "string"
}

```

WebCreateBed

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|

<h2 id="tocS_WebCreateOrUpdateBedGroup">WebCreateOrUpdateBedGroup</h2>
<!-- backwards compatibility -->
<a id="schemawebcreateorupdatebedgroup"></a>
<a id="schema_WebCreateOrUpdateBedGroup"></a>
<a id="tocSwebcreateorupdatebedgroup"></a>
<a id="tocswebcreateorupdatebedgroup"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "description": "string"
}

```

WebCreateOrUpdateBedGroup

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uuid)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebCreateOrUpdateDevice">WebCreateOrUpdateDevice</h2>
<!-- backwards compatibility -->
<a id="schemawebcreateorupdatedevice"></a>
<a id="schema_WebCreateOrUpdateDevice"></a>
<a id="tocSwebcreateorupdatedevice"></a>
<a id="tocswebcreateorupdatedevice"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "primary_identifier": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "device_code": "string"
}

```

WebCreateOrUpdateDevice

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|
|primary_identifier|string|true|none|none|
|gateway_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uuid)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|device_code|string|true|none|none|

<h2 id="tocS_WebDevice">WebDevice</h2>
<!-- backwards compatibility -->
<a id="schemawebdevice"></a>
<a id="schema_WebDevice"></a>
<a id="tocSwebdevice"></a>
<a id="tocswebdevice"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "config": {
    "audio_pause_enabled": true,
    "audio_enabled": true
  },
  "device_code": "string",
  "vital_ranges": [],
  "alerts": []
}

```

WebDevice

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
|location_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uuid)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gateway_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uuid)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|config|[DeviceConfig](#schemadeviceconfig)|true|none|none|
|device_code|string|true|none|none|
|vital_ranges|[[WebDeviceRange](#schemawebdevicerange)]|false|none|none|
|alerts|[[WebDeviceAlert](#schemawebdevicealert)]|false|none|none|

<h2 id="tocS_WebDeviceAlert">WebDeviceAlert</h2>
<!-- backwards compatibility -->
<a id="schemawebdevicealert"></a>
<a id="schema_WebDeviceAlert"></a>
<a id="tocSwebdevicealert"></a>
<a id="tocswebdevicealert"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "code": "string",
  "priority": "string",
  "createdAt": "2019-08-24T14:15:22Z"
}

```

WebDeviceAlert

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|code|string|true|none|none|
|priority|string|true|none|none|
|createdAt|string(date-time)|true|none|none|

<h2 id="tocS_WebDeviceRange">WebDeviceRange</h2>
<!-- backwards compatibility -->
<a id="schemawebdevicerange"></a>
<a id="schema_WebDeviceRange"></a>
<a id="tocSwebdevicerange"></a>
<a id="tocswebdevicerange"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "code": "string",
  "upper_limit": 0,
  "lower_limit": 0,
  "alert_condition_enabled": true
}

```

WebDeviceRange

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|code|string|true|none|none|
|upper_limit|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lower_limit|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alert_condition_enabled|boolean|true|none|none|

<h2 id="tocS_WebDeviceRangesResources">WebDeviceRangesResources</h2>
<!-- backwards compatibility -->
<a id="schemawebdevicerangesresources"></a>
<a id="schema_WebDeviceRangesResources"></a>
<a id="tocSwebdevicerangesresources"></a>
<a id="tocswebdevicerangesresources"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "code": "string",
      "upper_limit": 0,
      "lower_limit": 0,
      "alert_condition_enabled": true
    }
  ]
}

```

WebDeviceRangesResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebDeviceRange](#schemawebdevicerange)]|true|none|none|

<h2 id="tocS_WebDeviceResources">WebDeviceResources</h2>
<!-- backwards compatibility -->
<a id="schemawebdeviceresources"></a>
<a id="schema_WebDeviceResources"></a>
<a id="tocSwebdeviceresources"></a>
<a id="tocswebdeviceresources"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "config": {
        "audio_pause_enabled": true,
        "audio_enabled": true
      },
      "device_code": "string",
      "vital_ranges": [],
      "alerts": []
    }
  ]
}

```

WebDeviceResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebDevice](#schemawebdevice)]|true|none|none|

<h2 id="tocS_WebEHRAdmitPayload">WebEHRAdmitPayload</h2>
<!-- backwards compatibility -->
<a id="schemawebehradmitpayload"></a>
<a id="schema_WebEHRAdmitPayload"></a>
<a id="tocSwebehradmitpayload"></a>
<a id="tocswebehradmitpayload"></a>

```json
{
  "type": "ehr-search",
  "patientIdentifier": "string",
  "givenName": "-",
  "familyName": "-",
  "birthDate": "2019-08-24",
  "gender": "U"
}

```

WebEHRAdmitPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|patientIdentifier|string|true|none|none|
|givenName|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|familyName|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|birthDate|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[HL7GenderEnum](#schemahl7genderenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|ehr-search|

<h2 id="tocS_WebEncounter">WebEncounter</h2>
<!-- backwards compatibility -->
<a id="schemawebencounter"></a>
<a id="schema_WebEncounter"></a>
<a id="tocSwebencounter"></a>
<a id="tocswebencounter"></a>

```json
{
  "subjectId": "68460e63-0717-47f9-8fd8-d28f152cb30b",
  "deviceId": "4de4adb9-21ee-47e3-aeb4-8cf8ed6c109a",
  "createdAt": "2019-08-24T14:15:22Z",
  "status": "string",
  "startTime": "2019-08-24T14:15:22Z",
  "endTime": "2019-08-24T14:15:22Z"
}

```

WebEncounter

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subjectId|string(uuid)|true|none|none|
|deviceId|string(uuid)|true|none|none|
|createdAt|string(date-time)|true|none|none|
|status|string|true|none|none|
|startTime|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|endTime|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebPatient">WebPatient</h2>
<!-- backwards compatibility -->
<a id="schemawebpatient"></a>
<a id="schema_WebPatient"></a>
<a id="tocSwebpatient"></a>
<a id="tocswebpatient"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primaryIdentifier": "string",
  "active": true,
  "givenName": "pa$$word",
  "familyName": "pa$$word",
  "gender": "male",
  "birthDate": "2019-08-24"
}

```

WebPatient

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primaryIdentifier|string|true|none|none|
|active|boolean|true|none|none|
|givenName|string(password)|true|write-only|none|
|familyName|string(password)|true|write-only|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|none|
|birthDate|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebPatientAdmission">WebPatientAdmission</h2>
<!-- backwards compatibility -->
<a id="schemawebpatientadmission"></a>
<a id="schema_WebPatientAdmission"></a>
<a id="tocSwebpatientadmission"></a>
<a id="tocswebpatientadmission"></a>

```json
{
  "bedId": "f67e1026-328f-4d18-9ce4-e0f3bfea83d2",
  "payload": {
    "type": "quick-admit",
    "givenName": "string",
    "familyName": "string",
    "birthDate": "2019-08-24",
    "gender": "unknown"
  }
}

```

WebPatientAdmission

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bedId|string(uuid)|true|none|none|
|payload|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[WebQuickAdmitPayload](#schemawebquickadmitpayload)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[WebEHRAdmitPayload](#schemawebehradmitpayload)|false|none|none|

<h2 id="tocS_WebPatientAlert">WebPatientAlert</h2>
<!-- backwards compatibility -->
<a id="schemawebpatientalert"></a>
<a id="schema_WebPatientAlert"></a>
<a id="tocSwebpatientalert"></a>
<a id="tocswebpatientalert"></a>

```json
{
  "patientId": "460a6d87-689c-4661-a526-a52450bbe2d7",
  "primaryIdentifier": "string",
  "alerts": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "category": "string",
      "code": "string",
      "effectiveDt": "2019-08-24T14:15:22Z",
      "valueNumber": 0,
      "valueText": "string",
      "devicePrimaryIdentifier": "string",
      "deviceCode": "string"
    }
  ]
}

```

WebPatientAlert

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patientId|string(uuid)|true|none|none|
|primaryIdentifier|string|true|none|none|
|alerts|[[WebAlert](#schemawebalert)]|true|none|none|

<h2 id="tocS_WebPatientResources">WebPatientResources</h2>
<!-- backwards compatibility -->
<a id="schemawebpatientresources"></a>
<a id="schema_WebPatientResources"></a>
<a id="tocSwebpatientresources"></a>
<a id="tocswebpatientresources"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primaryIdentifier": "string",
      "active": true,
      "givenName": "pa$$word",
      "familyName": "pa$$word",
      "gender": "male",
      "birthDate": "2019-08-24"
    }
  ]
}

```

WebPatientResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebPatient](#schemawebpatient)]|true|none|none|

<h2 id="tocS_WebQuickAdmitPayload">WebQuickAdmitPayload</h2>
<!-- backwards compatibility -->
<a id="schemawebquickadmitpayload"></a>
<a id="schema_WebQuickAdmitPayload"></a>
<a id="tocSwebquickadmitpayload"></a>
<a id="tocswebquickadmitpayload"></a>

```json
{
  "type": "quick-admit",
  "givenName": "string",
  "familyName": "string",
  "birthDate": "2019-08-24",
  "gender": "unknown"
}

```

WebQuickAdmitPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|givenName|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|familyName|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|birthDate|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|gender|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[GenderEnum](#schemagenderenum)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|quick-admit|

<h2 id="tocS_WebSessionAlert">WebSessionAlert</h2>
<!-- backwards compatibility -->
<a id="schemawebsessionalert"></a>
<a id="schema_WebSessionAlert"></a>
<a id="tocSwebsessionalert"></a>
<a id="tocswebsessionalert"></a>

```json
{
  "code": "string",
  "startDeterminationTime": "2019-08-24T14:15:22Z",
  "endDeterminationTime": "2019-08-24T14:15:22Z",
  "valueText": "string",
  "devicePrimaryIdentifier": "string",
  "deviceCode": "string",
  "triggerLowerLimit": 0,
  "triggerUpperLimit": 0
}

```

WebSessionAlert

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|true|none|none|
|startDeterminationTime|string(date-time)|true|none|none|
|endDeterminationTime|string(date-time)|true|none|none|
|valueText|string|true|none|none|
|devicePrimaryIdentifier|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|deviceCode|string|true|none|none|
|triggerLowerLimit|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|triggerUpperLimit|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_WebSessionAlertResources">WebSessionAlertResources</h2>
<!-- backwards compatibility -->
<a id="schemawebsessionalertresources"></a>
<a id="schema_WebSessionAlertResources"></a>
<a id="tocSwebsessionalertresources"></a>
<a id="tocswebsessionalertresources"></a>

```json
{
  "resources": [
    {
      "code": "string",
      "startDeterminationTime": "2019-08-24T14:15:22Z",
      "endDeterminationTime": "2019-08-24T14:15:22Z",
      "valueText": "string",
      "devicePrimaryIdentifier": "string",
      "deviceCode": "string",
      "triggerLowerLimit": 0,
      "triggerUpperLimit": 0
    }
  ]
}

```

WebSessionAlertResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[WebSessionAlert](#schemawebsessionalert)]|true|none|none|

<h2 id="tocS_WebUpdateOrCreateBed">WebUpdateOrCreateBed</h2>
<!-- backwards compatibility -->
<a id="schemawebupdateorcreatebed"></a>
<a id="schema_WebUpdateOrCreateBed"></a>
<a id="tocSwebupdateorcreatebed"></a>
<a id="tocswebupdateorcreatebed"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

WebUpdateOrCreateBed

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uuid)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|

<h2 id="tocS_WebUpdateOrCreateConfig">WebUpdateOrCreateConfig</h2>
<!-- backwards compatibility -->
<a id="schemawebupdateorcreateconfig"></a>
<a id="schema_WebUpdateOrCreateConfig"></a>
<a id="tocSwebupdateorcreateconfig"></a>
<a id="tocswebupdateorcreateconfig"></a>

```json
{
  "MLLP_HOST": "string",
  "MLLP_PORT": 65535,
  "MLLP_EXPORT_INTERVAL_MINUTES": 100
}

```

WebUpdateOrCreateConfig

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|MLLP_HOST|string|true|none|none|
|MLLP_PORT|integer|true|none|none|
|MLLP_EXPORT_INTERVAL_MINUTES|integer|true|none|none|

<h2 id="tocS_WebUpdateOrCreateConfigPayload">WebUpdateOrCreateConfigPayload</h2>
<!-- backwards compatibility -->
<a id="schemawebupdateorcreateconfigpayload"></a>
<a id="schema_WebUpdateOrCreateConfigPayload"></a>
<a id="tocSwebupdateorcreateconfigpayload"></a>
<a id="tocswebupdateorcreateconfigpayload"></a>

```json
{
  "password": "pa$$word",
  "config": {
    "MLLP_HOST": "string",
    "MLLP_PORT": 65535,
    "MLLP_EXPORT_INTERVAL_MINUTES": 100
  }
}

```

WebUpdateOrCreateConfigPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|password|string(password)|true|write-only|none|
|config|[WebUpdateOrCreateConfig](#schemawebupdateorcreateconfig)|true|none|none|