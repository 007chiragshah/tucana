<div align="center">
<h2>⚜️ API Documentation</h2>
</div>

<h1 id="--healthcheck">HealthCheck</h1>

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

## get_health_check_api_emulator_health_get

<a id="opIdget_health_check_api_emulator_health_get"></a>

`GET /emulator/health`

*Get Health Check Api*

> Example responses

> 200 Response

```json
{
  "status": "Healthy"
}
```

<h3 id="get_health_check_api_emulator_health_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[HealthCheck](#schemahealthcheck)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="--alarms">Alarms</h1>

## put_alarm_api_emulator_alarm_put

<a id="opIdput_alarm_api_emulator_alarm_put"></a>

`PUT /emulator/alarm`

*Put Alarm Api*

> Body parameter

```json
{
  "patient_primary_identifier": "string",
  "code": "258098",
  "priority": "HI",
  "description": "string",
  "device_code": "ADAM",
  "device_primary_identifier": "string",
  "active": true,
  "determination_time": 0,
  "vital_range": {
    "code": "0001",
    "upper_limit": 0,
    "lower_limit": 0,
    "alert_condition_enabled": true
  },
  "latching": false
}
```

<h3 id="put_alarm_api_emulator_alarm_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AlarmPayload](#schemaalarmpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="put_alarm_api_emulator_alarm_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="put_alarm_api_emulator_alarm_put-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## put_technical_alert_emulator_technical_alert_put

<a id="opIdput_technical_alert_emulator_technical_alert_put"></a>

`PUT /emulator/technical_alert`

*Put Technical Alert*

> Body parameter

```json
{
  "patient_primary_identifier": "string",
  "device_primary_identifier": "string",
  "code": "258098",
  "priority": "HI",
  "device_code": "ADAM",
  "active": true,
  "determination_time": 0,
  "vital_range": {
    "code": "0001",
    "upper_limit": 0,
    "lower_limit": 0,
    "alert_condition_enabled": true
  }
}
```

<h3 id="put_technical_alert_emulator_technical_alert_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TechnicalAlarmPayload](#schematechnicalalarmpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="put_technical_alert_emulator_technical_alert_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="put_technical_alert_emulator_technical_alert_put-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## put_device_range_api_emulator_device_range_put

<a id="opIdput_device_range_api_emulator_device_range_put"></a>

`PUT /emulator/device/range`

*Put Device Range Api*

> Body parameter

```json
{
  "primary_identifier": "string",
  "ranges": [
    {
      "code": "258418",
      "lower_limit": 0,
      "upper_limit": 0,
      "alert_condition_enabled": true
    }
  ]
}
```

<h3 id="put_device_range_api_emulator_device_range_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeviceRangesPayload](#schemadevicerangespayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="put_device_range_api_emulator_device_range_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="put_device_range_api_emulator_device_range_put-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="--proxy">Proxy</h1>

## delete-device-command

<a id="opIddelete-device-command"></a>

`POST /emulator/proxy/device/command/DeleteDevice`

*Delete Device Command*

> Body parameter

```json
{
  "device_id": "3bafab7b-4400-4bcf-8e6e-09f954699940"
}
```

<h3 id="delete-device-command-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeleteDeviceSchema](#schemadeletedeviceschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-device-command-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete-device-command-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="--sensors">Sensors</h1>

## connect-sensor

<a id="opIdconnect-sensor"></a>

`POST /emulator/sensor/ConnectSensor`

*Connect Emulated Sensor*

> Body parameter

```json
{
  "primary_identifier": "string",
  "patient_monitor_primary_identifier": "string",
  "name": "string",
  "device_code": "ADAM"
}
```

<h3 id="connect-sensor-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeviceSensorSchema](#schemadevicesensorschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="connect-sensor-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="connect-sensor-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## disconnect-sensor

<a id="opIddisconnect-sensor"></a>

`POST /emulator/sensor/DisconnectSensor`

*Disconnect Emulated Sensor*

> Body parameter

```json
{
  "primary_identifier": "string"
}
```

<h3 id="disconnect-sensor-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DisconnectSensorSchema](#schemadisconnectsensorschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="disconnect-sensor-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="disconnect-sensor-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## update-sensor-mode

<a id="opIdupdate-sensor-mode"></a>

`POST /emulator/sensor/UpdateSensorMode`

*Update Sensor Mode*

> Body parameter

```json
{
  "primary_identifier": "string",
  "emulator_name": "MONITOR_CONNECTION_STATUS",
  "mode": "low"
}
```

<h3 id="update-sensor-mode-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdateSensorModeWebSchema](#schemaupdatesensormodewebschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="update-sensor-mode-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="update-sensor-mode-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="--monitor">Monitor</h1>

## get-emulated-patient-monitors

<a id="opIdget-emulated-patient-monitors"></a>

`GET /emulator/monitor`

*Get Emulated Patient Monitors*

> Example responses

> 200 Response

```json
{
  "resources": [
    {
      "primary_identifier": "string",
      "name": "string",
      "sensors": [
        {
          "primary_identifier": "string",
          "type": "string",
          "name": "string",
          "emulators": [
            {
              "name": "string",
              "current_mode": "string",
              "emulation_modes": [
                "string"
              ]
            }
          ]
        }
      ],
      "emulators": [
        {
          "name": "string",
          "current_mode": "string",
          "emulation_modes": [
            "string"
          ]
        }
      ],
      "patient": {
        "primary_identifier": "string",
        "given_name": "string",
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      }
    }
  ]
}
```

<h3 id="get-emulated-patient-monitors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[PatientMonitorResourcesSchema](#schemapatientmonitorresourcesschema)|

<aside class="success">
This operation does not require authentication
</aside>

## connect-patient-monitor

<a id="opIdconnect-patient-monitor"></a>

`POST /emulator/monitor/ConnectPatientMonitor`

*Connect Emulated Patient Monitor*

> Body parameter

```json
{
  "primary_identifier": "string",
  "name": "string",
  "patient": {
    "primary_identifier": "string",
    "given_name": "string",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "connected_sensors": [
    {
      "primary_identifier": "string",
      "name": "string",
      "device_code": "ADAM"
    }
  ],
  "config": {
    "audio_pause_enabled": false,
    "audio_enabled": true
  }
}
```

<h3 id="connect-patient-monitor-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeviceMonitorSchema](#schemadevicemonitorschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="connect-patient-monitor-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="connect-patient-monitor-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## disconnect-monitor

<a id="opIddisconnect-monitor"></a>

`POST /emulator/monitor/DisconnectMonitor`

*Disconnect Emulated Monitor*

> Body parameter

```json
{
  "primary_identifier": "string"
}
```

<h3 id="disconnect-monitor-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DisconnectMonitorSchema](#schemadisconnectmonitorschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="disconnect-monitor-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="disconnect-monitor-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## open-patient-session

<a id="opIdopen-patient-session"></a>

`POST /emulator/monitor/OpenPatientSession`

*Open Patient Session*

> Body parameter

```json
{
  "patient_monitor_primary_identifier": "string",
  "patient": {
    "primary_identifier": "string",
    "given_name": "string",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  }
}
```

<h3 id="open-patient-session-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PatientSessionOpenedPayload](#schemapatientsessionopenedpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="open-patient-session-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="open-patient-session-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## close-patient-session

<a id="opIdclose-patient-session"></a>

`POST /emulator/monitor/ClosePatientSession`

*Close Patient Session*

> Body parameter

```json
{
  "patient_monitor_primary_identifier": "string"
}
```

<h3 id="close-patient-session-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PatientSessionClosedPayload](#schemapatientsessionclosedpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="close-patient-session-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="close-patient-session-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## post_patient_monitor_configuration_emulator_monitor_UpdatePatientMonitorConfig_post

<a id="opIdpost_patient_monitor_configuration_emulator_monitor_UpdatePatientMonitorConfig_post"></a>

`POST /emulator/monitor/UpdatePatientMonitorConfig`

*Post Patient Monitor Configuration*

> Body parameter

```json
{
  "device_primary_identifier": "string",
  "audio_enabled": true,
  "audio_pause_enabled": false
}
```

<h3 id="post_patient_monitor_configuration_emulator_monitor_updatepatientmonitorconfig_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdatePatientMonitorConfigPayload](#schemaupdatepatientmonitorconfigpayload)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="post_patient_monitor_configuration_emulator_monitor_updatepatientmonitorconfig_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="post_patient_monitor_configuration_emulator_monitor_updatepatientmonitorconfig_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="--admission">Admission</h1>

## reject-patient-admission

<a id="opIdreject-patient-admission"></a>

`POST /emulator/RejectAdmission`

*Reject Patient Admission*

> Body parameter

```json
{
  "patient_monitor_primary_identifier": "string",
  "patient_primary_identifier": "string"
}
```

<h3 id="reject-patient-admission-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RejectPatientAdmissionSchema](#schemarejectpatientadmissionschema)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="reject-patient-admission-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="reject-patient-admission-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="--mllp">MLLP</h1>

## get_latest_mllp_messages_emulator_mllp_get

<a id="opIdget_latest_mllp_messages_emulator_mllp_get"></a>

`GET /emulator/mllp`

*Get Latest Mllp Messages*

<h3 id="get_latest_mllp_messages_emulator_mllp_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|none|

> Example responses

> 200 Response

```json
[
  {
    "content": "string",
    "timestamp": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="get_latest_mllp_messages_emulator_mllp_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_latest_mllp_messages_emulator_mllp_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Latest Mllp Messages Emulator Mllp Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Get Latest Mllp Messages Emulator Mllp Get|[[MLLPMessage](#schemamllpmessage)]|false|none|none|
|» MLLPMessage|[MLLPMessage](#schemamllpmessage)|false|none|none|
|»» content|string|true|none|none|
|»» timestamp|string(date-time)|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AlarmCodes">AlarmCodes</h2>
<!-- backwards compatibility -->
<a id="schemaalarmcodes"></a>
<a id="schema_AlarmCodes"></a>
<a id="tocSalarmcodes"></a>
<a id="tocsalarmcodes"></a>

```json
"258098"

```

AlarmCodes

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|AlarmCodes|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|AlarmCodes|258098|
|AlarmCodes|258118|
|AlarmCodes|258106|
|AlarmCodes|258102|
|AlarmCodes|258110|
|AlarmCodes|258146|
|AlarmCodes|258142|
|AlarmCodes|258150|
|AlarmCodes|258134|
|AlarmCodes|258122|
|AlarmCodes|258138|
|AlarmCodes|258126|
|AlarmCodes|258130|
|AlarmCodes|258114|
|AlarmCodes|258054|
|AlarmCodes|258053|
|AlarmCodes|258050|
|AlarmCodes|258049|
|AlarmCodes|258058|
|AlarmCodes|258057|
|AlarmCodes|258062|
|AlarmCodes|258061|
|AlarmCodes|258066|
|AlarmCodes|258065|
|AlarmCodes|258070|
|AlarmCodes|258069|
|AlarmCodes|258074|
|AlarmCodes|258073|
|AlarmCodes|258078|
|AlarmCodes|258077|
|AlarmCodes|258082|
|AlarmCodes|258081|
|AlarmCodes|258086|
|AlarmCodes|258085|
|AlarmCodes|258162|
|AlarmCodes|258161|
|AlarmCodes|258166|
|AlarmCodes|258165|
|AlarmCodes|258154|
|AlarmCodes|258153|
|AlarmCodes|258158|
|AlarmCodes|258157|
|AlarmCodes|258178|
|AlarmCodes|258177|
|AlarmCodes|258182|
|AlarmCodes|258181|
|AlarmCodes|258170|
|AlarmCodes|258169|
|AlarmCodes|258174|
|AlarmCodes|258173|

<h2 id="tocS_AlarmPayload">AlarmPayload</h2>
<!-- backwards compatibility -->
<a id="schemaalarmpayload"></a>
<a id="schema_AlarmPayload"></a>
<a id="tocSalarmpayload"></a>
<a id="tocsalarmpayload"></a>

```json
{
  "patient_primary_identifier": "string",
  "code": "258098",
  "priority": "HI",
  "description": "string",
  "device_code": "ADAM",
  "device_primary_identifier": "string",
  "active": true,
  "determination_time": 0,
  "vital_range": {
    "code": "0001",
    "upper_limit": 0,
    "lower_limit": 0,
    "alert_condition_enabled": true
  },
  "latching": false
}

```

AlarmPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patient_primary_identifier|string|true|none|none|
|code|[AlarmCodes](#schemaalarmcodes)|true|none|An enumeration.|
|priority|[AlarmPriorities](#schemaalarmpriorities)|true|none|An enumeration.|
|description|string|true|none|none|
|device_code|[DeviceTypes](#schemadevicetypes)|true|none|An enumeration.|
|device_primary_identifier|string|true|none|none|
|active|boolean|true|none|none|
|determination_time|number|false|none|none|
|vital_range|[AlarmRange](#schemaalarmrange)|false|none|none|
|latching|boolean|false|none|none|

<h2 id="tocS_AlarmPriorities">AlarmPriorities</h2>
<!-- backwards compatibility -->
<a id="schemaalarmpriorities"></a>
<a id="schema_AlarmPriorities"></a>
<a id="tocSalarmpriorities"></a>
<a id="tocsalarmpriorities"></a>

```json
"HI"

```

AlarmPriorities

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|AlarmPriorities|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|AlarmPriorities|HI|
|AlarmPriorities|ME|
|AlarmPriorities|LO|

<h2 id="tocS_AlarmRange">AlarmRange</h2>
<!-- backwards compatibility -->
<a id="schemaalarmrange"></a>
<a id="schema_AlarmRange"></a>
<a id="tocSalarmrange"></a>
<a id="tocsalarmrange"></a>

```json
{
  "code": "0001",
  "upper_limit": 0,
  "lower_limit": 0,
  "alert_condition_enabled": true
}

```

AlarmRange

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|upper_limit|number|false|none|none|
|lower_limit|number|false|none|none|
|alert_condition_enabled|boolean|false|none|none|

<h2 id="tocS_ConfigSchema">ConfigSchema</h2>
<!-- backwards compatibility -->
<a id="schemaconfigschema"></a>
<a id="schema_ConfigSchema"></a>
<a id="tocSconfigschema"></a>
<a id="tocsconfigschema"></a>

```json
{
  "audio_pause_enabled": false,
  "audio_enabled": true
}

```

ConfigSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_pause_enabled|boolean|false|none|none|
|audio_enabled|boolean|false|none|none|

<h2 id="tocS_ConnectedSensorPayload">ConnectedSensorPayload</h2>
<!-- backwards compatibility -->
<a id="schemaconnectedsensorpayload"></a>
<a id="schema_ConnectedSensorPayload"></a>
<a id="tocSconnectedsensorpayload"></a>
<a id="tocsconnectedsensorpayload"></a>

```json
{
  "primary_identifier": "string",
  "name": "string",
  "device_code": "ADAM"
}

```

ConnectedSensorPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
|device_code|[DeviceTypes](#schemadevicetypes)|true|none|An enumeration.|

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

<h2 id="tocS_DeviceEmulationModes">DeviceEmulationModes</h2>
<!-- backwards compatibility -->
<a id="schemadeviceemulationmodes"></a>
<a id="schema_DeviceEmulationModes"></a>
<a id="tocSdeviceemulationmodes"></a>
<a id="tocsdeviceemulationmodes"></a>

```json
"low"

```

DeviceEmulationModes

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DeviceEmulationModes|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|DeviceEmulationModes|low|
|DeviceEmulationModes|normal|
|DeviceEmulationModes|high|
|DeviceEmulationModes|error|
|DeviceEmulationModes|fixed|

<h2 id="tocS_DeviceEmulationNames">DeviceEmulationNames</h2>
<!-- backwards compatibility -->
<a id="schemadeviceemulationnames"></a>
<a id="schema_DeviceEmulationNames"></a>
<a id="tocSdeviceemulationnames"></a>
<a id="tocsdeviceemulationnames"></a>

```json
"MONITOR_CONNECTION_STATUS"

```

DeviceEmulationNames

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DeviceEmulationNames|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|DeviceEmulationNames|MONITOR_CONNECTION_STATUS|
|DeviceEmulationNames|BLOOD_PRESSURE|
|DeviceEmulationNames|HEART_RATE_EMULATOR|
|DeviceEmulationNames|ECG_EMULATOR|
|DeviceEmulationNames|CARDIAC_EMULATOR|
|DeviceEmulationNames|BLOOD_OXYGEN_EMULATOR|
|DeviceEmulationNames|PULSE_EMULATOR|
|DeviceEmulationNames|PULSE_RATE_EMULATOR|
|DeviceEmulationNames|PERFUSION_INDEX_EMULATOR|
|DeviceEmulationNames|BODY_TEMPERATURE_EMULATOR|
|DeviceEmulationNames|CHEST_TEMPERATURE_EMULATOR|
|DeviceEmulationNames|LIMB_TEMPERATURE_EMULATOR|
|DeviceEmulationNames|FALLS_EMULATOR|
|DeviceEmulationNames|POSITION_EMULATOR|
|DeviceEmulationNames|BODY_ANGLE_EMULATOR|
|DeviceEmulationNames|RESPIRATORY_RATE_EMULATOR|
|DeviceEmulationNames|MEAN_ARTERIAL_PRESSURE_EMULATOR|
|DeviceEmulationNames|PLETH_EMULATOR|
|DeviceEmulationNames|SENSOR_SIGNAL_EMULATOR|
|DeviceEmulationNames|SENSOR_BATTERY_EMULATOR|
|DeviceEmulationNames|SENSOR_BATTERY_CHARGING_STATE_EMULATOR|
|DeviceEmulationNames|SENSOR_MODULE_STATE_EMULATOR|
|DeviceEmulationNames|SENSOR_LEAD_STATE_EMULATOR|
|DeviceEmulationNames|SENSOR_CONTACT_STATE_EMULATOR|
|DeviceEmulationNames|SENSOR_CONNECTION_STATE_EMULATOR|

<h2 id="tocS_DeviceMonitorSchema">DeviceMonitorSchema</h2>
<!-- backwards compatibility -->
<a id="schemadevicemonitorschema"></a>
<a id="schema_DeviceMonitorSchema"></a>
<a id="tocSdevicemonitorschema"></a>
<a id="tocsdevicemonitorschema"></a>

```json
{
  "primary_identifier": "string",
  "name": "string",
  "patient": {
    "primary_identifier": "string",
    "given_name": "string",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  },
  "connected_sensors": [
    {
      "primary_identifier": "string",
      "name": "string",
      "device_code": "ADAM"
    }
  ],
  "config": {
    "audio_pause_enabled": false,
    "audio_enabled": true
  }
}

```

DeviceMonitorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
|patient|[PatientSchema](#schemapatientschema)|false|none|none|
|connected_sensors|[[ConnectedSensorPayload](#schemaconnectedsensorpayload)]|false|none|none|
|config|[ConfigSchema](#schemaconfigschema)|false|none|none|

<h2 id="tocS_DeviceRange">DeviceRange</h2>
<!-- backwards compatibility -->
<a id="schemadevicerange"></a>
<a id="schema_DeviceRange"></a>
<a id="tocSdevicerange"></a>
<a id="tocsdevicerange"></a>

```json
{
  "code": "258418",
  "lower_limit": 0,
  "upper_limit": 0,
  "alert_condition_enabled": true
}

```

DeviceRange

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|[RangeCodes](#schemarangecodes)|true|none|An enumeration.|
|lower_limit|number|false|none|none|
|upper_limit|number|false|none|none|
|alert_condition_enabled|boolean|false|none|none|

<h2 id="tocS_DeviceRangesPayload">DeviceRangesPayload</h2>
<!-- backwards compatibility -->
<a id="schemadevicerangespayload"></a>
<a id="schema_DeviceRangesPayload"></a>
<a id="tocSdevicerangespayload"></a>
<a id="tocsdevicerangespayload"></a>

```json
{
  "primary_identifier": "string",
  "ranges": [
    {
      "code": "258418",
      "lower_limit": 0,
      "upper_limit": 0,
      "alert_condition_enabled": true
    }
  ]
}

```

DeviceRangesPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|ranges|[[DeviceRange](#schemadevicerange)]|true|none|none|

<h2 id="tocS_DeviceSensorSchema">DeviceSensorSchema</h2>
<!-- backwards compatibility -->
<a id="schemadevicesensorschema"></a>
<a id="schema_DeviceSensorSchema"></a>
<a id="tocSdevicesensorschema"></a>
<a id="tocsdevicesensorschema"></a>

```json
{
  "primary_identifier": "string",
  "patient_monitor_primary_identifier": "string",
  "name": "string",
  "device_code": "ADAM"
}

```

DeviceSensorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|patient_monitor_primary_identifier|string|true|none|none|
|name|string|true|none|none|
|device_code|[DeviceTypes](#schemadevicetypes)|true|none|An enumeration.|

<h2 id="tocS_DeviceTypes">DeviceTypes</h2>
<!-- backwards compatibility -->
<a id="schemadevicetypes"></a>
<a id="schema_DeviceTypes"></a>
<a id="tocSdevicetypes"></a>
<a id="tocsdevicetypes"></a>

```json
"ADAM"

```

DeviceTypes

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DeviceTypes|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|DeviceTypes|ADAM|
|DeviceTypes|ANNE Chest|
|DeviceTypes|ANNE Limb|
|DeviceTypes|Nonin 3150|
|DeviceTypes|Viatom BP monitor|
|DeviceTypes|DMT Thermometer|
|DeviceTypes|Patient Monitor|

<h2 id="tocS_DisconnectMonitorSchema">DisconnectMonitorSchema</h2>
<!-- backwards compatibility -->
<a id="schemadisconnectmonitorschema"></a>
<a id="schema_DisconnectMonitorSchema"></a>
<a id="tocSdisconnectmonitorschema"></a>
<a id="tocsdisconnectmonitorschema"></a>

```json
{
  "primary_identifier": "string"
}

```

DisconnectMonitorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|

<h2 id="tocS_DisconnectSensorSchema">DisconnectSensorSchema</h2>
<!-- backwards compatibility -->
<a id="schemadisconnectsensorschema"></a>
<a id="schema_DisconnectSensorSchema"></a>
<a id="tocSdisconnectsensorschema"></a>
<a id="tocsdisconnectsensorschema"></a>

```json
{
  "primary_identifier": "string"
}

```

DisconnectSensorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|

<h2 id="tocS_EmulatorDetailSchema">EmulatorDetailSchema</h2>
<!-- backwards compatibility -->
<a id="schemaemulatordetailschema"></a>
<a id="schema_EmulatorDetailSchema"></a>
<a id="tocSemulatordetailschema"></a>
<a id="tocsemulatordetailschema"></a>

```json
{
  "name": "string",
  "current_mode": "string",
  "emulation_modes": [
    "string"
  ]
}

```

EmulatorDetailSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|current_mode|string|true|none|none|
|emulation_modes|[string]|true|none|none|

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
|GenderEnum|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|GenderEnum|male|
|GenderEnum|female|
|GenderEnum|other|
|GenderEnum|unknown|

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
|status|[HealthCheckStatus](#schemahealthcheckstatus)|true|none|An enumeration.|

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
|HealthCheckStatus|any|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|HealthCheckStatus|Healthy|
|HealthCheckStatus|Error|

<h2 id="tocS_MLLPMessage">MLLPMessage</h2>
<!-- backwards compatibility -->
<a id="schemamllpmessage"></a>
<a id="schema_MLLPMessage"></a>
<a id="tocSmllpmessage"></a>
<a id="tocsmllpmessage"></a>

```json
{
  "content": "string",
  "timestamp": "2019-08-24T14:15:22Z"
}

```

MLLPMessage

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|true|none|none|
|timestamp|string(date-time)|false|none|none|

<h2 id="tocS_PatientMonitorDetailSchema">PatientMonitorDetailSchema</h2>
<!-- backwards compatibility -->
<a id="schemapatientmonitordetailschema"></a>
<a id="schema_PatientMonitorDetailSchema"></a>
<a id="tocSpatientmonitordetailschema"></a>
<a id="tocspatientmonitordetailschema"></a>

```json
{
  "primary_identifier": "string",
  "name": "string",
  "sensors": [
    {
      "primary_identifier": "string",
      "type": "string",
      "name": "string",
      "emulators": [
        {
          "name": "string",
          "current_mode": "string",
          "emulation_modes": [
            "string"
          ]
        }
      ]
    }
  ],
  "emulators": [
    {
      "name": "string",
      "current_mode": "string",
      "emulation_modes": [
        "string"
      ]
    }
  ],
  "patient": {
    "primary_identifier": "string",
    "given_name": "string",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  }
}

```

PatientMonitorDetailSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|name|string|true|none|none|
|sensors|[[SensorDetailSchema](#schemasensordetailschema)]|true|none|none|
|emulators|[[EmulatorDetailSchema](#schemaemulatordetailschema)]|true|none|none|
|patient|[PatientSchema](#schemapatientschema)|false|none|none|

<h2 id="tocS_PatientMonitorResourcesSchema">PatientMonitorResourcesSchema</h2>
<!-- backwards compatibility -->
<a id="schemapatientmonitorresourcesschema"></a>
<a id="schema_PatientMonitorResourcesSchema"></a>
<a id="tocSpatientmonitorresourcesschema"></a>
<a id="tocspatientmonitorresourcesschema"></a>

```json
{
  "resources": [
    {
      "primary_identifier": "string",
      "name": "string",
      "sensors": [
        {
          "primary_identifier": "string",
          "type": "string",
          "name": "string",
          "emulators": [
            {
              "name": "string",
              "current_mode": "string",
              "emulation_modes": [
                "string"
              ]
            }
          ]
        }
      ],
      "emulators": [
        {
          "name": "string",
          "current_mode": "string",
          "emulation_modes": [
            "string"
          ]
        }
      ],
      "patient": {
        "primary_identifier": "string",
        "given_name": "string",
        "family_name": "string",
        "gender": "male",
        "birth_date": "2019-08-24"
      }
    }
  ]
}

```

PatientMonitorResourcesSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resources|[[PatientMonitorDetailSchema](#schemapatientmonitordetailschema)]|true|none|none|

<h2 id="tocS_PatientSchema">PatientSchema</h2>
<!-- backwards compatibility -->
<a id="schemapatientschema"></a>
<a id="schema_PatientSchema"></a>
<a id="tocSpatientschema"></a>
<a id="tocspatientschema"></a>

```json
{
  "primary_identifier": "string",
  "given_name": "string",
  "family_name": "string",
  "gender": "male",
  "birth_date": "2019-08-24"
}

```

PatientSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|given_name|string|true|none|none|
|family_name|string|true|none|none|
|gender|[GenderEnum](#schemagenderenum)|true|none|An enumeration.|
|birth_date|string(date)|false|none|none|

<h2 id="tocS_PatientSessionClosedPayload">PatientSessionClosedPayload</h2>
<!-- backwards compatibility -->
<a id="schemapatientsessionclosedpayload"></a>
<a id="schema_PatientSessionClosedPayload"></a>
<a id="tocSpatientsessionclosedpayload"></a>
<a id="tocspatientsessionclosedpayload"></a>

```json
{
  "patient_monitor_primary_identifier": "string"
}

```

PatientSessionClosedPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patient_monitor_primary_identifier|string|true|none|none|

<h2 id="tocS_PatientSessionOpenedPayload">PatientSessionOpenedPayload</h2>
<!-- backwards compatibility -->
<a id="schemapatientsessionopenedpayload"></a>
<a id="schema_PatientSessionOpenedPayload"></a>
<a id="tocSpatientsessionopenedpayload"></a>
<a id="tocspatientsessionopenedpayload"></a>

```json
{
  "patient_monitor_primary_identifier": "string",
  "patient": {
    "primary_identifier": "string",
    "given_name": "string",
    "family_name": "string",
    "gender": "male",
    "birth_date": "2019-08-24"
  }
}

```

PatientSessionOpenedPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patient_monitor_primary_identifier|string|true|none|none|
|patient|[PatientSchema](#schemapatientschema)|true|none|none|

<h2 id="tocS_RangeCodes">RangeCodes</h2>
<!-- backwards compatibility -->
<a id="schemarangecodes"></a>
<a id="schema_RangeCodes"></a>
<a id="tocSrangecodes"></a>
<a id="tocsrangecodes"></a>

```json
"258418"

```

RangeCodes

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|RangeCodes|string|false|none|An enumeration.|

#### Enumerated Values

|Property|Value|
|---|---|
|RangeCodes|258418|
|RangeCodes|258419|
|RangeCodes|258424|
|RangeCodes|258425|
|RangeCodes|258420|
|RangeCodes|258427|
|RangeCodes|8574701|
|RangeCodes|258426|
|RangeCodes|258422|
|RangeCodes|258421|

<h2 id="tocS_RejectPatientAdmissionSchema">RejectPatientAdmissionSchema</h2>
<!-- backwards compatibility -->
<a id="schemarejectpatientadmissionschema"></a>
<a id="schema_RejectPatientAdmissionSchema"></a>
<a id="tocSrejectpatientadmissionschema"></a>
<a id="tocsrejectpatientadmissionschema"></a>

```json
{
  "patient_monitor_primary_identifier": "string",
  "patient_primary_identifier": "string"
}

```

RejectPatientAdmissionSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patient_monitor_primary_identifier|string|true|none|none|
|patient_primary_identifier|string|true|none|none|

<h2 id="tocS_SensorDetailSchema">SensorDetailSchema</h2>
<!-- backwards compatibility -->
<a id="schemasensordetailschema"></a>
<a id="schema_SensorDetailSchema"></a>
<a id="tocSsensordetailschema"></a>
<a id="tocssensordetailschema"></a>

```json
{
  "primary_identifier": "string",
  "type": "string",
  "name": "string",
  "emulators": [
    {
      "name": "string",
      "current_mode": "string",
      "emulation_modes": [
        "string"
      ]
    }
  ]
}

```

SensorDetailSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|type|string|true|none|none|
|name|string|true|none|none|
|emulators|[[EmulatorDetailSchema](#schemaemulatordetailschema)]|true|none|none|

<h2 id="tocS_TechnicalAlarmPayload">TechnicalAlarmPayload</h2>
<!-- backwards compatibility -->
<a id="schematechnicalalarmpayload"></a>
<a id="schema_TechnicalAlarmPayload"></a>
<a id="tocStechnicalalarmpayload"></a>
<a id="tocstechnicalalarmpayload"></a>

```json
{
  "patient_primary_identifier": "string",
  "device_primary_identifier": "string",
  "code": "258098",
  "priority": "HI",
  "device_code": "ADAM",
  "active": true,
  "determination_time": 0,
  "vital_range": {
    "code": "0001",
    "upper_limit": 0,
    "lower_limit": 0,
    "alert_condition_enabled": true
  }
}

```

TechnicalAlarmPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|patient_primary_identifier|string|true|none|none|
|device_primary_identifier|string|true|none|none|
|code|[AlarmCodes](#schemaalarmcodes)|true|none|An enumeration.|
|priority|[AlarmPriorities](#schemaalarmpriorities)|true|none|An enumeration.|
|device_code|[DeviceTypes](#schemadevicetypes)|true|none|An enumeration.|
|active|boolean|true|none|none|
|determination_time|number|false|none|none|
|vital_range|[AlarmRange](#schemaalarmrange)|false|none|none|

<h2 id="tocS_UpdatePatientMonitorConfigPayload">UpdatePatientMonitorConfigPayload</h2>
<!-- backwards compatibility -->
<a id="schemaupdatepatientmonitorconfigpayload"></a>
<a id="schema_UpdatePatientMonitorConfigPayload"></a>
<a id="tocSupdatepatientmonitorconfigpayload"></a>
<a id="tocsupdatepatientmonitorconfigpayload"></a>

```json
{
  "device_primary_identifier": "string",
  "audio_enabled": true,
  "audio_pause_enabled": false
}

```

UpdatePatientMonitorConfigPayload

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|device_primary_identifier|string|true|none|none|
|audio_enabled|boolean|false|none|none|
|audio_pause_enabled|boolean|false|none|none|

<h2 id="tocS_UpdateSensorModeWebSchema">UpdateSensorModeWebSchema</h2>
<!-- backwards compatibility -->
<a id="schemaupdatesensormodewebschema"></a>
<a id="schema_UpdateSensorModeWebSchema"></a>
<a id="tocSupdatesensormodewebschema"></a>
<a id="tocsupdatesensormodewebschema"></a>

```json
{
  "primary_identifier": "string",
  "emulator_name": "MONITOR_CONNECTION_STATUS",
  "mode": "low"
}

```

UpdateSensorModeWebSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|primary_identifier|string|true|none|none|
|emulator_name|[DeviceEmulationNames](#schemadeviceemulationnames)|true|none|An enumeration.|
|mode|[DeviceEmulationModes](#schemadeviceemulationmodes)|true|none|An enumeration.|

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