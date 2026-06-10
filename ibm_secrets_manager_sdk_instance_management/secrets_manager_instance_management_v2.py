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

# IBM OpenAPI SDK Code Generator Version: 3.114.0-a902401e-20260427-192904

"""
With IBM Cloud® Secrets Manager Instance Management API, you can manage service instances
of the Vault Dedicated plan. Use the API for the following operations:
- Get service instance details including cluster state, endpoints, and key management
service.
- Generate a Vault admin token for authenticating to your Vault Dedicated cluster.
- Revoke all active Vault admin tokens.

API Version: 2.0.0
See: https://cloud.ibm.com/docs/secrets-manager
"""

from enum import Enum
from typing import Dict, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

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

        :param str region: (optional) The region where you provisioned your Vault Dedicated Instance. Available regions: us-south, eu-de, jp-tok
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
        **kwargs,
    ) -> DetailedResponse:
        """
        Generate admin token.

        Generate a Vault admin token for authenticating to your Vault Dedicated cluster.
        The token is valid for 1 hour and grants administrative privileges. Use only for
        initial setup and cluster management, then revoke immediately.

        :param str instance_id: The service instance ID.
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

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v2/instances/{instance_id}/admintokens'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_admintokens(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Revoke admin tokens.

        Revoke all active Vault admin tokens. This immediately invalidates all existing
        admin tokens.

        :param str instance_id: The service instance ID.
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
            operation_id='delete_instance_admintokens',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v2/instances/{instance_id}/admintokens'.format(**path_param_dict)
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

        :param str instance_id: The service instance ID.
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
        url = '/api/v2/instances/{instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class Instance:
    """
    Instance.

    :param VaultDedicatedInstanceMetadata instance: Instance metadata for Vault
          Dedicated instances.
    :param VaultDedicatedCluster vault_cluster: Vault cluster information for Vault
          Dedicated instances.
    :param VaultDedicatedInstanceEndpoints endpoints: Instance endpoints for Vault
          Dedicated instances.
    :param VaultDedicatedInstanceEncryption encryption: Vault encryption
          configuration for Vault Dedicated instances.
    """

    def __init__(
        self,
        instance: 'VaultDedicatedInstanceMetadata',
        vault_cluster: 'VaultDedicatedCluster',
        endpoints: 'VaultDedicatedInstanceEndpoints',
        encryption: 'VaultDedicatedInstanceEncryption',
    ) -> None:
        """
        Initialize a Instance object.

        :param VaultDedicatedInstanceMetadata instance: Instance metadata for Vault
               Dedicated instances.
        :param VaultDedicatedCluster vault_cluster: Vault cluster information for
               Vault Dedicated instances.
        :param VaultDedicatedInstanceEndpoints endpoints: Instance endpoints for
               Vault Dedicated instances.
        :param VaultDedicatedInstanceEncryption encryption: Vault encryption
               configuration for Vault Dedicated instances.
        """
        self.instance = instance
        self.vault_cluster = vault_cluster
        self.endpoints = endpoints
        self.encryption = encryption

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Instance':
        """Initialize a Instance object from a json dictionary."""
        args = {}
        if (instance := _dict.get('instance')) is not None:
            args['instance'] = VaultDedicatedInstanceMetadata.from_dict(instance)
        else:
            raise ValueError('Required property \'instance\' not present in Instance JSON')
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
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Instance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance') and self.instance is not None:
            if isinstance(self.instance, dict):
                _dict['instance'] = self.instance
            else:
                _dict['instance'] = self.instance.to_dict()
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


class Token:
    """
    Admin Token response.

    :param str token: The token value.
    """

    def __init__(
        self,
        token: str,
    ) -> None:
        """
        Initialize a Token object.

        :param str token: The token value.
        """
        self.token = token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Token':
        """Initialize a Token object from a json dictionary."""
        args = {}
        if (token := _dict.get('token')) is not None:
            args['token'] = token
        else:
            raise ValueError('Required property \'token\' not present in Token JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Token object from a json dictionary."""
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
        """Return a `str` version of this Token object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Token') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Token') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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


class VaultDedicatedInstanceMetadata:
    """
    Instance metadata for Vault Dedicated instances.

    :param str id: The instance CRN identifier.
    :param VaultDedicatedInstancePlan plan: Instance plan information.
    """

    def __init__(
        self,
        id: str,
        plan: 'VaultDedicatedInstancePlan',
    ) -> None:
        """
        Initialize a VaultDedicatedInstanceMetadata object.

        :param str id: The instance CRN identifier.
        :param VaultDedicatedInstancePlan plan: Instance plan information.
        """
        self.id = id
        self.plan = plan

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaultDedicatedInstanceMetadata':
        """Initialize a VaultDedicatedInstanceMetadata object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in VaultDedicatedInstanceMetadata JSON')
        if (plan := _dict.get('plan')) is not None:
            args['plan'] = VaultDedicatedInstancePlan.from_dict(plan)
        else:
            raise ValueError('Required property \'plan\' not present in VaultDedicatedInstanceMetadata JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaultDedicatedInstanceMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'plan') and self.plan is not None:
            if isinstance(self.plan, dict):
                _dict['plan'] = self.plan
            else:
                _dict['plan'] = self.plan.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VaultDedicatedInstanceMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaultDedicatedInstanceMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaultDedicatedInstanceMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VaultDedicatedInstancePlan:
    """
    Instance plan information.

    :param str name: The plan name of this instance.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        Initialize a VaultDedicatedInstancePlan object.

        :param str name: The plan name of this instance.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaultDedicatedInstancePlan':
        """Initialize a VaultDedicatedInstancePlan object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in VaultDedicatedInstancePlan JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaultDedicatedInstancePlan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VaultDedicatedInstancePlan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaultDedicatedInstancePlan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaultDedicatedInstancePlan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        The plan name of this instance.
        """

        TRIAL = 'trial'
        STANDARD = 'standard'
        DEDICATED = 'dedicated'

