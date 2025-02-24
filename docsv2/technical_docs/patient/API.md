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

<h1 id="fastapi-default">Default</h1>

## start-encounter

<a id="opIdstart-encounter"></a>

`POST /patient/PlanPatientAdmission`

*Plan Patient Admission Api*

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d"
}
```

<h3 id="start-encounter-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PatientAdmissionSchema](#schemapatientadmissionschema)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
  "created_at": "2019-08-24T14:15:22Z",
  "status": "planned",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}
```

<h3 id="start-encounter-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[EncounterSchema](#schemaencounterschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## dismiss_patient_admission_api_patient_DismissPatientAdmission_post

<a id="opIddismiss_patient_admission_api_patient_DismissPatientAdmission_post"></a>

`POST /patient/DismissPatientAdmission`

*Dismiss Patient Admission Api*

> Body parameter

```json
{
  "patient_id": "3854866a-5476-48be-8313-77029ccdd7a7"
}
```

<h3 id="dismiss_patient_admission_api_patient_dismisspatientadmission_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DismissPatientAdmissionPayload](#schemadismisspatientadmissionpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="dismiss_patient_admission_api_patient_dismisspatientadmission_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="dismiss_patient_admission_api_patient_dismisspatientadmission_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-patient-rest">Patient REST</h1>

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

## get-patient-list

<a id="opIdget-patient-list"></a>

`GET /patient`

*Get Patient List*

<h3 id="get-patient-list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|identifier|query|any|false|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "active": true,
      "family_name": "string",
      "gender": "male",
      "birth_date": "2019-08-24"
    }
  ]
}
```

<h3 id="get-patient-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientResources-Input](#schemapatientresources-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-patient-count

<a id="opIdget-patient-count"></a>

`GET /patient/count`

*Get Patient Count*

<h3 id="get-patient-count-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|identifier|query|any|false|none|

> Example responses

> 200 Response

```json
{
  "total": 0
}
```

<h3 id="get-patient-count-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientCount](#schemapatientcount)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-patient

<a id="opIdget-patient"></a>

`GET /patient/{patient_id}`

*Get Patient By Id*

<h3 id="get-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patient_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "active": true,
  "family_name": "string",
  "gender": "male",
  "birth_date": "2019-08-24"
}
```

<h3 id="get-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientSchema](#schemapatientschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-patient-by-identifier

<a id="opIdget-patient-by-identifier"></a>

`GET /patient/identifier/{identifier_id}`

*Get Patient By Identifier*

<h3 id="get-patient-by-identifier-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|identifier_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "active": true,
  "family_name": "string",
  "gender": "male",
  "birth_date": "2019-08-24"
}
```

<h3 id="get-patient-by-identifier-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientSchema](#schemapatientschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-patient-observations

<a id="opIdget-patient-observations"></a>

`GET /patient/observation`

*Get Patient Observations*

<h3 id="get-patient-observations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|isAlert|query|any|false|none|
|patientIds|query|array[string]|true|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "category": "string",
      "code": "string",
      "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
      "effective_dt": "2019-08-24T14:15:22Z",
      "value_number": 0,
      "value_text": "string",
      "device_primary_identifier": "string",
      "device_code": "string"
    }
  ]
}
```

<h3 id="get-patient-observations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientObservationResources-Input](#schemapatientobservationresources-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-physiological-alerts

<a id="opIdget-physiological-alerts"></a>

`GET /patient/{patient_id}/session/alerts`

*Get Physiological Alerts*

<h3 id="get-physiological-alerts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|patient_id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "code": "string",
    "start_determination_time": "2019-08-24T14:15:22Z",
    "end_determination_time": "2019-08-24T14:15:22Z",
    "value_text": "string",
    "device_primary_identifier": "string",
    "device_code": "string",
    "trigger_lower_limit": 0,
    "trigger_upper_limit": 0
  }
]
```

<h3 id="get-physiological-alerts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get-physiological-alerts-responseschema">Response Schema</h3>

Status Code **200**

*Response 200 Get-Physiological-Alerts*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response 200 Get-Physiological-Alerts|[[SessionPhysiologicalAlert](#schemasessionphysiologicalalert)]|false|none|none|
|» SessionPhysiologicalAlert|[SessionPhysiologicalAlert](#schemasessionphysiologicalalert)|false|none|none|
|»» code|string|true|none|none|
|»» start_determination_time|string(date-time)|true|none|none|
|»» end_determination_time|string(date-time)|true|none|none|
|»» value_text|string|true|none|none|
|»» device_primary_identifier|string|true|none|none|
|»» device_code|string|true|none|none|
|»» trigger_lower_limit|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|number|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» trigger_upper_limit|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|number|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get_beds_patient_bed_get

<a id="opIdget_beds_patient_bed_get"></a>

`GET /patient/bed`

*Get Beds*

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
        "primary_identifier": "string",
        "active": true,
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      },
      "encounter": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
        "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
        "created_at": "2019-08-24T14:15:22Z",
        "status": "planned",
        "start_time": "2019-08-24T14:15:22Z",
        "end_time": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="get_beds_patient_bed_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedResourcesSchema-Input](#schemabedresourcesschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-bed-groups

<a id="opIdget-bed-groups"></a>

`GET /patient/bed-group`

*Get Bed Groups*

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

<h3 id="get-bed-groups-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedGroupResourcesSchema-Input](#schemabedgroupresourcesschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-beds-for-group

<a id="opIdget-beds-for-group"></a>

`GET /patient/bed-group/{group_id}/beds`

*Get Beds In Group*

<h3 id="get-beds-for-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|group_id|path|string(uuid)|true|none|

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
        "primary_identifier": "string",
        "active": true,
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      },
      "encounter": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
        "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
        "created_at": "2019-08-24T14:15:22Z",
        "status": "planned",
        "start_time": "2019-08-24T14:15:22Z",
        "end_time": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="get-beds-for-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedResourcesSchema-Input](#schemabedresourcesschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-patient-commands">Patient Commands</h1>

## create-patient

<a id="opIdcreate-patient"></a>

`POST /patient/CreatePatient`

*Create Patient Api*

> Body parameter

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
  "family_name": "string",
  "gender": "male",
  "birth_date": "2019-08-24"
}
```

<h3 id="create-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientSchema](#schemapatientschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## update-patient

<a id="opIdupdate-patient"></a>

`POST /patient/UpdatePatientInfo`

*Update Patient Info Command*

> Body parameter

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

<h3 id="update-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdatePatientSchema](#schemaupdatepatientschema)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "active": true,
  "family_name": "string",
  "gender": "male",
  "birth_date": "2019-08-24"
}
```

<h3 id="update-patient-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientSchema](#schemapatientschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## delete-patient

<a id="opIddelete-patient"></a>

`POST /patient/DeletePatient`

*Delete Patient Command*

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
```

<h3 id="delete-patient-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeletePatientSchema](#schemadeletepatientschema)|true|none|

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
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete-patient-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-create-beds

<a id="opIdbatch-create-beds"></a>

`POST /patient/bed/BatchCreateBeds`

*Batch Create Beds*

> Body parameter

```json
{
  "beds": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}
```

<h3 id="batch-create-beds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchCreateBedsSchema](#schemabatchcreatebedsschema)|true|none|

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
        "primary_identifier": "string",
        "active": true,
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      },
      "encounter": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
        "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
        "created_at": "2019-08-24T14:15:22Z",
        "status": "planned",
        "start_time": "2019-08-24T14:15:22Z",
        "end_time": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="batch-create-beds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedResourcesSchema-Input](#schemabedresourcesschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## create-bed

<a id="opIdcreate-bed"></a>

`POST /patient/bed/CreateBed`

*Create Bed*

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}
```

<h3 id="create-bed-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateBedSchema](#schemacreatebedschema)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "patient": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "active": true,
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "encounter": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
    "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
    "created_at": "2019-08-24T14:15:22Z",
    "status": "planned",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z"
  }
}
```

<h3 id="create-bed-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedSchema-Input](#schemabedschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## delete-bed

<a id="opIddelete-bed"></a>

`POST /patient/bed/DeleteBed`

*Delete Bed*

> Body parameter

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d"
}
```

<h3 id="delete-bed-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeleteBedSchema](#schemadeletebedschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-bed-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="delete-bed-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-update-beds

<a id="opIdbatch-update-beds"></a>

`POST /patient/bed/BatchUpdateBeds`

*Batch Update Beds*

> Body parameter

```json
{
  "beds": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}
```

<h3 id="batch-update-beds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchUpdateBedsSchema](#schemabatchupdatebedsschema)|true|none|

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
        "primary_identifier": "string",
        "active": true,
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      },
      "encounter": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
        "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
        "created_at": "2019-08-24T14:15:22Z",
        "status": "planned",
        "start_time": "2019-08-24T14:15:22Z",
        "end_time": "2019-08-24T14:15:22Z"
      }
    }
  ]
}
```

<h3 id="batch-update-beds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedResourcesSchema-Input](#schemabedresourcesschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-delete-beds

<a id="opIdbatch-delete-beds"></a>

`POST /patient/bed/BatchDeleteBeds`

*Batch Delete Beds*

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
|body|body|[BatchDeleteBedSchema](#schemabatchdeletebedschema)|true|none|

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
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="batch-delete-beds-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-create-bed-groups

<a id="opIdbatch-create-bed-groups"></a>

`POST /patient/bed-group/BatchCreateBedGroups`

*Batch Create Bed Groups*

> Body parameter

```json
{
  "groups": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string"
    }
  ]
}
```

<h3 id="batch-create-bed-groups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchCreateBedGroupsSchema](#schemabatchcreatebedgroupsschema)|true|none|

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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedGroupResourcesSchema-Input](#schemabedgroupresourcesschema-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-update-bed-groups

<a id="opIdbatch-update-bed-groups"></a>

`POST /patient/bed-group/BatchUpdateBedGroups`

*Batch Update Bed Groups*

> Body parameter

```json
{
  "groups": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string"
    }
  ]
}
```

<h3 id="batch-update-bed-groups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchUpdateBedGroupsSchema](#schemabatchupdatebedgroupsschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-update-bed-groups-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="batch-update-bed-groups-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-delete-bed-groups

<a id="opIdbatch-delete-bed-groups"></a>

`POST /patient/bed-group/BatchDeleteBedGroups`

*Batch Delete Bed Groups*

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
|body|body|[BatchDeleteBedGroupsSchema](#schemabatchdeletebedgroupsschema)|true|none|

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
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="batch-delete-bed-groups-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## create-bed-group

<a id="opIdcreate-bed-group"></a>

`POST /patient/bed-group/CreateBedGroup`

*Create Bed Group*

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "description": "string"
}
```

<h3 id="create-bed-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateBedGroupSchema](#schemacreatebedgroupschema)|true|none|

> Example responses

> 200 Response

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

<h3 id="create-bed-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[BedGroupSchema](#schemabedgroupschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-assign-beds

<a id="opIdbatch-assign-beds"></a>

`POST /patient/bed-group/BatchAssignBeds`

*Batch Assign Beds*

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

<h3 id="batch-assign-beds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchAssignBedsSchema](#schemabatchassignbedsschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-assign-beds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="batch-assign-beds-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## add-bed-to-group

<a id="opIdadd-bed-to-group"></a>

`POST /patient/bed-group/AddBed`

*Add Bed To Group*

> Body parameter

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f"
}
```

<h3 id="add-bed-to-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AddBedToGroupSchema](#schemaaddbedtogroupschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="add-bed-to-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="add-bed-to-group-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## remove-bed-from-group

<a id="opIdremove-bed-from-group"></a>

`POST /patient/bed-group/RemoveBed`

*Remove Bed From Group*

> Body parameter

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f"
}
```

<h3 id="remove-bed-from-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RemoveBedFromGroupSchema](#schemaremovebedfromgroupschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="remove-bed-from-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="remove-bed-from-group-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## delete-bed-group

<a id="opIddelete-bed-group"></a>

`POST /patient/bed-group/DeleteBedGroup`

*Delete Bed Group*

> Body parameter

```json
{
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f"
}
```

<h3 id="delete-bed-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeleteBedGroupSchema](#schemadeletebedgroupschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-bed-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="delete-bed-group-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-device-rest">Device REST</h1>

## get-device-by-identifier

<a id="opIdget-device-by-identifier"></a>

`GET /device/{device_id}`

*Get Device By Identifier*

<h3 id="get-device-by-identifier-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|device_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string",
  "vital_ranges": [],
  "alerts": []
}
```

<h3 id="get-device-by-identifier-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[DeviceResource](#schemadeviceresource)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-device-list

<a id="opIdget-device-list"></a>

`GET /device`

*Get All Devices*

<h3 id="get-device-list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|device_code|query|any|false|none|
|gateway|query|any|false|none|
|location_id|query|array[string]|false|none|
|is_gateway|query|any|false|none|

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "audio_pause_enabled": false,
      "audio_enabled": true,
      "subject_identifier": "string",
      "model_number": "string",
      "vital_ranges": [],
      "alerts": []
    }
  ]
}
```

<h3 id="get-device-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[DeviceResources-Input](#schemadeviceresources-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-device-vital-ranges

<a id="opIdget-device-vital-ranges"></a>

`GET /device/{device_id}/ranges`

*Get Device Vital Ranges*

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
      "alert_condition_enabled": true,
      "upper_limit": 0,
      "lower_limit": 0
    }
  ]
}
```

<h3 id="get-device-vital-ranges-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[VitalRangesResources](#schemavitalrangesresources)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## get-device-encounters

<a id="opIdget-device-encounters"></a>

`GET /device/{primary_identifier}/admission`

*Get Device Admissions*

<h3 id="get-device-encounters-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|primary_identifier|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "resource": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "subject": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "active": true,
      "family_name": "string",
      "gender": "male",
      "birth_date": "2019-08-24"
    },
    "device": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "audio_pause_enabled": false,
      "audio_enabled": true,
      "subject_identifier": "string",
      "model_number": "string"
    },
    "created_at": "2019-08-24T14:15:22Z",
    "status": "planned",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z"
  }
}
```

<h3 id="get-device-encounters-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[AdmissionResource-Input](#schemaadmissionresource-input)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

<h1 id="fastapi-device-commands">Device Commands</h1>

## create-device

<a id="opIdcreate-device"></a>

`POST /device/CreateDevice`

*Create Device*

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}
```

<h3 id="create-device-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateDeviceSchema](#schemacreatedeviceschema)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}
```

<h3 id="create-device-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[DeviceSchema](#schemadeviceschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## update-device

<a id="opIdupdate-device"></a>

`POST /device/UpdateDevice`

*Update Device*

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}
```

<h3 id="update-device-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdateDeviceSchema](#schemaupdatedeviceschema)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}
```

<h3 id="update-device-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[DeviceSchema](#schemadeviceschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-assign-locations

<a id="opIdbatch-assign-locations"></a>

`POST /device/BatchAssignLocation`

*Batch Assign Location*

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

<h3 id="batch-assign-locations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchAssignLocationsSchema](#schemabatchassignlocationsschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-assign-locations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="batch-assign-locations-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## batch-unassign-locations

<a id="opIdbatch-unassign-locations"></a>

`POST /device/BatchUnassignLocation`

*Batch Unassign Location*

> Body parameter

```json
{
  "device_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}
```

<h3 id="batch-unassign-locations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchUnassignLocationsSchema](#schemabatchunassignlocationsschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="batch-unassign-locations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="batch-unassign-locations-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

## delete-device

<a id="opIddelete-device"></a>

`POST /device/DeleteDevice`

*Delete Device*

> Body parameter

```json
{
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
}
```

<h3 id="delete-device-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeleteDeviceSchema](#schemadeletedeviceschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-device-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[ErrorsSchema](#schemaerrorsschema)|

<h3 id="delete-device-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
HTTPBearer
</aside>

# Schemas

<h2 id="tocS_AddBedToGroupSchema">AddBedToGroupSchema</h2>
<!-- backwards compatibility -->
<a id="schemaaddbedtogroupschema"></a>
<a id="schema_AddBedToGroupSchema"></a>
<a id="tocSaddbedtogroupschema"></a>
<a id="tocsaddbedtogroupschema"></a>

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f"
}

```

AddBedToGroupSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_id|string(uuid)|true|none|none|
|group_id|string(uuid)|true|none|none|

<h2 id="tocS_AdmissionResource-Input">AdmissionResource-Input</h2>
<!-- backwards compatibility -->
<a id="schemaadmissionresource-input"></a>
<a id="schema_AdmissionResource-Input"></a>
<a id="tocSadmissionresource-input"></a>
<a id="tocsadmissionresource-input"></a>

```json
{
  "resource": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "subject": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "active": true,
      "given_name": "pa$$word",
      "family_name": "string",
      "gender": "male",
      "birth_date": "2019-08-24"
    },
    "device": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "audio_pause_enabled": false,
      "audio_enabled": true,
      "subject_identifier": "string",
      "model_number": "string"
    },
    "created_at": "2019-08-24T14:15:22Z",
    "status": "planned",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z"
  }
}

```

AdmissionResource

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resource|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[AdmissionSchema-Input](#schemaadmissionschema-input)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_AdmissionResource-Output">AdmissionResource-Output</h2>
<!-- backwards compatibility -->
<a id="schemaadmissionresource-output"></a>
<a id="schema_AdmissionResource-Output"></a>
<a id="tocSadmissionresource-output"></a>
<a id="tocsadmissionresource-output"></a>

```json
{
  "resource": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "subject": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "active": true,
      "given_name": "pa$$word",
      "family_name": "string",
      "gender": "male",
      "birth_date": "2019-08-24"
    },
    "device": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "audio_pause_enabled": false,
      "audio_enabled": true,
      "subject_identifier": "string",
      "model_number": "string"
    },
    "created_at": "2019-08-24T14:15:22Z",
    "status": "planned",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z"
  }
}

```

AdmissionResource

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resource|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[AdmissionSchema-Output](#schemaadmissionschema-output)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_AdmissionSchema-Input">AdmissionSchema-Input</h2>
<!-- backwards compatibility -->
<a id="schemaadmissionschema-input"></a>
<a id="schema_AdmissionSchema-Input"></a>
<a id="tocSadmissionschema-input"></a>
<a id="tocsadmissionschema-input"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "subject": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "active": true,
    "given_name": "pa$$word",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "device": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "name": "string",
    "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
    "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
    "audio_pause_enabled": false,
    "audio_enabled": true,
    "subject_identifier": "string",
    "model_number": "string"
  },
  "created_at": "2019-08-24T14:15:22Z",
  "status": "planned",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}

```

AdmissionSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|subject|[PatientSchema](#schemapatientschema)|true|none|none|
|device|[DeviceSchema](#schemadeviceschema)|true|none|none|
|created_at|string(date-time)|true|none|none|
|status|[EncounterStatus](#schemaencounterstatus)|true|none|none|
|start_time|any|false|none|none|

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
|end_time|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_AdmissionSchema-Output">AdmissionSchema-Output</h2>
<!-- backwards compatibility -->
<a id="schemaadmissionschema-output"></a>
<a id="schema_AdmissionSchema-Output"></a>
<a id="tocSadmissionschema-output"></a>
<a id="tocsadmissionschema-output"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "subject": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "active": true,
    "given_name": "pa$$word",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "device": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "name": "string",
    "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
    "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
    "audio_pause_enabled": false,
    "audio_enabled": true,
    "subject_identifier": "string",
    "model_number": "string"
  },
  "created_at": "2019-08-24T14:15:22Z",
  "status": "planned",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}

```

AdmissionSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|subject|[PatientSchema](#schemapatientschema)|true|none|none|
|device|[DeviceSchema](#schemadeviceschema)|true|none|none|
|created_at|string(date-time)|true|none|none|
|status|[EncounterStatus](#schemaencounterstatus)|true|none|none|
|start_time|any|false|none|none|

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
|end_time|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_AssignLocationSchema">AssignLocationSchema</h2>
<!-- backwards compatibility -->
<a id="schemaassignlocationschema"></a>
<a id="schema_AssignLocationSchema"></a>
<a id="tocSassignlocationschema"></a>
<a id="tocsassignlocationschema"></a>

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
}

```

AssignLocationSchema

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

<h2 id="tocS_BatchAssignBedsSchema">BatchAssignBedsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchassignbedsschema"></a>
<a id="schema_BatchAssignBedsSchema"></a>
<a id="tocSbatchassignbedsschema"></a>
<a id="tocsbatchassignbedsschema"></a>

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

BatchAssignBedsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[GroupBedAssignmentSchema](#schemagroupbedassignmentschema)]|true|none|none|

<h2 id="tocS_BatchAssignLocationsSchema">BatchAssignLocationsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchassignlocationsschema"></a>
<a id="schema_BatchAssignLocationsSchema"></a>
<a id="tocSbatchassignlocationsschema"></a>
<a id="tocsbatchassignlocationsschema"></a>

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

BatchAssignLocationsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|associations|[[AssignLocationSchema](#schemaassignlocationschema)]|true|none|none|

<h2 id="tocS_BatchCreateBedGroupsSchema">BatchCreateBedGroupsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchcreatebedgroupsschema"></a>
<a id="schema_BatchCreateBedGroupsSchema"></a>
<a id="tocSbatchcreatebedgroupsschema"></a>
<a id="tocsbatchcreatebedgroupsschema"></a>

```json
{
  "groups": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string"
    }
  ]
}

```

BatchCreateBedGroupsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|groups|[[CreateBedGroupSchema](#schemacreatebedgroupschema)]|true|none|none|

<h2 id="tocS_BatchCreateBedsSchema">BatchCreateBedsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchcreatebedsschema"></a>
<a id="schema_BatchCreateBedsSchema"></a>
<a id="tocSbatchcreatebedsschema"></a>
<a id="tocsbatchcreatebedsschema"></a>

```json
{
  "beds": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}

```

BatchCreateBedsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|beds|[[CreateBedSchema](#schemacreatebedschema)]|true|none|none|

<h2 id="tocS_BatchDeleteBedGroupsSchema">BatchDeleteBedGroupsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchdeletebedgroupsschema"></a>
<a id="schema_BatchDeleteBedGroupsSchema"></a>
<a id="tocSbatchdeletebedgroupsschema"></a>
<a id="tocsbatchdeletebedgroupsschema"></a>

```json
{
  "group_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

BatchDeleteBedGroupsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group_ids|[string]|true|none|none|

<h2 id="tocS_BatchDeleteBedSchema">BatchDeleteBedSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchdeletebedschema"></a>
<a id="schema_BatchDeleteBedSchema"></a>
<a id="tocSbatchdeletebedschema"></a>
<a id="tocsbatchdeletebedschema"></a>

```json
{
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

BatchDeleteBedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_ids|[string]|true|none|none|

<h2 id="tocS_BatchUnassignLocationsSchema">BatchUnassignLocationsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchunassignlocationsschema"></a>
<a id="schema_BatchUnassignLocationsSchema"></a>
<a id="tocSbatchunassignlocationsschema"></a>
<a id="tocsbatchunassignlocationsschema"></a>

```json
{
  "device_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

BatchUnassignLocationsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|device_ids|[string]|true|none|none|

<h2 id="tocS_BatchUpdateBedGroupsSchema">BatchUpdateBedGroupsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchupdatebedgroupsschema"></a>
<a id="schema_BatchUpdateBedGroupsSchema"></a>
<a id="tocSbatchupdatebedgroupsschema"></a>
<a id="tocsbatchupdatebedgroupsschema"></a>

```json
{
  "groups": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "description": "string"
    }
  ]
}

```

BatchUpdateBedGroupsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|groups|[[UpdateBedGroupSchema](#schemaupdatebedgroupschema)]|true|none|none|

<h2 id="tocS_BatchUpdateBedsSchema">BatchUpdateBedsSchema</h2>
<!-- backwards compatibility -->
<a id="schemabatchupdatebedsschema"></a>
<a id="schema_BatchUpdateBedsSchema"></a>
<a id="tocSbatchupdatebedsschema"></a>
<a id="tocsbatchupdatebedsschema"></a>

```json
{
  "beds": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string"
    }
  ]
}

```

BatchUpdateBedsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|beds|[[UpdateBedSchema](#schemaupdatebedschema)]|true|none|none|

<h2 id="tocS_BedGroupBedSchema">BedGroupBedSchema</h2>
<!-- backwards compatibility -->
<a id="schemabedgroupbedschema"></a>
<a id="schema_BedGroupBedSchema"></a>
<a id="tocSbedgroupbedschema"></a>
<a id="tocsbedgroupbedschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

BedGroupBedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|

<h2 id="tocS_BedGroupResourcesSchema-Input">BedGroupResourcesSchema-Input</h2>
<!-- backwards compatibility -->
<a id="schemabedgroupresourcesschema-input"></a>
<a id="schema_BedGroupResourcesSchema-Input"></a>
<a id="tocSbedgroupresourcesschema-input"></a>
<a id="tocsbedgroupresourcesschema-input"></a>

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

BedGroupResourcesSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[BedGroupSchema](#schemabedgroupschema)]|true|none|none|

<h2 id="tocS_BedGroupResourcesSchema-Output">BedGroupResourcesSchema-Output</h2>
<!-- backwards compatibility -->
<a id="schemabedgroupresourcesschema-output"></a>
<a id="schema_BedGroupResourcesSchema-Output"></a>
<a id="tocSbedgroupresourcesschema-output"></a>
<a id="tocsbedgroupresourcesschema-output"></a>

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

BedGroupResourcesSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[BedGroupSchema](#schemabedgroupschema)]|true|none|none|

<h2 id="tocS_BedGroupSchema">BedGroupSchema</h2>
<!-- backwards compatibility -->
<a id="schemabedgroupschema"></a>
<a id="schema_BedGroupSchema"></a>
<a id="tocSbedgroupschema"></a>
<a id="tocsbedgroupschema"></a>

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

BedGroupSchema

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
|beds|[[BedGroupBedSchema](#schemabedgroupbedschema)]|true|none|none|

<h2 id="tocS_BedResourcesSchema-Input">BedResourcesSchema-Input</h2>
<!-- backwards compatibility -->
<a id="schemabedresourcesschema-input"></a>
<a id="schema_BedResourcesSchema-Input"></a>
<a id="tocSbedresourcesschema-input"></a>
<a id="tocsbedresourcesschema-input"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primary_identifier": "string",
        "active": true,
        "given_name": "pa$$word",
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      },
      "encounter": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
        "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
        "created_at": "2019-08-24T14:15:22Z",
        "status": "planned",
        "start_time": "2019-08-24T14:15:22Z",
        "end_time": "2019-08-24T14:15:22Z"
      }
    }
  ]
}

```

BedResourcesSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[BedSchema-Input](#schemabedschema-input)]|true|none|none|

<h2 id="tocS_BedResourcesSchema-Output">BedResourcesSchema-Output</h2>
<!-- backwards compatibility -->
<a id="schemabedresourcesschema-output"></a>
<a id="schema_BedResourcesSchema-Output"></a>
<a id="tocSbedresourcesschema-output"></a>
<a id="tocsbedresourcesschema-output"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "patient": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "primary_identifier": "string",
        "active": true,
        "given_name": "pa$$word",
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      },
      "encounter": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
        "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
        "created_at": "2019-08-24T14:15:22Z",
        "status": "planned",
        "start_time": "2019-08-24T14:15:22Z",
        "end_time": "2019-08-24T14:15:22Z"
      }
    }
  ]
}

```

BedResourcesSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[BedSchema-Output](#schemabedschema-output)]|true|none|none|

<h2 id="tocS_BedSchema-Input">BedSchema-Input</h2>
<!-- backwards compatibility -->
<a id="schemabedschema-input"></a>
<a id="schema_BedSchema-Input"></a>
<a id="tocSbedschema-input"></a>
<a id="tocsbedschema-input"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "patient": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "active": true,
    "given_name": "pa$$word",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "encounter": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
    "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
    "created_at": "2019-08-24T14:15:22Z",
    "status": "planned",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z"
  }
}

```

BedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|
|patient|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PatientSchema](#schemapatientschema)|false|none|none|

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
|» *anonymous*|[EncounterSchema](#schemaencounterschema)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_BedSchema-Output">BedSchema-Output</h2>
<!-- backwards compatibility -->
<a id="schemabedschema-output"></a>
<a id="schema_BedSchema-Output"></a>
<a id="tocSbedschema-output"></a>
<a id="tocsbedschema-output"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "patient": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "primary_identifier": "string",
    "active": true,
    "given_name": "pa$$word",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "encounter": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
    "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
    "created_at": "2019-08-24T14:15:22Z",
    "status": "planned",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z"
  }
}

```

BedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|
|patient|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PatientSchema](#schemapatientschema)|false|none|none|

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
|» *anonymous*|[EncounterSchema](#schemaencounterschema)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_CreateBedGroupSchema">CreateBedGroupSchema</h2>
<!-- backwards compatibility -->
<a id="schemacreatebedgroupschema"></a>
<a id="schema_CreateBedGroupSchema"></a>
<a id="tocScreatebedgroupschema"></a>
<a id="tocscreatebedgroupschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "description": "string"
}

```

CreateBedGroupSchema

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

<h2 id="tocS_CreateBedSchema">CreateBedSchema</h2>
<!-- backwards compatibility -->
<a id="schemacreatebedschema"></a>
<a id="schema_CreateBedSchema"></a>
<a id="tocScreatebedschema"></a>
<a id="tocscreatebedschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

CreateBedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|

<h2 id="tocS_CreateDeviceSchema">CreateDeviceSchema</h2>
<!-- backwards compatibility -->
<a id="schemacreatedeviceschema"></a>
<a id="schema_CreateDeviceSchema"></a>
<a id="tocScreatedeviceschema"></a>
<a id="tocscreatedeviceschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}

```

CreateDeviceSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
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
|audio_pause_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subject_identifier|any|false|none|none|

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
|model_number|string|true|none|none|

<h2 id="tocS_CreatePatientSchema">CreatePatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemacreatepatientschema"></a>
<a id="schema_CreatePatientSchema"></a>
<a id="tocScreatepatientschema"></a>
<a id="tocscreatepatientschema"></a>

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

CreatePatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
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

<h2 id="tocS_DeleteBedGroupSchema">DeleteBedGroupSchema</h2>
<!-- backwards compatibility -->
<a id="schemadeletebedgroupschema"></a>
<a id="schema_DeleteBedGroupSchema"></a>
<a id="tocSdeletebedgroupschema"></a>
<a id="tocsdeletebedgroupschema"></a>

```json
{
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f"
}

```

DeleteBedGroupSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group_id|string(uuid)|true|none|none|

<h2 id="tocS_DeleteBedSchema">DeleteBedSchema</h2>
<!-- backwards compatibility -->
<a id="schemadeletebedschema"></a>
<a id="schema_DeleteBedSchema"></a>
<a id="tocSdeletebedschema"></a>
<a id="tocsdeletebedschema"></a>

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d"
}

```

DeleteBedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_id|string(uuid)|true|none|none|

<h2 id="tocS_DeleteDeviceSchema">DeleteDeviceSchema</h2>
<!-- backwards compatibility -->
<a id="schemadeletedeviceschema"></a>
<a id="schema_DeleteDeviceSchema"></a>
<a id="tocSdeletedeviceschema"></a>
<a id="tocsdeletedeviceschema"></a>

```json
{
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
}

```

DeleteDeviceSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|device_id|string(uuid)|true|none|none|

<h2 id="tocS_DeletePatientSchema">DeletePatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemadeletepatientschema"></a>
<a id="schema_DeletePatientSchema"></a>
<a id="tocSdeletepatientschema"></a>
<a id="tocsdeletepatientschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}

```

DeletePatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|

<h2 id="tocS_DeviceAlert">DeviceAlert</h2>
<!-- backwards compatibility -->
<a id="schemadevicealert"></a>
<a id="schema_DeviceAlert"></a>
<a id="tocSdevicealert"></a>
<a id="tocsdevicealert"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "code": "string",
  "priority": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

DeviceAlert

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|code|string|true|none|none|
|priority|string|true|none|none|
|created_at|string(date-time)|true|none|none|

<h2 id="tocS_DeviceResource">DeviceResource</h2>
<!-- backwards compatibility -->
<a id="schemadeviceresource"></a>
<a id="schema_DeviceResource"></a>
<a id="tocSdeviceresource"></a>
<a id="tocsdeviceresource"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string",
  "vital_ranges": [],
  "alerts": []
}

```

DeviceResource

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
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
|audio_pause_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subject_identifier|any|false|none|none|

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
|model_number|string|true|none|none|
|vital_ranges|[[VitalRange](#schemavitalrange)]|false|none|none|
|alerts|[[DeviceAlert](#schemadevicealert)]|false|none|none|

<h2 id="tocS_DeviceResources-Input">DeviceResources-Input</h2>
<!-- backwards compatibility -->
<a id="schemadeviceresources-input"></a>
<a id="schema_DeviceResources-Input"></a>
<a id="tocSdeviceresources-input"></a>
<a id="tocsdeviceresources-input"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "audio_pause_enabled": false,
      "audio_enabled": true,
      "subject_identifier": "string",
      "model_number": "string",
      "vital_ranges": [],
      "alerts": []
    }
  ]
}

```

DeviceResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[DeviceResource](#schemadeviceresource)]|true|none|none|

<h2 id="tocS_DeviceResources-Output">DeviceResources-Output</h2>
<!-- backwards compatibility -->
<a id="schemadeviceresources-output"></a>
<a id="schema_DeviceResources-Output"></a>
<a id="tocSdeviceresources-output"></a>
<a id="tocsdeviceresources-output"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "name": "string",
      "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
      "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
      "audio_pause_enabled": false,
      "audio_enabled": true,
      "subject_identifier": "string",
      "model_number": "string",
      "vital_ranges": [],
      "alerts": []
    }
  ]
}

```

DeviceResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[DeviceResource](#schemadeviceresource)]|true|none|none|

<h2 id="tocS_DeviceSchema">DeviceSchema</h2>
<!-- backwards compatibility -->
<a id="schemadeviceschema"></a>
<a id="schema_DeviceSchema"></a>
<a id="tocSdeviceschema"></a>
<a id="tocsdeviceschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}

```

DeviceSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
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
|audio_pause_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subject_identifier|any|false|none|none|

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
|model_number|string|true|none|none|

<h2 id="tocS_DismissPatientAdmissionPayload">DismissPatientAdmissionPayload</h2>
<!-- backwards compatibility -->
<a id="schemadismisspatientadmissionpayload"></a>
<a id="schema_DismissPatientAdmissionPayload"></a>
<a id="tocSdismisspatientadmissionpayload"></a>
<a id="tocsdismisspatientadmissionpayload"></a>

```json
{
  "patient_id": "3854866a-5476-48be-8313-77029ccdd7a7"
}

```

DismissPatientAdmissionPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patient_id|string(uuid)|true|none|none|

<h2 id="tocS_EncounterSchema">EncounterSchema</h2>
<!-- backwards compatibility -->
<a id="schemaencounterschema"></a>
<a id="schema_EncounterSchema"></a>
<a id="tocSencounterschema"></a>
<a id="tocsencounterschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940",
  "created_at": "2019-08-24T14:15:22Z",
  "status": "planned",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z"
}

```

EncounterSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|subject_id|string(uuid)|true|none|none|
|device_id|string(uuid)|true|none|none|
|created_at|string(date-time)|true|none|none|
|status|[EncounterStatus](#schemaencounterstatus)|true|none|none|
|start_time|any|false|none|none|

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
|end_time|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_EncounterStatus">EncounterStatus</h2>
<!-- backwards compatibility -->
<a id="schemaencounterstatus"></a>
<a id="schema_EncounterStatus"></a>
<a id="tocSencounterstatus"></a>
<a id="tocsencounterstatus"></a>

```json
"planned"

```

EncounterStatus

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|EncounterStatus|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|EncounterStatus|planned|
|EncounterStatus|in-progress|
|EncounterStatus|completed|
|EncounterStatus|cancelled|

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
|msg|string|true|none|none|
|type|string|true|none|none|
|ctx|object|false|none|none|

<h2 id="tocS_ErrorsSchema">ErrorsSchema</h2>
<!-- backwards compatibility -->
<a id="schemaerrorsschema"></a>
<a id="schema_ErrorsSchema"></a>
<a id="tocSerrorsschema"></a>
<a id="tocserrorsschema"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string",
      "ctx": {}
    }
  ]
}

```

ErrorsSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ErrorSchema](#schemaerrorschema)]|true|none|none|

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

<h2 id="tocS_GroupBedAssignmentSchema">GroupBedAssignmentSchema</h2>
<!-- backwards compatibility -->
<a id="schemagroupbedassignmentschema"></a>
<a id="schema_GroupBedAssignmentSchema"></a>
<a id="tocSgroupbedassignmentschema"></a>
<a id="tocsgroupbedassignmentschema"></a>

```json
{
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f",
  "bed_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

GroupBedAssignmentSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group_id|string(uuid)|true|none|none|
|bed_ids|[string]|true|none|none|

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

<h2 id="tocS_PatientAdmissionSchema">PatientAdmissionSchema</h2>
<!-- backwards compatibility -->
<a id="schemapatientadmissionschema"></a>
<a id="schema_PatientAdmissionSchema"></a>
<a id="tocSpatientadmissionschema"></a>
<a id="tocspatientadmissionschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d"
}

```

PatientAdmissionSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|subject_id|string(uuid)|true|none|none|
|bed_id|string(uuid)|true|none|none|

<h2 id="tocS_PatientCount">PatientCount</h2>
<!-- backwards compatibility -->
<a id="schemapatientcount"></a>
<a id="schema_PatientCount"></a>
<a id="tocSpatientcount"></a>
<a id="tocspatientcount"></a>

```json
{
  "total": 0
}

```

PatientCount

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total|integer|true|none|none|

<h2 id="tocS_PatientObservation-Input">PatientObservation-Input</h2>
<!-- backwards compatibility -->
<a id="schemapatientobservation-input"></a>
<a id="schema_PatientObservation-Input"></a>
<a id="tocSpatientobservation-input"></a>
<a id="tocspatientobservation-input"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "category": "string",
  "code": "string",
  "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
  "effective_dt": "2019-08-24T14:15:22Z",
  "value_number": 0,
  "value_text": "string",
  "device_primary_identifier": "string",
  "device_code": "string"
}

```

PatientObservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|category|string|true|none|none|
|code|string|true|none|none|
|subject_id|string(uuid)|true|none|none|
|effective_dt|string(date-time)|true|none|none|
|value_number|any|false|none|none|

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
|value_text|any|false|none|none|

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
|device_primary_identifier|any|false|none|none|

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
|device_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PatientObservation-Output">PatientObservation-Output</h2>
<!-- backwards compatibility -->
<a id="schemapatientobservation-output"></a>
<a id="schema_PatientObservation-Output"></a>
<a id="tocSpatientobservation-output"></a>
<a id="tocspatientobservation-output"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "category": "string",
  "code": "string",
  "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
  "effective_dt": "2019-08-24T14:15:22Z",
  "value_number": "string",
  "value_text": "string",
  "device_primary_identifier": "string",
  "device_code": "string"
}

```

PatientObservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|category|string|true|none|none|
|code|string|true|none|none|
|subject_id|string(uuid)|true|none|none|
|effective_dt|string(date-time)|true|none|none|
|value_number|any|false|none|none|

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
|value_text|any|false|none|none|

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
|device_primary_identifier|any|false|none|none|

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
|device_code|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PatientObservationResources-Input">PatientObservationResources-Input</h2>
<!-- backwards compatibility -->
<a id="schemapatientobservationresources-input"></a>
<a id="schema_PatientObservationResources-Input"></a>
<a id="tocSpatientobservationresources-input"></a>
<a id="tocspatientobservationresources-input"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "category": "string",
      "code": "string",
      "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
      "effective_dt": "2019-08-24T14:15:22Z",
      "value_number": 0,
      "value_text": "string",
      "device_primary_identifier": "string",
      "device_code": "string"
    }
  ]
}

```

PatientObservationResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[PatientObservation-Input](#schemapatientobservation-input)]|true|none|none|

<h2 id="tocS_PatientObservationResources-Output">PatientObservationResources-Output</h2>
<!-- backwards compatibility -->
<a id="schemapatientobservationresources-output"></a>
<a id="schema_PatientObservationResources-Output"></a>
<a id="tocSpatientobservationresources-output"></a>
<a id="tocspatientobservationresources-output"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "category": "string",
      "code": "string",
      "subject_id": "80e197be-61ad-4068-b4ff-a483fb5c18f9",
      "effective_dt": "2019-08-24T14:15:22Z",
      "value_number": "string",
      "value_text": "string",
      "device_primary_identifier": "string",
      "device_code": "string"
    }
  ]
}

```

PatientObservationResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[PatientObservation-Output](#schemapatientobservation-output)]|true|none|none|

<h2 id="tocS_PatientResources-Input">PatientResources-Input</h2>
<!-- backwards compatibility -->
<a id="schemapatientresources-input"></a>
<a id="schema_PatientResources-Input"></a>
<a id="tocSpatientresources-input"></a>
<a id="tocspatientresources-input"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "active": true,
      "given_name": "pa$$word",
      "family_name": "string",
      "gender": "male",
      "birth_date": "2019-08-24"
    }
  ]
}

```

PatientResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[PatientSchema](#schemapatientschema)]|true|none|none|

<h2 id="tocS_PatientResources-Output">PatientResources-Output</h2>
<!-- backwards compatibility -->
<a id="schemapatientresources-output"></a>
<a id="schema_PatientResources-Output"></a>
<a id="tocSpatientresources-output"></a>
<a id="tocspatientresources-output"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "primary_identifier": "string",
      "active": true,
      "given_name": "pa$$word",
      "family_name": "string",
      "gender": "male",
      "birth_date": "2019-08-24"
    }
  ]
}

```

PatientResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[PatientSchema](#schemapatientschema)]|true|none|none|

<h2 id="tocS_PatientSchema">PatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemapatientschema"></a>
<a id="schema_PatientSchema"></a>
<a id="tocSpatientschema"></a>
<a id="tocspatientschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "active": true,
  "given_name": "pa$$word",
  "family_name": "string",
  "gender": "male",
  "birth_date": "2019-08-24"
}

```

PatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|active|boolean|true|none|none|
|given_name|string(password)|true|write-only|none|
|family_name|string|true|none|none|
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

<h2 id="tocS_RemoveBedFromGroupSchema">RemoveBedFromGroupSchema</h2>
<!-- backwards compatibility -->
<a id="schemaremovebedfromgroupschema"></a>
<a id="schema_RemoveBedFromGroupSchema"></a>
<a id="tocSremovebedfromgroupschema"></a>
<a id="tocsremovebedfromgroupschema"></a>

```json
{
  "bed_id": "792fa722-82b1-4f7c-bcec-517c20675e0d",
  "group_id": "306db4e0-7449-4501-b76f-075576fe2d8f"
}

```

RemoveBedFromGroupSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bed_id|string(uuid)|true|none|none|
|group_id|string(uuid)|true|none|none|

<h2 id="tocS_SessionPhysiologicalAlert">SessionPhysiologicalAlert</h2>
<!-- backwards compatibility -->
<a id="schemasessionphysiologicalalert"></a>
<a id="schema_SessionPhysiologicalAlert"></a>
<a id="tocSsessionphysiologicalalert"></a>
<a id="tocssessionphysiologicalalert"></a>

```json
{
  "code": "string",
  "start_determination_time": "2019-08-24T14:15:22Z",
  "end_determination_time": "2019-08-24T14:15:22Z",
  "value_text": "string",
  "device_primary_identifier": "string",
  "device_code": "string",
  "trigger_lower_limit": 0,
  "trigger_upper_limit": 0
}

```

SessionPhysiologicalAlert

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|true|none|none|
|start_determination_time|string(date-time)|true|none|none|
|end_determination_time|string(date-time)|true|none|none|
|value_text|string|true|none|none|
|device_primary_identifier|string|true|none|none|
|device_code|string|true|none|none|
|trigger_lower_limit|any|false|none|none|

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
|trigger_upper_limit|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_UpdateBedGroupSchema">UpdateBedGroupSchema</h2>
<!-- backwards compatibility -->
<a id="schemaupdatebedgroupschema"></a>
<a id="schema_UpdateBedGroupSchema"></a>
<a id="tocSupdatebedgroupschema"></a>
<a id="tocsupdatebedgroupschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "description": "string"
}

```

UpdateBedGroupSchema

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

<h2 id="tocS_UpdateBedSchema">UpdateBedSchema</h2>
<!-- backwards compatibility -->
<a id="schemaupdatebedschema"></a>
<a id="schema_UpdateBedSchema"></a>
<a id="tocSupdatebedschema"></a>
<a id="tocsupdatebedschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

UpdateBedSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|name|string|true|none|none|

<h2 id="tocS_UpdateDeviceSchema">UpdateDeviceSchema</h2>
<!-- backwards compatibility -->
<a id="schemaupdatedeviceschema"></a>
<a id="schema_UpdateDeviceSchema"></a>
<a id="tocSupdatedeviceschema"></a>
<a id="tocsupdatedeviceschema"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "primary_identifier": "string",
  "name": "string",
  "gateway_id": "1e5bdd53-7c2c-40df-abae-1e0aaf757beb",
  "location_id": "46910cc3-ab41-4b80-b4a7-94dab9f1b795",
  "audio_pause_enabled": false,
  "audio_enabled": true,
  "subject_identifier": "string",
  "model_number": "string"
}

```

UpdateDeviceSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
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
|audio_pause_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_enabled|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subject_identifier|any|false|none|none|

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
|model_number|string|true|none|none|

<h2 id="tocS_UpdatePatientSchema">UpdatePatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemaupdatepatientschema"></a>
<a id="schema_UpdatePatientSchema"></a>
<a id="tocSupdatepatientschema"></a>
<a id="tocsupdatepatientschema"></a>

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

UpdatePatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
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

<h2 id="tocS_VitalRange">VitalRange</h2>
<!-- backwards compatibility -->
<a id="schemavitalrange"></a>
<a id="schema_VitalRange"></a>
<a id="tocSvitalrange"></a>
<a id="tocsvitalrange"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "code": "string",
  "alert_condition_enabled": true,
  "upper_limit": 0,
  "lower_limit": 0
}

```

VitalRange

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|code|string|true|none|none|
|alert_condition_enabled|boolean|true|none|none|
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

<h2 id="tocS_VitalRangesResources">VitalRangesResources</h2>
<!-- backwards compatibility -->
<a id="schemavitalrangesresources"></a>
<a id="schema_VitalRangesResources"></a>
<a id="tocSvitalrangesresources"></a>
<a id="tocsvitalrangesresources"></a>

```json
{
  "resources": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "code": "string",
      "alert_condition_enabled": true,
      "upper_limit": 0,
      "lower_limit": 0
    }
  ]
}

```

VitalRangesResources

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[VitalRange](#schemavitalrange)]|true|none|none|

