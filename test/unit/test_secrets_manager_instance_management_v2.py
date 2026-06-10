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
Unit Tests for SecretsManagerInstanceManagementV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_secrets_manager_sdk_instance_management.secrets_manager_instance_management_v2 import *


_service = SecretsManagerInstanceManagementV2(
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
    assert SecretsManagerInstanceManagementV2.construct_service_url() == default_formatted_url


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

        service = SecretsManagerInstanceManagementV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecretsManagerInstanceManagementV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecretsManagerInstanceManagementV2.new_instance(
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
        url = preprocess_url('/api/v2/instances/60b40daa-1fd3-4f35-a994-2409cc0f270c/admintokens')
        mock_response = '{"token": "hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = '60b40daa-1fd3-4f35-a994-2409cc0f270c'

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
        url = preprocess_url('/api/v2/instances/60b40daa-1fd3-4f35-a994-2409cc0f270c/admintokens')
        mock_response = '{"token": "hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = '60b40daa-1fd3-4f35-a994-2409cc0f270c'

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


class TestDeleteInstanceAdmintokens:
    """
    Test Class for delete_instance_admintokens
    """

    @responses.activate
    def test_delete_instance_admintokens_all_params(self):
        """
        delete_instance_admintokens()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/60b40daa-1fd3-4f35-a994-2409cc0f270c/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = '60b40daa-1fd3-4f35-a994-2409cc0f270c'

        # Invoke method
        response = _service.delete_instance_admintokens(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_instance_admintokens_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_admintokens_all_params.
        _service.enable_retries()
        self.test_delete_instance_admintokens_all_params()

        # Disable retries and run test_delete_instance_admintokens_all_params.
        _service.disable_retries()
        self.test_delete_instance_admintokens_all_params()

    @responses.activate
    def test_delete_instance_admintokens_value_error(self):
        """
        test_delete_instance_admintokens_value_error()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/60b40daa-1fd3-4f35-a994-2409cc0f270c/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = '60b40daa-1fd3-4f35-a994-2409cc0f270c'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_admintokens(**req_copy)

    def test_delete_instance_admintokens_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_admintokens_value_error.
        _service.enable_retries()
        self.test_delete_instance_admintokens_value_error()

        # Disable retries and run test_delete_instance_admintokens_value_error.
        _service.disable_retries()
        self.test_delete_instance_admintokens_value_error()


# endregion
##############################################################################
# End of Service: Tokens
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

        service = SecretsManagerInstanceManagementV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecretsManagerInstanceManagementV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecretsManagerInstanceManagementV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetInstance:
    """
    Test Class for get_instance
    """

    @responses.activate
    def test_get_instance_all_params(self):
        """
        get_instance()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/60b40daa-1fd3-4f35-a994-2409cc0f270c')
        mock_response = '{"instance": {"id": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": {"name": "standard"}}, "vault_cluster": {"status": "healthy", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '60b40daa-1fd3-4f35-a994-2409cc0f270c'

        # Invoke method
        response = _service.get_instance(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_all_params_with_retries(self):
        # Enable retries and run test_get_instance_all_params.
        _service.enable_retries()
        self.test_get_instance_all_params()

        # Disable retries and run test_get_instance_all_params.
        _service.disable_retries()
        self.test_get_instance_all_params()

    @responses.activate
    def test_get_instance_value_error(self):
        """
        test_get_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/api/v2/instances/60b40daa-1fd3-4f35-a994-2409cc0f270c')
        mock_response = '{"instance": {"id": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": {"name": "standard"}}, "vault_cluster": {"status": "healthy", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '60b40daa-1fd3-4f35-a994-2409cc0f270c'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance(**req_copy)

    def test_get_instance_value_error_with_retries(self):
        # Enable retries and run test_get_instance_value_error.
        _service.enable_retries()
        self.test_get_instance_value_error()

        # Disable retries and run test_get_instance_value_error.
        _service.disable_retries()
        self.test_get_instance_value_error()


# endregion
##############################################################################
# End of Service: Instances
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_Instance:
    """
    Test Class for Instance
    """

    def test_instance_serialization(self):
        """
        Test serialization/deserialization for Instance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        vault_dedicated_instance_plan_model = {}  # VaultDedicatedInstancePlan
        vault_dedicated_instance_plan_model['name'] = 'standard'

        vault_dedicated_instance_metadata_model = {}  # VaultDedicatedInstanceMetadata
        vault_dedicated_instance_metadata_model['id'] = 'crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::'
        vault_dedicated_instance_metadata_model['plan'] = vault_dedicated_instance_plan_model

        vault_dedicated_cluster_model = {}  # VaultDedicatedCluster
        vault_dedicated_cluster_model['status'] = 'healthy'
        vault_dedicated_cluster_model['version'] = '1.21.2+ent.hsm'

        vault_dedicated_endpoints_data_model = {}  # VaultDedicatedEndpointsData
        vault_dedicated_endpoints_data_model['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'
        vault_dedicated_endpoints_data_model['vault_ui'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui'

        vault_dedicated_instance_endpoints_model = {}  # VaultDedicatedInstanceEndpoints
        vault_dedicated_instance_endpoints_model['public'] = vault_dedicated_endpoints_data_model
        vault_dedicated_instance_endpoints_model['private'] = vault_dedicated_endpoints_data_model

        vault_dedicated_instance_encryption_model = {}  # VaultDedicatedInstanceEncryption
        vault_dedicated_instance_encryption_model['mode'] = 'service_managed'
        vault_dedicated_instance_encryption_model['provider'] = 'key_protect'
        vault_dedicated_instance_encryption_model['key_crn'] = 'crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc'

        # Construct a json representation of a Instance model
        instance_model_json = {}
        instance_model_json['instance'] = vault_dedicated_instance_metadata_model
        instance_model_json['vault_cluster'] = vault_dedicated_cluster_model
        instance_model_json['endpoints'] = vault_dedicated_instance_endpoints_model
        instance_model_json['encryption'] = vault_dedicated_instance_encryption_model

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


class TestModel_VaultDedicatedCluster:
    """
    Test Class for VaultDedicatedCluster
    """

    def test_vault_dedicated_cluster_serialization(self):
        """
        Test serialization/deserialization for VaultDedicatedCluster
        """

        # Construct a json representation of a VaultDedicatedCluster model
        vault_dedicated_cluster_model_json = {}
        vault_dedicated_cluster_model_json['status'] = 'healthy'
        vault_dedicated_cluster_model_json['version'] = '1.21.2+ent.hsm'

        # Construct a model instance of VaultDedicatedCluster by calling from_dict on the json representation
        vault_dedicated_cluster_model = VaultDedicatedCluster.from_dict(vault_dedicated_cluster_model_json)
        assert vault_dedicated_cluster_model != False

        # Construct a model instance of VaultDedicatedCluster by calling from_dict on the json representation
        vault_dedicated_cluster_model_dict = VaultDedicatedCluster.from_dict(vault_dedicated_cluster_model_json).__dict__
        vault_dedicated_cluster_model2 = VaultDedicatedCluster(**vault_dedicated_cluster_model_dict)

        # Verify the model instances are equivalent
        assert vault_dedicated_cluster_model == vault_dedicated_cluster_model2

        # Convert model instance back to dict and verify no loss of data
        vault_dedicated_cluster_model_json2 = vault_dedicated_cluster_model.to_dict()
        assert vault_dedicated_cluster_model_json2 == vault_dedicated_cluster_model_json


class TestModel_VaultDedicatedEndpointsData:
    """
    Test Class for VaultDedicatedEndpointsData
    """

    def test_vault_dedicated_endpoints_data_serialization(self):
        """
        Test serialization/deserialization for VaultDedicatedEndpointsData
        """

        # Construct a json representation of a VaultDedicatedEndpointsData model
        vault_dedicated_endpoints_data_model_json = {}
        vault_dedicated_endpoints_data_model_json['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'
        vault_dedicated_endpoints_data_model_json['vault_ui'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui'

        # Construct a model instance of VaultDedicatedEndpointsData by calling from_dict on the json representation
        vault_dedicated_endpoints_data_model = VaultDedicatedEndpointsData.from_dict(vault_dedicated_endpoints_data_model_json)
        assert vault_dedicated_endpoints_data_model != False

        # Construct a model instance of VaultDedicatedEndpointsData by calling from_dict on the json representation
        vault_dedicated_endpoints_data_model_dict = VaultDedicatedEndpointsData.from_dict(vault_dedicated_endpoints_data_model_json).__dict__
        vault_dedicated_endpoints_data_model2 = VaultDedicatedEndpointsData(**vault_dedicated_endpoints_data_model_dict)

        # Verify the model instances are equivalent
        assert vault_dedicated_endpoints_data_model == vault_dedicated_endpoints_data_model2

        # Convert model instance back to dict and verify no loss of data
        vault_dedicated_endpoints_data_model_json2 = vault_dedicated_endpoints_data_model.to_dict()
        assert vault_dedicated_endpoints_data_model_json2 == vault_dedicated_endpoints_data_model_json


class TestModel_VaultDedicatedInstanceEncryption:
    """
    Test Class for VaultDedicatedInstanceEncryption
    """

    def test_vault_dedicated_instance_encryption_serialization(self):
        """
        Test serialization/deserialization for VaultDedicatedInstanceEncryption
        """

        # Construct a json representation of a VaultDedicatedInstanceEncryption model
        vault_dedicated_instance_encryption_model_json = {}
        vault_dedicated_instance_encryption_model_json['mode'] = 'service_managed'
        vault_dedicated_instance_encryption_model_json['provider'] = 'key_protect'
        vault_dedicated_instance_encryption_model_json['key_crn'] = 'crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc'

        # Construct a model instance of VaultDedicatedInstanceEncryption by calling from_dict on the json representation
        vault_dedicated_instance_encryption_model = VaultDedicatedInstanceEncryption.from_dict(vault_dedicated_instance_encryption_model_json)
        assert vault_dedicated_instance_encryption_model != False

        # Construct a model instance of VaultDedicatedInstanceEncryption by calling from_dict on the json representation
        vault_dedicated_instance_encryption_model_dict = VaultDedicatedInstanceEncryption.from_dict(vault_dedicated_instance_encryption_model_json).__dict__
        vault_dedicated_instance_encryption_model2 = VaultDedicatedInstanceEncryption(**vault_dedicated_instance_encryption_model_dict)

        # Verify the model instances are equivalent
        assert vault_dedicated_instance_encryption_model == vault_dedicated_instance_encryption_model2

        # Convert model instance back to dict and verify no loss of data
        vault_dedicated_instance_encryption_model_json2 = vault_dedicated_instance_encryption_model.to_dict()
        assert vault_dedicated_instance_encryption_model_json2 == vault_dedicated_instance_encryption_model_json


class TestModel_VaultDedicatedInstanceEndpoints:
    """
    Test Class for VaultDedicatedInstanceEndpoints
    """

    def test_vault_dedicated_instance_endpoints_serialization(self):
        """
        Test serialization/deserialization for VaultDedicatedInstanceEndpoints
        """

        # Construct dict forms of any model objects needed in order to build this model.

        vault_dedicated_endpoints_data_model = {}  # VaultDedicatedEndpointsData
        vault_dedicated_endpoints_data_model['vault_api'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud'
        vault_dedicated_endpoints_data_model['vault_ui'] = 'https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui'

        # Construct a json representation of a VaultDedicatedInstanceEndpoints model
        vault_dedicated_instance_endpoints_model_json = {}
        vault_dedicated_instance_endpoints_model_json['public'] = vault_dedicated_endpoints_data_model
        vault_dedicated_instance_endpoints_model_json['private'] = vault_dedicated_endpoints_data_model

        # Construct a model instance of VaultDedicatedInstanceEndpoints by calling from_dict on the json representation
        vault_dedicated_instance_endpoints_model = VaultDedicatedInstanceEndpoints.from_dict(vault_dedicated_instance_endpoints_model_json)
        assert vault_dedicated_instance_endpoints_model != False

        # Construct a model instance of VaultDedicatedInstanceEndpoints by calling from_dict on the json representation
        vault_dedicated_instance_endpoints_model_dict = VaultDedicatedInstanceEndpoints.from_dict(vault_dedicated_instance_endpoints_model_json).__dict__
        vault_dedicated_instance_endpoints_model2 = VaultDedicatedInstanceEndpoints(**vault_dedicated_instance_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert vault_dedicated_instance_endpoints_model == vault_dedicated_instance_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        vault_dedicated_instance_endpoints_model_json2 = vault_dedicated_instance_endpoints_model.to_dict()
        assert vault_dedicated_instance_endpoints_model_json2 == vault_dedicated_instance_endpoints_model_json


class TestModel_VaultDedicatedInstanceMetadata:
    """
    Test Class for VaultDedicatedInstanceMetadata
    """

    def test_vault_dedicated_instance_metadata_serialization(self):
        """
        Test serialization/deserialization for VaultDedicatedInstanceMetadata
        """

        # Construct dict forms of any model objects needed in order to build this model.

        vault_dedicated_instance_plan_model = {}  # VaultDedicatedInstancePlan
        vault_dedicated_instance_plan_model['name'] = 'standard'

        # Construct a json representation of a VaultDedicatedInstanceMetadata model
        vault_dedicated_instance_metadata_model_json = {}
        vault_dedicated_instance_metadata_model_json['id'] = 'crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::'
        vault_dedicated_instance_metadata_model_json['plan'] = vault_dedicated_instance_plan_model

        # Construct a model instance of VaultDedicatedInstanceMetadata by calling from_dict on the json representation
        vault_dedicated_instance_metadata_model = VaultDedicatedInstanceMetadata.from_dict(vault_dedicated_instance_metadata_model_json)
        assert vault_dedicated_instance_metadata_model != False

        # Construct a model instance of VaultDedicatedInstanceMetadata by calling from_dict on the json representation
        vault_dedicated_instance_metadata_model_dict = VaultDedicatedInstanceMetadata.from_dict(vault_dedicated_instance_metadata_model_json).__dict__
        vault_dedicated_instance_metadata_model2 = VaultDedicatedInstanceMetadata(**vault_dedicated_instance_metadata_model_dict)

        # Verify the model instances are equivalent
        assert vault_dedicated_instance_metadata_model == vault_dedicated_instance_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        vault_dedicated_instance_metadata_model_json2 = vault_dedicated_instance_metadata_model.to_dict()
        assert vault_dedicated_instance_metadata_model_json2 == vault_dedicated_instance_metadata_model_json


class TestModel_VaultDedicatedInstancePlan:
    """
    Test Class for VaultDedicatedInstancePlan
    """

    def test_vault_dedicated_instance_plan_serialization(self):
        """
        Test serialization/deserialization for VaultDedicatedInstancePlan
        """

        # Construct a json representation of a VaultDedicatedInstancePlan model
        vault_dedicated_instance_plan_model_json = {}
        vault_dedicated_instance_plan_model_json['name'] = 'standard'

        # Construct a model instance of VaultDedicatedInstancePlan by calling from_dict on the json representation
        vault_dedicated_instance_plan_model = VaultDedicatedInstancePlan.from_dict(vault_dedicated_instance_plan_model_json)
        assert vault_dedicated_instance_plan_model != False

        # Construct a model instance of VaultDedicatedInstancePlan by calling from_dict on the json representation
        vault_dedicated_instance_plan_model_dict = VaultDedicatedInstancePlan.from_dict(vault_dedicated_instance_plan_model_json).__dict__
        vault_dedicated_instance_plan_model2 = VaultDedicatedInstancePlan(**vault_dedicated_instance_plan_model_dict)

        # Verify the model instances are equivalent
        assert vault_dedicated_instance_plan_model == vault_dedicated_instance_plan_model2

        # Convert model instance back to dict and verify no loss of data
        vault_dedicated_instance_plan_model_json2 = vault_dedicated_instance_plan_model.to_dict()
        assert vault_dedicated_instance_plan_model_json2 == vault_dedicated_instance_plan_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
