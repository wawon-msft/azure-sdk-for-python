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

from msrest.serialization import Model


class GroupContractProperties(Model):
    """Group contract Properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param display_name: Required. Group name.
    :type display_name: str
    :param description: Group description. Can contain HTML formatting tags.
    :type description: str
    :ivar built_in: true if the group is one of the three system groups
     (Administrators, Developers, or Guests); otherwise false.
    :vartype built_in: bool
    :param type: Group type. Possible values include: 'custom', 'system',
     'external'
    :type type: str or ~azure.mgmt.apimanagement.models.GroupType
    :param external_id: For external groups, this property contains the id of
     the group from the external identity provider, e.g. for Azure Active
     Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`;
     otherwise the value is null.
    :type external_id: str
    """

    _validation = {
        'display_name': {'required': True, 'max_length': 300, 'min_length': 1},
        'description': {'max_length': 1000},
        'built_in': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'built_in': {'key': 'builtIn', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'GroupType'},
        'external_id': {'key': 'externalId', 'type': 'str'},
    }

    def __init__(self, *, display_name: str, description: str=None, type=None, external_id: str=None, **kwargs) -> None:
        super(GroupContractProperties, self).__init__(**kwargs)
        self.display_name = display_name
        self.description = description
        self.built_in = None
        self.type = type
        self.external_id = external_id
