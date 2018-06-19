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


class ProductContract(Resource):
    """Product details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param description: Product description. May include HTML formatting tags.
    :type description: str
    :param terms: Product terms of use. Developers trying to subscribe to the
     product will be presented and required to accept these terms before they
     can complete the subscription process.
    :type terms: str
    :param subscription_required: Whether a product subscription is required
     for accessing APIs included in this product. If true, the product is
     referred to as "protected" and a valid subscription key is required for a
     request to an API included in the product to succeed. If false, the
     product is referred to as "open" and requests to an API included in the
     product can be made without a subscription key. If property is omitted
     when creating a new product it's value is assumed to be true.
    :type subscription_required: bool
    :param approval_required: whether subscription approval is required. If
     false, new subscriptions will be approved automatically enabling
     developers to call the product’s APIs immediately after subscribing. If
     true, administrators must manually approve the subscription before the
     developer can any of the product’s APIs. Can be present only if
     subscriptionRequired property is present and has a value of false.
    :type approval_required: bool
    :param subscriptions_limit: Whether the number of subscriptions a user can
     have to this product at the same time. Set to null or omit to allow
     unlimited per user subscriptions. Can be present only if
     subscriptionRequired property is present and has a value of false.
    :type subscriptions_limit: int
    :param state: whether product is published or not. Published products are
     discoverable by users of developer portal. Non published products are
     visible only to administrators. Default state of Product is notPublished.
     Possible values include: 'notPublished', 'published'
    :type state: str or ~azure.mgmt.apimanagement.models.ProductState
    :param display_name: Required. Product name.
    :type display_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'description': {'max_length': 1000, 'min_length': 1},
        'display_name': {'required': True, 'max_length': 300, 'min_length': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'terms': {'key': 'properties.terms', 'type': 'str'},
        'subscription_required': {'key': 'properties.subscriptionRequired', 'type': 'bool'},
        'approval_required': {'key': 'properties.approvalRequired', 'type': 'bool'},
        'subscriptions_limit': {'key': 'properties.subscriptionsLimit', 'type': 'int'},
        'state': {'key': 'properties.state', 'type': 'ProductState'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
    }

    def __init__(self, *, display_name: str, description: str=None, terms: str=None, subscription_required: bool=None, approval_required: bool=None, subscriptions_limit: int=None, state=None, **kwargs) -> None:
        super(ProductContract, self).__init__(**kwargs)
        self.description = description
        self.terms = terms
        self.subscription_required = subscription_required
        self.approval_required = approval_required
        self.subscriptions_limit = subscriptions_limit
        self.state = state
        self.display_name = display_name
