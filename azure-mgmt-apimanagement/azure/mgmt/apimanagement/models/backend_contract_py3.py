# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class BackendContract(Resource):
    """Backend details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param title: Backend Title.
    :type title: str
    :param description: Backend Description.
    :type description: str
    :param resource_id: Management Uri of the Resource in External System.
     This url can be the Arm Resource Id of Logic Apps, Function Apps or Api
     Apps.
    :type resource_id: str
    :param properties: Backend Properties contract
    :type properties: ~azure.mgmt.apimanagement.models.BackendProperties
    :param credentials: Backend Credentials Contract Properties
    :type credentials:
     ~azure.mgmt.apimanagement.models.BackendCredentialsContract
    :param proxy: Backend Proxy Contract Properties
    :type proxy: ~azure.mgmt.apimanagement.models.BackendProxyContract
    :param tls: Backend TLS Properties
    :type tls: ~azure.mgmt.apimanagement.models.BackendTlsProperties
    :param url: Required. Runtime Url of the Backend.
    :type url: str
    :param protocol: Required. Backend communication protocol. Possible values
     include: 'http', 'soap'
    :type protocol: str or ~azure.mgmt.apimanagement.models.BackendProtocol
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'title': {'max_length': 300, 'min_length': 1},
        'description': {'max_length': 2000, 'min_length': 1},
        'resource_id': {'max_length': 2000, 'min_length': 1},
        'url': {'required': True, 'max_length': 2000, 'min_length': 1},
        'protocol': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'properties': {'key': 'properties.properties', 'type': 'BackendProperties'},
        'credentials': {'key': 'properties.credentials', 'type': 'BackendCredentialsContract'},
        'proxy': {'key': 'properties.proxy', 'type': 'BackendProxyContract'},
        'tls': {'key': 'properties.tls', 'type': 'BackendTlsProperties'},
        'url': {'key': 'properties.url', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
    }

    def __init__(self, *, url: str, protocol, title: str=None, description: str=None, resource_id: str=None, properties=None, credentials=None, proxy=None, tls=None, **kwargs) -> None:
        super(BackendContract, self).__init__(**kwargs)
        self.title = title
        self.description = description
        self.resource_id = resource_id
        self.properties = properties
        self.credentials = credentials
        self.proxy = proxy
        self.tls = tls
        self.url = url
        self.protocol = protocol
