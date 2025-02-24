### Database Schema Design

| Field | Type |
|------|-------|
|entity_id   | String ID|
|timestamp| timestamp |
|data| jsonb |
|created_at|timestamp|
|updated_at|timestamp|
|emitted_by|String|
|performed_by| String|
|event_name|String |
|event_type|String|
|message_id| UUID|
|event_data| jsonb |


### Audit Traill event data samples
Below is the list of event which is consumed by Audit Trail micro service. 

1. **Device Created event**
```json
{
  "current_state": {
    "id": "4914fe23-5aec-4b36-ae98-6cb488679468",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": null,
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "PM24ZTGSJBM",
    "audio_pause_enabled": false
  },
  "previous_state": {}
}
```


2. **Device information updated**

```json
{
  "current_state": {
    "id": "1b121ef0-44fd-4618-8fab-de50585a521a",
    "code": "258419",
    "device_id": "568ef654-b574-4b73-945f-d9ba24d77504",
    "lower_limit": 5.0,
    "upper_limit": 30.0
  },
  "previous_state": {
    "id": "1b121ef0-44fd-4618-8fab-de50585a521a",
    "code": "258419",
    "device_id": "568ef654-b574-4b73-945f-d9ba24d77504",
    "lower_limit": 5.0,
    "upper_limit": 30.0
  }
}
```

3. **Bed Created**
```json
{
  "current_state": {
    "id": "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb",
    "name": "1"
  },
  "previous_state": {}
}
```

4.  **Bed Group Created**
```json
{
  "current_state": {
    "id": "6ade01c9-9813-4e14-b8b9-17ba2a5357bb",
    "beds": [],
    "name": "Group 1",
    "description": null
  },
  "previous_state": {}
}
```

5.  **Bed Added to Group**
```json
{
  "current_state": {
    "id": "6ade01c9-9813-4e14-b8b9-17ba2a5357bb",
    "beds": [
      "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb"
    ],
    "name": "Group 1",
    "description": null
  },
  "previous_state": {
    "id": "6ade01c9-9813-4e14-b8b9-17ba2a5357bb",
    "beds": [],
    "name": "Group 1",
    "description": null
  }
}
```


6.  **Alert deactivated**
```json
{
  "current_state": {
    "code": "258102",
    "active": false,
    "patient_id": "4bc49402-d8b6-4d65-92fa-4dca8518281b",
    "value_text": "ME",
    "device_code": "Patient Monitor",
    "determination_time": "2024-12-06T15:13:04.613000",
    "trigger_lower_limit": 20.0,
    "trigger_upper_limit": null,
    "device_primary_identifier": "PMQBNMHHI6T",
    "patient_primary_identifier": "1733443428458HI6T"
  },
  "previous_state": {}
}
```


7. **Vital Range Created**
```json 
{
  "current_state": {
    "id": "b19d9c20-1259-43e5-bd55-1e0600d6685c",
    "code": "196988",
    "device_id": "93f91f56-6601-47a6-b1af-e05c688c7a48",
    "lower_limit": -93.0,
    "upper_limit": null
  },
  "previous_state": {}
}
```
8. **Alert activated**
```json
{
  "current_state": {
    "code": "258102",
    "active": true,
    "patient_id": "74c488a3-8986-4c07-b9bb-4faa5cba659e",
    "value_text": "ME",
    "device_code": "Patient Monitor",
    "determination_time": "2024-12-06T22:47:01.393000",
    "trigger_lower_limit": 20.0,
    "trigger_upper_limit": null,
    "device_primary_identifier": "PMVQMNMADM9",
    "patient_primary_identifier": "Q8AhbGbS8SUX-UjA"
  },
  "previous_state": {}
}
```

9. **Encounter cancelled**
```json
{
  "current_state": {
    "id": "6e385b84-280c-4071-9f9a-5915997b0017",
    "device": {
      "id": "568ef654-b574-4b73-945f-d9ba24d77504",
      "name": "Patient Monitor",
      "gateway_id": null,
      "location_id": "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb",
      "model_number": "Patient Monitor",
      "audio_enabled": true,
      "primary_identifier": "PM5TW35XK0N",
      "audio_pause_enabled": false
    },
    "status": "cancelled",
    "patient": {
      "id": "24589c45-099c-4925-9e46-6985e8d1f116",
      "active": true,
      "gender": "male",
      "birth_date": "1993-12-07",
      "given_name": "Harshit",
      "family_name": "Shah",
      "primary_identifier": "58ha9ILWofHQxK4t"
    },
    "end_time": "2024-12-05T22:47:04.319400",
    "created_at": "2024-12-05T22:44:06.575528",
    "start_time": null
  },
  "previous_state": {
    "id": "6e385b84-280c-4071-9f9a-5915997b0017",
    "device": {
      "id": "568ef654-b574-4b73-945f-d9ba24d77504",
      "name": "Patient Monitor",
      "gateway_id": null,
      "location_id": "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb",
      "model_number": "Patient Monitor",
      "audio_enabled": true,
      "primary_identifier": "PM5TW35XK0N",
      "audio_pause_enabled": false
    },
    "status": "planned",
    "patient": {
      "id": "24589c45-099c-4925-9e46-6985e8d1f116",
      "active": true,
      "gender": "male",
      "birth_date": "1993-12-07",
      "given_name": "Harshit",
      "family_name": "Shah",
      "primary_identifier": "58ha9ILWofHQxK4t"
    },
    "end_time": null,
    "created_at": "2024-12-05T22:44:06.575528",
    "start_time": null
  }
}
```

10. **Assign location to device**
```json
{
  "current_state": {
    "id": "568ef654-b574-4b73-945f-d9ba24d77504",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": null,
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "PM5TW35XK0N",
    "audio_pause_enabled": false
  },
  "previous_state": {
    "id": "568ef654-b574-4b73-945f-d9ba24d77504",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": null,
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "PM5TW35XK0N",
    "audio_pause_enabled": false
  }
}
```

11. **Device Alert Updated**
```json
{
  "current_state": {
    "id": "116d72d2-4b3f-4e9d-b2c1-188f0a9c1c65",
    "code": "258102",
    "priority": "ME",
    "device_id": "82d8756f-41d0-484d-a2ae-e69756d19ceb"
  },
  "previous_state": {
    "id": "116d72d2-4b3f-4e9d-b2c1-188f0a9c1c65",
    "code": "258102",
    "priority": "ME",
    "device_id": "82d8756f-41d0-484d-a2ae-e69756d19ceb"
  }
}
```

12. **Encounter completed**
```json
{
  "current_state": {
    "id": "e757895a-54b4-44a1-87fa-4f6bce54b9e0",
    "device": {
      "id": "93f91f56-6601-47a6-b1af-e05c688c7a48",
      "name": "Patient Monitor",
      "gateway_id": null,
      "location_id": null,
      "model_number": "Patient Monitor",
      "audio_enabled": true,
      "primary_identifier": "PMQBNMHHI6T",
      "audio_pause_enabled": false
    },
    "status": "completed",
    "patient": {
      "id": "2e467d80-2f2c-4518-8461-f75babf99f93",
      "active": true,
      "gender": "male",
      "birth_date": "1969-12-01",
      "given_name": "Harry",
      "family_name": "Porter",
      "primary_identifier": "gwavba0Ey3I0kf5x"
    },
    "end_time": "2024-12-05T23:48:46.866416",
    "created_at": "2024-12-05T23:47:25.383939",
    "start_time": "2024-12-05T23:47:25.383936"
  },
  "previous_state": {
    "id": "e757895a-54b4-44a1-87fa-4f6bce54b9e0",
    "device": {
      "id": "93f91f56-6601-47a6-b1af-e05c688c7a48",
      "name": "Patient Monitor",
      "gateway_id": null,
      "location_id": null,
      "model_number": "Patient Monitor",
      "audio_enabled": true,
      "primary_identifier": "PMQBNMHHI6T",
      "audio_pause_enabled": false
    },
    "status": "in-progress",
    "patient": {
      "id": "2e467d80-2f2c-4518-8461-f75babf99f93",
      "active": true,
      "gender": "male",
      "birth_date": "1969-12-01",
      "given_name": "Harry",
      "family_name": "Porter",
      "primary_identifier": "gwavba0Ey3I0kf5x"
    },
    "end_time": null,
    "created_at": "2024-12-05T23:47:25.383939",
    "start_time": "2024-12-05T23:47:25.383936"
  }
}
```
13. **Observation Created**
```json
{
  "current_state": {
    "id": "04d88d5c-d308-47b5-a457-0cdf364d88f9",
    "code": "258050",
    "category": "vital-signs",
    "is_alert": true,
    "subject_id": "ab7b4126-ccc8-40cd-88a1-e2ec1f34cd22",
    "value_text": "ME",
    "effective_dt": "2025-01-20T19:53:23.771000",
    "value_number": null
  },
  "previous_state": {}
}
```

14. **Device deleted**
```json
{
  "current_state": {
    "id": "4790acde-1e8a-4c8a-8f9b-9428b67b3406",
    "name": "ANNE Limb",
    "gateway_id": "93f91f56-6601-47a6-b1af-e05c688c7a48",
    "location_id": null,
    "model_number": "ANNE Limb",
    "audio_enabled": true,
    "primary_identifier": "LJ10B5",
    "audio_pause_enabled": false
  },
  "previous_state": {
    "id": "4790acde-1e8a-4c8a-8f9b-9428b67b3406",
    "name": "ANNE Limb",
    "gateway_id": "93f91f56-6601-47a6-b1af-e05c688c7a48",
    "location_id": null,
    "model_number": "ANNE Limb",
    "audio_enabled": true,
    "primary_identifier": "LJ10B5",
    "audio_pause_enabled": false
  }
}
```

15. **Patient personal information updated**
```json
{
  "current_state": {
    "id": "17438c6e-7525-4575-a770-312da95efb99",
    "active": true,
    "gender": "unknown",
    "birth_date": "2005-12-06",
    "given_name": "Test",
    "family_name": "hgdhfgf",
    "primary_identifier": "J1AZvKofzLbFD2pB"
  },
  "previous_state": {
    "id": "17438c6e-7525-4575-a770-312da95efb99",
    "active": true,
    "gender": "female",
    "birth_date": "2005-12-06",
    "given_name": "Test",
    "family_name": "hgdhfgf",
    "primary_identifier": "J1AZvKofzLbFD2pB"
  }
}
```

16. **Unassign location**
```json
{
  "current_state": {
    "id": "568ef654-b574-4b73-945f-d9ba24d77504",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": null,
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "PM5TW35XK0N",
    "audio_pause_enabled": false
  },
  "previous_state": {
    "id": "568ef654-b574-4b73-945f-d9ba24d77504",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb",
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "PM5TW35XK0N",
    "audio_pause_enabled": false
  }
}
```

17. **Device Alert Created**
```json
{
  "current_state": {
    "id": "a474c622-4b0c-4485-9c45-b369b2292f45",
    "code": "258110",
    "priority": "LO",
    "device_id": "4ac5dc43-3a68-4df8-adc2-baeae3dd66f4"
  },
  "previous_state": {}
}
```

18. **Patient admitted**
```json
{
  "current_state": {
    "id": "6855e614-7dd0-4455-adf7-fa1d0d04f0ce",
    "device": {
      "id": "4914fe23-5aec-4b36-ae98-6cb488679468",
      "name": "Patient Monitor",
      "gateway_id": null,
      "location_id": null,
      "model_number": "Patient Monitor",
      "audio_enabled": true,
      "primary_identifier": "PM24ZTGSJBM",
      "audio_pause_enabled": false
    },
    "status": "in-progress",
    "patient": {
      "id": "6cb2bcb9-58b1-40f7-9cc5-f4ad10a4d990",
      "active": true,
      "gender": "unknown",
      "birth_date": null,
      "given_name": "-",
      "family_name": "-",
      "primary_identifier": "1733442063437SJBM"
    },
    "end_time": null,
    "created_at": "2024-12-05T23:41:05.723932",
    "start_time": "2024-12-05T23:41:05.723928"
  },
  "previous_state": {}
}
```

19. **Patient admission planned**
```json
{
  "current_state": {
    "id": "cc33b861-d8f7-461f-804d-76c8a00f31c8",
    "device": {
      "id": "e9a76826-9a56-49e9-9e0b-1afd89f8f652",
      "name": "Patient Monitor",
      "gateway_id": null,
      "location_id": "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb",
      "model_number": "Patient Monitor",
      "audio_enabled": true,
      "primary_identifier": "PMQOJY6P02Q",
      "audio_pause_enabled": false
    },
    "status": "planned",
    "patient": {
      "id": "17438c6e-7525-4575-a770-312da95efb99",
      "active": true,
      "gender": "female",
      "birth_date": "2005-12-06",
      "given_name": "Test",
      "family_name": "hgdhfgf",
      "primary_identifier": "J1AZvKofzLbFD2pB"
    },
    "end_time": null,
    "created_at": "2024-12-05T23:14:02.935506",
    "start_time": null
  },
  "previous_state": {}
}
```

20. **Bed removed from group**
```json 
{
  "current_state": {
    "id": "6ade01c9-9813-4e14-b8b9-17ba2a5357bb",
    "beds": [
      "70e8093e-c259-4aa9-9eca-78e7a8a87183"
    ],
    "name": "Group 1",
    "description": null
  },
  "previous_state": {
    "id": "6ade01c9-9813-4e14-b8b9-17ba2a5357bb",
    "beds": [
      "ffe73422-8dcf-4cd0-9d26-5bc1736a25fb",
      "70e8093e-c259-4aa9-9eca-78e7a8a87183"
    ],
    "name": "Group 1",
    "description": null
  }
}
```

21. **Bed deleted**
```json
{
  "current_state": {
    "id": "1e59283c-5e3d-47e8-9a4f-3bc8c65fdf14",
    "name": "4"
  },
  "previous_state": {
    "id": "1e59283c-5e3d-47e8-9a4f-3bc8c65fdf14",
    "name": "4"
  }
}
```

22. **Patient Created**
```json
{
  "current_state": {
    "id": "24589c45-099c-4925-9e46-6985e8d1f116",
    "active": true,
    "gender": "male",
    "birth_date": "1993-12-07",
    "given_name": "Harshit",
    "family_name": "Shah",
    "primary_identifier": "58ha9ILWofHQxK4t"
  },
  "previous_state": {}
}
```

23. **Device Alert Deleted**
```json
{
  "current_state": {
    "id": "2082fa9f-83f0-4e12-b111-07dd9be83483",
    "code": "258110",
    "priority": "LO",
    "device_id": "f3b5828c-8d33-473a-9892-0c2a7134dab2"
  },
  "previous_state": {
    "id": "2082fa9f-83f0-4e12-b111-07dd9be83483",
    "code": "258110",
    "priority": "LO",
    "device_id": "f3b5828c-8d33-473a-9892-0c2a7134dab2"
  }
}
```

24. **Device configuration updated**
```json
{
  "current_state": {
    "id": "62515039-197a-44d1-a453-c26ce594aafa",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": null,
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "R52X30G2JLA",
    "audio_pause_enabled": true
  },
  "previous_state": {
    "id": "62515039-197a-44d1-a453-c26ce594aafa",
    "name": "Patient Monitor",
    "gateway_id": null,
    "location_id": null,
    "model_number": "Patient Monitor",
    "audio_enabled": true,
    "primary_identifier": "R52X30G2JLA",
    "audio_pause_enabled": false
  }
}
```

25. **Obeservation Deleted**
```json
{
  "current_state": {
    "id": "083d9c46-fad6-4d61-89aa-6e41b926f302",
    "code": "258154",
    "category": "vital-signs",
    "is_alert": true,
    "subject_id": "4bc49402-d8b6-4d65-92fa-4dca8518281b",
    "value_text": "ME",
    "effective_dt": "2024-12-06T00:34:29.143000",
    "value_number": null
  },
  "previous_state": {
    "id": "083d9c46-fad6-4d61-89aa-6e41b926f302",
    "code": "258154",
    "category": "vital-signs",
    "is_alert": true,
    "subject_id": "4bc49402-d8b6-4d65-92fa-4dca8518281b",
    "value_text": "ME",
    "effective_dt": "2024-12-06T00:34:29.143000",
    "value_number": null
  }
}
```

26. **Login**
```json
{"current_state": {}, "previous_state": {}}
```

27. **Logout**
```json
{"current_state": {}, "previous_state": {}}
```

28. **User updated**
```json
{"current_state": {}, "previous_state": {}}
```