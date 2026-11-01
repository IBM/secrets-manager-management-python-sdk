# coding: utf-8

# (C) Copyright IBM Corp. 2026.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 3.117.3-3e91ab11-20261028-182643

"""
Use the IBM  Cloud® Secrets Manager Instance Management API to manage service instances of
the Vault Dedicated plan.
- Get service instance details including cluster state, endpoints, and key management
service.
- Generate a Vault admin token for authenticating to your Vault Dedicated cluster.
- Revoke all active Vault admin tokens.
- Request payloads must not exceed 1 MB; requests larger than this limit will be rejected
with a `413 Payload Too Large` response.

API Version: 2.0.0
See: https://cloud.ibm.com/docs/secrets-manager
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json
import sys

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class SecretsManagerInstanceManagementV2(BaseService):
    """The secrets-manager-instance-management V2 service."""

    DEFAULT_SERVICE_URL = 'https://us-south.secrets-manager.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'secrets_manager_instance_management'

    PARAMETERIZED_SERVICE_URL = 'https://{region}.secrets-manager.cloud.ibm.com'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'SecretsManagerInstanceManagementV2':
        """
        Return a new client for the secrets-manager-instance-management service
               using the specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    @classmethod
    def construct_service_url(
        cls,
        region: str = 'us-south',
    ) -> str:
        """
        Construct a service URL by formatting the parameterized service URL.

        The parameterized service URL is:
        'https://{region}.secrets-manager.cloud.ibm.com'

        :param str region: (optional) The region where you provisioned your Vault Dedicated Instance. Available regions: us-south, eu-de
            (default 'us-south')
        :return: The formatted URL with all variable placeholders replaced by values.
        :rtype: str
        """
        return cls.PARAMETERIZED_SERVICE_URL.format(
            region=region,
        )

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the secrets-manager-instance-management service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Tokens
    #########################

    def create_vault_admintoken(
        self,
        id: str,
        *,
        response_wrapping: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create admin token.

        Generate a Vault admin token for authenticating to your Vault Dedicated cluster.
        The token is valid for 1 hour and grants administrative privileges. Use only for
        initial setup and cluster management, then revoke immediately. Optionally, set
        response_wrapping to true in the request body to receive a Vault response-wrapped
        token instead of a plain admin token.

        :param str id: Secrets Manager instance ID.
        :param bool response_wrapping: (optional) If true, returns a Vault
               response-wrapped token (wrapped_token). If false or absent, returns a plain
               admin token (token).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Token` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_vault_admintoken',
        )
        headers.update(sdk_headers)

        data = {
            'response_wrapping': response_wrapping,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{id}/admintokens'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_admintokens(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete admin tokens.

        Revoke all active Vault admin tokens. This immediately invalidates all existing
        admin tokens.

        :param str id: Secrets Manager instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_admintokens',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{id}/admintokens'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Instances
    #########################

    def get_instance(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get instance details.

        Get service instance details including cluster state, endpoints, and key
        management service.

        :param str id: Secrets Manager instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Instance` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Destinations
    #########################

    def list_instance_destinations(
        self,
        instance_id: str,
        *,
        state: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List destinations.

        List all destinations for your Vault Dedicated cluster.

        :param str instance_id: Secrets Manager instance ID.
        :param str state: (optional) Filter by destination state.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DestinationCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_instance_destinations',
        )
        headers.update(sdk_headers)

        params = {
            'state': state,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_destination(
        self,
        instance_id: str,
        destination_prototype: 'CreateDestinationRequest',
        **kwargs,
    ) -> DetailedResponse:
        """
        Create destination.

        Create a new destination between your Vault Dedicated cluster and an IBM Cloud
        service instance.
        Returns `202 Accepted` with `state: provisioning`. Provisioning completes
        asynchronously — poll `GET /destinations/{id}` until `state` transitions to
        `succeeded` or `failed`.
        **Beta**: Only Gen 1 (Classic) IBM Cloud Database service instances are supported.
        Gen 2 instances are rejected with `422`. IBM Cloud Database service instances with
        no private endpoints are also rejected with `422`.
        **Rate Limit**: 10 requests per instance per minute
        **Quota**: Maximum 20 destinations per instance.

        :param str instance_id: Secrets Manager instance ID.
        :param CreateDestinationRequest destination_prototype:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IbmCloudDatabaseDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if destination_prototype is None:
            raise ValueError('destination_prototype must be provided')
        if isinstance(destination_prototype, CreateDestinationRequest):
            destination_prototype = convert_model(destination_prototype)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_instance_destination',
        )
        headers.update(sdk_headers)

        data = json.dumps(destination_prototype)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_destination(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get destination details.

        Retrieve details and current state for a specific destination for your Vault
        Dedicated cluster.
        Returns `404` if the destination does not exist. A destination undergoing deletion
        may appear with a `deleting` state before it is fully removed.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IbmCloudDatabaseDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_destination(
        self,
        instance_id: str,
        destination_id: str,
        destination_patch: 'DestinationPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update destination.

        Update mutable metadata fields (`name`, `description`) on a destination for your
        Vault Dedicated cluster. All other fields are immutable after creation.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param DestinationPatch destination_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IbmCloudDatabaseDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if destination_patch is None:
            raise ValueError('destination_patch must be provided')
        if isinstance(destination_patch, DestinationPatch):
            destination_patch = convert_model(destination_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_instance_destination',
        )
        headers.update(sdk_headers)

        data = json.dumps(destination_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_destination(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete destination.

        Delete a destination for your Vault Dedicated cluster. Returns `202 Accepted` and
        begins deletion asynchronously — the destination is removed from `GET
        /destinations` once deletion completes.
        A `failed` destination still counts against the per-instance quota until deleted.
        **Rate Limit**: 10 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IbmCloudDatabaseDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


class ListInstanceDestinationsEnums:
    """
    Enums for list_instance_destinations parameters.
    """

    class State(str, Enum):
        """
        Filter by destination state.
        """

        NOT_STARTED = 'not_started'
        PROVISIONING = 'provisioning'
        SUCCEEDED = 'succeeded'
        FAILED = 'failed'
        DELETING = 'deleting'


##############################################################################
# Models
##############################################################################


class CreateDestinationRequest:
    """
    Request body for creating a destination.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a CreateDestinationRequest object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['CreateDestinationRequestIbmCloudDatabaseDestinationPrototype'])
        )
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateDestinationRequest':
        """Initialize a CreateDestinationRequest object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'CreateDestinationRequest'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join(['CreateDestinationRequestIbmCloudDatabaseDestinationPrototype'])
        )
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a CreateDestinationRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['ibm_cloud_database'] = 'CreateDestinationRequestIbmCloudDatabaseDestinationPrototype'
        disc_value = _dict.get('type')
        if disc_value is None:
            raise ValueError('Discriminator property \'type\' not found in CreateDestinationRequest JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class Destination:
    """
    A destination resource representing a private network link to a service instance on a
    Vault Dedicated cluster.

    :param str id: Destination ID.
    :param str href: (optional) The URL of the destination resource.
    :param str name: Destination name.
    :param str type: Destination type.
    :param str description: (optional) Optional description.
    :param str state: Destination state:
          - `not_started`: Initial state before the first provisioning attempt begins
          - `provisioning`: Provisioning in progress — poll until `succeeded` or `failed`
          - `succeeded`: Destination ready and usable
          - `failed`: Terminal state reached when provisioning or deletion fails. A
          `failed` destination still counts against the per-instance quota until deleted.
          - `deleting`: Deletion in progress.
    :param datetime created_at: Timestamp when the destination was created.
    :param datetime updated_at: Timestamp when the destination was last updated.
    :param str created_by: (optional) IAM identity that created the destination.
    :param str message: (optional) Human-readable message providing additional
          context about the current state. Present only when non-empty — set when `state`
          is `failed`, describing why provisioning or deletion failed.
    """

    def __init__(
        self,
        id: str,
        name: str,
        type: str,
        state: str,
        created_at: datetime,
        updated_at: datetime,
        *,
        href: Optional[str] = None,
        description: Optional[str] = None,
        created_by: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a Destination object.

        :param str id: Destination ID.
        :param str name: Destination name.
        :param str type: Destination type.
        :param str state: Destination state:
               - `not_started`: Initial state before the first provisioning attempt begins
               - `provisioning`: Provisioning in progress — poll until `succeeded` or
               `failed`
               - `succeeded`: Destination ready and usable
               - `failed`: Terminal state reached when provisioning or deletion fails. A
               `failed` destination still counts against the per-instance quota until
               deleted.
               - `deleting`: Deletion in progress.
        :param datetime created_at: Timestamp when the destination was created.
        :param datetime updated_at: Timestamp when the destination was last
               updated.
        :param str description: (optional) Optional description.
        """
        self.id = id
        self.href = href
        self.name = name
        self.type = type
        self.description = description
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Destination':
        """Initialize a Destination object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Destination JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Destination JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in Destination JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in Destination JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in Destination JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in Destination JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Destination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and getattr(self, 'created_by') is not None:
            _dict['created_by'] = getattr(self, 'created_by')
        if hasattr(self, 'message') and getattr(self, 'message') is not None:
            _dict['message'] = getattr(self, 'message')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Destination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Destination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Destination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Destination type.
        """

        IBM_CLOUD_DATABASE = 'ibm_cloud_database'


    class StateEnum(str, Enum):
        """
        Destination state:
        - `not_started`: Initial state before the first provisioning attempt begins
        - `provisioning`: Provisioning in progress — poll until `succeeded` or `failed`
        - `succeeded`: Destination ready and usable
        - `failed`: Terminal state reached when provisioning or deletion fails. A `failed`
        destination still counts against the per-instance quota until deleted.
        - `deleting`: Deletion in progress.
        """

        NOT_STARTED = 'not_started'
        PROVISIONING = 'provisioning'
        SUCCEEDED = 'succeeded'
        FAILED = 'failed'
        DELETING = 'deleting'



class DestinationCollection:
    """
    List of destinations for a Vault Dedicated cluster.

    :param List[Destination] destinations: List of destinations.
    :param int total: Total number of destinations. Maximum 20 per instance.
    """

    def __init__(
        self,
        destinations: List['Destination'],
        total: int,
    ) -> None:
        """
        Initialize a DestinationCollection object.

        :param List[Destination] destinations: List of destinations.
        :param int total: Total number of destinations. Maximum 20 per instance.
        """
        self.destinations = destinations
        self.total = total

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DestinationCollection':
        """Initialize a DestinationCollection object from a json dictionary."""
        args = {}
        if (destinations := _dict.get('destinations')) is not None:
            args['destinations'] = [Destination.from_dict(v) for v in destinations]
        else:
            raise ValueError('Required property \'destinations\' not present in DestinationCollection JSON')
        if (total := _dict.get('total')) is not None:
            args['total'] = total
        else:
            raise ValueError('Required property \'total\' not present in DestinationCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DestinationCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'destinations') and self.destinations is not None:
            destinations_list = []
            for v in self.destinations:
                if isinstance(v, dict):
                    destinations_list.append(v)
                else:
                    destinations_list.append(v.to_dict())
            _dict['destinations'] = destinations_list
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DestinationCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DestinationCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DestinationCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DestinationPatch:
    """
    Fields to update on a destination. At least one field must be provided.

    :param str name: (optional) Updated name.
    :param str description: (optional) Updated description.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a DestinationPatch object.

        :param str name: (optional) Updated name.
        :param str description: (optional) Updated description.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DestinationPatch':
        """Initialize a DestinationPatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DestinationPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DestinationPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DestinationPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DestinationPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IbmCloudDatabaseDestination:
    """
    A destination resource representing a private network link to an IBM Cloud Database
    service instance on a Vault Dedicated cluster.

    :param str id: Destination ID.
    :param str href: (optional) The URL of the destination resource.
    :param str name: Destination name.
    :param str type: Destination type.
    :param str description: (optional) Optional description.
    :param str state: Destination state:
          - `not_started`: Initial state before the first provisioning attempt begins
          - `provisioning`: Provisioning in progress — poll until `succeeded` or `failed`
          - `succeeded`: Destination ready and usable
          - `failed`: Terminal state reached when provisioning or deletion fails. A
          `failed` destination still counts against the per-instance quota until deleted.
          - `deleting`: Deletion in progress.
    :param datetime created_at: Timestamp when the destination was created.
    :param datetime updated_at: Timestamp when the destination was last updated.
    :param str created_by: (optional) IAM identity that created the destination.
    :param str message: (optional) Human-readable message providing additional
          context about the current state. Present only when non-empty — set when `state`
          is `failed`, describing why provisioning or deletion failed.
    :param str crn: IBM Cloud Database service instance CRN.
    """

    def __init__(
        self,
        id: str,
        name: str,
        type: str,
        state: str,
        created_at: datetime,
        updated_at: datetime,
        crn: str,
        *,
        href: Optional[str] = None,
        description: Optional[str] = None,
        created_by: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a IbmCloudDatabaseDestination object.

        :param str id: Destination ID.
        :param str name: Destination name.
        :param str type: Destination type.
        :param str state: Destination state:
               - `not_started`: Initial state before the first provisioning attempt begins
               - `provisioning`: Provisioning in progress — poll until `succeeded` or
               `failed`
               - `succeeded`: Destination ready and usable
               - `failed`: Terminal state reached when provisioning or deletion fails. A
               `failed` destination still counts against the per-instance quota until
               deleted.
               - `deleting`: Deletion in progress.
        :param datetime created_at: Timestamp when the destination was created.
        :param datetime updated_at: Timestamp when the destination was last
               updated.
        :param str crn: IBM Cloud Database service instance CRN.
        :param str description: (optional) Optional description.
        """
        self.id = id
        self.href = href
        self.name = name
        self.type = type
        self.description = description
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.message = message
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IbmCloudDatabaseDestination':
        """Initialize a IbmCloudDatabaseDestination object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in IbmCloudDatabaseDestination JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in IbmCloudDatabaseDestination JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in IbmCloudDatabaseDestination JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in IbmCloudDatabaseDestination JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in IbmCloudDatabaseDestination JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in IbmCloudDatabaseDestination JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in IbmCloudDatabaseDestination JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IbmCloudDatabaseDestination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and getattr(self, 'created_by') is not None:
            _dict['created_by'] = getattr(self, 'created_by')
        if hasattr(self, 'message') and getattr(self, 'message') is not None:
            _dict['message'] = getattr(self, 'message')
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IbmCloudDatabaseDestination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IbmCloudDatabaseDestination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IbmCloudDatabaseDestination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Destination type.
        """

        IBM_CLOUD_DATABASE = 'ibm_cloud_database'


    class StateEnum(str, Enum):
        """
        Destination state:
        - `not_started`: Initial state before the first provisioning attempt begins
        - `provisioning`: Provisioning in progress — poll until `succeeded` or `failed`
        - `succeeded`: Destination ready and usable
        - `failed`: Terminal state reached when provisioning or deletion fails. A `failed`
        destination still counts against the per-instance quota until deleted.
        - `deleting`: Deletion in progress.
        """

        NOT_STARTED = 'not_started'
        PROVISIONING = 'provisioning'
        SUCCEEDED = 'succeeded'
        FAILED = 'failed'
        DELETING = 'deleting'



class Instance:
    """
    The service instance information.

    :param str id: The instance ID.
    :param str name: The instance name.
    :param str instance_crn: The instance CRN identifier.
    :param str plan: Instance plan name.
    :param VaultDedicatedCluster vault_cluster: Vault cluster information for Vault
          Dedicated instances.
    :param VaultDedicatedInstanceEndpoints endpoints: Instance endpoints for Vault
          Dedicated instances.
    :param VaultDedicatedInstanceEncryption encryption: Vault encryption
          configuration for Vault Dedicated instances.
    :param str href: (optional) The URL of the instance resource.
    """

    def __init__(
        self,
        id: str,
        name: str,
        instance_crn: str,
        plan: str,
        vault_cluster: 'VaultDedicatedCluster',
        endpoints: 'VaultDedicatedInstanceEndpoints',
        encryption: 'VaultDedicatedInstanceEncryption',
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a Instance object.

        :param str id: The instance ID.
        :param str name: The instance name.
        :param str instance_crn: The instance CRN identifier.
        :param str plan: Instance plan name.
        :param VaultDedicatedCluster vault_cluster: Vault cluster information for
               Vault Dedicated instances.
        :param VaultDedicatedInstanceEndpoints endpoints: Instance endpoints for
               Vault Dedicated instances.
        :param VaultDedicatedInstanceEncryption encryption: Vault encryption
               configuration for Vault Dedicated instances.
        """
        self.id = id
        self.name = name
        self.instance_crn = instance_crn
        self.plan = plan
        self.vault_cluster = vault_cluster
        self.endpoints = endpoints
        self.encryption = encryption
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Instance':
        """Initialize a Instance object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Instance JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Instance JSON')
        if (instance_crn := _dict.get('instance_crn')) is not None:
            args['instance_crn'] = instance_crn
        else:
            raise ValueError('Required property \'instance_crn\' not present in Instance JSON')
        if (plan := _dict.get('plan')) is not None:
            args['plan'] = plan
        else:
            raise ValueError('Required property \'plan\' not present in Instance JSON')
        if (vault_cluster := _dict.get('vault_cluster')) is not None:
            args['vault_cluster'] = VaultDedicatedCluster.from_dict(vault_cluster)
        else:
            raise ValueError('Required property \'vault_cluster\' not present in Instance JSON')
        if (endpoints := _dict.get('endpoints')) is not None:
            args['endpoints'] = VaultDedicatedInstanceEndpoints.from_dict(endpoints)
        else:
            raise ValueError('Required property \'endpoints\' not present in Instance JSON')
        if (encryption := _dict.get('encryption')) is not None:
            args['encryption'] = VaultDedicatedInstanceEncryption.from_dict(encryption)
        else:
            raise ValueError('Required property \'encryption\' not present in Instance JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Instance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
        if hasattr(self, 'plan') and self.plan is not None:
            _dict['plan'] = self.plan
        if hasattr(self, 'vault_cluster') and self.vault_cluster is not None:
            if isinstance(self.vault_cluster, dict):
                _dict['vault_cluster'] = self.vault_cluster
            else:
                _dict['vault_cluster'] = self.vault_cluster.to_dict()
        if hasattr(self, 'endpoints') and self.endpoints is not None:
            if isinstance(self.endpoints, dict):
                _dict['endpoints'] = self.endpoints
            else:
                _dict['endpoints'] = self.endpoints.to_dict()
        if hasattr(self, 'encryption') and self.encryption is not None:
            if isinstance(self.encryption, dict):
                _dict['encryption'] = self.encryption
            else:
                _dict['encryption'] = self.encryption.to_dict()
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Instance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Instance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Instance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PlanEnum(str, Enum):
        """
        Instance plan name.
        """

        DEDICATED = 'dedicated'



class Token:
    """
    Admin token response. Exactly one of token or wrapped_token is present, never both.
    wrapped_token is returned only when response_wrapping: true is requested.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a Token object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['TokenPlainAdminToken', 'TokenWrappedAdminToken'])
        )
        raise Exception(msg)


class VaultDedicatedCluster:
    """
    Vault cluster information for Vault Dedicated instances.

    :param str status: Vault cluster status. Possible values:
          - sealed: The Vault cluster is sealed and requires unsealing to access secrets
          - not_initialized: The Vault cluster has not been initialized yet
          - healthy: The Vault cluster is operational and ready to serve requests.
    :param str version: Vault cluster version.
    """

    def __init__(
        self,
        status: str,
        version: str,
    ) -> None:
        """
        Initialize a VaultDedicatedCluster object.

        :param str status: Vault cluster status. Possible values:
               - sealed: The Vault cluster is sealed and requires unsealing to access
               secrets
               - not_initialized: The Vault cluster has not been initialized yet
               - healthy: The Vault cluster is operational and ready to serve requests.
        :param str version: Vault cluster version.
        """
        self.status = status
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaultDedicatedCluster':
        """Initialize a VaultDedicatedCluster object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in VaultDedicatedCluster JSON')
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in VaultDedicatedCluster JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaultDedicatedCluster object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VaultDedicatedCluster object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaultDedicatedCluster') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaultDedicatedCluster') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Vault cluster status. Possible values:
        - sealed: The Vault cluster is sealed and requires unsealing to access secrets
        - not_initialized: The Vault cluster has not been initialized yet
        - healthy: The Vault cluster is operational and ready to serve requests.
        """

        SEALED = 'sealed'
        NOT_INITIALIZED = 'not_initialized'
        HEALTHY = 'healthy'



class VaultDedicatedEndpointsData:
    """
    Endpoint URLs for accessing the Vault Dedicated instance.

    :param str vault_api: Vault API endpoint URL.
    :param str vault_ui: Vault UI endpoint URL.
    """

    def __init__(
        self,
        vault_api: str,
        vault_ui: str,
    ) -> None:
        """
        Initialize a VaultDedicatedEndpointsData object.

        :param str vault_api: Vault API endpoint URL.
        :param str vault_ui: Vault UI endpoint URL.
        """
        self.vault_api = vault_api
        self.vault_ui = vault_ui

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaultDedicatedEndpointsData':
        """Initialize a VaultDedicatedEndpointsData object from a json dictionary."""
        args = {}
        if (vault_api := _dict.get('vault_api')) is not None:
            args['vault_api'] = vault_api
        else:
            raise ValueError('Required property \'vault_api\' not present in VaultDedicatedEndpointsData JSON')
        if (vault_ui := _dict.get('vault_ui')) is not None:
            args['vault_ui'] = vault_ui
        else:
            raise ValueError('Required property \'vault_ui\' not present in VaultDedicatedEndpointsData JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaultDedicatedEndpointsData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'vault_api') and self.vault_api is not None:
            _dict['vault_api'] = self.vault_api
        if hasattr(self, 'vault_ui') and self.vault_ui is not None:
            _dict['vault_ui'] = self.vault_ui
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VaultDedicatedEndpointsData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaultDedicatedEndpointsData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaultDedicatedEndpointsData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VaultDedicatedInstanceEncryption:
    """
    Vault encryption configuration for Vault Dedicated instances.

    :param str mode: Vault encryption mode.
    :param str provider: (optional) Vault encryption provider (only present for
          customer_managed mode). Valid value - 'key_protect'.
    :param str key_crn: (optional) Vault encryption key CRN (only present for
          customer_managed mode).
    """

    def __init__(
        self,
        mode: str,
        *,
        provider: Optional[str] = None,
        key_crn: Optional[str] = None,
    ) -> None:
        """
        Initialize a VaultDedicatedInstanceEncryption object.

        :param str mode: Vault encryption mode.
        :param str provider: (optional) Vault encryption provider (only present for
               customer_managed mode). Valid value - 'key_protect'.
        :param str key_crn: (optional) Vault encryption key CRN (only present for
               customer_managed mode).
        """
        self.mode = mode
        self.provider = provider
        self.key_crn = key_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaultDedicatedInstanceEncryption':
        """Initialize a VaultDedicatedInstanceEncryption object from a json dictionary."""
        args = {}
        if (mode := _dict.get('mode')) is not None:
            args['mode'] = mode
        else:
            raise ValueError('Required property \'mode\' not present in VaultDedicatedInstanceEncryption JSON')
        if (provider := _dict.get('provider')) is not None:
            args['provider'] = provider
        if (key_crn := _dict.get('key_crn')) is not None:
            args['key_crn'] = key_crn
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaultDedicatedInstanceEncryption object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'provider') and self.provider is not None:
            _dict['provider'] = self.provider
        if hasattr(self, 'key_crn') and self.key_crn is not None:
            _dict['key_crn'] = self.key_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VaultDedicatedInstanceEncryption object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaultDedicatedInstanceEncryption') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaultDedicatedInstanceEncryption') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        Vault encryption mode.
        """

        CUSTOMER_MANAGED = 'customer_managed'
        SERVICE_MANAGED = 'service_managed'



class VaultDedicatedInstanceEndpoints:
    """
    Instance endpoints for Vault Dedicated instances.

    :param VaultDedicatedEndpointsData public: (optional) Endpoint URLs for
          accessing the Vault Dedicated instance.
    :param VaultDedicatedEndpointsData private: Endpoint URLs for accessing the
          Vault Dedicated instance.
    """

    def __init__(
        self,
        private: 'VaultDedicatedEndpointsData',
        *,
        public: Optional['VaultDedicatedEndpointsData'] = None,
    ) -> None:
        """
        Initialize a VaultDedicatedInstanceEndpoints object.

        :param VaultDedicatedEndpointsData private: Endpoint URLs for accessing the
               Vault Dedicated instance.
        :param VaultDedicatedEndpointsData public: (optional) Endpoint URLs for
               accessing the Vault Dedicated instance.
        """
        self.public = public
        self.private = private

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaultDedicatedInstanceEndpoints':
        """Initialize a VaultDedicatedInstanceEndpoints object from a json dictionary."""
        args = {}
        if (public := _dict.get('public')) is not None:
            args['public'] = VaultDedicatedEndpointsData.from_dict(public)
        if (private := _dict.get('private')) is not None:
            args['private'] = VaultDedicatedEndpointsData.from_dict(private)
        else:
            raise ValueError('Required property \'private\' not present in VaultDedicatedInstanceEndpoints JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaultDedicatedInstanceEndpoints object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'public') and self.public is not None:
            if isinstance(self.public, dict):
                _dict['public'] = self.public
            else:
                _dict['public'] = self.public.to_dict()
        if hasattr(self, 'private') and self.private is not None:
            if isinstance(self.private, dict):
                _dict['private'] = self.private
            else:
                _dict['private'] = self.private.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VaultDedicatedInstanceEndpoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaultDedicatedInstanceEndpoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaultDedicatedInstanceEndpoints') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateDestinationRequestIbmCloudDatabaseDestinationPrototype(CreateDestinationRequest):
    """
    Request body for creating an IBM Cloud Database destination.

    :param str name: Destination name.
    :param str type: Destination type.
    :param str description: (optional) Optional description.
    :param str crn: IBM Cloud Database service instance CRN.
    """

    def __init__(
        self,
        name: str,
        type: str,
        crn: str,
        *,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype object.

        :param str name: Destination name.
        :param str type: Destination type.
        :param str crn: IBM Cloud Database service instance CRN.
        :param str description: (optional) Optional description.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.type = type
        self.description = description
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateDestinationRequestIbmCloudDatabaseDestinationPrototype':
        """Initialize a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in CreateDestinationRequestIbmCloudDatabaseDestinationPrototype JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in CreateDestinationRequestIbmCloudDatabaseDestinationPrototype JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in CreateDestinationRequestIbmCloudDatabaseDestinationPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateDestinationRequestIbmCloudDatabaseDestinationPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateDestinationRequestIbmCloudDatabaseDestinationPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateDestinationRequestIbmCloudDatabaseDestinationPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Destination type.
        """

        IBM_CLOUD_DATABASE = 'ibm_cloud_database'



class TokenPlainAdminToken(Token):
    """
    Response containing a plain Vault admin token.

    :param str token: The plain Vault admin token.
    """

    def __init__(
        self,
        token: str,
    ) -> None:
        """
        Initialize a TokenPlainAdminToken object.

        :param str token: The plain Vault admin token.
        """
        # pylint: disable=super-init-not-called
        self.token = token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TokenPlainAdminToken':
        """Initialize a TokenPlainAdminToken object from a json dictionary."""
        args = {}
        if (token := _dict.get('token')) is not None:
            args['token'] = token
        else:
            raise ValueError('Required property \'token\' not present in TokenPlainAdminToken JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TokenPlainAdminToken object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token') and self.token is not None:
            _dict['token'] = self.token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TokenPlainAdminToken object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TokenPlainAdminToken') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TokenPlainAdminToken') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TokenWrappedAdminToken(Token):
    """
    Response containing a Vault response-wrapped token.

    :param str wrapped_token: A Vault response-wrapped token. Present only when
          response_wrapping: true is requested.
    """

    def __init__(
        self,
        wrapped_token: str,
    ) -> None:
        """
        Initialize a TokenWrappedAdminToken object.

        :param str wrapped_token: A Vault response-wrapped token. Present only when
               response_wrapping: true is requested.
        """
        # pylint: disable=super-init-not-called
        self.wrapped_token = wrapped_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TokenWrappedAdminToken':
        """Initialize a TokenWrappedAdminToken object from a json dictionary."""
        args = {}
        if (wrapped_token := _dict.get('wrapped_token')) is not None:
            args['wrapped_token'] = wrapped_token
        else:
            raise ValueError('Required property \'wrapped_token\' not present in TokenWrappedAdminToken JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TokenWrappedAdminToken object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'wrapped_token') and self.wrapped_token is not None:
            _dict['wrapped_token'] = self.wrapped_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TokenWrappedAdminToken object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TokenWrappedAdminToken') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TokenWrappedAdminToken') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
