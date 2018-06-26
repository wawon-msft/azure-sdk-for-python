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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class TagResourceOperations(object):
    """TagResourceOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. Constant value: "2018-06-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-06-01-preview"

        self.config = config

    def list_by_service(
            self, resource_group_name, service_name, filter=None, top=None, skip=None, custom_headers=None, raw=False, **operation_config):
        """Lists a collection of resources associated with tags.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param filter: | Field       | Supported operators    | Supported
         functions                         |
         |-------------|------------------------|---------------------------------------------|
         | id          | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | name        | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | aid         | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | apiName     | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | apiRevision | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | path        | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | description | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | method      | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | urlTemplate | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | terms       | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | state       | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
         | isCurrent   | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |
        :type filter: str
        :param top: Number of records to return.
        :type top: int
        :param skip: Number of records to skip.
        :type skip: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of TagResourceContract
        :rtype:
         ~azure.mgmt.apimanagement.models.TagResourceContractPaged[~azure.mgmt.apimanagement.models.TagResourceContract]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_service.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=1)
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int', minimum=0)
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.TagResourceContractPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.TagResourceContractPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tagResources'}
