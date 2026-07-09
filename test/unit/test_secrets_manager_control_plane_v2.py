# -*- coding: utf-8 -*-
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

"""
Unit Tests for SecretsManagerControlPlaneV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud.secrets_manager_control_plane_v2 import *


_service = SecretsManagerControlPlaneV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://us-south.secrets-manager.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


def test_parameterized_url():
    """
    Test formatting the parameterized service URL with the default variable values.
    """
    default_formatted_url = 'https://us-south.secrets-manager.cloud.ibm.com'
    assert SecretsManagerControlPlaneV2.construct_service_url() == default_formatted_url


##############################################################################
# Start of Service: Tokens
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecretsManagerControlPlaneV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecretsManagerControlPlaneV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecretsManagerControlPlaneV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateVaultAdmintoken:
    """
    Test Class for create_vault_admintoken
    """

    @responses.activate
    def test_create_vault_admintoken_all_params(self):
        """
        create_vault_admintoken()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/testString/admintokens')
        mock_response = '{"token": "hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.create_vault_admintoken(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_vault_admintoken_all_params_with_retries(self):
        # Enable retries and run test_create_vault_admintoken_all_params.
        _service.enable_retries()
        self.test_create_vault_admintoken_all_params()

        # Disable retries and run test_create_vault_admintoken_all_params.
        _service.disable_retries()
        self.test_create_vault_admintoken_all_params()

    @responses.activate
    def test_create_vault_admintoken_value_error(self):
        """
        test_create_vault_admintoken_value_error()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/testString/admintokens')
        mock_response = '{"token": "hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_vault_admintoken(**req_copy)

    def test_create_vault_admintoken_value_error_with_retries(self):
        # Enable retries and run test_create_vault_admintoken_value_error.
        _service.enable_retries()
        self.test_create_vault_admintoken_value_error()

        # Disable retries and run test_create_vault_admintoken_value_error.
        _service.disable_retries()
        self.test_create_vault_admintoken_value_error()


class TestDeleteApiInstanceAdmintokens:
    """
    Test Class for delete_api_instance_admintokens
    """

    @responses.activate
    def test_delete_api_instance_admintokens_all_params(self):
        """
        delete_api_instance_admintokens()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/testString/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.delete_api_instance_admintokens(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_api_instance_admintokens_all_params_with_retries(self):
        # Enable retries and run test_delete_api_instance_admintokens_all_params.
        _service.enable_retries()
        self.test_delete_api_instance_admintokens_all_params()

        # Disable retries and run test_delete_api_instance_admintokens_all_params.
        _service.disable_retries()
        self.test_delete_api_instance_admintokens_all_params()

    @responses.activate
    def test_delete_api_instance_admintokens_value_error(self):
        """
        test_delete_api_instance_admintokens_value_error()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/testString/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_api_instance_admintokens(**req_copy)

    def test_delete_api_instance_admintokens_value_error_with_retries(self):
        # Enable retries and run test_delete_api_instance_admintokens_value_error.
        _service.enable_retries()
        self.test_delete_api_instance_admintokens_value_error()

        # Disable retries and run test_delete_api_instance_admintokens_value_error.
        _service.disable_retries()
        self.test_delete_api_instance_admintokens_value_error()


# endregion
##############################################################################
# End of Service: Tokens
##############################################################################

##############################################################################
# Start of Service: Endpoints
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecretsManagerControlPlaneV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecretsManagerControlPlaneV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecretsManagerControlPlaneV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetServiceInstanceEndpoints:
    """
    Test Class for get_service_instance_endpoints
    """

    @responses.activate
    def test_get_service_instance_endpoints_all_params(self):
        """
        get_service_instance_endpoints()
        """
        # Set up mock
        url = preprocess_url('/api/v1/instances/testString/endpoints')
        mock_response = '{"plan": "trial", "public_endpoints": {"service_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/api", "vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud"}, "private_endpoints": {"service_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud/api", "vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud"}, "encryption": {"provider_managed_encryption": "key_protect", "encryption_key_crn": "crn:v1:staging:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.get_service_instance_endpoints(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_service_instance_endpoints_all_params_with_retries(self):
        # Enable retries and run test_get_service_instance_endpoints_all_params.
        _service.enable_retries()
        self.test_get_service_instance_endpoints_all_params()

        # Disable retries and run test_get_service_instance_endpoints_all_params.
        _service.disable_retries()
        self.test_get_service_instance_endpoints_all_params()

    @responses.activate
    def test_get_service_instance_endpoints_value_error(self):
        """
        test_get_service_instance_endpoints_value_error()
        """
        # Set up mock
        url = preprocess_url('/api/v1/instances/testString/endpoints')
        mock_response = '{"plan": "trial", "public_endpoints": {"service_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/api", "vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud"}, "private_endpoints": {"service_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud/api", "vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud"}, "encryption": {"provider_managed_encryption": "key_protect", "encryption_key_crn": "crn:v1:staging:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_service_instance_endpoints(**req_copy)

    def test_get_service_instance_endpoints_value_error_with_retries(self):
        # Enable retries and run test_get_service_instance_endpoints_value_error.
        _service.enable_retries()
        self.test_get_service_instance_endpoints_value_error()

        # Disable retries and run test_get_service_instance_endpoints_value_error.
        _service.disable_retries()
        self.test_get_service_instance_endpoints_value_error()


# endregion
##############################################################################
# End of Service: Endpoints
##############################################################################

##############################################################################
# Start of Service: Instances
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecretsManagerControlPlaneV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecretsManagerControlPlaneV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecretsManagerControlPlaneV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetServiceInstanceDetails:
    """
    Test Class for get_service_instance_details
    """

    @responses.activate
    def test_get_service_instance_details_all_params(self):
        """
        get_service_instance_details()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/testString')
        mock_response = '{"instance": {"id": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": {"name": "standard"}}, "vault_cluster": {"status": "active", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.get_service_instance_details(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_service_instance_details_all_params_with_retries(self):
        # Enable retries and run test_get_service_instance_details_all_params.
        _service.enable_retries()
        self.test_get_service_instance_details_all_params()

        # Disable retries and run test_get_service_instance_details_all_params.
        _service.disable_retries()
        self.test_get_service_instance_details_all_params()

    @responses.activate
    def test_get_service_instance_details_value_error(self):
        """
        test_get_service_instance_details_value_error()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/testString')
        mock_response = '{"instance": {"id": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": {"name": "standard"}}, "vault_cluster": {"status": "active", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_service_instance_details(**req_copy)

    def test_get_service_instance_details_value_error_with_retries(self):
        # Enable retries and run test_get_service_instance_details_value_error.
        _service.enable_retries()
        self.test_get_service_instance_details_value_error()

        # Disable retries and run test_get_service_instance_details_value_error.
        _service.disable_retries()
        self.test_get_service_instance_details_value_error()


# endregion
##############################################################################
# End of Service: Instances
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_EncryptionInfo:
    """
    Test Class for EncryptionInfo
    """

    def test_encryption_info_serialization(self):
        """
        Test serialization/deserialization for EncryptionInfo
        """

        # Construct a json representation of a EncryptionInfo model
        encryption_info_model_json = {}
        encryption_info_model_json['provider_managed_encryption'] = 'key_protect'
        encryption_info_model_json['encryption_key_crn'] = 'crn:v1:staging:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc'

        # Construct a model instance of EncryptionInfo by calling from_dict on the json representation
        encryption_info_model = EncryptionInfo.from_dict(encryption_info_model_json)
        assert encryption_info_model != False

        # Construct a model instance of EncryptionInfo by calling from_dict on the json representation
        encryption_info_model_dict = EncryptionInfo.from_dict(encryption_info_model_json).__dict__
        encryption_info_model2 = EncryptionInfo(**encryption_info_model_dict)

        # Verify the model instances are equivalent
        assert encryption_info_model == encryption_info_model2

        # Convert model instance back to dict and verify no loss of data
        encryption_info_model_json2 = encryption_info_model.to_dict()
        assert encryption_info_model_json2 == encryption_info_model_json


class TestModel_Endpoints:
    """
    Test Class for Endpoints
    """

    def test_endpoints_serialization(self):
        """
        Test serialization/deserialization for Endpoints
        """

        # Construct dict forms of any model objects needed in order to build this model.

        public_endpoints_model = {}  # PublicEndpoints
        public_endpoints_model['service_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/api'
        public_endpoints_model['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'

        private_endpoints_model = {}  # PrivateEndpoints
        private_endpoints_model['service_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud/api'
        private_endpoints_model['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud'

        encryption_info_model = {}  # EncryptionInfo
        encryption_info_model['provider_managed_encryption'] = 'key_protect'
        encryption_info_model['encryption_key_crn'] = 'crn:v1:staging:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc'

        # Construct a json representation of a Endpoints model
        endpoints_model_json = {}
        endpoints_model_json['plan'] = 'trial'
        endpoints_model_json['public_endpoints'] = public_endpoints_model
        endpoints_model_json['private_endpoints'] = private_endpoints_model
        endpoints_model_json['encryption'] = encryption_info_model

        # Construct a model instance of Endpoints by calling from_dict on the json representation
        endpoints_model = Endpoints.from_dict(endpoints_model_json)
        assert endpoints_model != False

        # Construct a model instance of Endpoints by calling from_dict on the json representation
        endpoints_model_dict = Endpoints.from_dict(endpoints_model_json).__dict__
        endpoints_model2 = Endpoints(**endpoints_model_dict)

        # Verify the model instances are equivalent
        assert endpoints_model == endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        endpoints_model_json2 = endpoints_model.to_dict()
        assert endpoints_model_json2 == endpoints_model_json


class TestModel_Instance:
    """
    Test Class for Instance
    """

    def test_instance_serialization(self):
        """
        Test serialization/deserialization for Instance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        vaas_instance_plan_model = {}  # VaasInstancePlan
        vaas_instance_plan_model['name'] = 'standard'

        vaas_instance_metadata_model = {}  # VaasInstanceMetadata
        vaas_instance_metadata_model['id'] = 'crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::'
        vaas_instance_metadata_model['plan'] = vaas_instance_plan_model

        vaas_vault_cluster_model = {}  # VaasVaultCluster
        vaas_vault_cluster_model['status'] = 'active'
        vaas_vault_cluster_model['version'] = '1.21.2+ent.hsm'

        vaas_endpoints_data_model = {}  # VaasEndpointsData
        vaas_endpoints_data_model['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'
        vaas_endpoints_data_model['vault_ui'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui'

        vaas_instance_endpoints_model = {}  # VaasInstanceEndpoints
        vaas_instance_endpoints_model['public'] = vaas_endpoints_data_model
        vaas_instance_endpoints_model['private'] = vaas_endpoints_data_model

        vaas_instance_encryption_model = {}  # VaasInstanceEncryption
        vaas_instance_encryption_model['mode'] = 'service_managed'
        vaas_instance_encryption_model['provider'] = 'key_protect'
        vaas_instance_encryption_model['key_crn'] = 'crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc'

        # Construct a json representation of a Instance model
        instance_model_json = {}
        instance_model_json['instance'] = vaas_instance_metadata_model
        instance_model_json['vault_cluster'] = vaas_vault_cluster_model
        instance_model_json['endpoints'] = vaas_instance_endpoints_model
        instance_model_json['encryption'] = vaas_instance_encryption_model

        # Construct a model instance of Instance by calling from_dict on the json representation
        instance_model = Instance.from_dict(instance_model_json)
        assert instance_model != False

        # Construct a model instance of Instance by calling from_dict on the json representation
        instance_model_dict = Instance.from_dict(instance_model_json).__dict__
        instance_model2 = Instance(**instance_model_dict)

        # Verify the model instances are equivalent
        assert instance_model == instance_model2

        # Convert model instance back to dict and verify no loss of data
        instance_model_json2 = instance_model.to_dict()
        assert instance_model_json2 == instance_model_json


class TestModel_PrivateEndpoints:
    """
    Test Class for PrivateEndpoints
    """

    def test_private_endpoints_serialization(self):
        """
        Test serialization/deserialization for PrivateEndpoints
        """

        # Construct a json representation of a PrivateEndpoints model
        private_endpoints_model_json = {}
        private_endpoints_model_json['service_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud/api'
        private_endpoints_model_json['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.private.us-south.secrets-manager.appdomain.cloud'

        # Construct a model instance of PrivateEndpoints by calling from_dict on the json representation
        private_endpoints_model = PrivateEndpoints.from_dict(private_endpoints_model_json)
        assert private_endpoints_model != False

        # Construct a model instance of PrivateEndpoints by calling from_dict on the json representation
        private_endpoints_model_dict = PrivateEndpoints.from_dict(private_endpoints_model_json).__dict__
        private_endpoints_model2 = PrivateEndpoints(**private_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert private_endpoints_model == private_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        private_endpoints_model_json2 = private_endpoints_model.to_dict()
        assert private_endpoints_model_json2 == private_endpoints_model_json


class TestModel_PublicEndpoints:
    """
    Test Class for PublicEndpoints
    """

    def test_public_endpoints_serialization(self):
        """
        Test serialization/deserialization for PublicEndpoints
        """

        # Construct a json representation of a PublicEndpoints model
        public_endpoints_model_json = {}
        public_endpoints_model_json['service_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/api'
        public_endpoints_model_json['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'

        # Construct a model instance of PublicEndpoints by calling from_dict on the json representation
        public_endpoints_model = PublicEndpoints.from_dict(public_endpoints_model_json)
        assert public_endpoints_model != False

        # Construct a model instance of PublicEndpoints by calling from_dict on the json representation
        public_endpoints_model_dict = PublicEndpoints.from_dict(public_endpoints_model_json).__dict__
        public_endpoints_model2 = PublicEndpoints(**public_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert public_endpoints_model == public_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        public_endpoints_model_json2 = public_endpoints_model.to_dict()
        assert public_endpoints_model_json2 == public_endpoints_model_json


class TestModel_Token:
    """
    Test Class for Token
    """

    def test_token_serialization(self):
        """
        Test serialization/deserialization for Token
        """

        # Construct a json representation of a Token model
        token_model_json = {}
        token_model_json['token'] = 'hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg'

        # Construct a model instance of Token by calling from_dict on the json representation
        token_model = Token.from_dict(token_model_json)
        assert token_model != False

        # Construct a model instance of Token by calling from_dict on the json representation
        token_model_dict = Token.from_dict(token_model_json).__dict__
        token_model2 = Token(**token_model_dict)

        # Verify the model instances are equivalent
        assert token_model == token_model2

        # Convert model instance back to dict and verify no loss of data
        token_model_json2 = token_model.to_dict()
        assert token_model_json2 == token_model_json


class TestModel_VaasEndpointsData:
    """
    Test Class for VaasEndpointsData
    """

    def test_vaas_endpoints_data_serialization(self):
        """
        Test serialization/deserialization for VaasEndpointsData
        """

        # Construct a json representation of a VaasEndpointsData model
        vaas_endpoints_data_model_json = {}
        vaas_endpoints_data_model_json['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'
        vaas_endpoints_data_model_json['vault_ui'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui'

        # Construct a model instance of VaasEndpointsData by calling from_dict on the json representation
        vaas_endpoints_data_model = VaasEndpointsData.from_dict(vaas_endpoints_data_model_json)
        assert vaas_endpoints_data_model != False

        # Construct a model instance of VaasEndpointsData by calling from_dict on the json representation
        vaas_endpoints_data_model_dict = VaasEndpointsData.from_dict(vaas_endpoints_data_model_json).__dict__
        vaas_endpoints_data_model2 = VaasEndpointsData(**vaas_endpoints_data_model_dict)

        # Verify the model instances are equivalent
        assert vaas_endpoints_data_model == vaas_endpoints_data_model2

        # Convert model instance back to dict and verify no loss of data
        vaas_endpoints_data_model_json2 = vaas_endpoints_data_model.to_dict()
        assert vaas_endpoints_data_model_json2 == vaas_endpoints_data_model_json


class TestModel_VaasInstanceEncryption:
    """
    Test Class for VaasInstanceEncryption
    """

    def test_vaas_instance_encryption_serialization(self):
        """
        Test serialization/deserialization for VaasInstanceEncryption
        """

        # Construct a json representation of a VaasInstanceEncryption model
        vaas_instance_encryption_model_json = {}
        vaas_instance_encryption_model_json['mode'] = 'service_managed'
        vaas_instance_encryption_model_json['provider'] = 'key_protect'
        vaas_instance_encryption_model_json['key_crn'] = 'crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc'

        # Construct a model instance of VaasInstanceEncryption by calling from_dict on the json representation
        vaas_instance_encryption_model = VaasInstanceEncryption.from_dict(vaas_instance_encryption_model_json)
        assert vaas_instance_encryption_model != False

        # Construct a model instance of VaasInstanceEncryption by calling from_dict on the json representation
        vaas_instance_encryption_model_dict = VaasInstanceEncryption.from_dict(vaas_instance_encryption_model_json).__dict__
        vaas_instance_encryption_model2 = VaasInstanceEncryption(**vaas_instance_encryption_model_dict)

        # Verify the model instances are equivalent
        assert vaas_instance_encryption_model == vaas_instance_encryption_model2

        # Convert model instance back to dict and verify no loss of data
        vaas_instance_encryption_model_json2 = vaas_instance_encryption_model.to_dict()
        assert vaas_instance_encryption_model_json2 == vaas_instance_encryption_model_json


class TestModel_VaasInstanceEndpoints:
    """
    Test Class for VaasInstanceEndpoints
    """

    def test_vaas_instance_endpoints_serialization(self):
        """
        Test serialization/deserialization for VaasInstanceEndpoints
        """

        # Construct dict forms of any model objects needed in order to build this model.

        vaas_endpoints_data_model = {}  # VaasEndpointsData
        vaas_endpoints_data_model['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'
        vaas_endpoints_data_model['vault_ui'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui'

        # Construct a json representation of a VaasInstanceEndpoints model
        vaas_instance_endpoints_model_json = {}
        vaas_instance_endpoints_model_json['public'] = vaas_endpoints_data_model
        vaas_instance_endpoints_model_json['private'] = vaas_endpoints_data_model

        # Construct a model instance of VaasInstanceEndpoints by calling from_dict on the json representation
        vaas_instance_endpoints_model = VaasInstanceEndpoints.from_dict(vaas_instance_endpoints_model_json)
        assert vaas_instance_endpoints_model != False

        # Construct a model instance of VaasInstanceEndpoints by calling from_dict on the json representation
        vaas_instance_endpoints_model_dict = VaasInstanceEndpoints.from_dict(vaas_instance_endpoints_model_json).__dict__
        vaas_instance_endpoints_model2 = VaasInstanceEndpoints(**vaas_instance_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert vaas_instance_endpoints_model == vaas_instance_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        vaas_instance_endpoints_model_json2 = vaas_instance_endpoints_model.to_dict()
        assert vaas_instance_endpoints_model_json2 == vaas_instance_endpoints_model_json


class TestModel_VaasInstanceMetadata:
    """
    Test Class for VaasInstanceMetadata
    """

    def test_vaas_instance_metadata_serialization(self):
        """
        Test serialization/deserialization for VaasInstanceMetadata
        """

        # Construct dict forms of any model objects needed in order to build this model.

        vaas_instance_plan_model = {}  # VaasInstancePlan
        vaas_instance_plan_model['name'] = 'standard'

        # Construct a json representation of a VaasInstanceMetadata model
        vaas_instance_metadata_model_json = {}
        vaas_instance_metadata_model_json['id'] = 'crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::'
        vaas_instance_metadata_model_json['plan'] = vaas_instance_plan_model

        # Construct a model instance of VaasInstanceMetadata by calling from_dict on the json representation
        vaas_instance_metadata_model = VaasInstanceMetadata.from_dict(vaas_instance_metadata_model_json)
        assert vaas_instance_metadata_model != False

        # Construct a model instance of VaasInstanceMetadata by calling from_dict on the json representation
        vaas_instance_metadata_model_dict = VaasInstanceMetadata.from_dict(vaas_instance_metadata_model_json).__dict__
        vaas_instance_metadata_model2 = VaasInstanceMetadata(**vaas_instance_metadata_model_dict)

        # Verify the model instances are equivalent
        assert vaas_instance_metadata_model == vaas_instance_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        vaas_instance_metadata_model_json2 = vaas_instance_metadata_model.to_dict()
        assert vaas_instance_metadata_model_json2 == vaas_instance_metadata_model_json


class TestModel_VaasInstancePlan:
    """
    Test Class for VaasInstancePlan
    """

    def test_vaas_instance_plan_serialization(self):
        """
        Test serialization/deserialization for VaasInstancePlan
        """

        # Construct a json representation of a VaasInstancePlan model
        vaas_instance_plan_model_json = {}
        vaas_instance_plan_model_json['name'] = 'standard'

        # Construct a model instance of VaasInstancePlan by calling from_dict on the json representation
        vaas_instance_plan_model = VaasInstancePlan.from_dict(vaas_instance_plan_model_json)
        assert vaas_instance_plan_model != False

        # Construct a model instance of VaasInstancePlan by calling from_dict on the json representation
        vaas_instance_plan_model_dict = VaasInstancePlan.from_dict(vaas_instance_plan_model_json).__dict__
        vaas_instance_plan_model2 = VaasInstancePlan(**vaas_instance_plan_model_dict)

        # Verify the model instances are equivalent
        assert vaas_instance_plan_model == vaas_instance_plan_model2

        # Convert model instance back to dict and verify no loss of data
        vaas_instance_plan_model_json2 = vaas_instance_plan_model.to_dict()
        assert vaas_instance_plan_model_json2 == vaas_instance_plan_model_json


class TestModel_VaasVaultCluster:
    """
    Test Class for VaasVaultCluster
    """

    def test_vaas_vault_cluster_serialization(self):
        """
        Test serialization/deserialization for VaasVaultCluster
        """

        # Construct a json representation of a VaasVaultCluster model
        vaas_vault_cluster_model_json = {}
        vaas_vault_cluster_model_json['status'] = 'active'
        vaas_vault_cluster_model_json['version'] = '1.21.2+ent.hsm'

        # Construct a model instance of VaasVaultCluster by calling from_dict on the json representation
        vaas_vault_cluster_model = VaasVaultCluster.from_dict(vaas_vault_cluster_model_json)
        assert vaas_vault_cluster_model != False

        # Construct a model instance of VaasVaultCluster by calling from_dict on the json representation
        vaas_vault_cluster_model_dict = VaasVaultCluster.from_dict(vaas_vault_cluster_model_json).__dict__
        vaas_vault_cluster_model2 = VaasVaultCluster(**vaas_vault_cluster_model_dict)

        # Verify the model instances are equivalent
        assert vaas_vault_cluster_model == vaas_vault_cluster_model2

        # Convert model instance back to dict and verify no loss of data
        vaas_vault_cluster_model_json2 = vaas_vault_cluster_model.to_dict()
        assert vaas_vault_cluster_model_json2 == vaas_vault_cluster_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
