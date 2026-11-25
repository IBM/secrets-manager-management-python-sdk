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
- Delete all active Vault admin tokens.
- Manage destinations for your Vault Dedicated cluster.
- Manage HSM destinations and their related resources, including HA groups, paths, server
CAs, and client certificates.
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
        instance_id: str,
        *,
        response_wrapping: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create admin token.

        Generate a Vault admin token for authenticating to your Vault Dedicated cluster.
        The token is valid for 1 hour and grants administrative privileges. Use only for
        initial setup and cluster management, then delete immediately. Optionally, set
        response_wrapping to true in the request body to receive a Vault response-wrapped
        token instead of a plain admin token.

        :param str instance_id: Secrets Manager instance ID.
        :param bool response_wrapping: (optional) If true, returns a Vault
               response-wrapped token (wrapped_token). If false or absent, returns a plain
               admin token (token).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Token` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/admintokens'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_vault_admintokens(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete admin tokens.

        Delete all active Vault admin tokens. This immediately invalidates all existing
        admin tokens including wrapped tokens.

        :param str instance_id: Secrets Manager instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_vault_admintokens',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/admintokens'.format(**path_param_dict)
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
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get instance details.

        Get service instance details including cluster state, endpoints, and key
        management service.

        :param str instance_id: Secrets Manager instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Instance` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}'.format(**path_param_dict)
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

    #########################
    # HSM Destination
    #########################

    def list_instance_hsm_destinations(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List destinations.

        List all HSM Destinations for this SM instance. Typically returns a single entry
        since only one destination per vendor is allowed.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMDestinationCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_instance_hsm_destinations',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_hsm_destination(
        self,
        instance_id: str,
        name: str,
        vendor: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create destination.

        Create the HSM Destination for this SM instance. Each SM instance may have exactly
        **one** HSM Destination per vendor. Calling POST again returns `409 Conflict`.
        The response `account_id` is required for account policy setup on your gateway.
        Without this step, path provisioning cannot proceed.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str name: Human-readable display name. Required.
        :param str vendor: HSM vendor. Immutable after creation. Currently only
               `thales_luna` is accepted.
        :param str description: (optional) Optional description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if vendor is None:
            raise ValueError('vendor must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_instance_hsm_destination',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'vendor': vendor,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_hsm_destination(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get destination.

        Retrieve a single HSM Destination by its ID.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance_hsm_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_hsm_destination(
        self,
        instance_id: str,
        destination_id: str,
        hsm_destination_patch: 'HSMDestinationPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update destination.

        Update `name` or `description`. Does not stage any HSM config file changes. If
        `name` is omitted, the existing name is preserved (merge-patch semantics).
        `health_state` and `health_as_of` are read-only — if supplied they are silently
        ignored.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param HSMDestinationPatch hsm_destination_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMDestination` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if hsm_destination_patch is None:
            raise ValueError('hsm_destination_patch must be provided')
        if isinstance(hsm_destination_patch, HSMDestinationPatch):
            hsm_destination_patch = convert_model(hsm_destination_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_instance_hsm_destination',
        )
        headers.update(sdk_headers)

        data = json.dumps(hsm_destination_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_hsm_destination(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a destination asynchronously.

        Initiate an asynchronous hard delete of the destination and all its sub-resources
        (HSM HA Groups, paths, Server CAs, client certificates, private keys). Sets
        `provisioning_state` to `deleting`. Poll `GET …/{destination_id}` until `404` to
        confirm completion. **This operation cannot be undone.**
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AsyncDeleteResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_hsm_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_hsm_destination_health_snapshot(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get destination health snapshot.

        Return the persisted AS-OF health snapshot for this destination. Does not trigger
        a new evaluation. Poll until `health_state` is no longer `evaluating` or
        `in_progress`.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DestinationHealthSnapshot` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_hsm_destination_health_snapshot',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/health'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def run_hsm_destination_health_check(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Trigger an async destination health check.

        Start an asynchronous health check across all paths, HSM HA Groups, and client
        certificates. Sets `health_state` to `evaluating` on the destination and all
        sub-resources immediately. Returns `202 Accepted`. Poll `GET …/health` until
        `health_state` is no longer `evaluating`.
        Returns `409 health_check_in_progress` if `health_state` is already `evaluating`
        or `in_progress`.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AsyncHealthCheckAckResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='run_hsm_destination_health_check',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/health'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def apply_hsm_destination(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Trigger an async HSM configuration apply.

        Applies the current configuration (paths, HSM HA Groups, Server CAs, and client
        certificates) of the destination. Sets `health_state` to `in_progress` on the
        destination and all sub-resources immediately, then continues asynchronously.
        Returns `202 Accepted`. On success, automatically triggers a health check. On
        failure, sets all `health_state` to `unknown`.
        Returns `409 apply_not_allowed` if `health_state` is already `in_progress` or
        `evaluating`. Poll `GET …/health` until `health_state` is no longer `in_progress`.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AsyncHealthAckResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='apply_hsm_destination',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/apply'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # HSM HA Groups
    #########################

    def list_instance_hsm_destination_ha_groups(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List HSM HA Groups.

        List all HSM HA Groups for this destination. Returns an empty array if none have
        been created. Results are ordered by creation time ascending.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMHAGroupCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_instance_hsm_destination_ha_groups',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/ha_groups'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_hsm_destination_ha_group(
        self,
        instance_id: str,
        destination_id: str,
        name: str,
        group_label: str,
        group_serial: str,
        member_serials: List[str],
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create HA Group.

        Create a new HA Group. `group_label` must be unique within the destination —
        returns `409 group_label_already_exists` if duplicate. Max 20 HSM HA Groups per
        destination — returns `409 ha_group_limit_reached` if exceeded.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str name: Human-readable display name. Required.
        :param str group_label: HA Group virtual token label. Immutable after
               creation.
        :param str group_serial: HA Group serial number. Immutable after creation.
        :param List[str] member_serials: Ordered list of HSM node member serial
               numbers for this HA Group. At least one entry required. Max 100 unique
               members. Not linked to path resource IDs.
        :param str description: (optional) Optional description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMHAGroup` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if group_label is None:
            raise ValueError('group_label must be provided')
        if group_serial is None:
            raise ValueError('group_serial must be provided')
        if member_serials is None:
            raise ValueError('member_serials must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_instance_hsm_destination_ha_group',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'group_label': group_label,
            'group_serial': group_serial,
            'member_serials': member_serials,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/ha_groups'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_hsm_destination_ha_group(
        self,
        instance_id: str,
        destination_id: str,
        ha_group_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get HA Group.

        Retrieve a single HA Group by its ID.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str ha_group_id: The identifier of the HA Group to operate on.
               Matches the `id` field in the `HSMHAGroup` response schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMHAGroup` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not ha_group_id:
            raise ValueError('ha_group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance_hsm_destination_ha_group',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'ha_group_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, ha_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/ha_groups/{ha_group_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_hsm_destination_ha_group(
        self,
        instance_id: str,
        destination_id: str,
        ha_group_id: str,
        hsmha_group_patch: 'HSMHAGroupPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update HA Group.

        Update an HA Group. `group_serial` and `group_label` are immutable after creation
        — return `400` if supplied. If `name` is omitted, the existing name is preserved
        (merge-patch semantics). `name` cannot be set to `null`.
        `member_serials` can be updated to add or remove members (at least one entry
        required).
        `health_state` and `health_as_of` are read-only — silently ignored if supplied.
        **HSM Config File**: staged when `member_serials` is changed.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str ha_group_id: The identifier of the HA Group to operate on.
               Matches the `id` field in the `HSMHAGroup` response schema.
        :param HSMHAGroupPatch hsmha_group_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMHAGroup` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not ha_group_id:
            raise ValueError('ha_group_id must be provided')
        if hsmha_group_patch is None:
            raise ValueError('hsmha_group_patch must be provided')
        if isinstance(hsmha_group_patch, HSMHAGroupPatch):
            hsmha_group_patch = convert_model(hsmha_group_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_instance_hsm_destination_ha_group',
        )
        headers.update(sdk_headers)

        data = json.dumps(hsmha_group_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'ha_group_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, ha_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/ha_groups/{ha_group_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_hsm_destination_ha_group(
        self,
        instance_id: str,
        destination_id: str,
        ha_group_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete HA Group (synchronous hard delete).

        Synchronous hard delete — returns 204 immediately.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str ha_group_id: The identifier of the HA Group to operate on.
               Matches the `id` field in the `HSMHAGroup` response schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not ha_group_id:
            raise ValueError('ha_group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_hsm_destination_ha_group',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'destination_id', 'ha_group_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, ha_group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/ha_groups/{ha_group_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Paths
    #########################

    def list_instance_hsm_destination_paths(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List paths.

        List all paths (nodes) for this destination. Returns an empty array if none have
        been created. Results are ordered by creation time ascending.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PathCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_instance_hsm_destination_paths',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_hsm_destination_path(
        self,
        instance_id: str,
        destination_id: str,
        name: str,
        crn: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create path.

        Create a new path. `crn` is immutable. Must be unique within the destination —
        returns `409 crn_already_in_use` if duplicate. Max 20 paths per destination —
        returns `409 path_limit_reached` if exceeded.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str name: Human-readable display name. Required.
        :param str crn: CRN of the gateway through which the HSM is reached.
               Immutable after creation.
        :param str description: (optional) Optional description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Path` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_instance_hsm_destination_path',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'crn': crn,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_hsm_destination_path(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get path.

        Retrieve a single path by its ID.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Path` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance_hsm_destination_path',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_hsm_destination_path(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        path_patch: 'PathPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update path.

        Update `name` or `description` (merge-patch semantics). `crn` is immutable.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param PathPatch path_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Path` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        if path_patch is None:
            raise ValueError('path_patch must be provided')
        if isinstance(path_patch, PathPatch):
            path_patch = convert_model(path_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_instance_hsm_destination_path',
        )
        headers.update(sdk_headers)

        data = json.dumps(path_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_hsm_destination_path(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete path (async hard delete).

        Async hard delete of the path and its Server CAs. Sets `provisioning_state` to
        `deleting`. Poll `GET …/{path_id}` until `404`.
        **This operation cannot be undone.**
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Path` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_hsm_destination_path',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_path_build(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Build path (trigger provisioning).

        Trigger provisioning of the path. The customer must first approve the Secrets
        Manager account policy for the gateway. Moves path from `pending_account_policy` →
        `provisioning`. Returns `409` if already `provisioning`.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `VpeProvisioningResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_path_build',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/build'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_path_vpe_status(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Health check path (check provisioning status).

        Check the current provisioning status of this path. Can be called while the path
        is in `provisioning` or `pending_approval` state. Returns the latest health state
        and the resulting path `provisioning_state`.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `VpeStatusResult` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_path_vpe_status',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/health_check'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def reset_hsm_destination_path(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Reset a path to its initial pending state.

        Reset path to `pending_account_policy` so `POST /build` can be retried. Allowed
        from `crn_already_in_use`, `approval_declined`, `completed`, or
        `vpe_provisioning_failed`. Returns `409` otherwise.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HSMPathReset` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='reset_hsm_destination_path',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/reset'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Server CAs
    #########################

    def list_instance_hsm_destination_path_server_cas(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List Server CA certificates.

        List all Server CA certificates for this path. Returns an empty array if none have
        been added. At most one certificate can be active at a time; up to 10 certificates
        total per path. Results are ordered by creation time ascending.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerCaCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_instance_hsm_destination_path_server_cas',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/server_cas'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_hsm_destination_path_server_ca(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        name: str,
        certificate: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add Server CA certificate.

        Add a Server CA (PEM). Starts `inactive`. Max 10 per path — returns `409
        server_ca_limit_reached` if exceeded. Certificate must not be expired — returns
        `400 cert_expired`.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param str name: Human-readable display name. Required.
        :param str certificate: PEM-encoded Server CA certificate. Immutable after
               creation.
        :param str description: (optional) Optional description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerCa` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if certificate is None:
            raise ValueError('certificate must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_instance_hsm_destination_path_server_ca',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'certificate': certificate,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/server_cas'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_hsm_destination_path_server_ca(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        server_ca_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Server CA certificate.

        Retrieve a single Server CA certificate by its ID.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param str server_ca_id: The identifier of the Server CA to operate on.
               Matches the `id` field in the `ServerCa` response schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerCa` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        if not server_ca_id:
            raise ValueError('server_ca_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance_hsm_destination_path_server_ca',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id', 'server_ca_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id, server_ca_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/server_cas/{server_ca_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_hsm_destination_path_server_ca(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        server_ca_id: str,
        server_ca_patch: 'ServerCaPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update or activate Server CA.

        Rename, update description, or activate a Server CA (merge-patch semantics).
        `certificate` is immutable. Activating demotes the currently active CA to
        `inactive`.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param str server_ca_id: The identifier of the Server CA to operate on.
               Matches the `id` field in the `ServerCa` response schema.
        :param ServerCaPatch server_ca_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerCa` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        if not server_ca_id:
            raise ValueError('server_ca_id must be provided')
        if server_ca_patch is None:
            raise ValueError('server_ca_patch must be provided')
        if isinstance(server_ca_patch, ServerCaPatch):
            server_ca_patch = convert_model(server_ca_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_instance_hsm_destination_path_server_ca',
        )
        headers.update(sdk_headers)

        data = json.dumps(server_ca_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'path_id', 'server_ca_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id, server_ca_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/server_cas/{server_ca_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_hsm_destination_path_server_ca(
        self,
        instance_id: str,
        destination_id: str,
        path_id: str,
        server_ca_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete Server CA certificate.

        Hard delete a Server CA certificate. Cannot delete the active Server CA — returns
        `409`. Synchronous (204, no body).
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str path_id: Path ID.
        :param str server_ca_id: The identifier of the Server CA to operate on.
               Matches the `id` field in the `ServerCa` response schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not path_id:
            raise ValueError('path_id must be provided')
        if not server_ca_id:
            raise ValueError('server_ca_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_hsm_destination_path_server_ca',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'destination_id', 'path_id', 'server_ca_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, path_id, server_ca_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/paths/{path_id}/server_cas/{server_ca_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Client Certificates
    #########################

    def list_instance_hsm_destination_client_certificates(
        self,
        instance_id: str,
        destination_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List client certificates.

        List all client certificates for this destination. Returns an empty array if none
        have been created. At most one certificate can be active; up to 10 inactive or
        pending certificates may exist in addition. Results are ordered by creation time
        ascending.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClientCertificateCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_instance_hsm_destination_client_certificates',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/client_certificates'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_hsm_destination_client_certificate(
        self,
        instance_id: str,
        destination_id: str,
        name: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Generate client certificate (CSR).

        Generate an RSA private key and CSR. CSR is immediately available in the response.
        Max 10 inactive/csr_generated certificates — returns `409 cert_limit_exceeded` if
        exceeded.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str name: Human-readable display name. Required.
        :param str description: (optional) Optional description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClientCertificate` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_instance_hsm_destination_client_certificate',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/client_certificates'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_hsm_destination_client_certificate(
        self,
        instance_id: str,
        destination_id: str,
        cert_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get client certificate.

        Retrieve a single client certificate by its ID.
        **Rate Limit**: 100 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str cert_id: The identifier of the Client Certificate to operate on.
               Matches the `id` field in the `ClientCertificate` response schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClientCertificate` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not cert_id:
            raise ValueError('cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_instance_hsm_destination_client_certificate',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'cert_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, cert_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/client_certificates/{cert_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_hsm_destination_client_certificate(
        self,
        instance_id: str,
        destination_id: str,
        cert_id: str,
        client_certificate_patch: 'ClientCertificatePatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update, upload signed cert, and/or activate.

        Update name/description, upload `signed_cert`, or activate (merge-patch
        semantics). `signed_cert` must match the generated CSR — returns `400
        csr_mismatch` otherwise.
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str cert_id: The identifier of the Client Certificate to operate on.
               Matches the `id` field in the `ClientCertificate` response schema.
        :param ClientCertificatePatch client_certificate_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClientCertificate` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not cert_id:
            raise ValueError('cert_id must be provided')
        if client_certificate_patch is None:
            raise ValueError('client_certificate_patch must be provided')
        if isinstance(client_certificate_patch, ClientCertificatePatch):
            client_certificate_patch = convert_model(client_certificate_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_instance_hsm_destination_client_certificate',
        )
        headers.update(sdk_headers)

        data = json.dumps(client_certificate_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'destination_id', 'cert_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, cert_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/client_certificates/{cert_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_hsm_destination_client_certificate(
        self,
        instance_id: str,
        destination_id: str,
        cert_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete client certificate.

        Delete a client certificate and purge its private key from Vault. Cannot delete
        the active certificate — returns `409 Conflict`. Synchronous (204, no body).
        **Rate Limit**: 5 requests per instance per minute.

        :param str instance_id: Secrets Manager instance ID.
        :param str destination_id: Destination ID.
        :param str cert_id: The identifier of the Client Certificate to operate on.
               Matches the `id` field in the `ClientCertificate` response schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not destination_id:
            raise ValueError('destination_id must be provided')
        if not cert_id:
            raise ValueError('cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_instance_hsm_destination_client_certificate',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'destination_id', 'cert_id']
        path_param_values = self.encode_path_vars(instance_id, destination_id, cert_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/instances/{instance_id}/hsm_destinations/{destination_id}/client_certificates/{cert_id}'.format(**path_param_dict)
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


class AsyncDeleteResponse:
    """
    Response body for async DELETE operations (202 Accepted). The `type` field is
    intentionally omitted — the caller knows which resource they deleted.

    :param str href: (optional) URL of the resource being deleted.
    :param str id: (optional) ID of the resource being deleted.
    :param str provisioning_state: Lifecycle state of the deleted resource. Always
          `deleting` on a 202 response.
    """

    def __init__(
        self,
        provisioning_state: str,
        *,
        href: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a AsyncDeleteResponse object.

        :param str provisioning_state: Lifecycle state of the deleted resource.
               Always `deleting` on a 202 response.
        """
        self.href = href
        self.id = id
        self.provisioning_state = provisioning_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AsyncDeleteResponse':
        """Initialize a AsyncDeleteResponse object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in AsyncDeleteResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AsyncDeleteResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AsyncDeleteResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AsyncDeleteResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AsyncDeleteResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the deleted resource. Always `deleting` on a 202 response.
        """

        DELETING = 'deleting'



class AsyncHealthAckResponse:
    """
    Response body for the async apply operation (202 Accepted). The body is currently an
    empty object;
    `href`, when present, is the `GET …/health` polling endpoint. Poll `GET …/health`
    until `health_state` is no longer `in_progress`.

    :param str href: (optional) URL of the GET …/health snapshot endpoint to poll
          for results. Not currently returned.
    """

    def __init__(
        self,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a AsyncHealthAckResponse object.

        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AsyncHealthAckResponse':
        """Initialize a AsyncHealthAckResponse object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AsyncHealthAckResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AsyncHealthAckResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AsyncHealthAckResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AsyncHealthAckResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AsyncHealthCheckAckResponse:
    """
    Response body for the async destination health-check operation (202 Accepted).
    Contains the `href` of the `GET …/health` polling endpoint and the health state known
    at acceptance time. Sub-resource arrays are empty when none exist. Poll `GET …/health`
    until `health_state` is no longer `evaluating`.

    :param str href: (optional) URL of the GET …/health snapshot endpoint to poll
          for results.
    :param str destination_id: (optional) ID of the destination.
    :param str health_state: AS OF (point-in-time) health state. Written exclusively
          by POST …/health and POST …/apply:
          - `unknown`: Health check not yet performed, or destination is
          deleting/deletion_failed.
          - `evaluating`: A health check (POST …/health) is in progress. Set on
          acceptance; replaced when the check completes.
          - `in_progress`: An apply operation (POST …/apply) is running. Set on
          acceptance; replaced by the health check result once apply completes (or set to
          `unknown` on failure).
          - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with
          active non-expired Server CA, and ≥1 active non-expired client certificate).
          - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or `degraded`.
          - `degraded`: Some non-`not_configured` HSM HA Groups are `unhealthy`/`unknown`
          AND at least one is `healthy`.
          - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
          `unknown`.
    :param datetime health_as_of: (optional) Timestamp of the health state, when
          available.
    :param List[HealthSnapshotClientCert] client_certificates: Client certificates
          for this destination. Empty array if none exist.
    :param List[HealthSnapshotHSMHAGroup] ha_groups: HSM HA Groups for this
          destination. Empty array if none exist.
    :param List[HealthSnapshotConnection] paths: Paths for this destination. Empty
          array if none exist.
    """

    def __init__(
        self,
        health_state: str,
        client_certificates: List['HealthSnapshotClientCert'],
        ha_groups: List['HealthSnapshotHSMHAGroup'],
        paths: List['HealthSnapshotConnection'],
        *,
        href: Optional[str] = None,
        destination_id: Optional[str] = None,
        health_as_of: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a AsyncHealthCheckAckResponse object.

        :param str health_state: AS OF (point-in-time) health state. Written
               exclusively by POST …/health and POST …/apply:
               - `unknown`: Health check not yet performed, or destination is
               deleting/deletion_failed.
               - `evaluating`: A health check (POST …/health) is in progress. Set on
               acceptance; replaced when the check completes.
               - `in_progress`: An apply operation (POST …/apply) is running. Set on
               acceptance; replaced by the health check result once apply completes (or
               set to `unknown` on failure).
               - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with
               active non-expired Server CA, and ≥1 active non-expired client
               certificate).
               - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or
               `degraded`.
               - `degraded`: Some non-`not_configured` HSM HA Groups are
               `unhealthy`/`unknown` AND at least one is `healthy`.
               - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
               `unknown`.
        :param List[HealthSnapshotClientCert] client_certificates: Client
               certificates for this destination. Empty array if none exist.
        :param List[HealthSnapshotHSMHAGroup] ha_groups: HSM HA Groups for this
               destination. Empty array if none exist.
        :param List[HealthSnapshotConnection] paths: Paths for this destination.
               Empty array if none exist.
        :param str destination_id: (optional) ID of the destination.
        :param datetime health_as_of: (optional) Timestamp of the health state,
               when available.
        """
        self.href = href
        self.destination_id = destination_id
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.client_certificates = client_certificates
        self.ha_groups = ha_groups
        self.paths = paths

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AsyncHealthCheckAckResponse':
        """Initialize a AsyncHealthCheckAckResponse object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (destination_id := _dict.get('destination_id')) is not None:
            args['destination_id'] = destination_id
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in AsyncHealthCheckAckResponse JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        if (client_certificates := _dict.get('client_certificates')) is not None:
            args['client_certificates'] = [HealthSnapshotClientCert.from_dict(v) for v in client_certificates]
        else:
            raise ValueError('Required property \'client_certificates\' not present in AsyncHealthCheckAckResponse JSON')
        if (ha_groups := _dict.get('ha_groups')) is not None:
            args['ha_groups'] = [HealthSnapshotHSMHAGroup.from_dict(v) for v in ha_groups]
        else:
            raise ValueError('Required property \'ha_groups\' not present in AsyncHealthCheckAckResponse JSON')
        if (paths := _dict.get('paths')) is not None:
            args['paths'] = [HealthSnapshotConnection.from_dict(v) for v in paths]
        else:
            raise ValueError('Required property \'paths\' not present in AsyncHealthCheckAckResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AsyncHealthCheckAckResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'destination_id') and self.destination_id is not None:
            _dict['destination_id'] = self.destination_id
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'client_certificates') and self.client_certificates is not None:
            client_certificates_list = []
            for v in self.client_certificates:
                if isinstance(v, dict):
                    client_certificates_list.append(v)
                else:
                    client_certificates_list.append(v.to_dict())
            _dict['client_certificates'] = client_certificates_list
        if hasattr(self, 'ha_groups') and self.ha_groups is not None:
            ha_groups_list = []
            for v in self.ha_groups:
                if isinstance(v, dict):
                    ha_groups_list.append(v)
                else:
                    ha_groups_list.append(v.to_dict())
            _dict['ha_groups'] = ha_groups_list
        if hasattr(self, 'paths') and self.paths is not None:
            paths_list = []
            for v in self.paths:
                if isinstance(v, dict):
                    paths_list.append(v)
                else:
                    paths_list.append(v.to_dict())
            _dict['paths'] = paths_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AsyncHealthCheckAckResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AsyncHealthCheckAckResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AsyncHealthCheckAckResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF (point-in-time) health state. Written exclusively by POST …/health and POST
        …/apply:
        - `unknown`: Health check not yet performed, or destination is
        deleting/deletion_failed.
        - `evaluating`: A health check (POST …/health) is in progress. Set on acceptance;
        replaced when the check completes.
        - `in_progress`: An apply operation (POST …/apply) is running. Set on acceptance;
        replaced by the health check result once apply completes (or set to `unknown` on
        failure).
        - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with active
        non-expired Server CA, and ≥1 active non-expired client certificate).
        - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or `degraded`.
        - `degraded`: Some non-`not_configured` HSM HA Groups are `unhealthy`/`unknown`
        AND at least one is `healthy`.
        - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
        `unknown`.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        DEGRADED = 'degraded'
        UNHEALTHY = 'unhealthy'
        NOT_CONFIGURED = 'not_configured'



class ClientCertificate:
    """
    A client certificate resource. csr, signed_cert, and expires_at are top-level fields.
    There is no vendor_config wrapper. CSR and private key are platform-generated. CN
    (`csr_cn`) is set to the SM instance UUID. The private key is stored securely and is
    NOT exposed in any API response. Max 10 inactive/csr_generated certificates at any
    time. Active certificate cannot be deleted.
    `csr` and `csr_cn` are populated on creation.

    :param str id: (optional) Certificate ID. Immutable.
    :param str href: (optional) URL of the client certificate resource.
    :param str name: Human-readable display name.
    :param str description: (optional) Optional description. Omitted if not set.
    :param str status: (optional) Request-only. Set to `active` in a PATCH to
          activate this certificate. Never returned; read the current state from
          `provisioning_state`.
    :param str provisioning_state: Lifecycle state of the client certificate:
          - `csr_generated`: CSR and private key generated successfully. `csr` and
          `csr_cn` are populated. Initial state on POST. Waiting for signed_cert to be
          uploaded via PATCH.
          - `inactive`: signed_cert has been uploaded but the certificate has not been
          activated yet.
          - `active`: This certificate is the active client certificate for the
          destination. Only one can be active at a time.
    :param str health_state: AS OF health state of the client certificate. Written
          exclusively by POST …/health:
          - `unknown`: Initial state on creation, and for csr_generated certs with no
          signed_cert.
          - `evaluating`: A health check is in progress for this client certificate.
          - `valid`: Certificate is within its validity period (expires_at is in the
          future).
          - `expired`: Certificate has passed its expires_at date.
    :param datetime health_as_of: Timestamp of the last health evaluation. On
          creation equals `created_at`. Updated only by POST …/health.
    :param str csr: PEM-encoded CSR. Platform-generated. Immutable once set.
          Populated on creation (always present once the resource exists).
    :param str csr_cn: Common Name embedded in the CSR. Set to the SM instance UUID
          at generation time. Immutable once set. Populated on creation (always present
          once the resource exists).
    :param str signed_cert: (optional) CA-signed certificate (PEM). Omitted until
          uploaded via PATCH.
    :param datetime expires_at: (optional) Parsed from signed_cert NotAfter field.
          Omitted until signed_cert is uploaded.
    :param datetime created_at: Computed field.
    :param datetime updated_at: (optional) Computed field. Omitted until first
          update.
    :param str created_by: Computed field.
    :param str updated_by: (optional) Computed field. Omitted until first update.
    """

    def __init__(
        self,
        name: str,
        provisioning_state: str,
        health_state: str,
        health_as_of: datetime,
        csr: str,
        csr_cn: str,
        created_at: datetime,
        created_by: str,
        *,
        id: Optional[str] = None,
        href: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        signed_cert: Optional[str] = None,
        expires_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[str] = None,
    ) -> None:
        """
        Initialize a ClientCertificate object.

        :param str name: Human-readable display name.
        :param str provisioning_state: Lifecycle state of the client certificate:
               - `csr_generated`: CSR and private key generated successfully. `csr` and
               `csr_cn` are populated. Initial state on POST. Waiting for signed_cert to
               be uploaded via PATCH.
               - `inactive`: signed_cert has been uploaded but the certificate has not
               been activated yet.
               - `active`: This certificate is the active client certificate for the
               destination. Only one can be active at a time.
        :param str health_state: AS OF health state of the client certificate.
               Written exclusively by POST …/health:
               - `unknown`: Initial state on creation, and for csr_generated certs with no
               signed_cert.
               - `evaluating`: A health check is in progress for this client certificate.
               - `valid`: Certificate is within its validity period (expires_at is in the
               future).
               - `expired`: Certificate has passed its expires_at date.
        :param datetime health_as_of: Timestamp of the last health evaluation. On
               creation equals `created_at`. Updated only by POST …/health.
        :param str csr: PEM-encoded CSR. Platform-generated. Immutable once set.
               Populated on creation (always present once the resource exists).
        :param str csr_cn: Common Name embedded in the CSR. Set to the SM instance
               UUID at generation time. Immutable once set. Populated on creation (always
               present once the resource exists).
        :param datetime created_at: Computed field.
        :param str created_by: Computed field.
        :param str description: (optional) Optional description. Omitted if not
               set.
        :param str status: (optional) Request-only. Set to `active` in a PATCH to
               activate this certificate. Never returned; read the current state from
               `provisioning_state`.
        :param str signed_cert: (optional) CA-signed certificate (PEM). Omitted
               until uploaded via PATCH.
        :param datetime expires_at: (optional) Parsed from signed_cert NotAfter
               field. Omitted until signed_cert is uploaded.
        :param datetime updated_at: (optional) Computed field. Omitted until first
               update.
        :param str updated_by: (optional) Computed field. Omitted until first
               update.
        """
        self.id = id
        self.href = href
        self.name = name
        self.description = description
        self.status = status
        self.provisioning_state = provisioning_state
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.csr = csr
        self.csr_cn = csr_cn
        self.signed_cert = signed_cert
        self.expires_at = expires_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClientCertificate':
        """Initialize a ClientCertificate object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ClientCertificate JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in ClientCertificate JSON')
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in ClientCertificate JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        else:
            raise ValueError('Required property \'health_as_of\' not present in ClientCertificate JSON')
        if (csr := _dict.get('csr')) is not None:
            args['csr'] = csr
        else:
            raise ValueError('Required property \'csr\' not present in ClientCertificate JSON')
        if (csr_cn := _dict.get('csr_cn')) is not None:
            args['csr_cn'] = csr_cn
        else:
            raise ValueError('Required property \'csr_cn\' not present in ClientCertificate JSON')
        if (signed_cert := _dict.get('signed_cert')) is not None:
            args['signed_cert'] = signed_cert
        if (expires_at := _dict.get('expires_at')) is not None:
            args['expires_at'] = string_to_datetime(expires_at)
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in ClientCertificate JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in ClientCertificate JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClientCertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'csr') and self.csr is not None:
            _dict['csr'] = self.csr
        if hasattr(self, 'csr_cn') and self.csr_cn is not None:
            _dict['csr_cn'] = self.csr_cn
        if hasattr(self, 'signed_cert') and self.signed_cert is not None:
            _dict['signed_cert'] = self.signed_cert
        if hasattr(self, 'expires_at') and self.expires_at is not None:
            _dict['expires_at'] = datetime_to_string(self.expires_at)
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClientCertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClientCertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClientCertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the client certificate:
        - `csr_generated`: CSR and private key generated successfully. `csr` and `csr_cn`
        are populated. Initial state on POST. Waiting for signed_cert to be uploaded via
        PATCH.
        - `inactive`: signed_cert has been uploaded but the certificate has not been
        activated yet.
        - `active`: This certificate is the active client certificate for the destination.
        Only one can be active at a time.
        """

        CSR_GENERATED = 'csr_generated'
        INACTIVE = 'inactive'
        ACTIVE = 'active'


    class HealthStateEnum(str, Enum):
        """
        AS OF health state of the client certificate. Written exclusively by POST
        …/health:
        - `unknown`: Initial state on creation, and for csr_generated certs with no
        signed_cert.
        - `evaluating`: A health check is in progress for this client certificate.
        - `valid`: Certificate is within its validity period (expires_at is in the
        future).
        - `expired`: Certificate has passed its expires_at date.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        VALID = 'valid'
        EXPIRED = 'expired'



class ClientCertificateCollection:
    """
    A collection of client certificates.

    :param List[ClientCertificate] client_certificates: The list of client
          certificates for this destination.
    """

    def __init__(
        self,
        client_certificates: List['ClientCertificate'],
    ) -> None:
        """
        Initialize a ClientCertificateCollection object.

        :param List[ClientCertificate] client_certificates: The list of client
               certificates for this destination.
        """
        self.client_certificates = client_certificates

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClientCertificateCollection':
        """Initialize a ClientCertificateCollection object from a json dictionary."""
        args = {}
        if (client_certificates := _dict.get('client_certificates')) is not None:
            args['client_certificates'] = [ClientCertificate.from_dict(v) for v in client_certificates]
        else:
            raise ValueError('Required property \'client_certificates\' not present in ClientCertificateCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClientCertificateCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_certificates') and self.client_certificates is not None:
            client_certificates_list = []
            for v in self.client_certificates:
                if isinstance(v, dict):
                    client_certificates_list.append(v)
                else:
                    client_certificates_list.append(v.to_dict())
            _dict['client_certificates'] = client_certificates_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClientCertificateCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClientCertificateCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClientCertificateCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClientCertificatePatch:
    """
    Fields to update on the client certificate. Only supplied fields are changed
    (merge-patch semantics).

    :param str name: (optional) Updated display name for the certificate.
    :param str description: (optional) Updated description. Set to empty string to
          clear.
    :param str status: (optional) Set to `active` to activate this certificate. Only
          `active` is allowed.
    :param str signed_cert: (optional) CA-signed certificate (PEM). Makes cert
          eligible for activation.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        signed_cert: Optional[str] = None,
    ) -> None:
        """
        Initialize a ClientCertificatePatch object.

        :param str name: (optional) Updated display name for the certificate.
        :param str description: (optional) Updated description. Set to empty string
               to clear.
        :param str status: (optional) Set to `active` to activate this certificate.
               Only `active` is allowed.
        :param str signed_cert: (optional) CA-signed certificate (PEM). Makes cert
               eligible for activation.
        """
        self.name = name
        self.description = description
        self.status = status
        self.signed_cert = signed_cert

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClientCertificatePatch':
        """Initialize a ClientCertificatePatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (signed_cert := _dict.get('signed_cert')) is not None:
            args['signed_cert'] = signed_cert
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClientCertificatePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'signed_cert') and self.signed_cert is not None:
            _dict['signed_cert'] = self.signed_cert
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClientCertificatePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClientCertificatePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClientCertificatePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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

    :param str id: A standard UUID string (RFC 4122).
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

        :param str id: A standard UUID string (RFC 4122).
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


class DestinationHealthSnapshot:
    """
    Persisted AS-OF health snapshot for a destination. Returned by GET
    /hsm_destinations/{destination_id}/health and by the async POST
    /hsm_destinations/{destination_id}/health and POST
    /hsm_destinations/{destination_id}/apply flows
    (poll until health_state is no longer `evaluating` or `in_progress`). All health_state
    values reflect the last completed evaluation.

    :param str href: (optional) URL of the health snapshot endpoint for this
          destination.
    :param str destination_id: ID of the destination. Echoed from path param.
    :param str health_state: AS OF (point-in-time) health state. Written exclusively
          by POST …/health and POST …/apply:
          - `unknown`: Health check not yet performed, or destination is
          deleting/deletion_failed.
          - `evaluating`: A health check (POST …/health) is in progress. Set on
          acceptance; replaced when the check completes.
          - `in_progress`: An apply operation (POST …/apply) is running. Set on
          acceptance; replaced by the health check result once apply completes (or set to
          `unknown` on failure).
          - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with
          active non-expired Server CA, and ≥1 active non-expired client certificate).
          - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or `degraded`.
          - `degraded`: Some non-`not_configured` HSM HA Groups are `unhealthy`/`unknown`
          AND at least one is `healthy`.
          - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
          `unknown`.
    :param datetime health_as_of: Timestamp of this health check — always the
          current time of the live probe.
    :param List[HealthSnapshotClientCert] client_certificates: All client
          certificates for this destination (active, inactive, csr_generated).
          health_state freshly evaluated for all certs with a signed_cert.
    :param List[HealthSnapshotHSMHAGroup] ha_groups: All HSM HA Groups for this
          destination. Empty array if none exist.
    :param List[HealthSnapshotConnection] paths: All paths for this destination.
          Empty array if none exist.
    """

    def __init__(
        self,
        destination_id: str,
        health_state: str,
        health_as_of: datetime,
        client_certificates: List['HealthSnapshotClientCert'],
        ha_groups: List['HealthSnapshotHSMHAGroup'],
        paths: List['HealthSnapshotConnection'],
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a DestinationHealthSnapshot object.

        :param str destination_id: ID of the destination. Echoed from path param.
        :param str health_state: AS OF (point-in-time) health state. Written
               exclusively by POST …/health and POST …/apply:
               - `unknown`: Health check not yet performed, or destination is
               deleting/deletion_failed.
               - `evaluating`: A health check (POST …/health) is in progress. Set on
               acceptance; replaced when the check completes.
               - `in_progress`: An apply operation (POST …/apply) is running. Set on
               acceptance; replaced by the health check result once apply completes (or
               set to `unknown` on failure).
               - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with
               active non-expired Server CA, and ≥1 active non-expired client
               certificate).
               - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or
               `degraded`.
               - `degraded`: Some non-`not_configured` HSM HA Groups are
               `unhealthy`/`unknown` AND at least one is `healthy`.
               - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
               `unknown`.
        :param datetime health_as_of: Timestamp of this health check — always the
               current time of the live probe.
        :param List[HealthSnapshotClientCert] client_certificates: All client
               certificates for this destination (active, inactive, csr_generated).
               health_state freshly evaluated for all certs with a signed_cert.
        :param List[HealthSnapshotHSMHAGroup] ha_groups: All HSM HA Groups for this
               destination. Empty array if none exist.
        :param List[HealthSnapshotConnection] paths: All paths for this
               destination. Empty array if none exist.
        """
        self.href = href
        self.destination_id = destination_id
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.client_certificates = client_certificates
        self.ha_groups = ha_groups
        self.paths = paths

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DestinationHealthSnapshot':
        """Initialize a DestinationHealthSnapshot object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (destination_id := _dict.get('destination_id')) is not None:
            args['destination_id'] = destination_id
        else:
            raise ValueError('Required property \'destination_id\' not present in DestinationHealthSnapshot JSON')
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in DestinationHealthSnapshot JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        else:
            raise ValueError('Required property \'health_as_of\' not present in DestinationHealthSnapshot JSON')
        if (client_certificates := _dict.get('client_certificates')) is not None:
            args['client_certificates'] = [HealthSnapshotClientCert.from_dict(v) for v in client_certificates]
        else:
            raise ValueError('Required property \'client_certificates\' not present in DestinationHealthSnapshot JSON')
        if (ha_groups := _dict.get('ha_groups')) is not None:
            args['ha_groups'] = [HealthSnapshotHSMHAGroup.from_dict(v) for v in ha_groups]
        else:
            raise ValueError('Required property \'ha_groups\' not present in DestinationHealthSnapshot JSON')
        if (paths := _dict.get('paths')) is not None:
            args['paths'] = [HealthSnapshotConnection.from_dict(v) for v in paths]
        else:
            raise ValueError('Required property \'paths\' not present in DestinationHealthSnapshot JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DestinationHealthSnapshot object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'destination_id') and self.destination_id is not None:
            _dict['destination_id'] = self.destination_id
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'client_certificates') and self.client_certificates is not None:
            client_certificates_list = []
            for v in self.client_certificates:
                if isinstance(v, dict):
                    client_certificates_list.append(v)
                else:
                    client_certificates_list.append(v.to_dict())
            _dict['client_certificates'] = client_certificates_list
        if hasattr(self, 'ha_groups') and self.ha_groups is not None:
            ha_groups_list = []
            for v in self.ha_groups:
                if isinstance(v, dict):
                    ha_groups_list.append(v)
                else:
                    ha_groups_list.append(v.to_dict())
            _dict['ha_groups'] = ha_groups_list
        if hasattr(self, 'paths') and self.paths is not None:
            paths_list = []
            for v in self.paths:
                if isinstance(v, dict):
                    paths_list.append(v)
                else:
                    paths_list.append(v.to_dict())
            _dict['paths'] = paths_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DestinationHealthSnapshot object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DestinationHealthSnapshot') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DestinationHealthSnapshot') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF (point-in-time) health state. Written exclusively by POST …/health and POST
        …/apply:
        - `unknown`: Health check not yet performed, or destination is
        deleting/deletion_failed.
        - `evaluating`: A health check (POST …/health) is in progress. Set on acceptance;
        replaced when the check completes.
        - `in_progress`: An apply operation (POST …/apply) is running. Set on acceptance;
        replaced by the health check result once apply completes (or set to `unknown` on
        failure).
        - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with active
        non-expired Server CA, and ≥1 active non-expired client certificate).
        - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or `degraded`.
        - `degraded`: Some non-`not_configured` HSM HA Groups are `unhealthy`/`unknown`
        AND at least one is `healthy`.
        - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
        `unknown`.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        DEGRADED = 'degraded'
        UNHEALTHY = 'unhealthy'
        NOT_CONFIGURED = 'not_configured'



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


class HSMDestination:
    """
    An HSM Destination resource.

    :param str id: (optional) Destination ID. Immutable. System-managed.
    :param str href: (optional) URL of the destination resource.
    :param str account_id: (optional) IBM Cloud account ID. System-managed. Required
          for account policy setup.
    :param str name: Human-readable display name.
    :param str description: (optional) Optional description. Omitted if not set.
    :param str vendor: HSM vendor. Immutable after creation.
    :param str provisioning_state: Lifecycle state of the destination:
          - `completed`: Destination created and available for configuration. Initial
          state on POST.
          - `deleting`: Hard delete initiated; asynchronous cleanup in progress.
          - `deletion_failed`: Asynchronous delete failed; the destination still exists.
          Retry DELETE to re-initiate.
    :param str health_state: AS OF (point-in-time) health state. Written exclusively
          by POST …/health and POST …/apply:
          - `unknown`: Health check not yet performed, or destination is
          deleting/deletion_failed.
          - `evaluating`: A health check (POST …/health) is in progress. Set on
          acceptance; replaced when the check completes.
          - `in_progress`: An apply operation (POST …/apply) is running. Set on
          acceptance; replaced by the health check result once apply completes (or set to
          `unknown` on failure).
          - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with
          active non-expired Server CA, and ≥1 active non-expired client certificate).
          - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or `degraded`.
          - `degraded`: Some non-`not_configured` HSM HA Groups are `unhealthy`/`unknown`
          AND at least one is `healthy`.
          - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
          `unknown`.
    :param datetime health_as_of: Timestamp of the last health evaluation. On
          creation equals `created_at`. Updated only by POST …/health.
    :param datetime created_at: Computed field. When the resource was created.
    :param datetime updated_at: (optional) Computed field. Omitted until first
          update.
    :param str created_by: IAM identity of creator. Computed field.
    :param str updated_by: (optional) IAM identity of last updater. Computed field.
          Omitted until first update.
    """

    def __init__(
        self,
        name: str,
        vendor: str,
        provisioning_state: str,
        health_state: str,
        health_as_of: datetime,
        created_at: datetime,
        created_by: str,
        *,
        id: Optional[str] = None,
        href: Optional[str] = None,
        account_id: Optional[str] = None,
        description: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[str] = None,
    ) -> None:
        """
        Initialize a HSMDestination object.

        :param str name: Human-readable display name.
        :param str vendor: HSM vendor. Immutable after creation.
        :param str provisioning_state: Lifecycle state of the destination:
               - `completed`: Destination created and available for configuration. Initial
               state on POST.
               - `deleting`: Hard delete initiated; asynchronous cleanup in progress.
               - `deletion_failed`: Asynchronous delete failed; the destination still
               exists. Retry DELETE to re-initiate.
        :param str health_state: AS OF (point-in-time) health state. Written
               exclusively by POST …/health and POST …/apply:
               - `unknown`: Health check not yet performed, or destination is
               deleting/deletion_failed.
               - `evaluating`: A health check (POST …/health) is in progress. Set on
               acceptance; replaced when the check completes.
               - `in_progress`: An apply operation (POST …/apply) is running. Set on
               acceptance; replaced by the health check result once apply completes (or
               set to `unknown` on failure).
               - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with
               active non-expired Server CA, and ≥1 active non-expired client
               certificate).
               - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or
               `degraded`.
               - `degraded`: Some non-`not_configured` HSM HA Groups are
               `unhealthy`/`unknown` AND at least one is `healthy`.
               - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
               `unknown`.
        :param datetime health_as_of: Timestamp of the last health evaluation. On
               creation equals `created_at`. Updated only by POST …/health.
        :param datetime created_at: Computed field. When the resource was created.
        :param str created_by: IAM identity of creator. Computed field.
        :param str description: (optional) Optional description. Omitted if not
               set.
        :param datetime updated_at: (optional) Computed field. Omitted until first
               update.
        :param str updated_by: (optional) IAM identity of last updater. Computed
               field. Omitted until first update.
        """
        self.id = id
        self.href = href
        self.account_id = account_id
        self.name = name
        self.description = description
        self.vendor = vendor
        self.provisioning_state = provisioning_state
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMDestination':
        """Initialize a HSMDestination object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in HSMDestination JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (vendor := _dict.get('vendor')) is not None:
            args['vendor'] = vendor
        else:
            raise ValueError('Required property \'vendor\' not present in HSMDestination JSON')
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in HSMDestination JSON')
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in HSMDestination JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        else:
            raise ValueError('Required property \'health_as_of\' not present in HSMDestination JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in HSMDestination JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in HSMDestination JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMDestination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'account_id') and getattr(self, 'account_id') is not None:
            _dict['account_id'] = getattr(self, 'account_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'vendor') and self.vendor is not None:
            _dict['vendor'] = self.vendor
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HSMDestination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMDestination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMDestination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class VendorEnum(str, Enum):
        """
        HSM vendor. Immutable after creation.
        """

        THALES_LUNA = 'thales_luna'


    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the destination:
        - `completed`: Destination created and available for configuration. Initial state
        on POST.
        - `deleting`: Hard delete initiated; asynchronous cleanup in progress.
        - `deletion_failed`: Asynchronous delete failed; the destination still exists.
        Retry DELETE to re-initiate.
        """

        COMPLETED = 'completed'
        DELETING = 'deleting'
        DELETION_FAILED = 'deletion_failed'


    class HealthStateEnum(str, Enum):
        """
        AS OF (point-in-time) health state. Written exclusively by POST …/health and POST
        …/apply:
        - `unknown`: Health check not yet performed, or destination is
        deleting/deletion_failed.
        - `evaluating`: A health check (POST …/health) is in progress. Set on acceptance;
        replaced when the check completes.
        - `in_progress`: An apply operation (POST …/apply) is running. Set on acceptance;
        replaced by the health check result once apply completes (or set to `unknown` on
        failure).
        - `not_configured`: Prerequisites not met (needs ≥1 HA Group, ≥1 path with active
        non-expired Server CA, and ≥1 active non-expired client certificate).
        - `healthy`: All non-`not_configured` HSM HA Groups are `healthy` or `degraded`.
        - `degraded`: Some non-`not_configured` HSM HA Groups are `unhealthy`/`unknown`
        AND at least one is `healthy`.
        - `unhealthy`: All non-`not_configured` HSM HA Groups are `unhealthy` or
        `unknown`.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        DEGRADED = 'degraded'
        UNHEALTHY = 'unhealthy'
        NOT_CONFIGURED = 'not_configured'



class HSMDestinationCollection:
    """
    A collection of HSM Destinations.

    :param int total_count: Total number of HSM Destinations in the collection.
    :param List[HSMDestination] hsm_destinations: The list of HSM Destinations. At
          most 5 destinations may exist per SM instance.
    """

    def __init__(
        self,
        total_count: int,
        hsm_destinations: List['HSMDestination'],
    ) -> None:
        """
        Initialize a HSMDestinationCollection object.

        :param int total_count: Total number of HSM Destinations in the collection.
        :param List[HSMDestination] hsm_destinations: The list of HSM Destinations.
               At most 5 destinations may exist per SM instance.
        """
        self.total_count = total_count
        self.hsm_destinations = hsm_destinations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMDestinationCollection':
        """Initialize a HSMDestinationCollection object from a json dictionary."""
        args = {}
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in HSMDestinationCollection JSON')
        if (hsm_destinations := _dict.get('hsm_destinations')) is not None:
            args['hsm_destinations'] = [HSMDestination.from_dict(v) for v in hsm_destinations]
        else:
            raise ValueError('Required property \'hsm_destinations\' not present in HSMDestinationCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMDestinationCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'hsm_destinations') and self.hsm_destinations is not None:
            hsm_destinations_list = []
            for v in self.hsm_destinations:
                if isinstance(v, dict):
                    hsm_destinations_list.append(v)
                else:
                    hsm_destinations_list.append(v.to_dict())
            _dict['hsm_destinations'] = hsm_destinations_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HSMDestinationCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMDestinationCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMDestinationCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HSMDestinationPatch:
    """
    Fields to update on the HSM Destination. Only supplied fields are changed (merge-patch
    semantics).

    :param str name: (optional) Updated display name for the destination.
    :param str description: (optional) Updated description for the destination. Set
          to empty string to clear.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a HSMDestinationPatch object.

        :param str name: (optional) Updated display name for the destination.
        :param str description: (optional) Updated description for the destination.
               Set to empty string to clear.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMDestinationPatch':
        """Initialize a HSMDestinationPatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMDestinationPatch object from a json dictionary."""
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
        """Return a `str` version of this HSMDestinationPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMDestinationPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMDestinationPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HSMHAGroup:
    """
    An HA Group resource. All fields are top-level — no vendor_config wrapper.

    :param str id: (optional) HA Group ID. Immutable. System-managed.
    :param str href: (optional) URL of the HA Group resource.
    :param str name: Human-readable display name.
    :param str description: (optional) Optional description. Omitted if not set.
    :param str provisioning_state: Lifecycle state of the HA Group:
          - `completed`: HA Group has been created and its config has been staged in the
          HSM config file. Initial and only state.
          **Note:** New values may be added to this enumeration in future API versions.
          Clients MUST handle unknown values gracefully and MUST NOT fail on unrecognised
          states.
    :param str health_state: AS OF health state. Written exclusively by POST
          …/health and POST …/apply:
          - `unknown`: Initial state on creation. No health check has been performed yet.
          - `evaluating`: A health check is in progress for this resource.
          - `in_progress`: An apply operation is running across the destination.
          - `healthy`: Configured AND all member HSM nodes are healthy.
          - `degraded`: Configured AND any one member is unhealthy (but not all).
          - `unhealthy`: Configured AND all members are unhealthy or unknown.
          - `not_configured`: Prerequisites not met (destination needs ≥1 path with active
          non-expired Server CA AND ≥1 active non-expired client certificate).
    :param datetime health_as_of: Timestamp of the last health evaluation. On
          creation equals `created_at`. Updated only by POST …/health.
    :param str group_label: HA Group virtual token label. Immutable after creation.
    :param str group_serial: HA Group serial number. Immutable after creation.
    :param List[str] member_serials: Ordered list of HSM node member serial numbers
          for this HA Group. Max 100 unique members.
    :param datetime created_at: Computed field.
    :param datetime updated_at: (optional) Computed field. Omitted until first
          update.
    :param str created_by: Computed field.
    :param str updated_by: (optional) Computed field. Omitted until first update.
    """

    def __init__(
        self,
        name: str,
        provisioning_state: str,
        health_state: str,
        health_as_of: datetime,
        group_label: str,
        group_serial: str,
        member_serials: List[str],
        created_at: datetime,
        created_by: str,
        *,
        id: Optional[str] = None,
        href: Optional[str] = None,
        description: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[str] = None,
    ) -> None:
        """
        Initialize a HSMHAGroup object.

        :param str name: Human-readable display name.
        :param str provisioning_state: Lifecycle state of the HA Group:
               - `completed`: HA Group has been created and its config has been staged in
               the HSM config file. Initial and only state.
               **Note:** New values may be added to this enumeration in future API
               versions. Clients MUST handle unknown values gracefully and MUST NOT fail
               on unrecognised states.
        :param str health_state: AS OF health state. Written exclusively by POST
               …/health and POST …/apply:
               - `unknown`: Initial state on creation. No health check has been performed
               yet.
               - `evaluating`: A health check is in progress for this resource.
               - `in_progress`: An apply operation is running across the destination.
               - `healthy`: Configured AND all member HSM nodes are healthy.
               - `degraded`: Configured AND any one member is unhealthy (but not all).
               - `unhealthy`: Configured AND all members are unhealthy or unknown.
               - `not_configured`: Prerequisites not met (destination needs ≥1 path with
               active non-expired Server CA AND ≥1 active non-expired client certificate).
        :param datetime health_as_of: Timestamp of the last health evaluation. On
               creation equals `created_at`. Updated only by POST …/health.
        :param str group_label: HA Group virtual token label. Immutable after
               creation.
        :param str group_serial: HA Group serial number. Immutable after creation.
        :param List[str] member_serials: Ordered list of HSM node member serial
               numbers for this HA Group. Max 100 unique members.
        :param datetime created_at: Computed field.
        :param str created_by: Computed field.
        :param str description: (optional) Optional description. Omitted if not
               set.
        :param datetime updated_at: (optional) Computed field. Omitted until first
               update.
        :param str updated_by: (optional) Computed field. Omitted until first
               update.
        """
        self.id = id
        self.href = href
        self.name = name
        self.description = description
        self.provisioning_state = provisioning_state
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.group_label = group_label
        self.group_serial = group_serial
        self.member_serials = member_serials
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMHAGroup':
        """Initialize a HSMHAGroup object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in HSMHAGroup JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in HSMHAGroup JSON')
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in HSMHAGroup JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        else:
            raise ValueError('Required property \'health_as_of\' not present in HSMHAGroup JSON')
        if (group_label := _dict.get('group_label')) is not None:
            args['group_label'] = group_label
        else:
            raise ValueError('Required property \'group_label\' not present in HSMHAGroup JSON')
        if (group_serial := _dict.get('group_serial')) is not None:
            args['group_serial'] = group_serial
        else:
            raise ValueError('Required property \'group_serial\' not present in HSMHAGroup JSON')
        if (member_serials := _dict.get('member_serials')) is not None:
            args['member_serials'] = member_serials
        else:
            raise ValueError('Required property \'member_serials\' not present in HSMHAGroup JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in HSMHAGroup JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in HSMHAGroup JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMHAGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'group_label') and self.group_label is not None:
            _dict['group_label'] = self.group_label
        if hasattr(self, 'group_serial') and self.group_serial is not None:
            _dict['group_serial'] = self.group_serial
        if hasattr(self, 'member_serials') and self.member_serials is not None:
            _dict['member_serials'] = self.member_serials
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HSMHAGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMHAGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMHAGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the HA Group:
        - `completed`: HA Group has been created and its config has been staged in the HSM
        config file. Initial and only state.
        **Note:** New values may be added to this enumeration in future API versions.
        Clients MUST handle unknown values gracefully and MUST NOT fail on unrecognised
        states.
        """

        COMPLETED = 'completed'


    class HealthStateEnum(str, Enum):
        """
        AS OF health state. Written exclusively by POST …/health and POST …/apply:
        - `unknown`: Initial state on creation. No health check has been performed yet.
        - `evaluating`: A health check is in progress for this resource.
        - `in_progress`: An apply operation is running across the destination.
        - `healthy`: Configured AND all member HSM nodes are healthy.
        - `degraded`: Configured AND any one member is unhealthy (but not all).
        - `unhealthy`: Configured AND all members are unhealthy or unknown.
        - `not_configured`: Prerequisites not met (destination needs ≥1 path with active
        non-expired Server CA AND ≥1 active non-expired client certificate).
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        DEGRADED = 'degraded'
        UNHEALTHY = 'unhealthy'
        NOT_CONFIGURED = 'not_configured'



class HSMHAGroupCollection:
    """
    A collection of HSM HA Groups.

    :param List[HSMHAGroup] ha_groups: HSM HA Groups for this destination. At most
          20 HSM HA Groups may exist per destination.
    """

    def __init__(
        self,
        ha_groups: List['HSMHAGroup'],
    ) -> None:
        """
        Initialize a HSMHAGroupCollection object.

        :param List[HSMHAGroup] ha_groups: HSM HA Groups for this destination. At
               most 20 HSM HA Groups may exist per destination.
        """
        self.ha_groups = ha_groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMHAGroupCollection':
        """Initialize a HSMHAGroupCollection object from a json dictionary."""
        args = {}
        if (ha_groups := _dict.get('ha_groups')) is not None:
            args['ha_groups'] = [HSMHAGroup.from_dict(v) for v in ha_groups]
        else:
            raise ValueError('Required property \'ha_groups\' not present in HSMHAGroupCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMHAGroupCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ha_groups') and self.ha_groups is not None:
            ha_groups_list = []
            for v in self.ha_groups:
                if isinstance(v, dict):
                    ha_groups_list.append(v)
                else:
                    ha_groups_list.append(v.to_dict())
            _dict['ha_groups'] = ha_groups_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HSMHAGroupCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMHAGroupCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMHAGroupCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HSMHAGroupPatch:
    """
    Request body for updating an HA Group. group_serial and group_label are immutable —
    return 400 if supplied. If name is omitted, existing name is preserved (merge-patch
    semantics). name cannot be set to null. HSM Config File is staged when member_serials
    is changed.

    :param str name: (optional) Updated display name for the HA Group.
    :param str description: (optional) Updated description for the HA Group. Set to
          empty string to clear.
    :param List[str] member_serials: (optional) Update the member serial list. At
          least one entry required if supplied. Max 100 unique serials. Stages HSM config
          file change.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        member_serials: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a HSMHAGroupPatch object.

        :param str name: (optional) Updated display name for the HA Group.
        :param str description: (optional) Updated description for the HA Group.
               Set to empty string to clear.
        :param List[str] member_serials: (optional) Update the member serial list.
               At least one entry required if supplied. Max 100 unique serials. Stages HSM
               config file change.
        """
        self.name = name
        self.description = description
        self.member_serials = member_serials

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMHAGroupPatch':
        """Initialize a HSMHAGroupPatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (member_serials := _dict.get('member_serials')) is not None:
            args['member_serials'] = member_serials
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMHAGroupPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'member_serials') and self.member_serials is not None:
            _dict['member_serials'] = self.member_serials
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HSMHAGroupPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMHAGroupPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMHAGroupPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HSMPathReset:
    """
    Response body for POST .../paths/{path_id}/reset.

    :param str href: (optional) URL of the path resource.
    :param str provisioning_state: Lifecycle state of the path:
          - `pending_server_ca`: Path created. Waiting for a Server CA to be added and
          activated.
          - `pending_account_policy`: Server CA active. Customer must review and confirm
          the Secrets Manager account policy for the gateway before proceeding.
          - `provisioning`: Connectivity setup in progress (async). Triggered by POST
          /build.
          - `pending_approval`: Connectivity created. Waiting for customer approval.
          - `completed`: Connectivity established. Path fully operational.
          - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset then
          retry POST /build.
          - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is already
          in use by another Secrets Manager instance in the same region. Obtain a new CRN
          and update via PATCH, then call POST /reset.
          - `approval_declined`: Customer declined the pending approval. Call POST /reset.
          - `deleting`: Delete initiated; async cleanup in progress.
          - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
    """

    def __init__(
        self,
        provisioning_state: str,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a HSMPathReset object.

        :param str provisioning_state: Lifecycle state of the path:
               - `pending_server_ca`: Path created. Waiting for a Server CA to be added
               and activated.
               - `pending_account_policy`: Server CA active. Customer must review and
               confirm the Secrets Manager account policy for the gateway before
               proceeding.
               - `provisioning`: Connectivity setup in progress (async). Triggered by POST
               /build.
               - `pending_approval`: Connectivity created. Waiting for customer approval.
               - `completed`: Connectivity established. Path fully operational.
               - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset
               then retry POST /build.
               - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is
               already in use by another Secrets Manager instance in the same region.
               Obtain a new CRN and update via PATCH, then call POST /reset.
               - `approval_declined`: Customer declined the pending approval. Call POST
               /reset.
               - `deleting`: Delete initiated; async cleanup in progress.
               - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
        """
        self.href = href
        self.provisioning_state = provisioning_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HSMPathReset':
        """Initialize a HSMPathReset object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in HSMPathReset JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HSMPathReset object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HSMPathReset object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HSMPathReset') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HSMPathReset') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the path:
        - `pending_server_ca`: Path created. Waiting for a Server CA to be added and
        activated.
        - `pending_account_policy`: Server CA active. Customer must review and confirm the
        Secrets Manager account policy for the gateway before proceeding.
        - `provisioning`: Connectivity setup in progress (async). Triggered by POST
        /build.
        - `pending_approval`: Connectivity created. Waiting for customer approval.
        - `completed`: Connectivity established. Path fully operational.
        - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset then
        retry POST /build.
        - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is already in
        use by another Secrets Manager instance in the same region. Obtain a new CRN and
        update via PATCH, then call POST /reset.
        - `approval_declined`: Customer declined the pending approval. Call POST /reset.
        - `deleting`: Delete initiated; async cleanup in progress.
        - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
        """

        PENDING_SERVER_CA = 'pending_server_ca'
        PENDING_ACCOUNT_POLICY = 'pending_account_policy'
        PROVISIONING = 'provisioning'
        PENDING_APPROVAL = 'pending_approval'
        COMPLETED = 'completed'
        VPE_PROVISIONING_FAILED = 'vpe_provisioning_failed'
        CRN_ALREADY_IN_USE = 'crn_already_in_use'
        APPROVAL_DECLINED = 'approval_declined'
        DELETING = 'deleting'
        DELETION_FAILED = 'deletion_failed'



class HealthSnapshotClientCert:
    """
    Client certificate summary within a DestinationHealthSnapshot.

    :param str id: Client certificate ID.
    :param str name: (optional) Human-readable display name.
    :param str health_state: AS OF health state of the client certificate. Written
          exclusively by POST …/health:
          - `unknown`: Initial state on creation, and for csr_generated certs with no
          signed_cert.
          - `evaluating`: A health check is in progress for this client certificate.
          - `valid`: Certificate is within its validity period (expires_at is in the
          future).
          - `expired`: Certificate has passed its expires_at date.
    """

    def __init__(
        self,
        id: str,
        health_state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a HealthSnapshotClientCert object.

        :param str id: Client certificate ID.
        :param str health_state: AS OF health state of the client certificate.
               Written exclusively by POST …/health:
               - `unknown`: Initial state on creation, and for csr_generated certs with no
               signed_cert.
               - `evaluating`: A health check is in progress for this client certificate.
               - `valid`: Certificate is within its validity period (expires_at is in the
               future).
               - `expired`: Certificate has passed its expires_at date.
        :param str name: (optional) Human-readable display name.
        """
        self.id = id
        self.name = name
        self.health_state = health_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthSnapshotClientCert':
        """Initialize a HealthSnapshotClientCert object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in HealthSnapshotClientCert JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in HealthSnapshotClientCert JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthSnapshotClientCert object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthSnapshotClientCert object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthSnapshotClientCert') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthSnapshotClientCert') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF health state of the client certificate. Written exclusively by POST
        …/health:
        - `unknown`: Initial state on creation, and for csr_generated certs with no
        signed_cert.
        - `evaluating`: A health check is in progress for this client certificate.
        - `valid`: Certificate is within its validity period (expires_at is in the
        future).
        - `expired`: Certificate has passed its expires_at date.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        VALID = 'valid'
        EXPIRED = 'expired'



class HealthSnapshotConnection:
    """
    Path summary within a DestinationHealthSnapshot.

    :param str id: Path ID.
    :param str name: (optional) Human-readable display name.
    :param str health_state: AS OF health state. Written exclusively by POST
          …/health and POST …/apply:
          - `unknown`: Initial state on creation. Health check not yet performed, or path
          is deleting/deletion_failed.
          - `evaluating`: A health check is in progress for this path.
          - `in_progress`: An apply operation is running across the destination.
          - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the active
          Server CA has expired.
          - `not_configured`: Path is not yet provisioned (pending_account_policy,
          provisioning, pending_approval, approval_declined, crn_already_in_use,
          vpe_provisioning_failed) — AND active Server CA is valid. If active CA is
          missing or expired, no_valid_server_ca takes priority.
          - `healthy`: Active Server CA valid AND connectivity check to the HSM succeeded.
          - `unhealthy`: Active Server CA valid AND connectivity check to the HSM failed.
    :param List[HealthSnapshotServerCa] server_cas: All Server CAs for this path
          (active and inactive). Empty array if none.
    """

    def __init__(
        self,
        id: str,
        health_state: str,
        server_cas: List['HealthSnapshotServerCa'],
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a HealthSnapshotConnection object.

        :param str id: Path ID.
        :param str health_state: AS OF health state. Written exclusively by POST
               …/health and POST …/apply:
               - `unknown`: Initial state on creation. Health check not yet performed, or
               path is deleting/deletion_failed.
               - `evaluating`: A health check is in progress for this path.
               - `in_progress`: An apply operation is running across the destination.
               - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the
               active Server CA has expired.
               - `not_configured`: Path is not yet provisioned (pending_account_policy,
               provisioning, pending_approval, approval_declined, crn_already_in_use,
               vpe_provisioning_failed) — AND active Server CA is valid. If active CA is
               missing or expired, no_valid_server_ca takes priority.
               - `healthy`: Active Server CA valid AND connectivity check to the HSM
               succeeded.
               - `unhealthy`: Active Server CA valid AND connectivity check to the HSM
               failed.
        :param List[HealthSnapshotServerCa] server_cas: All Server CAs for this
               path (active and inactive). Empty array if none.
        :param str name: (optional) Human-readable display name.
        """
        self.id = id
        self.name = name
        self.health_state = health_state
        self.server_cas = server_cas

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthSnapshotConnection':
        """Initialize a HealthSnapshotConnection object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in HealthSnapshotConnection JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in HealthSnapshotConnection JSON')
        if (server_cas := _dict.get('server_cas')) is not None:
            args['server_cas'] = [HealthSnapshotServerCa.from_dict(v) for v in server_cas]
        else:
            raise ValueError('Required property \'server_cas\' not present in HealthSnapshotConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthSnapshotConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'server_cas') and self.server_cas is not None:
            server_cas_list = []
            for v in self.server_cas:
                if isinstance(v, dict):
                    server_cas_list.append(v)
                else:
                    server_cas_list.append(v.to_dict())
            _dict['server_cas'] = server_cas_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthSnapshotConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthSnapshotConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthSnapshotConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF health state. Written exclusively by POST …/health and POST …/apply:
        - `unknown`: Initial state on creation. Health check not yet performed, or path is
        deleting/deletion_failed.
        - `evaluating`: A health check is in progress for this path.
        - `in_progress`: An apply operation is running across the destination.
        - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the active
        Server CA has expired.
        - `not_configured`: Path is not yet provisioned (pending_account_policy,
        provisioning, pending_approval, approval_declined, crn_already_in_use,
        vpe_provisioning_failed) — AND active Server CA is valid. If active CA is missing
        or expired, no_valid_server_ca takes priority.
        - `healthy`: Active Server CA valid AND connectivity check to the HSM succeeded.
        - `unhealthy`: Active Server CA valid AND connectivity check to the HSM failed.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        UNHEALTHY = 'unhealthy'
        NO_VALID_SERVER_CA = 'no_valid_server_ca'
        NOT_CONFIGURED = 'not_configured'



class HealthSnapshotHSMHAGroup:
    """
    HA Group summary within a DestinationHealthSnapshot.

    :param str id: HA Group ID.
    :param str name: (optional) Human-readable display name.
    :param str health_state: AS OF health state. Written exclusively by POST
          …/health and POST …/apply:
          - `unknown`: Initial state on creation. No health check has been performed yet.
          - `evaluating`: A health check is in progress for this resource.
          - `in_progress`: An apply operation is running across the destination.
          - `healthy`: Configured AND all member HSM nodes are healthy.
          - `degraded`: Configured AND any one member is unhealthy (but not all).
          - `unhealthy`: Configured AND all members are unhealthy or unknown.
          - `not_configured`: Prerequisites not met (destination needs ≥1 path with active
          non-expired Server CA AND ≥1 active non-expired client certificate).
    """

    def __init__(
        self,
        id: str,
        health_state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a HealthSnapshotHSMHAGroup object.

        :param str id: HA Group ID.
        :param str health_state: AS OF health state. Written exclusively by POST
               …/health and POST …/apply:
               - `unknown`: Initial state on creation. No health check has been performed
               yet.
               - `evaluating`: A health check is in progress for this resource.
               - `in_progress`: An apply operation is running across the destination.
               - `healthy`: Configured AND all member HSM nodes are healthy.
               - `degraded`: Configured AND any one member is unhealthy (but not all).
               - `unhealthy`: Configured AND all members are unhealthy or unknown.
               - `not_configured`: Prerequisites not met (destination needs ≥1 path with
               active non-expired Server CA AND ≥1 active non-expired client certificate).
        :param str name: (optional) Human-readable display name.
        """
        self.id = id
        self.name = name
        self.health_state = health_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthSnapshotHSMHAGroup':
        """Initialize a HealthSnapshotHSMHAGroup object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in HealthSnapshotHSMHAGroup JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in HealthSnapshotHSMHAGroup JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthSnapshotHSMHAGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthSnapshotHSMHAGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthSnapshotHSMHAGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthSnapshotHSMHAGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF health state. Written exclusively by POST …/health and POST …/apply:
        - `unknown`: Initial state on creation. No health check has been performed yet.
        - `evaluating`: A health check is in progress for this resource.
        - `in_progress`: An apply operation is running across the destination.
        - `healthy`: Configured AND all member HSM nodes are healthy.
        - `degraded`: Configured AND any one member is unhealthy (but not all).
        - `unhealthy`: Configured AND all members are unhealthy or unknown.
        - `not_configured`: Prerequisites not met (destination needs ≥1 path with active
        non-expired Server CA AND ≥1 active non-expired client certificate).
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        DEGRADED = 'degraded'
        UNHEALTHY = 'unhealthy'
        NOT_CONFIGURED = 'not_configured'



class HealthSnapshotServerCa:
    """
    Server CA summary within a HealthSnapshotConnection.

    :param str id: Server CA ID.
    :param str name: (optional) Human-readable display name.
    :param str health_state: AS OF health state of the Server CA certificate.
          Written exclusively by POST …/health:
          - `unknown`: Initial state on creation. Health check not yet performed.
          - `evaluating`: A health check is in progress for this Server CA.
          - `valid`: Certificate is within its validity period (expires_at is in the
          future).
          - `expired`: Certificate has passed its expires_at date.
    """

    def __init__(
        self,
        id: str,
        health_state: str,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a HealthSnapshotServerCa object.

        :param str id: Server CA ID.
        :param str health_state: AS OF health state of the Server CA certificate.
               Written exclusively by POST …/health:
               - `unknown`: Initial state on creation. Health check not yet performed.
               - `evaluating`: A health check is in progress for this Server CA.
               - `valid`: Certificate is within its validity period (expires_at is in the
               future).
               - `expired`: Certificate has passed its expires_at date.
        :param str name: (optional) Human-readable display name.
        """
        self.id = id
        self.name = name
        self.health_state = health_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthSnapshotServerCa':
        """Initialize a HealthSnapshotServerCa object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in HealthSnapshotServerCa JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in HealthSnapshotServerCa JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthSnapshotServerCa object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthSnapshotServerCa object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthSnapshotServerCa') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthSnapshotServerCa') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF health state of the Server CA certificate. Written exclusively by POST
        …/health:
        - `unknown`: Initial state on creation. Health check not yet performed.
        - `evaluating`: A health check is in progress for this Server CA.
        - `valid`: Certificate is within its validity period (expires_at is in the
        future).
        - `expired`: Certificate has passed its expires_at date.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        VALID = 'valid'
        EXPIRED = 'expired'



class IbmCloudDatabaseDestination:
    """
    A destination resource representing a private network link to an IBM Cloud Database
    service instance on a Vault Dedicated cluster.

    :param str id: A standard UUID string (RFC 4122).
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

        :param str id: A standard UUID string (RFC 4122).
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

    :param str id: A standard UUID string (RFC 4122).
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

        :param str id: A standard UUID string (RFC 4122).
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



class Path:
    """
    A path resource. crn is a top-level field — no vendor_config wrapper. Paths are
    independent of HSM HA Groups. crn is immutable after creation.

    :param str id: (optional) Path ID. Immutable. System-managed.
    :param str href: (optional) URL of the path resource.
    :param str name: Human-readable display name.
    :param str description: (optional) Optional description. Omitted if not set.
    :param str crn: CRN of the gateway through which the HSM is reached. Immutable.
    :param str provisioning_state: Lifecycle state of the path:
          - `pending_server_ca`: Path created. Waiting for a Server CA to be added and
          activated.
          - `pending_account_policy`: Server CA active. Customer must review and confirm
          the Secrets Manager account policy for the gateway before proceeding.
          - `provisioning`: Connectivity setup in progress (async). Triggered by POST
          /build.
          - `pending_approval`: Connectivity created. Waiting for customer approval.
          - `completed`: Connectivity established. Path fully operational.
          - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset then
          retry POST /build.
          - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is already
          in use by another Secrets Manager instance in the same region. Obtain a new CRN
          and update via PATCH, then call POST /reset.
          - `approval_declined`: Customer declined the pending approval. Call POST /reset.
          - `deleting`: Delete initiated; async cleanup in progress.
          - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
    :param str health_state: AS OF health state. Written exclusively by POST
          …/health and POST …/apply:
          - `unknown`: Initial state on creation. Health check not yet performed, or path
          is deleting/deletion_failed.
          - `evaluating`: A health check is in progress for this path.
          - `in_progress`: An apply operation is running across the destination.
          - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the active
          Server CA has expired.
          - `not_configured`: Path is not yet provisioned (pending_account_policy,
          provisioning, pending_approval, approval_declined, crn_already_in_use,
          vpe_provisioning_failed) — AND active Server CA is valid. If active CA is
          missing or expired, no_valid_server_ca takes priority.
          - `healthy`: Active Server CA valid AND connectivity check to the HSM succeeded.
          - `unhealthy`: Active Server CA valid AND connectivity check to the HSM failed.
    :param datetime health_as_of: Timestamp of the last health evaluation. On
          creation equals `created_at`. Updated only by POST …/health.
    :param datetime created_at: Computed field.
    :param datetime updated_at: (optional) Computed field. Omitted until first
          update.
    :param str created_by: Computed field.
    :param str updated_by: (optional) Computed field. Omitted until first update.
    """

    def __init__(
        self,
        name: str,
        crn: str,
        provisioning_state: str,
        health_state: str,
        health_as_of: datetime,
        created_at: datetime,
        created_by: str,
        *,
        id: Optional[str] = None,
        href: Optional[str] = None,
        description: Optional[str] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[str] = None,
    ) -> None:
        """
        Initialize a Path object.

        :param str name: Human-readable display name.
        :param str crn: CRN of the gateway through which the HSM is reached.
               Immutable.
        :param str provisioning_state: Lifecycle state of the path:
               - `pending_server_ca`: Path created. Waiting for a Server CA to be added
               and activated.
               - `pending_account_policy`: Server CA active. Customer must review and
               confirm the Secrets Manager account policy for the gateway before
               proceeding.
               - `provisioning`: Connectivity setup in progress (async). Triggered by POST
               /build.
               - `pending_approval`: Connectivity created. Waiting for customer approval.
               - `completed`: Connectivity established. Path fully operational.
               - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset
               then retry POST /build.
               - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is
               already in use by another Secrets Manager instance in the same region.
               Obtain a new CRN and update via PATCH, then call POST /reset.
               - `approval_declined`: Customer declined the pending approval. Call POST
               /reset.
               - `deleting`: Delete initiated; async cleanup in progress.
               - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
        :param str health_state: AS OF health state. Written exclusively by POST
               …/health and POST …/apply:
               - `unknown`: Initial state on creation. Health check not yet performed, or
               path is deleting/deletion_failed.
               - `evaluating`: A health check is in progress for this path.
               - `in_progress`: An apply operation is running across the destination.
               - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the
               active Server CA has expired.
               - `not_configured`: Path is not yet provisioned (pending_account_policy,
               provisioning, pending_approval, approval_declined, crn_already_in_use,
               vpe_provisioning_failed) — AND active Server CA is valid. If active CA is
               missing or expired, no_valid_server_ca takes priority.
               - `healthy`: Active Server CA valid AND connectivity check to the HSM
               succeeded.
               - `unhealthy`: Active Server CA valid AND connectivity check to the HSM
               failed.
        :param datetime health_as_of: Timestamp of the last health evaluation. On
               creation equals `created_at`. Updated only by POST …/health.
        :param datetime created_at: Computed field.
        :param str created_by: Computed field.
        :param str description: (optional) Optional description. Omitted if not
               set.
        :param datetime updated_at: (optional) Computed field. Omitted until first
               update.
        :param str updated_by: (optional) Computed field. Omitted until first
               update.
        """
        self.id = id
        self.href = href
        self.name = name
        self.description = description
        self.crn = crn
        self.provisioning_state = provisioning_state
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Path':
        """Initialize a Path object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Path JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in Path JSON')
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in Path JSON')
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in Path JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        else:
            raise ValueError('Required property \'health_as_of\' not present in Path JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in Path JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in Path JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Path object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Path object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Path') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Path') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the path:
        - `pending_server_ca`: Path created. Waiting for a Server CA to be added and
        activated.
        - `pending_account_policy`: Server CA active. Customer must review and confirm the
        Secrets Manager account policy for the gateway before proceeding.
        - `provisioning`: Connectivity setup in progress (async). Triggered by POST
        /build.
        - `pending_approval`: Connectivity created. Waiting for customer approval.
        - `completed`: Connectivity established. Path fully operational.
        - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset then
        retry POST /build.
        - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is already in
        use by another Secrets Manager instance in the same region. Obtain a new CRN and
        update via PATCH, then call POST /reset.
        - `approval_declined`: Customer declined the pending approval. Call POST /reset.
        - `deleting`: Delete initiated; async cleanup in progress.
        - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
        """

        PENDING_SERVER_CA = 'pending_server_ca'
        PENDING_ACCOUNT_POLICY = 'pending_account_policy'
        PROVISIONING = 'provisioning'
        PENDING_APPROVAL = 'pending_approval'
        COMPLETED = 'completed'
        VPE_PROVISIONING_FAILED = 'vpe_provisioning_failed'
        CRN_ALREADY_IN_USE = 'crn_already_in_use'
        APPROVAL_DECLINED = 'approval_declined'
        DELETING = 'deleting'
        DELETION_FAILED = 'deletion_failed'


    class HealthStateEnum(str, Enum):
        """
        AS OF health state. Written exclusively by POST …/health and POST …/apply:
        - `unknown`: Initial state on creation. Health check not yet performed, or path is
        deleting/deletion_failed.
        - `evaluating`: A health check is in progress for this path.
        - `in_progress`: An apply operation is running across the destination.
        - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the active
        Server CA has expired.
        - `not_configured`: Path is not yet provisioned (pending_account_policy,
        provisioning, pending_approval, approval_declined, crn_already_in_use,
        vpe_provisioning_failed) — AND active Server CA is valid. If active CA is missing
        or expired, no_valid_server_ca takes priority.
        - `healthy`: Active Server CA valid AND connectivity check to the HSM succeeded.
        - `unhealthy`: Active Server CA valid AND connectivity check to the HSM failed.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        UNHEALTHY = 'unhealthy'
        NO_VALID_SERVER_CA = 'no_valid_server_ca'
        NOT_CONFIGURED = 'not_configured'



class PathCollection:
    """
    A collection of paths.

    :param List[Path] paths: Paths for this destination. At most 20 paths may exist
          per destination.
    """

    def __init__(
        self,
        paths: List['Path'],
    ) -> None:
        """
        Initialize a PathCollection object.

        :param List[Path] paths: Paths for this destination. At most 20 paths may
               exist per destination.
        """
        self.paths = paths

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PathCollection':
        """Initialize a PathCollection object from a json dictionary."""
        args = {}
        if (paths := _dict.get('paths')) is not None:
            args['paths'] = [Path.from_dict(v) for v in paths]
        else:
            raise ValueError('Required property \'paths\' not present in PathCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PathCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'paths') and self.paths is not None:
            paths_list = []
            for v in self.paths:
                if isinstance(v, dict):
                    paths_list.append(v)
                else:
                    paths_list.append(v.to_dict())
            _dict['paths'] = paths_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PathCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PathCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PathCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PathPatch:
    """
    Fields to update on the path. Only supplied fields are changed (merge-patch
    semantics).

    :param str name: (optional) Updated display name for the path.
    :param str description: (optional) Updated description for the path. Set to
          empty string to clear.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a PathPatch object.

        :param str name: (optional) Updated display name for the path.
        :param str description: (optional) Updated description for the path. Set to
               empty string to clear.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PathPatch':
        """Initialize a PathPatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PathPatch object from a json dictionary."""
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
        """Return a `str` version of this PathPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PathPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PathPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServerCa:
    """
    A Server CA certificate resource. certificate and expires_at are top-level fields.
    There is no vendor_config wrapper. Only one Server CA can be active per path.
    Constraint: Cannot leave a path with zero active Server CAs if a client certificate is
    already active.

    :param str id: (optional) Server CA ID. Immutable.
    :param str name: Human-readable display name.
    :param str description: (optional) Optional description. Omitted if not set.
    :param str certificate: (optional) PEM-encoded Server CA certificate. Immutable.
    :param datetime expires_at: Expiry parsed from certificate NotAfter field.
          System-managed. Populated on creation.
    :param str status: Only one Server CA can be active per path. Starts inactive on
          creation.
    :param str health_state: AS OF health state of the Server CA certificate.
          Written exclusively by POST …/health:
          - `unknown`: Initial state on creation. Health check not yet performed.
          - `evaluating`: A health check is in progress for this Server CA.
          - `valid`: Certificate is within its validity period (expires_at is in the
          future).
          - `expired`: Certificate has passed its expires_at date.
    :param datetime health_as_of: (optional) Timestamp of the last health
          evaluation. On creation equals `created_at`. Updated only by POST …/health.
    :param datetime created_at: Computed field.
    :param datetime updated_at: (optional) Computed field. Omitted until first
          update.
    :param str created_by: Computed field.
    :param str updated_by: (optional) Computed field. Omitted until first update.
    """

    def __init__(
        self,
        name: str,
        expires_at: datetime,
        status: str,
        health_state: str,
        created_at: datetime,
        created_by: str,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        certificate: Optional[str] = None,
        health_as_of: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[str] = None,
    ) -> None:
        """
        Initialize a ServerCa object.

        :param str name: Human-readable display name.
        :param datetime expires_at: Expiry parsed from certificate NotAfter field.
               System-managed. Populated on creation.
        :param str status: Only one Server CA can be active per path. Starts
               inactive on creation.
        :param str health_state: AS OF health state of the Server CA certificate.
               Written exclusively by POST …/health:
               - `unknown`: Initial state on creation. Health check not yet performed.
               - `evaluating`: A health check is in progress for this Server CA.
               - `valid`: Certificate is within its validity period (expires_at is in the
               future).
               - `expired`: Certificate has passed its expires_at date.
        :param datetime created_at: Computed field.
        :param str created_by: Computed field.
        :param str description: (optional) Optional description. Omitted if not
               set.
        :param str certificate: (optional) PEM-encoded Server CA certificate.
               Immutable.
        :param datetime health_as_of: (optional) Timestamp of the last health
               evaluation. On creation equals `created_at`. Updated only by POST …/health.
        :param datetime updated_at: (optional) Computed field. Omitted until first
               update.
        :param str updated_by: (optional) Computed field. Omitted until first
               update.
        """
        self.id = id
        self.name = name
        self.description = description
        self.certificate = certificate
        self.expires_at = expires_at
        self.status = status
        self.health_state = health_state
        self.health_as_of = health_as_of
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.updated_by = updated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerCa':
        """Initialize a ServerCa object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ServerCa JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (certificate := _dict.get('certificate')) is not None:
            args['certificate'] = certificate
        if (expires_at := _dict.get('expires_at')) is not None:
            args['expires_at'] = string_to_datetime(expires_at)
        else:
            raise ValueError('Required property \'expires_at\' not present in ServerCa JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ServerCa JSON')
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in ServerCa JSON')
        if (health_as_of := _dict.get('health_as_of')) is not None:
            args['health_as_of'] = string_to_datetime(health_as_of)
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in ServerCa JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in ServerCa JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerCa object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate
        if hasattr(self, 'expires_at') and self.expires_at is not None:
            _dict['expires_at'] = datetime_to_string(self.expires_at)
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_as_of') and self.health_as_of is not None:
            _dict['health_as_of'] = datetime_to_string(self.health_as_of)
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServerCa object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerCa') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerCa') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Only one Server CA can be active per path. Starts inactive on creation.
        """

        ACTIVE = 'active'
        INACTIVE = 'inactive'


    class HealthStateEnum(str, Enum):
        """
        AS OF health state of the Server CA certificate. Written exclusively by POST
        …/health:
        - `unknown`: Initial state on creation. Health check not yet performed.
        - `evaluating`: A health check is in progress for this Server CA.
        - `valid`: Certificate is within its validity period (expires_at is in the
        future).
        - `expired`: Certificate has passed its expires_at date.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        VALID = 'valid'
        EXPIRED = 'expired'



class ServerCaCollection:
    """
    A collection of Server CA certificates.

    :param List[ServerCa] server_cas: The list of Server CA certificates for this
          path.
    """

    def __init__(
        self,
        server_cas: List['ServerCa'],
    ) -> None:
        """
        Initialize a ServerCaCollection object.

        :param List[ServerCa] server_cas: The list of Server CA certificates for
               this path.
        """
        self.server_cas = server_cas

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerCaCollection':
        """Initialize a ServerCaCollection object from a json dictionary."""
        args = {}
        if (server_cas := _dict.get('server_cas')) is not None:
            args['server_cas'] = [ServerCa.from_dict(v) for v in server_cas]
        else:
            raise ValueError('Required property \'server_cas\' not present in ServerCaCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerCaCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'server_cas') and self.server_cas is not None:
            server_cas_list = []
            for v in self.server_cas:
                if isinstance(v, dict):
                    server_cas_list.append(v)
                else:
                    server_cas_list.append(v.to_dict())
            _dict['server_cas'] = server_cas_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServerCaCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerCaCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerCaCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServerCaPatch:
    """
    Fields to update on the Server CA. Only supplied fields are changed (merge-patch
    semantics).

    :param str name: (optional) Updated display name for the Server CA.
    :param str description: (optional) Updated description. Set to empty string to
          clear.
    :param str status: (optional) Set to `active` to activate this certificate. Only
          `active` is allowed.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
    ) -> None:
        """
        Initialize a ServerCaPatch object.

        :param str name: (optional) Updated display name for the Server CA.
        :param str description: (optional) Updated description. Set to empty string
               to clear.
        :param str status: (optional) Set to `active` to activate this certificate.
               Only `active` is allowed.
        """
        self.name = name
        self.description = description
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerCaPatch':
        """Initialize a ServerCaPatch object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerCaPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServerCaPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerCaPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerCaPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Set to `active` to activate this certificate. Only `active` is allowed.
        """

        ACTIVE = 'active'



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


class VpeProvisioningResponse:
    """
    Response body for POST .../paths/{path_id}/build (202 Accepted).

    :param str id: (optional) ID of the path being provisioned.
    :param str provisioning_state: Always `provisioning` on a 202 response.
    """

    def __init__(
        self,
        provisioning_state: str,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a VpeProvisioningResponse object.

        :param str provisioning_state: Always `provisioning` on a 202 response.
        """
        self.id = id
        self.provisioning_state = provisioning_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VpeProvisioningResponse':
        """Initialize a VpeProvisioningResponse object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in VpeProvisioningResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VpeProvisioningResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VpeProvisioningResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VpeProvisioningResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VpeProvisioningResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProvisioningStateEnum(str, Enum):
        """
        Always `provisioning` on a 202 response.
        """

        PROVISIONING = 'provisioning'



class VpeStatusResult:
    """
    Response body for POST .../paths/{path_id}/health_check. Reflects the current health
    state and provisioning state of the HSM path.

    :param str health_state: AS OF health state. Written exclusively by POST
          …/health and POST …/apply:
          - `unknown`: Initial state on creation. Health check not yet performed, or path
          is deleting/deletion_failed.
          - `evaluating`: A health check is in progress for this path.
          - `in_progress`: An apply operation is running across the destination.
          - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the active
          Server CA has expired.
          - `not_configured`: Path is not yet provisioned (pending_account_policy,
          provisioning, pending_approval, approval_declined, crn_already_in_use,
          vpe_provisioning_failed) — AND active Server CA is valid. If active CA is
          missing or expired, no_valid_server_ca takes priority.
          - `healthy`: Active Server CA valid AND connectivity check to the HSM succeeded.
          - `unhealthy`: Active Server CA valid AND connectivity check to the HSM failed.
    :param datetime health_time_stamp: RFC 3339 timestamp of the last health
          evaluation.
    :param str provisioning_state: Lifecycle state of the path:
          - `pending_server_ca`: Path created. Waiting for a Server CA to be added and
          activated.
          - `pending_account_policy`: Server CA active. Customer must review and confirm
          the Secrets Manager account policy for the gateway before proceeding.
          - `provisioning`: Connectivity setup in progress (async). Triggered by POST
          /build.
          - `pending_approval`: Connectivity created. Waiting for customer approval.
          - `completed`: Connectivity established. Path fully operational.
          - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset then
          retry POST /build.
          - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is already
          in use by another Secrets Manager instance in the same region. Obtain a new CRN
          and update via PATCH, then call POST /reset.
          - `approval_declined`: Customer declined the pending approval. Call POST /reset.
          - `deleting`: Delete initiated; async cleanup in progress.
          - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
    """

    def __init__(
        self,
        health_state: str,
        health_time_stamp: datetime,
        provisioning_state: str,
    ) -> None:
        """
        Initialize a VpeStatusResult object.

        :param str health_state: AS OF health state. Written exclusively by POST
               …/health and POST …/apply:
               - `unknown`: Initial state on creation. Health check not yet performed, or
               path is deleting/deletion_failed.
               - `evaluating`: A health check is in progress for this path.
               - `in_progress`: An apply operation is running across the destination.
               - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the
               active Server CA has expired.
               - `not_configured`: Path is not yet provisioned (pending_account_policy,
               provisioning, pending_approval, approval_declined, crn_already_in_use,
               vpe_provisioning_failed) — AND active Server CA is valid. If active CA is
               missing or expired, no_valid_server_ca takes priority.
               - `healthy`: Active Server CA valid AND connectivity check to the HSM
               succeeded.
               - `unhealthy`: Active Server CA valid AND connectivity check to the HSM
               failed.
        :param datetime health_time_stamp: RFC 3339 timestamp of the last health
               evaluation.
        :param str provisioning_state: Lifecycle state of the path:
               - `pending_server_ca`: Path created. Waiting for a Server CA to be added
               and activated.
               - `pending_account_policy`: Server CA active. Customer must review and
               confirm the Secrets Manager account policy for the gateway before
               proceeding.
               - `provisioning`: Connectivity setup in progress (async). Triggered by POST
               /build.
               - `pending_approval`: Connectivity created. Waiting for customer approval.
               - `completed`: Connectivity established. Path fully operational.
               - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset
               then retry POST /build.
               - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is
               already in use by another Secrets Manager instance in the same region.
               Obtain a new CRN and update via PATCH, then call POST /reset.
               - `approval_declined`: Customer declined the pending approval. Call POST
               /reset.
               - `deleting`: Delete initiated; async cleanup in progress.
               - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
        """
        self.health_state = health_state
        self.health_time_stamp = health_time_stamp
        self.provisioning_state = provisioning_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VpeStatusResult':
        """Initialize a VpeStatusResult object from a json dictionary."""
        args = {}
        if (health_state := _dict.get('health_state')) is not None:
            args['health_state'] = health_state
        else:
            raise ValueError('Required property \'health_state\' not present in VpeStatusResult JSON')
        if (health_time_stamp := _dict.get('health_time_stamp')) is not None:
            args['health_time_stamp'] = string_to_datetime(health_time_stamp)
        else:
            raise ValueError('Required property \'health_time_stamp\' not present in VpeStatusResult JSON')
        if (provisioning_state := _dict.get('provisioning_state')) is not None:
            args['provisioning_state'] = provisioning_state
        else:
            raise ValueError('Required property \'provisioning_state\' not present in VpeStatusResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VpeStatusResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'health_state') and self.health_state is not None:
            _dict['health_state'] = self.health_state
        if hasattr(self, 'health_time_stamp') and self.health_time_stamp is not None:
            _dict['health_time_stamp'] = datetime_to_string(self.health_time_stamp)
        if hasattr(self, 'provisioning_state') and self.provisioning_state is not None:
            _dict['provisioning_state'] = self.provisioning_state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VpeStatusResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VpeStatusResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VpeStatusResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthStateEnum(str, Enum):
        """
        AS OF health state. Written exclusively by POST …/health and POST …/apply:
        - `unknown`: Initial state on creation. Health check not yet performed, or path is
        deleting/deletion_failed.
        - `evaluating`: A health check is in progress for this path.
        - `in_progress`: An apply operation is running across the destination.
        - `no_valid_server_ca`: Pre-check failed — no Server CA is active, or the active
        Server CA has expired.
        - `not_configured`: Path is not yet provisioned (pending_account_policy,
        provisioning, pending_approval, approval_declined, crn_already_in_use,
        vpe_provisioning_failed) — AND active Server CA is valid. If active CA is missing
        or expired, no_valid_server_ca takes priority.
        - `healthy`: Active Server CA valid AND connectivity check to the HSM succeeded.
        - `unhealthy`: Active Server CA valid AND connectivity check to the HSM failed.
        """

        UNKNOWN = 'unknown'
        EVALUATING = 'evaluating'
        IN_PROGRESS = 'in_progress'
        HEALTHY = 'healthy'
        UNHEALTHY = 'unhealthy'
        NO_VALID_SERVER_CA = 'no_valid_server_ca'
        NOT_CONFIGURED = 'not_configured'


    class ProvisioningStateEnum(str, Enum):
        """
        Lifecycle state of the path:
        - `pending_server_ca`: Path created. Waiting for a Server CA to be added and
        activated.
        - `pending_account_policy`: Server CA active. Customer must review and confirm the
        Secrets Manager account policy for the gateway before proceeding.
        - `provisioning`: Connectivity setup in progress (async). Triggered by POST
        /build.
        - `pending_approval`: Connectivity created. Waiting for customer approval.
        - `completed`: Connectivity established. Path fully operational.
        - `vpe_provisioning_failed`: Connectivity setup failed. Call POST /reset then
        retry POST /build.
        - `crn_already_in_use`: Connectivity setup failed — the gateway CRN is already in
        use by another Secrets Manager instance in the same region. Obtain a new CRN and
        update via PATCH, then call POST /reset.
        - `approval_declined`: Customer declined the pending approval. Call POST /reset.
        - `deleting`: Delete initiated; async cleanup in progress.
        - `deletion_failed`: Async deletion failed. Retry DELETE to re-initiate.
        """

        PENDING_SERVER_CA = 'pending_server_ca'
        PENDING_ACCOUNT_POLICY = 'pending_account_policy'
        PROVISIONING = 'provisioning'
        PENDING_APPROVAL = 'pending_approval'
        COMPLETED = 'completed'
        VPE_PROVISIONING_FAILED = 'vpe_provisioning_failed'
        CRN_ALREADY_IN_USE = 'crn_already_in_use'
        APPROVAL_DECLINED = 'approval_declined'
        DELETING = 'deleting'
        DELETION_FAILED = 'deletion_failed'



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
