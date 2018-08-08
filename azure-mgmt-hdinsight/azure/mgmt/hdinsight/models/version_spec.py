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


class VersionSpec(Model):
    """The version properties.

    :param friendly_name: The friendly name
    :type friendly_name: str
    :param display_name: The display name
    :type display_name: str
    :param is_default: Whether or not the version is the default version.
    :type is_default: str
    :param component_versions: The component version property.
    :type component_versions: dict[str, str]
    """

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'str'},
        'component_versions': {'key': 'componentVersions', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(VersionSpec, self).__init__(**kwargs)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.display_name = kwargs.get('display_name', None)
        self.is_default = kwargs.get('is_default', None)
        self.component_versions = kwargs.get('component_versions', None)
