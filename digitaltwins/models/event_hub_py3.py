# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .digital_twins_endpoint_resource_properties_py3 import DigitalTwinsEndpointResourceProperties


class EventHub(DigitalTwinsEndpointResourceProperties):
    """properties related to eventhub.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Provisioning', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~digitaltwins.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to
     DigitalTwinsInstance.
    :vartype created_time: datetime
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    :param connection_string_primary_key: Required. PrimaryConnectionString of
     the endpoint. Will be obfuscated during read
    :type connection_string_primary_key: str
    :param connection_string_secondary_key: Required.
     SecondaryConnectionString of the endpoint. Will be obfuscated during read
    :type connection_string_secondary_key: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'endpoint_type': {'required': True},
        'connection_string_primary_key': {'required': True},
        'connection_string_secondary_key': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'connection_string_primary_key': {'key': 'connectionString-PrimaryKey', 'type': 'str'},
        'connection_string_secondary_key': {'key': 'connectionString-SecondaryKey', 'type': 'str'},
    }

    def __init__(self, *, connection_string_primary_key: str, connection_string_secondary_key: str, tags=None, **kwargs) -> None:
        super(EventHub, self).__init__(tags=tags, **kwargs)
        self.connection_string_primary_key = connection_string_primary_key
        self.connection_string_secondary_key = connection_string_secondary_key
        self.endpoint_type = 'EventHub'
