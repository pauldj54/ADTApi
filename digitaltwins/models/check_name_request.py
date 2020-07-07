# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CheckNameRequest(Model):
    """The result returned from a database check name availability request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Resource name.
    :type name: str
    :ivar type: Required. The type of resource, for instance
     Microsoft.DigitalTwins/digitalTwinsInstances. Default value:
     "Microsoft.DigitalTwins/digitalTwinsInstances" .
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.DigitalTwins/digitalTwinsInstances"

    def __init__(self, **kwargs):
        super(CheckNameRequest, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
