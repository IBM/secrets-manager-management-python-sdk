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

# IBM OpenAPI SDK Code Generator Version: 3.113.1-d76630af-20260320-135953

"""
With IBM Cloud® Secrets Manager, you can create, lease, and centrally manage secrets that
are used in IBM Cloud services or your custom-built applications.

API Version: 2.0.0
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


class SecretsManagerControlPlaneV2(BaseService):
    """The secrets-manager-control-plane V2 service."""

    DEFAULT_SERVICE_URL = 'https://us-south.secrets-manager.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'secrets_manager_control_plane'

    PARAMETERIZED_SERVICE_URL = 'https://{region}.secrets-manager.cloud.ibm.com'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'SecretsManagerControlPlaneV2':
        """
        Return a new client for the secrets-manager-control-plane service using the
               specified parameters and external configuration.
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

        :param str region: (optional) No description provided.
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
        Construct a new client for the secrets-manager-control-plane service.

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
        Generate Admin Token.

        Creates a Vault admin token that can be used to authenticate to your Vault
        Enterprise cluster. The admin token grants administrative privileges and should be
        used only for initial setup and cluster management tasks. It is recommended to
        revoke the token as soon as it is no longer needed. A successful request returns a
        new token that is valid for 1 hour.

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

    def delete_api_instance_admintokens(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Revoke Admin Tokens.

        Revokes all active Vault admin tokens in your Vault Enterprise cluster.

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
            operation_id='delete_api_instance_admintokens',
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
    # Endpoints
    #########################

    def get_service_instance_endpoints(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get service instance endpoints.

        Get service instance endpoints: api and vault.

        :param str instance_id: The service instance CRN.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Endpoints` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_service_instance_endpoints',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/api/v1/instances/{instance_id}/endpoints'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Instances
    #########################

    def get_service_instance_details(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get service instance.

        Get service instance metadata + managed Vault cluster state in a single
        control-plane call.

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
            operation_id='get_service_instance_details',
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


class EncryptionInfo:
    """
    Encryption configuration for the instance.

    :param str provider_managed_encryption: The encryption provider type.
    :param str encryption_key_crn: (optional) The CRN of the encryption key.
    """

    def __init__(
        self,
        provider_managed_encryption: str,
        *,
        encryption_key_crn: Optional[str] = None,
    ) -> None:
        """
        Initialize a EncryptionInfo object.

        :param str provider_managed_encryption: The encryption provider type.
        :param str encryption_key_crn: (optional) The CRN of the encryption key.
        """
        self.provider_managed_encryption = provider_managed_encryption
        self.encryption_key_crn = encryption_key_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EncryptionInfo':
        """Initialize a EncryptionInfo object from a json dictionary."""
        args = {}
        if (provider_managed_encryption := _dict.get('provider_managed_encryption')) is not None:
            args['provider_managed_encryption'] = provider_managed_encryption
        else:
            raise ValueError('Required property \'provider_managed_encryption\' not present in EncryptionInfo JSON')
        if (encryption_key_crn := _dict.get('encryption_key_crn')) is not None:
            args['encryption_key_crn'] = encryption_key_crn
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EncryptionInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_managed_encryption') and self.provider_managed_encryption is not None:
            _dict['provider_managed_encryption'] = self.provider_managed_encryption
        if hasattr(self, 'encryption_key_crn') and self.encryption_key_crn is not None:
            _dict['encryption_key_crn'] = self.encryption_key_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EncryptionInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EncryptionInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EncryptionInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProviderManagedEncryptionEnum(str, Enum):
        """
        The encryption provider type.
        """

        PROVIDER_MANAGED_ENCRYPTION = 'provider_managed_encryption'
        KEY_PROTECT = 'key_protect'



class Endpoints:
    """
    Endpoints response.

    :param str plan: The plan of this instance.
    :param PublicEndpoints public_endpoints: Public instance endpoints.
    :param PrivateEndpoints private_endpoints: (optional) Private instance
          endpoints.
    :param EncryptionInfo encryption: Encryption configuration for the instance.
    """

    def __init__(
        self,
        plan: str,
        public_endpoints: 'PublicEndpoints',
        encryption: 'EncryptionInfo',
        *,
        private_endpoints: Optional['PrivateEndpoints'] = None,
    ) -> None:
        """
        Initialize a Endpoints object.

        :param str plan: The plan of this instance.
        :param PublicEndpoints public_endpoints: Public instance endpoints.
        :param EncryptionInfo encryption: Encryption configuration for the
               instance.
        :param PrivateEndpoints private_endpoints: (optional) Private instance
               endpoints.
        """
        self.plan = plan
        self.public_endpoints = public_endpoints
        self.private_endpoints = private_endpoints
        self.encryption = encryption

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Endpoints':
        """Initialize a Endpoints object from a json dictionary."""
        args = {}
        if (plan := _dict.get('plan')) is not None:
            args['plan'] = plan
        else:
            raise ValueError('Required property \'plan\' not present in Endpoints JSON')
        if (public_endpoints := _dict.get('public_endpoints')) is not None:
            args['public_endpoints'] = PublicEndpoints.from_dict(public_endpoints)
        else:
            raise ValueError('Required property \'public_endpoints\' not present in Endpoints JSON')
        if (private_endpoints := _dict.get('private_endpoints')) is not None:
            args['private_endpoints'] = PrivateEndpoints.from_dict(private_endpoints)
        if (encryption := _dict.get('encryption')) is not None:
            args['encryption'] = EncryptionInfo.from_dict(encryption)
        else:
            raise ValueError('Required property \'encryption\' not present in Endpoints JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Endpoints object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan') and self.plan is not None:
            _dict['plan'] = self.plan
        if hasattr(self, 'public_endpoints') and self.public_endpoints is not None:
            if isinstance(self.public_endpoints, dict):
                _dict['public_endpoints'] = self.public_endpoints
            else:
                _dict['public_endpoints'] = self.public_endpoints.to_dict()
        if hasattr(self, 'private_endpoints') and self.private_endpoints is not None:
            if isinstance(self.private_endpoints, dict):
                _dict['private_endpoints'] = self.private_endpoints
            else:
                _dict['private_endpoints'] = self.private_endpoints.to_dict()
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
        """Return a `str` version of this Endpoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Endpoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Endpoints') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PlanEnum(str, Enum):
        """
        The plan of this instance.
        """

        TRIAL = 'trial'
        STANDARD = 'standard'
        VAAS = 'vaas'



class Instance:
    """
    Instance.

    :param VaasInstanceMetadata instance: Instance metadata for VaaS instances.
    :param VaasVaultCluster vault_cluster: Vault cluster information for VaaS
          instances.
    :param VaasInstanceEndpoints endpoints: Instance endpoints for VaaS instances.
    :param VaasInstanceEncryption encryption: Vault encryption configuration for
          VaaS instances.
    """

    def __init__(
        self,
        instance: 'VaasInstanceMetadata',
        vault_cluster: 'VaasVaultCluster',
        endpoints: 'VaasInstanceEndpoints',
        encryption: 'VaasInstanceEncryption',
    ) -> None:
        """
        Initialize a Instance object.

        :param VaasInstanceMetadata instance: Instance metadata for VaaS instances.
        :param VaasVaultCluster vault_cluster: Vault cluster information for VaaS
               instances.
        :param VaasInstanceEndpoints endpoints: Instance endpoints for VaaS
               instances.
        :param VaasInstanceEncryption encryption: Vault encryption configuration
               for VaaS instances.
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
            args['instance'] = VaasInstanceMetadata.from_dict(instance)
        else:
            raise ValueError('Required property \'instance\' not present in Instance JSON')
        if (vault_cluster := _dict.get('vault_cluster')) is not None:
            args['vault_cluster'] = VaasVaultCluster.from_dict(vault_cluster)
        else:
            raise ValueError('Required property \'vault_cluster\' not present in Instance JSON')
        if (endpoints := _dict.get('endpoints')) is not None:
            args['endpoints'] = VaasInstanceEndpoints.from_dict(endpoints)
        else:
            raise ValueError('Required property \'endpoints\' not present in Instance JSON')
        if (encryption := _dict.get('encryption')) is not None:
            args['encryption'] = VaasInstanceEncryption.from_dict(encryption)
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


class PrivateEndpoints:
    """
    Private instance endpoints.

    :param str service_api: (optional) Service API endpoint.
    :param str vault_api: Vault API endpoint.
    """

    def __init__(
        self,
        vault_api: str,
        *,
        service_api: Optional[str] = None,
    ) -> None:
        """
        Initialize a PrivateEndpoints object.

        :param str vault_api: Vault API endpoint.
        :param str service_api: (optional) Service API endpoint.
        """
        self.service_api = service_api
        self.vault_api = vault_api

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrivateEndpoints':
        """Initialize a PrivateEndpoints object from a json dictionary."""
        args = {}
        if (service_api := _dict.get('service_api')) is not None:
            args['service_api'] = service_api
        if (vault_api := _dict.get('vault_api')) is not None:
            args['vault_api'] = vault_api
        else:
            raise ValueError('Required property \'vault_api\' not present in PrivateEndpoints JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrivateEndpoints object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service_api') and self.service_api is not None:
            _dict['service_api'] = self.service_api
        if hasattr(self, 'vault_api') and self.vault_api is not None:
            _dict['vault_api'] = self.vault_api
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrivateEndpoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrivateEndpoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrivateEndpoints') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PublicEndpoints:
    """
    Public instance endpoints.

    :param str service_api: (optional) Service Api endpoint.
    :param str vault_api: Vault Api endpoint.
    """

    def __init__(
        self,
        vault_api: str,
        *,
        service_api: Optional[str] = None,
    ) -> None:
        """
        Initialize a PublicEndpoints object.

        :param str vault_api: Vault Api endpoint.
        :param str service_api: (optional) Service Api endpoint.
        """
        self.service_api = service_api
        self.vault_api = vault_api

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PublicEndpoints':
        """Initialize a PublicEndpoints object from a json dictionary."""
        args = {}
        if (service_api := _dict.get('service_api')) is not None:
            args['service_api'] = service_api
        if (vault_api := _dict.get('vault_api')) is not None:
            args['vault_api'] = vault_api
        else:
            raise ValueError('Required property \'vault_api\' not present in PublicEndpoints JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PublicEndpoints object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service_api') and self.service_api is not None:
            _dict['service_api'] = self.service_api
        if hasattr(self, 'vault_api') and self.vault_api is not None:
            _dict['vault_api'] = self.vault_api
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PublicEndpoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PublicEndpoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PublicEndpoints') -> bool:
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


class VaasEndpointsData:
    """
    Endpoint URLs for accessing the Vault instance.

    :param str vault_api: Vault API endpoint URL.
    :param str vault_ui: Vault UI endpoint URL.
    """

    def __init__(
        self,
        vault_api: str,
        vault_ui: str,
    ) -> None:
        """
        Initialize a VaasEndpointsData object.

        :param str vault_api: Vault API endpoint URL.
        :param str vault_ui: Vault UI endpoint URL.
        """
        self.vault_api = vault_api
        self.vault_ui = vault_ui

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaasEndpointsData':
        """Initialize a VaasEndpointsData object from a json dictionary."""
        args = {}
        if (vault_api := _dict.get('vault_api')) is not None:
            args['vault_api'] = vault_api
        else:
            raise ValueError('Required property \'vault_api\' not present in VaasEndpointsData JSON')
        if (vault_ui := _dict.get('vault_ui')) is not None:
            args['vault_ui'] = vault_ui
        else:
            raise ValueError('Required property \'vault_ui\' not present in VaasEndpointsData JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaasEndpointsData object from a json dictionary."""
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
        """Return a `str` version of this VaasEndpointsData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaasEndpointsData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaasEndpointsData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VaasInstanceEncryption:
    """
    Vault encryption configuration for VaaS instances.

    :param str mode: Vault encryption mode.
    :param str provider: (optional) Vault encryption provider (only present for
          customer_managed mode).
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
        Initialize a VaasInstanceEncryption object.

        :param str mode: Vault encryption mode.
        :param str provider: (optional) Vault encryption provider (only present for
               customer_managed mode).
        :param str key_crn: (optional) Vault encryption key CRN (only present for
               customer_managed mode).
        """
        self.mode = mode
        self.provider = provider
        self.key_crn = key_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaasInstanceEncryption':
        """Initialize a VaasInstanceEncryption object from a json dictionary."""
        args = {}
        if (mode := _dict.get('mode')) is not None:
            args['mode'] = mode
        else:
            raise ValueError('Required property \'mode\' not present in VaasInstanceEncryption JSON')
        if (provider := _dict.get('provider')) is not None:
            args['provider'] = provider
        if (key_crn := _dict.get('key_crn')) is not None:
            args['key_crn'] = key_crn
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaasInstanceEncryption object from a json dictionary."""
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
        """Return a `str` version of this VaasInstanceEncryption object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaasInstanceEncryption') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaasInstanceEncryption') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        Vault encryption mode.
        """

        CUSTOMER_MANAGED = 'customer_managed'
        SERVICE_MANAGED = 'service_managed'


    class ProviderEnum(str, Enum):
        """
        Vault encryption provider (only present for customer_managed mode).
        """

        KEY_PROTECT = 'key_protect'
        HYPER_PROTECT_CRYPTO_SERVICES = 'hyper_protect_crypto_services'



class VaasInstanceEndpoints:
    """
    Instance endpoints for VaaS instances.

    :param VaasEndpointsData public: (optional) Endpoint URLs for accessing the
          Vault instance.
    :param VaasEndpointsData private: Endpoint URLs for accessing the Vault
          instance.
    """

    def __init__(
        self,
        private: 'VaasEndpointsData',
        *,
        public: Optional['VaasEndpointsData'] = None,
    ) -> None:
        """
        Initialize a VaasInstanceEndpoints object.

        :param VaasEndpointsData private: Endpoint URLs for accessing the Vault
               instance.
        :param VaasEndpointsData public: (optional) Endpoint URLs for accessing the
               Vault instance.
        """
        self.public = public
        self.private = private

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaasInstanceEndpoints':
        """Initialize a VaasInstanceEndpoints object from a json dictionary."""
        args = {}
        if (public := _dict.get('public')) is not None:
            args['public'] = VaasEndpointsData.from_dict(public)
        if (private := _dict.get('private')) is not None:
            args['private'] = VaasEndpointsData.from_dict(private)
        else:
            raise ValueError('Required property \'private\' not present in VaasInstanceEndpoints JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaasInstanceEndpoints object from a json dictionary."""
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
        """Return a `str` version of this VaasInstanceEndpoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaasInstanceEndpoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaasInstanceEndpoints') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VaasInstanceMetadata:
    """
    Instance metadata for VaaS instances.

    :param str id: The instance CRN identifier.
    :param VaasInstancePlan plan: Instance plan information.
    """

    def __init__(
        self,
        id: str,
        plan: 'VaasInstancePlan',
    ) -> None:
        """
        Initialize a VaasInstanceMetadata object.

        :param str id: The instance CRN identifier.
        :param VaasInstancePlan plan: Instance plan information.
        """
        self.id = id
        self.plan = plan

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaasInstanceMetadata':
        """Initialize a VaasInstanceMetadata object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in VaasInstanceMetadata JSON')
        if (plan := _dict.get('plan')) is not None:
            args['plan'] = VaasInstancePlan.from_dict(plan)
        else:
            raise ValueError('Required property \'plan\' not present in VaasInstanceMetadata JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaasInstanceMetadata object from a json dictionary."""
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
        """Return a `str` version of this VaasInstanceMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaasInstanceMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaasInstanceMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VaasInstancePlan:
    """
    Instance plan information.

    :param str name: The plan name of this instance.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        Initialize a VaasInstancePlan object.

        :param str name: The plan name of this instance.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaasInstancePlan':
        """Initialize a VaasInstancePlan object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in VaasInstancePlan JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaasInstancePlan object from a json dictionary."""
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
        """Return a `str` version of this VaasInstancePlan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaasInstancePlan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaasInstancePlan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        The plan name of this instance.
        """

        TRIAL = 'trial'
        STANDARD = 'standard'
        VAAS = 'vaas'



class VaasVaultCluster:
    """
    Vault cluster information for VaaS instances.

    :param str status: Vault cluster status.
    :param str version: Vault cluster version.
    """

    def __init__(
        self,
        status: str,
        version: str,
    ) -> None:
        """
        Initialize a VaasVaultCluster object.

        :param str status: Vault cluster status.
        :param str version: Vault cluster version.
        """
        self.status = status
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VaasVaultCluster':
        """Initialize a VaasVaultCluster object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in VaasVaultCluster JSON')
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in VaasVaultCluster JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VaasVaultCluster object from a json dictionary."""
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
        """Return a `str` version of this VaasVaultCluster object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VaasVaultCluster') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VaasVaultCluster') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Vault cluster status.
        """

        ACTIVE = 'active'
        PROVISIONING = 'provisioning'
        FAILED = 'failed'

