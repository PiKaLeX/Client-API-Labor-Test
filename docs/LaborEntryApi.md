# swagger_client.LaborEntryApi

All URIs are relative to *http://testerp.kinovaapps.com/entity/MANUFACTURING/18.100.001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**labor_entry_delete_by_id**](LaborEntryApi.md#labor_entry_delete_by_id) | **DELETE** /LaborEntry/{id} | Deletes the record by its session identifier.
[**labor_entry_get_ad_hoc_schema**](LaborEntryApi.md#labor_entry_get_ad_hoc_schema) | **GET** /LaborEntry/$adHocSchema | Retrieves the schema of custom fields of the entity from the system.
[**labor_entry_get_by_id**](LaborEntryApi.md#labor_entry_get_by_id) | **GET** /LaborEntry/{id} | Retrieves a record by the value of the session entity ID from the system.
[**labor_entry_get_list**](LaborEntryApi.md#labor_entry_get_list) | **GET** /LaborEntry | Retrieves records that satisfy the specified conditions from the system.
[**labor_entry_put_entity**](LaborEntryApi.md#labor_entry_put_entity) | **PUT** /LaborEntry | Creates a record or updates an existing record.


# **labor_entry_delete_by_id**
> labor_entry_delete_by_id(id)

Deletes the record by its session identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LaborEntryApi()
id = 'id_example' # str | The session ID of the record.

try:
    # Deletes the record by its session identifier.
    api_instance.labor_entry_delete_by_id(id)
except ApiException as e:
    print("Exception when calling LaborEntryApi->labor_entry_delete_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The session ID of the record. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labor_entry_get_ad_hoc_schema**
> LaborEntry labor_entry_get_ad_hoc_schema()

Retrieves the schema of custom fields of the entity from the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LaborEntryApi()

try:
    # Retrieves the schema of custom fields of the entity from the system.
    api_response = api_instance.labor_entry_get_ad_hoc_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaborEntryApi->labor_entry_get_ad_hoc_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LaborEntry**](LaborEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labor_entry_get_by_id**
> LaborEntry labor_entry_get_by_id(id, select=select, filter=filter, expand=expand, custom=custom)

Retrieves a record by the value of the session entity ID from the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LaborEntryApi()
id = 'id_example' # str | The session ID of the record.
select = 'select_example' # str | The fields of the entity to be returned from the system. (optional)
filter = 'filter_example' # str | The conditions that determine which records should be selected from the system. (optional)
expand = 'expand_example' # str | The linked and detail entities that should be expanded. (optional)
custom = 'custom_example' # str | The fields that are not defined in the contract of the endpoint to be returned from the system. (optional)

try:
    # Retrieves a record by the value of the session entity ID from the system.
    api_response = api_instance.labor_entry_get_by_id(id, select=select, filter=filter, expand=expand, custom=custom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaborEntryApi->labor_entry_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The session ID of the record. | 
 **select** | **str**| The fields of the entity to be returned from the system. | [optional] 
 **filter** | **str**| The conditions that determine which records should be selected from the system. | [optional] 
 **expand** | **str**| The linked and detail entities that should be expanded. | [optional] 
 **custom** | **str**| The fields that are not defined in the contract of the endpoint to be returned from the system. | [optional] 

### Return type

[**LaborEntry**](LaborEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labor_entry_get_list**
> list[LaborEntry] labor_entry_get_list(select=select, filter=filter, expand=expand, custom=custom, skip=skip, top=top)

Retrieves records that satisfy the specified conditions from the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LaborEntryApi()
select = 'select_example' # str | The fields of the entity to be returned from the system. (optional)
filter = 'filter_example' # str | The conditions that determine which records should be selected from the system. (optional)
expand = 'expand_example' # str | The linked and detail entities that should be expanded. (optional)
custom = 'custom_example' # str | The fields that are not defined in the contract of the endpoint to be returned from the system. (optional)
skip = 56 # int | The number of records to be skipped from the list of returned records. (optional)
top = 56 # int | The number of records to be returned from the system. (optional)

try:
    # Retrieves records that satisfy the specified conditions from the system.
    api_response = api_instance.labor_entry_get_list(select=select, filter=filter, expand=expand, custom=custom, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaborEntryApi->labor_entry_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| The fields of the entity to be returned from the system. | [optional] 
 **filter** | **str**| The conditions that determine which records should be selected from the system. | [optional] 
 **expand** | **str**| The linked and detail entities that should be expanded. | [optional] 
 **custom** | **str**| The fields that are not defined in the contract of the endpoint to be returned from the system. | [optional] 
 **skip** | **int**| The number of records to be skipped from the list of returned records. | [optional] 
 **top** | **int**| The number of records to be returned from the system. | [optional] 

### Return type

[**list[LaborEntry]**](LaborEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labor_entry_put_entity**
> LaborEntry labor_entry_put_entity(entity, select=select, filter=filter, expand=expand, custom=custom)

Creates a record or updates an existing record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LaborEntryApi()
entity = swagger_client.LaborEntry() # LaborEntry | The record to be passed to the system.
select = 'select_example' # str | The fields of the entity to be returned from the system. (optional)
filter = 'filter_example' # str | The conditions that determine which records should be selected from the system. (optional)
expand = 'expand_example' # str | The linked and detail entities that should be expanded. (optional)
custom = 'custom_example' # str | The fields that are not defined in the contract of the endpoint to be returned from the system. (optional)

try:
    # Creates a record or updates an existing record.
    api_response = api_instance.labor_entry_put_entity(entity, select=select, filter=filter, expand=expand, custom=custom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaborEntryApi->labor_entry_put_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**LaborEntry**](LaborEntry.md)| The record to be passed to the system. | 
 **select** | **str**| The fields of the entity to be returned from the system. | [optional] 
 **filter** | **str**| The conditions that determine which records should be selected from the system. | [optional] 
 **expand** | **str**| The linked and detail entities that should be expanded. | [optional] 
 **custom** | **str**| The fields that are not defined in the contract of the endpoint to be returned from the system. | [optional] 

### Return type

[**LaborEntry**](LaborEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

