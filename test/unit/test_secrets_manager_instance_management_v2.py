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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
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
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/admintokens')
        mock_response = '{"token": "hvs.CAESIC202dQW-jogohoywlivU-AMllTdeNT0QBiob9OBmyfnGigKImh2cy5yUkxpcmVaZURzTmw5cgtevFoyelBpYkguYW82SlMQyr0Q"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        response_wrapping = True

        # Invoke method
        response = _service.create_vault_admintoken(
            instance_id,
            response_wrapping=response_wrapping,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['response_wrapping'] == True

    def test_create_vault_admintoken_all_params_with_retries(self):
        # Enable retries and run test_create_vault_admintoken_all_params.
        _service.enable_retries()
        self.test_create_vault_admintoken_all_params()

        # Disable retries and run test_create_vault_admintoken_all_params.
        _service.disable_retries()
        self.test_create_vault_admintoken_all_params()

    @responses.activate
    def test_create_vault_admintoken_required_params(self):
        """
        test_create_vault_admintoken_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/admintokens')
        mock_response = '{"token": "hvs.CAESIC202dQW-jogohoywlivU-AMllTdeNT0QBiob9OBmyfnGigKImh2cy5yUkxpcmVaZURzTmw5cgtevFoyelBpYkguYW82SlMQyr0Q"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Invoke method
        response = _service.create_vault_admintoken(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_vault_admintoken_required_params_with_retries(self):
        # Enable retries and run test_create_vault_admintoken_required_params.
        _service.enable_retries()
        self.test_create_vault_admintoken_required_params()

        # Disable retries and run test_create_vault_admintoken_required_params.
        _service.disable_retries()
        self.test_create_vault_admintoken_required_params()

    @responses.activate
    def test_create_vault_admintoken_value_error(self):
        """
        test_create_vault_admintoken_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/admintokens')
        mock_response = '{"token": "hvs.CAESIC202dQW-jogohoywlivU-AMllTdeNT0QBiob9OBmyfnGigKImh2cy5yUkxpcmVaZURzTmw5cgtevFoyelBpYkguYW82SlMQyr0Q"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

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


class TestDeleteVaultAdmintokens:
    """
    Test Class for delete_vault_admintokens
    """

    @responses.activate
    def test_delete_vault_admintokens_all_params(self):
        """
        delete_vault_admintokens()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Invoke method
        response = _service.delete_vault_admintokens(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_vault_admintokens_all_params_with_retries(self):
        # Enable retries and run test_delete_vault_admintokens_all_params.
        _service.enable_retries()
        self.test_delete_vault_admintokens_all_params()

        # Disable retries and run test_delete_vault_admintokens_all_params.
        _service.disable_retries()
        self.test_delete_vault_admintokens_all_params()

    @responses.activate
    def test_delete_vault_admintokens_value_error(self):
        """
        test_delete_vault_admintokens_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_vault_admintokens(**req_copy)

    def test_delete_vault_admintokens_value_error_with_retries(self):
        # Enable retries and run test_delete_vault_admintokens_value_error.
        _service.enable_retries()
        self.test_delete_vault_admintokens_value_error()

        # Disable retries and run test_delete_vault_admintokens_value_error.
        _service.disable_retries()
        self.test_delete_vault_admintokens_value_error()


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
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "name": "name", "instance_crn": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": "dedicated", "vault_cluster": {"status": "healthy", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}, "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

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
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "name": "name", "instance_crn": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": "dedicated", "vault_cluster": {"status": "healthy", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}, "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

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
# Start of Service: Destinations
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


class TestListInstanceDestinations:
    """
    Test Class for list_instance_destinations
    """

    @responses.activate
    def test_list_instance_destinations_all_params(self):
        """
        list_instance_destinations()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations')
        mock_response = '{"destinations": [{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision"}], "total": 0}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        state = 'not_started'

        # Invoke method
        response = _service.list_instance_destinations(
            instance_id,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'state={}'.format(state) in query_string

    def test_list_instance_destinations_all_params_with_retries(self):
        # Enable retries and run test_list_instance_destinations_all_params.
        _service.enable_retries()
        self.test_list_instance_destinations_all_params()

        # Disable retries and run test_list_instance_destinations_all_params.
        _service.disable_retries()
        self.test_list_instance_destinations_all_params()

    @responses.activate
    def test_list_instance_destinations_required_params(self):
        """
        test_list_instance_destinations_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations')
        mock_response = '{"destinations": [{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision"}], "total": 0}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Invoke method
        response = _service.list_instance_destinations(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_destinations_required_params_with_retries(self):
        # Enable retries and run test_list_instance_destinations_required_params.
        _service.enable_retries()
        self.test_list_instance_destinations_required_params()

        # Disable retries and run test_list_instance_destinations_required_params.
        _service.disable_retries()
        self.test_list_instance_destinations_required_params()

    @responses.activate
    def test_list_instance_destinations_value_error(self):
        """
        test_list_instance_destinations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations')
        mock_response = '{"destinations": [{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision"}], "total": 0}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_destinations(**req_copy)

    def test_list_instance_destinations_value_error_with_retries(self):
        # Enable retries and run test_list_instance_destinations_value_error.
        _service.enable_retries()
        self.test_list_instance_destinations_value_error()

        # Disable retries and run test_list_instance_destinations_value_error.
        _service.disable_retries()
        self.test_list_instance_destinations_value_error()


class TestCreateInstanceDestination:
    """
    Test Class for create_instance_destination
    """

    @responses.activate
    def test_create_instance_destination_all_params(self):
        """
        create_instance_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype model
        create_destination_request_model = {}
        create_destination_request_model['name'] = 'my-postgres'
        create_destination_request_model['type'] = 'ibm_cloud_database'
        create_destination_request_model['description'] = 'Production PostgreSQL database'
        create_destination_request_model['crn'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/e91c8f42b3d74e1a9c2f05d8b67a3e10:3f8b1c7a-9d42-4e6f-b8a5-2c1d9e7f4b83::'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_prototype = create_destination_request_model

        # Invoke method
        response = _service.create_instance_destination(
            instance_id,
            destination_prototype,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == destination_prototype

    def test_create_instance_destination_all_params_with_retries(self):
        # Enable retries and run test_create_instance_destination_all_params.
        _service.enable_retries()
        self.test_create_instance_destination_all_params()

        # Disable retries and run test_create_instance_destination_all_params.
        _service.disable_retries()
        self.test_create_instance_destination_all_params()

    @responses.activate
    def test_create_instance_destination_value_error(self):
        """
        test_create_instance_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype model
        create_destination_request_model = {}
        create_destination_request_model['name'] = 'my-postgres'
        create_destination_request_model['type'] = 'ibm_cloud_database'
        create_destination_request_model['description'] = 'Production PostgreSQL database'
        create_destination_request_model['crn'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/e91c8f42b3d74e1a9c2f05d8b67a3e10:3f8b1c7a-9d42-4e6f-b8a5-2c1d9e7f4b83::'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_prototype = create_destination_request_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_prototype": destination_prototype,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_destination(**req_copy)

    def test_create_instance_destination_value_error_with_retries(self):
        # Enable retries and run test_create_instance_destination_value_error.
        _service.enable_retries()
        self.test_create_instance_destination_value_error()

        # Disable retries and run test_create_instance_destination_value_error.
        _service.disable_retries()
        self.test_create_instance_destination_value_error()


class TestGetInstanceDestination:
    """
    Test Class for get_instance_destination
    """

    @responses.activate
    def test_get_instance_destination_all_params(self):
        """
        get_instance_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.get_instance_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_destination_all_params_with_retries(self):
        # Enable retries and run test_get_instance_destination_all_params.
        _service.enable_retries()
        self.test_get_instance_destination_all_params()

        # Disable retries and run test_get_instance_destination_all_params.
        _service.disable_retries()
        self.test_get_instance_destination_all_params()

    @responses.activate
    def test_get_instance_destination_value_error(self):
        """
        test_get_instance_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_destination(**req_copy)

    def test_get_instance_destination_value_error_with_retries(self):
        # Enable retries and run test_get_instance_destination_value_error.
        _service.enable_retries()
        self.test_get_instance_destination_value_error()

        # Disable retries and run test_get_instance_destination_value_error.
        _service.disable_retries()
        self.test_get_instance_destination_value_error()


class TestUpdateInstanceDestination:
    """
    Test Class for update_instance_destination
    """

    @responses.activate
    def test_update_instance_destination_all_params(self):
        """
        update_instance_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DestinationPatch model
        destination_patch_model = {}
        destination_patch_model['name'] = 'my-postgres-updated'
        destination_patch_model['description'] = 'Production PostgreSQL database'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        destination_patch = destination_patch_model

        # Invoke method
        response = _service.update_instance_destination(
            instance_id,
            destination_id,
            destination_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == destination_patch

    def test_update_instance_destination_all_params_with_retries(self):
        # Enable retries and run test_update_instance_destination_all_params.
        _service.enable_retries()
        self.test_update_instance_destination_all_params()

        # Disable retries and run test_update_instance_destination_all_params.
        _service.disable_retries()
        self.test_update_instance_destination_all_params()

    @responses.activate
    def test_update_instance_destination_value_error(self):
        """
        test_update_instance_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DestinationPatch model
        destination_patch_model = {}
        destination_patch_model['name'] = 'my-postgres-updated'
        destination_patch_model['description'] = 'Production PostgreSQL database'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        destination_patch = destination_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "destination_patch": destination_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_destination(**req_copy)

    def test_update_instance_destination_value_error_with_retries(self):
        # Enable retries and run test_update_instance_destination_value_error.
        _service.enable_retries()
        self.test_update_instance_destination_value_error()

        # Disable retries and run test_update_instance_destination_value_error.
        _service.disable_retries()
        self.test_update_instance_destination_value_error()


class TestDeleteInstanceDestination:
    """
    Test Class for delete_instance_destination
    """

    @responses.activate
    def test_delete_instance_destination_all_params(self):
        """
        delete_instance_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.delete_instance_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_instance_destination_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_destination_all_params.
        _service.enable_retries()
        self.test_delete_instance_destination_all_params()

        # Disable retries and run test_delete_instance_destination_all_params.
        _service.disable_retries()
        self.test_delete_instance_destination_all_params()

    @responses.activate
    def test_delete_instance_destination_value_error(self):
        """
        test_delete_instance_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "message": "failed to provision", "crn": "crn"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_destination(**req_copy)

    def test_delete_instance_destination_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_destination_value_error.
        _service.enable_retries()
        self.test_delete_instance_destination_value_error()

        # Disable retries and run test_delete_instance_destination_value_error.
        _service.disable_retries()
        self.test_delete_instance_destination_value_error()


# endregion
##############################################################################
# End of Service: Destinations
##############################################################################

##############################################################################
# Start of Service: HSMDestination
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


class TestListInstanceHsmDestinations:
    """
    Test Class for list_instance_hsm_destinations
    """

    @responses.activate
    def test_list_instance_hsm_destinations_all_params(self):
        """
        list_instance_hsm_destinations()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations')
        mock_response = '{"total_count": 1, "hsm_destinations": [{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Invoke method
        response = _service.list_instance_hsm_destinations(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_hsm_destinations_all_params_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destinations_all_params.
        _service.enable_retries()
        self.test_list_instance_hsm_destinations_all_params()

        # Disable retries and run test_list_instance_hsm_destinations_all_params.
        _service.disable_retries()
        self.test_list_instance_hsm_destinations_all_params()

    @responses.activate
    def test_list_instance_hsm_destinations_value_error(self):
        """
        test_list_instance_hsm_destinations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations')
        mock_response = '{"total_count": 1, "hsm_destinations": [{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_hsm_destinations(**req_copy)

    def test_list_instance_hsm_destinations_value_error_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destinations_value_error.
        _service.enable_retries()
        self.test_list_instance_hsm_destinations_value_error()

        # Disable retries and run test_list_instance_hsm_destinations_value_error.
        _service.disable_retries()
        self.test_list_instance_hsm_destinations_value_error()


class TestCreateInstanceHsmDestination:
    """
    Test Class for create_instance_hsm_destination
    """

    @responses.activate
    def test_create_instance_hsm_destination_all_params(self):
        """
        create_instance_hsm_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations')
        mock_response = '{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        name = 'prod-hsm-destination'
        vendor = 'thales_luna'
        description = 'Primary Thales Luna destination'

        # Invoke method
        response = _service.create_instance_hsm_destination(
            instance_id,
            name,
            vendor,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'prod-hsm-destination'
        assert req_body['vendor'] == 'thales_luna'
        assert req_body['description'] == 'Primary Thales Luna destination'

    def test_create_instance_hsm_destination_all_params_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_all_params.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_all_params()

        # Disable retries and run test_create_instance_hsm_destination_all_params.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_all_params()

    @responses.activate
    def test_create_instance_hsm_destination_value_error(self):
        """
        test_create_instance_hsm_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations')
        mock_response = '{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        name = 'prod-hsm-destination'
        vendor = 'thales_luna'
        description = 'Primary Thales Luna destination'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "vendor": vendor,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_hsm_destination(**req_copy)

    def test_create_instance_hsm_destination_value_error_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_value_error.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_value_error()

        # Disable retries and run test_create_instance_hsm_destination_value_error.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_value_error()


class TestGetInstanceHsmDestination:
    """
    Test Class for get_instance_hsm_destination
    """

    @responses.activate
    def test_get_instance_hsm_destination_all_params(self):
        """
        get_instance_hsm_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.get_instance_hsm_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_hsm_destination_all_params_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_all_params.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_all_params()

        # Disable retries and run test_get_instance_hsm_destination_all_params.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_all_params()

    @responses.activate
    def test_get_instance_hsm_destination_value_error(self):
        """
        test_get_instance_hsm_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_hsm_destination(**req_copy)

    def test_get_instance_hsm_destination_value_error_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_value_error.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_value_error()

        # Disable retries and run test_get_instance_hsm_destination_value_error.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_value_error()


class TestUpdateInstanceHsmDestination:
    """
    Test Class for update_instance_hsm_destination
    """

    @responses.activate
    def test_update_instance_hsm_destination_all_params(self):
        """
        update_instance_hsm_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HSMDestinationPatch model
        hsm_destination_patch_model = {}
        hsm_destination_patch_model['name'] = 'my-hsm-destination'
        hsm_destination_patch_model['description'] = 'testString'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        hsm_destination_patch = hsm_destination_patch_model

        # Invoke method
        response = _service.update_instance_hsm_destination(
            instance_id,
            destination_id,
            hsm_destination_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == hsm_destination_patch

    def test_update_instance_hsm_destination_all_params_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_all_params.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_all_params()

        # Disable retries and run test_update_instance_hsm_destination_all_params.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_all_params()

    @responses.activate
    def test_update_instance_hsm_destination_value_error(self):
        """
        test_update_instance_hsm_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "account_id": "a/abc123def456", "name": "prod-hsm-destination", "description": "Primary Thales Luna destination", "vendor": "thales_luna", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HSMDestinationPatch model
        hsm_destination_patch_model = {}
        hsm_destination_patch_model['name'] = 'my-hsm-destination'
        hsm_destination_patch_model['description'] = 'testString'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        hsm_destination_patch = hsm_destination_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "hsm_destination_patch": hsm_destination_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_hsm_destination(**req_copy)

    def test_update_instance_hsm_destination_value_error_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_value_error.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_value_error()

        # Disable retries and run test_update_instance_hsm_destination_value_error.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_value_error()


class TestDeleteInstanceHsmDestination:
    """
    Test Class for delete_instance_hsm_destination
    """

    @responses.activate
    def test_delete_instance_hsm_destination_all_params(self):
        """
        delete_instance_hsm_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "provisioning_state": "deleting"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.delete_instance_hsm_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_instance_hsm_destination_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_all_params.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_all_params()

        # Disable retries and run test_delete_instance_hsm_destination_all_params.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_all_params()

    @responses.activate
    def test_delete_instance_hsm_destination_value_error(self):
        """
        test_delete_instance_hsm_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02", "id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "provisioning_state": "deleting"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_hsm_destination(**req_copy)

    def test_delete_instance_hsm_destination_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_value_error.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_value_error()

        # Disable retries and run test_delete_instance_hsm_destination_value_error.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_value_error()


class TestGetHsmDestinationHealthSnapshot:
    """
    Test Class for get_hsm_destination_health_snapshot
    """

    @responses.activate
    def test_get_hsm_destination_health_snapshot_all_params(self):
        """
        get_hsm_destination_health_snapshot()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/health')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/health", "destination_id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "client_certificates": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "health_state": "valid"}], "ha_groups": [{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "health_state": "healthy"}], "paths": [{"id": "fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "health_state": "healthy", "server_cas": [{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "health_state": "valid"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.get_hsm_destination_health_snapshot(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_hsm_destination_health_snapshot_all_params_with_retries(self):
        # Enable retries and run test_get_hsm_destination_health_snapshot_all_params.
        _service.enable_retries()
        self.test_get_hsm_destination_health_snapshot_all_params()

        # Disable retries and run test_get_hsm_destination_health_snapshot_all_params.
        _service.disable_retries()
        self.test_get_hsm_destination_health_snapshot_all_params()

    @responses.activate
    def test_get_hsm_destination_health_snapshot_value_error(self):
        """
        test_get_hsm_destination_health_snapshot_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/health')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/health", "destination_id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "client_certificates": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "health_state": "valid"}], "ha_groups": [{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "health_state": "healthy"}], "paths": [{"id": "fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "health_state": "healthy", "server_cas": [{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "health_state": "valid"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_hsm_destination_health_snapshot(**req_copy)

    def test_get_hsm_destination_health_snapshot_value_error_with_retries(self):
        # Enable retries and run test_get_hsm_destination_health_snapshot_value_error.
        _service.enable_retries()
        self.test_get_hsm_destination_health_snapshot_value_error()

        # Disable retries and run test_get_hsm_destination_health_snapshot_value_error.
        _service.disable_retries()
        self.test_get_hsm_destination_health_snapshot_value_error()


class TestRunHsmDestinationHealthCheck:
    """
    Test Class for run_hsm_destination_health_check
    """

    @responses.activate
    def test_run_hsm_destination_health_check_all_params(self):
        """
        run_hsm_destination_health_check()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/health')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/health", "destination_id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "client_certificates": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "health_state": "valid"}], "ha_groups": [{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "health_state": "healthy"}], "paths": [{"id": "fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "health_state": "healthy", "server_cas": [{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "health_state": "valid"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.run_hsm_destination_health_check(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_run_hsm_destination_health_check_all_params_with_retries(self):
        # Enable retries and run test_run_hsm_destination_health_check_all_params.
        _service.enable_retries()
        self.test_run_hsm_destination_health_check_all_params()

        # Disable retries and run test_run_hsm_destination_health_check_all_params.
        _service.disable_retries()
        self.test_run_hsm_destination_health_check_all_params()

    @responses.activate
    def test_run_hsm_destination_health_check_value_error(self):
        """
        test_run_hsm_destination_health_check_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/health')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/health", "destination_id": "b49ad385-0cb7-3694-a71c-2579d6e94b02", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "client_certificates": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "health_state": "valid"}], "ha_groups": [{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "health_state": "healthy"}], "paths": [{"id": "fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "health_state": "healthy", "server_cas": [{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "health_state": "valid"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.run_hsm_destination_health_check(**req_copy)

    def test_run_hsm_destination_health_check_value_error_with_retries(self):
        # Enable retries and run test_run_hsm_destination_health_check_value_error.
        _service.enable_retries()
        self.test_run_hsm_destination_health_check_value_error()

        # Disable retries and run test_run_hsm_destination_health_check_value_error.
        _service.disable_retries()
        self.test_run_hsm_destination_health_check_value_error()


class TestApplyHsmDestination:
    """
    Test Class for apply_hsm_destination
    """

    @responses.activate
    def test_apply_hsm_destination_all_params(self):
        """
        apply_hsm_destination()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/apply')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/health"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.apply_hsm_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_apply_hsm_destination_all_params_with_retries(self):
        # Enable retries and run test_apply_hsm_destination_all_params.
        _service.enable_retries()
        self.test_apply_hsm_destination_all_params()

        # Disable retries and run test_apply_hsm_destination_all_params.
        _service.disable_retries()
        self.test_apply_hsm_destination_all_params()

    @responses.activate
    def test_apply_hsm_destination_value_error(self):
        """
        test_apply_hsm_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/apply')
        mock_response = '{"href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/health"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.apply_hsm_destination(**req_copy)

    def test_apply_hsm_destination_value_error_with_retries(self):
        # Enable retries and run test_apply_hsm_destination_value_error.
        _service.enable_retries()
        self.test_apply_hsm_destination_value_error()

        # Disable retries and run test_apply_hsm_destination_value_error.
        _service.disable_retries()
        self.test_apply_hsm_destination_value_error()


# endregion
##############################################################################
# End of Service: HSMDestination
##############################################################################

##############################################################################
# Start of Service: HSMHAGroups
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


class TestListInstanceHsmDestinationHaGroups:
    """
    Test Class for list_instance_hsm_destination_ha_groups
    """

    @responses.activate
    def test_list_instance_hsm_destination_ha_groups_all_params(self):
        """
        list_instance_hsm_destination_ha_groups()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups')
        mock_response = '{"ha_groups": [{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.list_instance_hsm_destination_ha_groups(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_hsm_destination_ha_groups_all_params_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_ha_groups_all_params.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_ha_groups_all_params()

        # Disable retries and run test_list_instance_hsm_destination_ha_groups_all_params.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_ha_groups_all_params()

    @responses.activate
    def test_list_instance_hsm_destination_ha_groups_value_error(self):
        """
        test_list_instance_hsm_destination_ha_groups_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups')
        mock_response = '{"ha_groups": [{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_hsm_destination_ha_groups(**req_copy)

    def test_list_instance_hsm_destination_ha_groups_value_error_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_ha_groups_value_error.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_ha_groups_value_error()

        # Disable retries and run test_list_instance_hsm_destination_ha_groups_value_error.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_ha_groups_value_error()


class TestCreateInstanceHsmDestinationHaGroup:
    """
    Test Class for create_instance_hsm_destination_ha_group
    """

    @responses.activate
    def test_create_instance_hsm_destination_ha_group_all_params(self):
        """
        create_instance_hsm_destination_ha_group()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups')
        mock_response = '{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        name = 'production-ha-group'
        group_label = 'prod_ha_group'
        group_serial = '11323465009866'
        member_serials = ['123456', '123457']
        description = 'Primary HA Group for prod'

        # Invoke method
        response = _service.create_instance_hsm_destination_ha_group(
            instance_id,
            destination_id,
            name,
            group_label,
            group_serial,
            member_serials,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'production-ha-group'
        assert req_body['group_label'] == 'prod_ha_group'
        assert req_body['group_serial'] == '11323465009866'
        assert req_body['member_serials'] == ['123456', '123457']
        assert req_body['description'] == 'Primary HA Group for prod'

    def test_create_instance_hsm_destination_ha_group_all_params_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_ha_group_all_params.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_ha_group_all_params()

        # Disable retries and run test_create_instance_hsm_destination_ha_group_all_params.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_ha_group_all_params()

    @responses.activate
    def test_create_instance_hsm_destination_ha_group_value_error(self):
        """
        test_create_instance_hsm_destination_ha_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups')
        mock_response = '{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        name = 'production-ha-group'
        group_label = 'prod_ha_group'
        group_serial = '11323465009866'
        member_serials = ['123456', '123457']
        description = 'Primary HA Group for prod'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "name": name,
            "group_label": group_label,
            "group_serial": group_serial,
            "member_serials": member_serials,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_hsm_destination_ha_group(**req_copy)

    def test_create_instance_hsm_destination_ha_group_value_error_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_ha_group_value_error.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_ha_group_value_error()

        # Disable retries and run test_create_instance_hsm_destination_ha_group_value_error.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_ha_group_value_error()


class TestGetInstanceHsmDestinationHaGroup:
    """
    Test Class for get_instance_hsm_destination_ha_group
    """

    @responses.activate
    def test_get_instance_hsm_destination_ha_group_all_params(self):
        """
        get_instance_hsm_destination_ha_group()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0')
        mock_response = '{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        ha_group_id = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'

        # Invoke method
        response = _service.get_instance_hsm_destination_ha_group(
            instance_id,
            destination_id,
            ha_group_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_hsm_destination_ha_group_all_params_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_ha_group_all_params.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_ha_group_all_params()

        # Disable retries and run test_get_instance_hsm_destination_ha_group_all_params.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_ha_group_all_params()

    @responses.activate
    def test_get_instance_hsm_destination_ha_group_value_error(self):
        """
        test_get_instance_hsm_destination_ha_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0')
        mock_response = '{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        ha_group_id = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "ha_group_id": ha_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_hsm_destination_ha_group(**req_copy)

    def test_get_instance_hsm_destination_ha_group_value_error_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_ha_group_value_error.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_ha_group_value_error()

        # Disable retries and run test_get_instance_hsm_destination_ha_group_value_error.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_ha_group_value_error()


class TestUpdateInstanceHsmDestinationHaGroup:
    """
    Test Class for update_instance_hsm_destination_ha_group
    """

    @responses.activate
    def test_update_instance_hsm_destination_ha_group_all_params(self):
        """
        update_instance_hsm_destination_ha_group()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0')
        mock_response = '{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HSMHAGroupPatch model
        hsmha_group_patch_model = {}
        hsmha_group_patch_model['name'] = 'dr-ha-group'
        hsmha_group_patch_model['description'] = 'DR HA Group for failover'
        hsmha_group_patch_model['member_serials'] = ['123456', '123457', '123458']

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        ha_group_id = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'
        hsmha_group_patch = hsmha_group_patch_model

        # Invoke method
        response = _service.update_instance_hsm_destination_ha_group(
            instance_id,
            destination_id,
            ha_group_id,
            hsmha_group_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == hsmha_group_patch

    def test_update_instance_hsm_destination_ha_group_all_params_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_ha_group_all_params.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_ha_group_all_params()

        # Disable retries and run test_update_instance_hsm_destination_ha_group_all_params.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_ha_group_all_params()

    @responses.activate
    def test_update_instance_hsm_destination_ha_group_value_error(self):
        """
        test_update_instance_hsm_destination_ha_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0')
        mock_response = '{"id": "ee52ebb6-1728-4580-8ede-13f6504e3ae0", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0", "name": "production-ha-group", "description": "Primary HA Group for prod", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T16:00:00.000Z", "group_label": "prod_ha_group", "group_serial": "11323465009866", "member_serials": ["member_serials"], "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T16:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HSMHAGroupPatch model
        hsmha_group_patch_model = {}
        hsmha_group_patch_model['name'] = 'dr-ha-group'
        hsmha_group_patch_model['description'] = 'DR HA Group for failover'
        hsmha_group_patch_model['member_serials'] = ['123456', '123457', '123458']

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        ha_group_id = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'
        hsmha_group_patch = hsmha_group_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "ha_group_id": ha_group_id,
            "hsmha_group_patch": hsmha_group_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_hsm_destination_ha_group(**req_copy)

    def test_update_instance_hsm_destination_ha_group_value_error_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_ha_group_value_error.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_ha_group_value_error()

        # Disable retries and run test_update_instance_hsm_destination_ha_group_value_error.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_ha_group_value_error()


class TestDeleteInstanceHsmDestinationHaGroup:
    """
    Test Class for delete_instance_hsm_destination_ha_group
    """

    @responses.activate
    def test_delete_instance_hsm_destination_ha_group_all_params(self):
        """
        delete_instance_hsm_destination_ha_group()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        ha_group_id = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'

        # Invoke method
        response = _service.delete_instance_hsm_destination_ha_group(
            instance_id,
            destination_id,
            ha_group_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_instance_hsm_destination_ha_group_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_ha_group_all_params.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_ha_group_all_params()

        # Disable retries and run test_delete_instance_hsm_destination_ha_group_all_params.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_ha_group_all_params()

    @responses.activate
    def test_delete_instance_hsm_destination_ha_group_value_error(self):
        """
        test_delete_instance_hsm_destination_ha_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/ha_groups/ee52ebb6-1728-4580-8ede-13f6504e3ae0')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        ha_group_id = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "ha_group_id": ha_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_hsm_destination_ha_group(**req_copy)

    def test_delete_instance_hsm_destination_ha_group_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_ha_group_value_error.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_ha_group_value_error()

        # Disable retries and run test_delete_instance_hsm_destination_ha_group_value_error.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_ha_group_value_error()


# endregion
##############################################################################
# End of Service: HSMHAGroups
##############################################################################

##############################################################################
# Start of Service: Paths
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


class TestListInstanceHsmDestinationPaths:
    """
    Test Class for list_instance_hsm_destination_paths
    """

    @responses.activate
    def test_list_instance_hsm_destination_paths_all_params(self):
        """
        list_instance_hsm_destination_paths()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths')
        mock_response = '{"paths": [{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.list_instance_hsm_destination_paths(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_hsm_destination_paths_all_params_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_paths_all_params.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_paths_all_params()

        # Disable retries and run test_list_instance_hsm_destination_paths_all_params.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_paths_all_params()

    @responses.activate
    def test_list_instance_hsm_destination_paths_value_error(self):
        """
        test_list_instance_hsm_destination_paths_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths')
        mock_response = '{"paths": [{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_hsm_destination_paths(**req_copy)

    def test_list_instance_hsm_destination_paths_value_error_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_paths_value_error.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_paths_value_error()

        # Disable retries and run test_list_instance_hsm_destination_paths_value_error.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_paths_value_error()


class TestCreateInstanceHsmDestinationPath:
    """
    Test Class for create_instance_hsm_destination_path
    """

    @responses.activate
    def test_create_instance_hsm_destination_path_all_params(self):
        """
        create_instance_hsm_destination_path()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        name = 'hsm-node-1'
        crn = 'crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1'
        description = 'testString'

        # Invoke method
        response = _service.create_instance_hsm_destination_path(
            instance_id,
            destination_id,
            name,
            crn,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'hsm-node-1'
        assert req_body['crn'] == 'crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1'
        assert req_body['description'] == 'testString'

    def test_create_instance_hsm_destination_path_all_params_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_path_all_params.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_path_all_params()

        # Disable retries and run test_create_instance_hsm_destination_path_all_params.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_path_all_params()

    @responses.activate
    def test_create_instance_hsm_destination_path_value_error(self):
        """
        test_create_instance_hsm_destination_path_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        name = 'hsm-node-1'
        crn = 'crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "name": name,
            "crn": crn,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_hsm_destination_path(**req_copy)

    def test_create_instance_hsm_destination_path_value_error_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_path_value_error.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_path_value_error()

        # Disable retries and run test_create_instance_hsm_destination_path_value_error.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_path_value_error()


class TestGetInstanceHsmDestinationPath:
    """
    Test Class for get_instance_hsm_destination_path
    """

    @responses.activate
    def test_get_instance_hsm_destination_path_all_params(self):
        """
        get_instance_hsm_destination_path()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Invoke method
        response = _service.get_instance_hsm_destination_path(
            instance_id,
            destination_id,
            path_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_hsm_destination_path_all_params_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_path_all_params.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_path_all_params()

        # Disable retries and run test_get_instance_hsm_destination_path_all_params.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_path_all_params()

    @responses.activate
    def test_get_instance_hsm_destination_path_value_error(self):
        """
        test_get_instance_hsm_destination_path_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_hsm_destination_path(**req_copy)

    def test_get_instance_hsm_destination_path_value_error_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_path_value_error.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_path_value_error()

        # Disable retries and run test_get_instance_hsm_destination_path_value_error.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_path_value_error()


class TestUpdateInstanceHsmDestinationPath:
    """
    Test Class for update_instance_hsm_destination_path
    """

    @responses.activate
    def test_update_instance_hsm_destination_path_all_params(self):
        """
        update_instance_hsm_destination_path()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PathPatch model
        path_patch_model = {}
        path_patch_model['name'] = 'hsm-node-1-renamed'
        path_patch_model['description'] = 'testString'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        path_patch = path_patch_model

        # Invoke method
        response = _service.update_instance_hsm_destination_path(
            instance_id,
            destination_id,
            path_id,
            path_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == path_patch

    def test_update_instance_hsm_destination_path_all_params_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_path_all_params.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_path_all_params()

        # Disable retries and run test_update_instance_hsm_destination_path_all_params.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_path_all_params()

    @responses.activate
    def test_update_instance_hsm_destination_path_value_error(self):
        """
        test_update_instance_hsm_destination_path_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PathPatch model
        path_patch_model = {}
        path_patch_model['name'] = 'hsm-node-1-renamed'
        path_patch_model['description'] = 'testString'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        path_patch = path_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
            "path_patch": path_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_hsm_destination_path(**req_copy)

    def test_update_instance_hsm_destination_path_value_error_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_path_value_error.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_path_value_error()

        # Disable retries and run test_update_instance_hsm_destination_path_value_error.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_path_value_error()


class TestDeleteInstanceHsmDestinationPath:
    """
    Test Class for delete_instance_hsm_destination_path
    """

    @responses.activate
    def test_delete_instance_hsm_destination_path_all_params(self):
        """
        delete_instance_hsm_destination_path()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Invoke method
        response = _service.delete_instance_hsm_destination_path(
            instance_id,
            destination_id,
            path_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_instance_hsm_destination_path_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_path_all_params.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_path_all_params()

        # Disable retries and run test_delete_instance_hsm_destination_path_all_params.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_path_all_params()

    @responses.activate
    def test_delete_instance_hsm_destination_path_value_error(self):
        """
        test_delete_instance_hsm_destination_path_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/paths/fa3d1234-0000-0000-0000-000000000001", "name": "hsm-node-1", "description": "Primary HSM node for prod", "crn": "crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1", "provisioning_state": "completed", "health_state": "healthy", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:00:00.000Z", "updated_at": "2026-07-09T15:30:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_hsm_destination_path(**req_copy)

    def test_delete_instance_hsm_destination_path_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_path_value_error.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_path_value_error()

        # Disable retries and run test_delete_instance_hsm_destination_path_value_error.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_path_value_error()


class TestCreatePathBuild:
    """
    Test Class for create_path_build
    """

    @responses.activate
    def test_create_path_build_all_params(self):
        """
        create_path_build()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/build')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "provisioning_state": "provisioning"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Invoke method
        response = _service.create_path_build(
            instance_id,
            destination_id,
            path_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_create_path_build_all_params_with_retries(self):
        # Enable retries and run test_create_path_build_all_params.
        _service.enable_retries()
        self.test_create_path_build_all_params()

        # Disable retries and run test_create_path_build_all_params.
        _service.disable_retries()
        self.test_create_path_build_all_params()

    @responses.activate
    def test_create_path_build_value_error(self):
        """
        test_create_path_build_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/build')
        mock_response = '{"id": "fa3d1234-0000-0000-0000-000000000001", "provisioning_state": "provisioning"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_path_build(**req_copy)

    def test_create_path_build_value_error_with_retries(self):
        # Enable retries and run test_create_path_build_value_error.
        _service.enable_retries()
        self.test_create_path_build_value_error()

        # Disable retries and run test_create_path_build_value_error.
        _service.disable_retries()
        self.test_create_path_build_value_error()


class TestGetPathVpeStatus:
    """
    Test Class for get_path_vpe_status
    """

    @responses.activate
    def test_get_path_vpe_status_all_params(self):
        """
        get_path_vpe_status()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/health_check')
        mock_response = '{"health_state": "healthy", "health_time_stamp": "2026-11-13T07:14:16.000Z", "provisioning_state": "completed"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Invoke method
        response = _service.get_path_vpe_status(
            instance_id,
            destination_id,
            path_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_path_vpe_status_all_params_with_retries(self):
        # Enable retries and run test_get_path_vpe_status_all_params.
        _service.enable_retries()
        self.test_get_path_vpe_status_all_params()

        # Disable retries and run test_get_path_vpe_status_all_params.
        _service.disable_retries()
        self.test_get_path_vpe_status_all_params()

    @responses.activate
    def test_get_path_vpe_status_value_error(self):
        """
        test_get_path_vpe_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/health_check')
        mock_response = '{"health_state": "healthy", "health_time_stamp": "2026-11-13T07:14:16.000Z", "provisioning_state": "completed"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_path_vpe_status(**req_copy)

    def test_get_path_vpe_status_value_error_with_retries(self):
        # Enable retries and run test_get_path_vpe_status_value_error.
        _service.enable_retries()
        self.test_get_path_vpe_status_value_error()

        # Disable retries and run test_get_path_vpe_status_value_error.
        _service.disable_retries()
        self.test_get_path_vpe_status_value_error()


class TestResetHsmDestinationPath:
    """
    Test Class for reset_hsm_destination_path
    """

    @responses.activate
    def test_reset_hsm_destination_path_all_params(self):
        """
        reset_hsm_destination_path()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/reset')
        mock_response = '{"href": "href", "provisioning_state": "completed"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Invoke method
        response = _service.reset_hsm_destination_path(
            instance_id,
            destination_id,
            path_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_reset_hsm_destination_path_all_params_with_retries(self):
        # Enable retries and run test_reset_hsm_destination_path_all_params.
        _service.enable_retries()
        self.test_reset_hsm_destination_path_all_params()

        # Disable retries and run test_reset_hsm_destination_path_all_params.
        _service.disable_retries()
        self.test_reset_hsm_destination_path_all_params()

    @responses.activate
    def test_reset_hsm_destination_path_value_error(self):
        """
        test_reset_hsm_destination_path_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/reset')
        mock_response = '{"href": "href", "provisioning_state": "completed"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.reset_hsm_destination_path(**req_copy)

    def test_reset_hsm_destination_path_value_error_with_retries(self):
        # Enable retries and run test_reset_hsm_destination_path_value_error.
        _service.enable_retries()
        self.test_reset_hsm_destination_path_value_error()

        # Disable retries and run test_reset_hsm_destination_path_value_error.
        _service.disable_retries()
        self.test_reset_hsm_destination_path_value_error()


# endregion
##############################################################################
# End of Service: Paths
##############################################################################

##############################################################################
# Start of Service: ServerCAs
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


class TestListInstanceHsmDestinationPathServerCas:
    """
    Test Class for list_instance_hsm_destination_path_server_cas
    """

    @responses.activate
    def test_list_instance_hsm_destination_path_server_cas_all_params(self):
        """
        list_instance_hsm_destination_path_server_cas()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas')
        mock_response = '{"server_cas": [{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Invoke method
        response = _service.list_instance_hsm_destination_path_server_cas(
            instance_id,
            destination_id,
            path_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_hsm_destination_path_server_cas_all_params_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_path_server_cas_all_params.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_path_server_cas_all_params()

        # Disable retries and run test_list_instance_hsm_destination_path_server_cas_all_params.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_path_server_cas_all_params()

    @responses.activate
    def test_list_instance_hsm_destination_path_server_cas_value_error(self):
        """
        test_list_instance_hsm_destination_path_server_cas_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas')
        mock_response = '{"server_cas": [{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_hsm_destination_path_server_cas(**req_copy)

    def test_list_instance_hsm_destination_path_server_cas_value_error_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_path_server_cas_value_error.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_path_server_cas_value_error()

        # Disable retries and run test_list_instance_hsm_destination_path_server_cas_value_error.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_path_server_cas_value_error()


class TestCreateInstanceHsmDestinationPathServerCa:
    """
    Test Class for create_instance_hsm_destination_path_server_ca
    """

    @responses.activate
    def test_create_instance_hsm_destination_path_server_ca_all_params(self):
        """
        create_instance_hsm_destination_path_server_ca()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas')
        mock_response = '{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        name = 'HSM1_Server_CA'
        certificate = '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        description = 'testString'

        # Invoke method
        response = _service.create_instance_hsm_destination_path_server_ca(
            instance_id,
            destination_id,
            path_id,
            name,
            certificate,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'HSM1_Server_CA'
        assert req_body['certificate'] == '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        assert req_body['description'] == 'testString'

    def test_create_instance_hsm_destination_path_server_ca_all_params_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_path_server_ca_all_params.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_path_server_ca_all_params()

        # Disable retries and run test_create_instance_hsm_destination_path_server_ca_all_params.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_path_server_ca_all_params()

    @responses.activate
    def test_create_instance_hsm_destination_path_server_ca_value_error(self):
        """
        test_create_instance_hsm_destination_path_server_ca_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas')
        mock_response = '{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        name = 'HSM1_Server_CA'
        certificate = '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
            "name": name,
            "certificate": certificate,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_hsm_destination_path_server_ca(**req_copy)

    def test_create_instance_hsm_destination_path_server_ca_value_error_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_path_server_ca_value_error.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_path_server_ca_value_error()

        # Disable retries and run test_create_instance_hsm_destination_path_server_ca_value_error.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_path_server_ca_value_error()


class TestGetInstanceHsmDestinationPathServerCa:
    """
    Test Class for get_instance_hsm_destination_path_server_ca
    """

    @responses.activate
    def test_get_instance_hsm_destination_path_server_ca_all_params(self):
        """
        get_instance_hsm_destination_path_server_ca()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas/5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f')
        mock_response = '{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        server_ca_id = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'

        # Invoke method
        response = _service.get_instance_hsm_destination_path_server_ca(
            instance_id,
            destination_id,
            path_id,
            server_ca_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_hsm_destination_path_server_ca_all_params_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_path_server_ca_all_params.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_path_server_ca_all_params()

        # Disable retries and run test_get_instance_hsm_destination_path_server_ca_all_params.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_path_server_ca_all_params()

    @responses.activate
    def test_get_instance_hsm_destination_path_server_ca_value_error(self):
        """
        test_get_instance_hsm_destination_path_server_ca_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas/5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f')
        mock_response = '{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        server_ca_id = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
            "server_ca_id": server_ca_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_hsm_destination_path_server_ca(**req_copy)

    def test_get_instance_hsm_destination_path_server_ca_value_error_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_path_server_ca_value_error.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_path_server_ca_value_error()

        # Disable retries and run test_get_instance_hsm_destination_path_server_ca_value_error.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_path_server_ca_value_error()


class TestUpdateInstanceHsmDestinationPathServerCa:
    """
    Test Class for update_instance_hsm_destination_path_server_ca
    """

    @responses.activate
    def test_update_instance_hsm_destination_path_server_ca_all_params(self):
        """
        update_instance_hsm_destination_path_server_ca()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas/5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f')
        mock_response = '{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ServerCaPatch model
        server_ca_patch_model = {}
        server_ca_patch_model['name'] = 'HSM1_Server_CA_renamed'
        server_ca_patch_model['description'] = 'testString'
        server_ca_patch_model['status'] = 'active'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        server_ca_id = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'
        server_ca_patch = server_ca_patch_model

        # Invoke method
        response = _service.update_instance_hsm_destination_path_server_ca(
            instance_id,
            destination_id,
            path_id,
            server_ca_id,
            server_ca_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == server_ca_patch

    def test_update_instance_hsm_destination_path_server_ca_all_params_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_path_server_ca_all_params.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_path_server_ca_all_params()

        # Disable retries and run test_update_instance_hsm_destination_path_server_ca_all_params.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_path_server_ca_all_params()

    @responses.activate
    def test_update_instance_hsm_destination_path_server_ca_value_error(self):
        """
        test_update_instance_hsm_destination_path_server_ca_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas/5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f')
        mock_response = '{"id": "5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f", "name": "HSM1_Server_CA", "description": "Primary CA for HSM node 1", "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T15:10:00.000Z", "status": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "created_at": "2026-07-09T15:10:00.000Z", "updated_at": "2026-07-09T15:20:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ServerCaPatch model
        server_ca_patch_model = {}
        server_ca_patch_model['name'] = 'HSM1_Server_CA_renamed'
        server_ca_patch_model['description'] = 'testString'
        server_ca_patch_model['status'] = 'active'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        server_ca_id = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'
        server_ca_patch = server_ca_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
            "server_ca_id": server_ca_id,
            "server_ca_patch": server_ca_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_hsm_destination_path_server_ca(**req_copy)

    def test_update_instance_hsm_destination_path_server_ca_value_error_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_path_server_ca_value_error.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_path_server_ca_value_error()

        # Disable retries and run test_update_instance_hsm_destination_path_server_ca_value_error.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_path_server_ca_value_error()


class TestDeleteInstanceHsmDestinationPathServerCa:
    """
    Test Class for delete_instance_hsm_destination_path_server_ca
    """

    @responses.activate
    def test_delete_instance_hsm_destination_path_server_ca_all_params(self):
        """
        delete_instance_hsm_destination_path_server_ca()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas/5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        server_ca_id = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'

        # Invoke method
        response = _service.delete_instance_hsm_destination_path_server_ca(
            instance_id,
            destination_id,
            path_id,
            server_ca_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_instance_hsm_destination_path_server_ca_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_path_server_ca_all_params.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_path_server_ca_all_params()

        # Disable retries and run test_delete_instance_hsm_destination_path_server_ca_all_params.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_path_server_ca_all_params()

    @responses.activate
    def test_delete_instance_hsm_destination_path_server_ca_value_error(self):
        """
        test_delete_instance_hsm_destination_path_server_ca_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/paths/fa3d1234-0000-0000-0000-000000000001/server_cas/5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        path_id = 'fa3d1234-0000-0000-0000-000000000001'
        server_ca_id = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "path_id": path_id,
            "server_ca_id": server_ca_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_hsm_destination_path_server_ca(**req_copy)

    def test_delete_instance_hsm_destination_path_server_ca_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_path_server_ca_value_error.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_path_server_ca_value_error()

        # Disable retries and run test_delete_instance_hsm_destination_path_server_ca_value_error.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_path_server_ca_value_error()


# endregion
##############################################################################
# End of Service: ServerCAs
##############################################################################

##############################################################################
# Start of Service: ClientCertificates
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


class TestListInstanceHsmDestinationClientCertificates:
    """
    Test Class for list_instance_hsm_destination_client_certificates
    """

    @responses.activate
    def test_list_instance_hsm_destination_client_certificates_all_params(self):
        """
        list_instance_hsm_destination_client_certificates()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates')
        mock_response = '{"client_certificates": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.list_instance_hsm_destination_client_certificates(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_hsm_destination_client_certificates_all_params_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_client_certificates_all_params.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_client_certificates_all_params()

        # Disable retries and run test_list_instance_hsm_destination_client_certificates_all_params.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_client_certificates_all_params()

    @responses.activate
    def test_list_instance_hsm_destination_client_certificates_value_error(self):
        """
        test_list_instance_hsm_destination_client_certificates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates')
        mock_response = '{"client_certificates": [{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_hsm_destination_client_certificates(**req_copy)

    def test_list_instance_hsm_destination_client_certificates_value_error_with_retries(self):
        # Enable retries and run test_list_instance_hsm_destination_client_certificates_value_error.
        _service.enable_retries()
        self.test_list_instance_hsm_destination_client_certificates_value_error()

        # Disable retries and run test_list_instance_hsm_destination_client_certificates_value_error.
        _service.disable_retries()
        self.test_list_instance_hsm_destination_client_certificates_value_error()


class TestCreateInstanceHsmDestinationClientCertificate:
    """
    Test Class for create_instance_hsm_destination_client_certificate
    """

    @responses.activate
    def test_create_instance_hsm_destination_client_certificate_all_params(self):
        """
        create_instance_hsm_destination_client_certificate()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates')
        mock_response = '{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        name = 'hsm-client-cert-prod'
        description = 'testString'

        # Invoke method
        response = _service.create_instance_hsm_destination_client_certificate(
            instance_id,
            destination_id,
            name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'hsm-client-cert-prod'
        assert req_body['description'] == 'testString'

    def test_create_instance_hsm_destination_client_certificate_all_params_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_client_certificate_all_params.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_client_certificate_all_params()

        # Disable retries and run test_create_instance_hsm_destination_client_certificate_all_params.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_client_certificate_all_params()

    @responses.activate
    def test_create_instance_hsm_destination_client_certificate_value_error(self):
        """
        test_create_instance_hsm_destination_client_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates')
        mock_response = '{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        name = 'hsm-client-cert-prod'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_hsm_destination_client_certificate(**req_copy)

    def test_create_instance_hsm_destination_client_certificate_value_error_with_retries(self):
        # Enable retries and run test_create_instance_hsm_destination_client_certificate_value_error.
        _service.enable_retries()
        self.test_create_instance_hsm_destination_client_certificate_value_error()

        # Disable retries and run test_create_instance_hsm_destination_client_certificate_value_error.
        _service.disable_retries()
        self.test_create_instance_hsm_destination_client_certificate_value_error()


class TestGetInstanceHsmDestinationClientCertificate:
    """
    Test Class for get_instance_hsm_destination_client_certificate
    """

    @responses.activate
    def test_get_instance_hsm_destination_client_certificate_all_params(self):
        """
        get_instance_hsm_destination_client_certificate()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7')
        mock_response = '{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        cert_id = '7c9e6679-7425-40de-944b-e07fc1f90ae7'

        # Invoke method
        response = _service.get_instance_hsm_destination_client_certificate(
            instance_id,
            destination_id,
            cert_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_hsm_destination_client_certificate_all_params_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_client_certificate_all_params.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_client_certificate_all_params()

        # Disable retries and run test_get_instance_hsm_destination_client_certificate_all_params.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_client_certificate_all_params()

    @responses.activate
    def test_get_instance_hsm_destination_client_certificate_value_error(self):
        """
        test_get_instance_hsm_destination_client_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7')
        mock_response = '{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        cert_id = '7c9e6679-7425-40de-944b-e07fc1f90ae7'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "cert_id": cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_hsm_destination_client_certificate(**req_copy)

    def test_get_instance_hsm_destination_client_certificate_value_error_with_retries(self):
        # Enable retries and run test_get_instance_hsm_destination_client_certificate_value_error.
        _service.enable_retries()
        self.test_get_instance_hsm_destination_client_certificate_value_error()

        # Disable retries and run test_get_instance_hsm_destination_client_certificate_value_error.
        _service.disable_retries()
        self.test_get_instance_hsm_destination_client_certificate_value_error()


class TestUpdateInstanceHsmDestinationClientCertificate:
    """
    Test Class for update_instance_hsm_destination_client_certificate
    """

    @responses.activate
    def test_update_instance_hsm_destination_client_certificate_all_params(self):
        """
        update_instance_hsm_destination_client_certificate()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7')
        mock_response = '{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ClientCertificatePatch model
        client_certificate_patch_model = {}
        client_certificate_patch_model['name'] = 'hsm-client-cert-renamed'
        client_certificate_patch_model['description'] = 'testString'
        client_certificate_patch_model['status'] = 'testString'
        client_certificate_patch_model['signed_cert'] = 'testString'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        cert_id = '7c9e6679-7425-40de-944b-e07fc1f90ae7'
        client_certificate_patch = client_certificate_patch_model

        # Invoke method
        response = _service.update_instance_hsm_destination_client_certificate(
            instance_id,
            destination_id,
            cert_id,
            client_certificate_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == client_certificate_patch

    def test_update_instance_hsm_destination_client_certificate_all_params_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_client_certificate_all_params.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_client_certificate_all_params()

        # Disable retries and run test_update_instance_hsm_destination_client_certificate_all_params.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_client_certificate_all_params()

    @responses.activate
    def test_update_instance_hsm_destination_client_certificate_value_error(self):
        """
        test_update_instance_hsm_destination_client_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7')
        mock_response = '{"id": "7c9e6679-7425-40de-944b-e07fc1f90ae7", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/hsm_destinations/b49ad385-0cb7-3694-a71c-2579d6e94b02/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7", "name": "hsm-client-cert-prod", "description": "Primary client cert for prod", "status": "status", "provisioning_state": "active", "health_state": "valid", "health_as_of": "2026-07-09T15:30:00.000Z", "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----", "csr_cn": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "signed_cert": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----", "expires_at": "2028-07-09T10:00:00.000Z", "created_at": "2026-07-09T10:00:00.000Z", "updated_at": "2026-07-09T11:00:00.000Z", "created_by": "iam-ServiceId-abc123", "updated_by": "iam-ServiceId-abc123"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ClientCertificatePatch model
        client_certificate_patch_model = {}
        client_certificate_patch_model['name'] = 'hsm-client-cert-renamed'
        client_certificate_patch_model['description'] = 'testString'
        client_certificate_patch_model['status'] = 'testString'
        client_certificate_patch_model['signed_cert'] = 'testString'

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        cert_id = '7c9e6679-7425-40de-944b-e07fc1f90ae7'
        client_certificate_patch = client_certificate_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "cert_id": cert_id,
            "client_certificate_patch": client_certificate_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_hsm_destination_client_certificate(**req_copy)

    def test_update_instance_hsm_destination_client_certificate_value_error_with_retries(self):
        # Enable retries and run test_update_instance_hsm_destination_client_certificate_value_error.
        _service.enable_retries()
        self.test_update_instance_hsm_destination_client_certificate_value_error()

        # Disable retries and run test_update_instance_hsm_destination_client_certificate_value_error.
        _service.disable_retries()
        self.test_update_instance_hsm_destination_client_certificate_value_error()


class TestDeleteInstanceHsmDestinationClientCertificate:
    """
    Test Class for delete_instance_hsm_destination_client_certificate
    """

    @responses.activate
    def test_delete_instance_hsm_destination_client_certificate_all_params(self):
        """
        delete_instance_hsm_destination_client_certificate()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        cert_id = '7c9e6679-7425-40de-944b-e07fc1f90ae7'

        # Invoke method
        response = _service.delete_instance_hsm_destination_client_certificate(
            instance_id,
            destination_id,
            cert_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_instance_hsm_destination_client_certificate_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_client_certificate_all_params.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_client_certificate_all_params()

        # Disable retries and run test_delete_instance_hsm_destination_client_certificate_all_params.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_client_certificate_all_params()

    @responses.activate
    def test_delete_instance_hsm_destination_client_certificate_value_error(self):
        """
        test_delete_instance_hsm_destination_client_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/fe5c5c27-3e44-474a-9484-55892e12d6d1/hsm_destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901/client_certificates/7c9e6679-7425-40de-944b-e07fc1f90ae7')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'fe5c5c27-3e44-474a-9484-55892e12d6d1'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        cert_id = '7c9e6679-7425-40de-944b-e07fc1f90ae7'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
            "cert_id": cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_hsm_destination_client_certificate(**req_copy)

    def test_delete_instance_hsm_destination_client_certificate_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_hsm_destination_client_certificate_value_error.
        _service.enable_retries()
        self.test_delete_instance_hsm_destination_client_certificate_value_error()

        # Disable retries and run test_delete_instance_hsm_destination_client_certificate_value_error.
        _service.disable_retries()
        self.test_delete_instance_hsm_destination_client_certificate_value_error()


# endregion
##############################################################################
# End of Service: ClientCertificates
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AsyncDeleteResponse:
    """
    Test Class for AsyncDeleteResponse
    """

    def test_async_delete_response_serialization(self):
        """
        Test serialization/deserialization for AsyncDeleteResponse
        """

        # Construct a json representation of a AsyncDeleteResponse model
        async_delete_response_model_json = {}
        async_delete_response_model_json['provisioning_state'] = 'deleting'

        # Construct a model instance of AsyncDeleteResponse by calling from_dict on the json representation
        async_delete_response_model = AsyncDeleteResponse.from_dict(async_delete_response_model_json)
        assert async_delete_response_model != False

        # Construct a model instance of AsyncDeleteResponse by calling from_dict on the json representation
        async_delete_response_model_dict = AsyncDeleteResponse.from_dict(async_delete_response_model_json).__dict__
        async_delete_response_model2 = AsyncDeleteResponse(**async_delete_response_model_dict)

        # Verify the model instances are equivalent
        assert async_delete_response_model == async_delete_response_model2

        # Convert model instance back to dict and verify no loss of data
        async_delete_response_model_json2 = async_delete_response_model.to_dict()
        assert async_delete_response_model_json2 == async_delete_response_model_json


class TestModel_AsyncHealthAckResponse:
    """
    Test Class for AsyncHealthAckResponse
    """

    def test_async_health_ack_response_serialization(self):
        """
        Test serialization/deserialization for AsyncHealthAckResponse
        """

        # Construct a json representation of a AsyncHealthAckResponse model
        async_health_ack_response_model_json = {}

        # Construct a model instance of AsyncHealthAckResponse by calling from_dict on the json representation
        async_health_ack_response_model = AsyncHealthAckResponse.from_dict(async_health_ack_response_model_json)
        assert async_health_ack_response_model != False

        # Construct a model instance of AsyncHealthAckResponse by calling from_dict on the json representation
        async_health_ack_response_model_dict = AsyncHealthAckResponse.from_dict(async_health_ack_response_model_json).__dict__
        async_health_ack_response_model2 = AsyncHealthAckResponse(**async_health_ack_response_model_dict)

        # Verify the model instances are equivalent
        assert async_health_ack_response_model == async_health_ack_response_model2

        # Convert model instance back to dict and verify no loss of data
        async_health_ack_response_model_json2 = async_health_ack_response_model.to_dict()
        assert async_health_ack_response_model_json2 == async_health_ack_response_model_json


class TestModel_AsyncHealthCheckAckResponse:
    """
    Test Class for AsyncHealthCheckAckResponse
    """

    def test_async_health_check_ack_response_serialization(self):
        """
        Test serialization/deserialization for AsyncHealthCheckAckResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        health_snapshot_client_cert_model = {}  # HealthSnapshotClientCert
        health_snapshot_client_cert_model['id'] = '7c9e6679-7425-40de-944b-e07fc1f90ae7'
        health_snapshot_client_cert_model['name'] = 'hsm-client-cert-prod'
        health_snapshot_client_cert_model['health_state'] = 'valid'

        health_snapshot_hsmha_group_model = {}  # HealthSnapshotHSMHAGroup
        health_snapshot_hsmha_group_model['id'] = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'
        health_snapshot_hsmha_group_model['name'] = 'production-ha-group'
        health_snapshot_hsmha_group_model['health_state'] = 'healthy'

        health_snapshot_server_ca_model = {}  # HealthSnapshotServerCa
        health_snapshot_server_ca_model['id'] = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'
        health_snapshot_server_ca_model['name'] = 'HSM1_Server_CA'
        health_snapshot_server_ca_model['health_state'] = 'valid'

        health_snapshot_connection_model = {}  # HealthSnapshotConnection
        health_snapshot_connection_model['id'] = 'fa3d1234-0000-0000-0000-000000000001'
        health_snapshot_connection_model['name'] = 'hsm-node-1'
        health_snapshot_connection_model['health_state'] = 'healthy'
        health_snapshot_connection_model['server_cas'] = [health_snapshot_server_ca_model]

        # Construct a json representation of a AsyncHealthCheckAckResponse model
        async_health_check_ack_response_model_json = {}
        async_health_check_ack_response_model_json['destination_id'] = 'b49ad385-0cb7-3694-a71c-2579d6e94b02'
        async_health_check_ack_response_model_json['health_state'] = 'healthy'
        async_health_check_ack_response_model_json['health_as_of'] = '2026-07-09T15:30:00Z'
        async_health_check_ack_response_model_json['client_certificates'] = [health_snapshot_client_cert_model]
        async_health_check_ack_response_model_json['ha_groups'] = [health_snapshot_hsmha_group_model]
        async_health_check_ack_response_model_json['paths'] = [health_snapshot_connection_model]

        # Construct a model instance of AsyncHealthCheckAckResponse by calling from_dict on the json representation
        async_health_check_ack_response_model = AsyncHealthCheckAckResponse.from_dict(async_health_check_ack_response_model_json)
        assert async_health_check_ack_response_model != False

        # Construct a model instance of AsyncHealthCheckAckResponse by calling from_dict on the json representation
        async_health_check_ack_response_model_dict = AsyncHealthCheckAckResponse.from_dict(async_health_check_ack_response_model_json).__dict__
        async_health_check_ack_response_model2 = AsyncHealthCheckAckResponse(**async_health_check_ack_response_model_dict)

        # Verify the model instances are equivalent
        assert async_health_check_ack_response_model == async_health_check_ack_response_model2

        # Convert model instance back to dict and verify no loss of data
        async_health_check_ack_response_model_json2 = async_health_check_ack_response_model.to_dict()
        assert async_health_check_ack_response_model_json2 == async_health_check_ack_response_model_json


class TestModel_ClientCertificate:
    """
    Test Class for ClientCertificate
    """

    def test_client_certificate_serialization(self):
        """
        Test serialization/deserialization for ClientCertificate
        """

        # Construct a json representation of a ClientCertificate model
        client_certificate_model_json = {}
        client_certificate_model_json['name'] = 'hsm-client-cert-prod'
        client_certificate_model_json['description'] = 'Primary client cert for prod'
        client_certificate_model_json['status'] = 'testString'
        client_certificate_model_json['provisioning_state'] = 'active'
        client_certificate_model_json['health_state'] = 'valid'
        client_certificate_model_json['health_as_of'] = '2026-07-09T15:30:00Z'
        client_certificate_model_json['csr'] = '-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----'
        client_certificate_model_json['csr_cn'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        client_certificate_model_json['signed_cert'] = '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        client_certificate_model_json['expires_at'] = '2028-07-09T10:00:00Z'
        client_certificate_model_json['created_at'] = '2026-07-09T10:00:00Z'
        client_certificate_model_json['updated_at'] = '2026-07-09T11:00:00Z'
        client_certificate_model_json['created_by'] = 'iam-ServiceId-abc123'
        client_certificate_model_json['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a model instance of ClientCertificate by calling from_dict on the json representation
        client_certificate_model = ClientCertificate.from_dict(client_certificate_model_json)
        assert client_certificate_model != False

        # Construct a model instance of ClientCertificate by calling from_dict on the json representation
        client_certificate_model_dict = ClientCertificate.from_dict(client_certificate_model_json).__dict__
        client_certificate_model2 = ClientCertificate(**client_certificate_model_dict)

        # Verify the model instances are equivalent
        assert client_certificate_model == client_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        client_certificate_model_json2 = client_certificate_model.to_dict()
        assert client_certificate_model_json2 == client_certificate_model_json


class TestModel_ClientCertificateCollection:
    """
    Test Class for ClientCertificateCollection
    """

    def test_client_certificate_collection_serialization(self):
        """
        Test serialization/deserialization for ClientCertificateCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        client_certificate_model = {}  # ClientCertificate
        client_certificate_model['name'] = 'hsm-client-cert-prod'
        client_certificate_model['description'] = 'Primary client cert for prod'
        client_certificate_model['status'] = 'testString'
        client_certificate_model['provisioning_state'] = 'active'
        client_certificate_model['health_state'] = 'valid'
        client_certificate_model['health_as_of'] = '2026-07-09T15:30:00Z'
        client_certificate_model['csr'] = '-----BEGIN CERTIFICATE REQUEST-----\nMIICvDCCAaQCAQAwdzEL...\n-----END CERTIFICATE REQUEST-----'
        client_certificate_model['csr_cn'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        client_certificate_model['signed_cert'] = '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        client_certificate_model['expires_at'] = '2028-07-09T10:00:00Z'
        client_certificate_model['created_at'] = '2026-07-09T10:00:00Z'
        client_certificate_model['updated_at'] = '2026-07-09T11:00:00Z'
        client_certificate_model['created_by'] = 'iam-ServiceId-abc123'
        client_certificate_model['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a json representation of a ClientCertificateCollection model
        client_certificate_collection_model_json = {}
        client_certificate_collection_model_json['client_certificates'] = [client_certificate_model]

        # Construct a model instance of ClientCertificateCollection by calling from_dict on the json representation
        client_certificate_collection_model = ClientCertificateCollection.from_dict(client_certificate_collection_model_json)
        assert client_certificate_collection_model != False

        # Construct a model instance of ClientCertificateCollection by calling from_dict on the json representation
        client_certificate_collection_model_dict = ClientCertificateCollection.from_dict(client_certificate_collection_model_json).__dict__
        client_certificate_collection_model2 = ClientCertificateCollection(**client_certificate_collection_model_dict)

        # Verify the model instances are equivalent
        assert client_certificate_collection_model == client_certificate_collection_model2

        # Convert model instance back to dict and verify no loss of data
        client_certificate_collection_model_json2 = client_certificate_collection_model.to_dict()
        assert client_certificate_collection_model_json2 == client_certificate_collection_model_json


class TestModel_ClientCertificatePatch:
    """
    Test Class for ClientCertificatePatch
    """

    def test_client_certificate_patch_serialization(self):
        """
        Test serialization/deserialization for ClientCertificatePatch
        """

        # Construct a json representation of a ClientCertificatePatch model
        client_certificate_patch_model_json = {}
        client_certificate_patch_model_json['name'] = 'testString'
        client_certificate_patch_model_json['description'] = 'testString'
        client_certificate_patch_model_json['status'] = 'testString'
        client_certificate_patch_model_json['signed_cert'] = 'testString'

        # Construct a model instance of ClientCertificatePatch by calling from_dict on the json representation
        client_certificate_patch_model = ClientCertificatePatch.from_dict(client_certificate_patch_model_json)
        assert client_certificate_patch_model != False

        # Construct a model instance of ClientCertificatePatch by calling from_dict on the json representation
        client_certificate_patch_model_dict = ClientCertificatePatch.from_dict(client_certificate_patch_model_json).__dict__
        client_certificate_patch_model2 = ClientCertificatePatch(**client_certificate_patch_model_dict)

        # Verify the model instances are equivalent
        assert client_certificate_patch_model == client_certificate_patch_model2

        # Convert model instance back to dict and verify no loss of data
        client_certificate_patch_model_json2 = client_certificate_patch_model.to_dict()
        assert client_certificate_patch_model_json2 == client_certificate_patch_model_json


class TestModel_Destination:
    """
    Test Class for Destination
    """

    def test_destination_serialization(self):
        """
        Test serialization/deserialization for Destination
        """

        # Construct a json representation of a Destination model
        destination_model_json = {}
        destination_model_json['id'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        destination_model_json['name'] = 'testString'
        destination_model_json['type'] = 'ibm_cloud_database'
        destination_model_json['description'] = 'testString'
        destination_model_json['state'] = 'not_started'
        destination_model_json['created_at'] = '2019-01-01T12:00:00Z'
        destination_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of Destination by calling from_dict on the json representation
        destination_model = Destination.from_dict(destination_model_json)
        assert destination_model != False

        # Construct a model instance of Destination by calling from_dict on the json representation
        destination_model_dict = Destination.from_dict(destination_model_json).__dict__
        destination_model2 = Destination(**destination_model_dict)

        # Verify the model instances are equivalent
        assert destination_model == destination_model2

        # Convert model instance back to dict and verify no loss of data
        destination_model_json2 = destination_model.to_dict()
        assert destination_model_json2 == destination_model_json


class TestModel_DestinationCollection:
    """
    Test Class for DestinationCollection
    """

    def test_destination_collection_serialization(self):
        """
        Test serialization/deserialization for DestinationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_model = {}  # Destination
        destination_model['id'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        destination_model['name'] = 'testString'
        destination_model['type'] = 'ibm_cloud_database'
        destination_model['description'] = 'testString'
        destination_model['state'] = 'not_started'
        destination_model['created_at'] = '2019-01-01T12:00:00Z'
        destination_model['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a DestinationCollection model
        destination_collection_model_json = {}
        destination_collection_model_json['destinations'] = [destination_model]
        destination_collection_model_json['total'] = 0

        # Construct a model instance of DestinationCollection by calling from_dict on the json representation
        destination_collection_model = DestinationCollection.from_dict(destination_collection_model_json)
        assert destination_collection_model != False

        # Construct a model instance of DestinationCollection by calling from_dict on the json representation
        destination_collection_model_dict = DestinationCollection.from_dict(destination_collection_model_json).__dict__
        destination_collection_model2 = DestinationCollection(**destination_collection_model_dict)

        # Verify the model instances are equivalent
        assert destination_collection_model == destination_collection_model2

        # Convert model instance back to dict and verify no loss of data
        destination_collection_model_json2 = destination_collection_model.to_dict()
        assert destination_collection_model_json2 == destination_collection_model_json


class TestModel_DestinationHealthSnapshot:
    """
    Test Class for DestinationHealthSnapshot
    """

    def test_destination_health_snapshot_serialization(self):
        """
        Test serialization/deserialization for DestinationHealthSnapshot
        """

        # Construct dict forms of any model objects needed in order to build this model.

        health_snapshot_client_cert_model = {}  # HealthSnapshotClientCert
        health_snapshot_client_cert_model['id'] = '7c9e6679-7425-40de-944b-e07fc1f90ae7'
        health_snapshot_client_cert_model['name'] = 'hsm-client-cert-prod'
        health_snapshot_client_cert_model['health_state'] = 'valid'

        health_snapshot_hsmha_group_model = {}  # HealthSnapshotHSMHAGroup
        health_snapshot_hsmha_group_model['id'] = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'
        health_snapshot_hsmha_group_model['name'] = 'production-ha-group'
        health_snapshot_hsmha_group_model['health_state'] = 'healthy'

        health_snapshot_server_ca_model = {}  # HealthSnapshotServerCa
        health_snapshot_server_ca_model['id'] = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'
        health_snapshot_server_ca_model['name'] = 'HSM1_Server_CA'
        health_snapshot_server_ca_model['health_state'] = 'valid'

        health_snapshot_connection_model = {}  # HealthSnapshotConnection
        health_snapshot_connection_model['id'] = 'fa3d1234-0000-0000-0000-000000000001'
        health_snapshot_connection_model['name'] = 'hsm-node-1'
        health_snapshot_connection_model['health_state'] = 'healthy'
        health_snapshot_connection_model['server_cas'] = [health_snapshot_server_ca_model]

        # Construct a json representation of a DestinationHealthSnapshot model
        destination_health_snapshot_model_json = {}
        destination_health_snapshot_model_json['destination_id'] = 'b49ad385-0cb7-3694-a71c-2579d6e94b02'
        destination_health_snapshot_model_json['health_state'] = 'healthy'
        destination_health_snapshot_model_json['health_as_of'] = '2026-07-09T15:30:00Z'
        destination_health_snapshot_model_json['client_certificates'] = [health_snapshot_client_cert_model]
        destination_health_snapshot_model_json['ha_groups'] = [health_snapshot_hsmha_group_model]
        destination_health_snapshot_model_json['paths'] = [health_snapshot_connection_model]

        # Construct a model instance of DestinationHealthSnapshot by calling from_dict on the json representation
        destination_health_snapshot_model = DestinationHealthSnapshot.from_dict(destination_health_snapshot_model_json)
        assert destination_health_snapshot_model != False

        # Construct a model instance of DestinationHealthSnapshot by calling from_dict on the json representation
        destination_health_snapshot_model_dict = DestinationHealthSnapshot.from_dict(destination_health_snapshot_model_json).__dict__
        destination_health_snapshot_model2 = DestinationHealthSnapshot(**destination_health_snapshot_model_dict)

        # Verify the model instances are equivalent
        assert destination_health_snapshot_model == destination_health_snapshot_model2

        # Convert model instance back to dict and verify no loss of data
        destination_health_snapshot_model_json2 = destination_health_snapshot_model.to_dict()
        assert destination_health_snapshot_model_json2 == destination_health_snapshot_model_json


class TestModel_DestinationPatch:
    """
    Test Class for DestinationPatch
    """

    def test_destination_patch_serialization(self):
        """
        Test serialization/deserialization for DestinationPatch
        """

        # Construct a json representation of a DestinationPatch model
        destination_patch_model_json = {}
        destination_patch_model_json['name'] = 'production-postgres-db'
        destination_patch_model_json['description'] = 'Updated description for production database'

        # Construct a model instance of DestinationPatch by calling from_dict on the json representation
        destination_patch_model = DestinationPatch.from_dict(destination_patch_model_json)
        assert destination_patch_model != False

        # Construct a model instance of DestinationPatch by calling from_dict on the json representation
        destination_patch_model_dict = DestinationPatch.from_dict(destination_patch_model_json).__dict__
        destination_patch_model2 = DestinationPatch(**destination_patch_model_dict)

        # Verify the model instances are equivalent
        assert destination_patch_model == destination_patch_model2

        # Convert model instance back to dict and verify no loss of data
        destination_patch_model_json2 = destination_patch_model.to_dict()
        assert destination_patch_model_json2 == destination_patch_model_json


class TestModel_HSMDestination:
    """
    Test Class for HSMDestination
    """

    def test_hsm_destination_serialization(self):
        """
        Test serialization/deserialization for HSMDestination
        """

        # Construct a json representation of a HSMDestination model
        hsm_destination_model_json = {}
        hsm_destination_model_json['name'] = 'prod-hsm-destination'
        hsm_destination_model_json['description'] = 'Primary Thales Luna destination'
        hsm_destination_model_json['vendor'] = 'thales_luna'
        hsm_destination_model_json['provisioning_state'] = 'completed'
        hsm_destination_model_json['health_state'] = 'healthy'
        hsm_destination_model_json['health_as_of'] = '2026-07-09T15:30:00Z'
        hsm_destination_model_json['created_at'] = '2026-07-09T15:00:00Z'
        hsm_destination_model_json['updated_at'] = '2026-07-09T15:30:00Z'
        hsm_destination_model_json['created_by'] = 'iam-ServiceId-abc123'
        hsm_destination_model_json['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a model instance of HSMDestination by calling from_dict on the json representation
        hsm_destination_model = HSMDestination.from_dict(hsm_destination_model_json)
        assert hsm_destination_model != False

        # Construct a model instance of HSMDestination by calling from_dict on the json representation
        hsm_destination_model_dict = HSMDestination.from_dict(hsm_destination_model_json).__dict__
        hsm_destination_model2 = HSMDestination(**hsm_destination_model_dict)

        # Verify the model instances are equivalent
        assert hsm_destination_model == hsm_destination_model2

        # Convert model instance back to dict and verify no loss of data
        hsm_destination_model_json2 = hsm_destination_model.to_dict()
        assert hsm_destination_model_json2 == hsm_destination_model_json


class TestModel_HSMDestinationCollection:
    """
    Test Class for HSMDestinationCollection
    """

    def test_hsm_destination_collection_serialization(self):
        """
        Test serialization/deserialization for HSMDestinationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hsm_destination_model = {}  # HSMDestination
        hsm_destination_model['name'] = 'prod-hsm-destination'
        hsm_destination_model['description'] = 'Primary Thales Luna destination'
        hsm_destination_model['vendor'] = 'thales_luna'
        hsm_destination_model['provisioning_state'] = 'completed'
        hsm_destination_model['health_state'] = 'healthy'
        hsm_destination_model['health_as_of'] = '2026-07-09T15:30:00Z'
        hsm_destination_model['created_at'] = '2026-07-09T15:00:00Z'
        hsm_destination_model['updated_at'] = '2026-07-09T15:30:00Z'
        hsm_destination_model['created_by'] = 'iam-ServiceId-abc123'
        hsm_destination_model['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a json representation of a HSMDestinationCollection model
        hsm_destination_collection_model_json = {}
        hsm_destination_collection_model_json['total_count'] = 1
        hsm_destination_collection_model_json['hsm_destinations'] = [hsm_destination_model]

        # Construct a model instance of HSMDestinationCollection by calling from_dict on the json representation
        hsm_destination_collection_model = HSMDestinationCollection.from_dict(hsm_destination_collection_model_json)
        assert hsm_destination_collection_model != False

        # Construct a model instance of HSMDestinationCollection by calling from_dict on the json representation
        hsm_destination_collection_model_dict = HSMDestinationCollection.from_dict(hsm_destination_collection_model_json).__dict__
        hsm_destination_collection_model2 = HSMDestinationCollection(**hsm_destination_collection_model_dict)

        # Verify the model instances are equivalent
        assert hsm_destination_collection_model == hsm_destination_collection_model2

        # Convert model instance back to dict and verify no loss of data
        hsm_destination_collection_model_json2 = hsm_destination_collection_model.to_dict()
        assert hsm_destination_collection_model_json2 == hsm_destination_collection_model_json


class TestModel_HSMDestinationPatch:
    """
    Test Class for HSMDestinationPatch
    """

    def test_hsm_destination_patch_serialization(self):
        """
        Test serialization/deserialization for HSMDestinationPatch
        """

        # Construct a json representation of a HSMDestinationPatch model
        hsm_destination_patch_model_json = {}
        hsm_destination_patch_model_json['name'] = 'testString'
        hsm_destination_patch_model_json['description'] = 'testString'

        # Construct a model instance of HSMDestinationPatch by calling from_dict on the json representation
        hsm_destination_patch_model = HSMDestinationPatch.from_dict(hsm_destination_patch_model_json)
        assert hsm_destination_patch_model != False

        # Construct a model instance of HSMDestinationPatch by calling from_dict on the json representation
        hsm_destination_patch_model_dict = HSMDestinationPatch.from_dict(hsm_destination_patch_model_json).__dict__
        hsm_destination_patch_model2 = HSMDestinationPatch(**hsm_destination_patch_model_dict)

        # Verify the model instances are equivalent
        assert hsm_destination_patch_model == hsm_destination_patch_model2

        # Convert model instance back to dict and verify no loss of data
        hsm_destination_patch_model_json2 = hsm_destination_patch_model.to_dict()
        assert hsm_destination_patch_model_json2 == hsm_destination_patch_model_json


class TestModel_HSMHAGroup:
    """
    Test Class for HSMHAGroup
    """

    def test_hsmha_group_serialization(self):
        """
        Test serialization/deserialization for HSMHAGroup
        """

        # Construct a json representation of a HSMHAGroup model
        hsmha_group_model_json = {}
        hsmha_group_model_json['name'] = 'production-ha-group'
        hsmha_group_model_json['description'] = 'Primary HA Group for prod'
        hsmha_group_model_json['provisioning_state'] = 'completed'
        hsmha_group_model_json['health_state'] = 'healthy'
        hsmha_group_model_json['health_as_of'] = '2026-07-09T16:00:00Z'
        hsmha_group_model_json['group_label'] = 'prod_ha_group'
        hsmha_group_model_json['group_serial'] = '11323465009866'
        hsmha_group_model_json['member_serials'] = ['123456', '123457']
        hsmha_group_model_json['created_at'] = '2026-07-09T15:00:00Z'
        hsmha_group_model_json['updated_at'] = '2026-07-09T16:00:00Z'
        hsmha_group_model_json['created_by'] = 'iam-ServiceId-abc123'
        hsmha_group_model_json['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a model instance of HSMHAGroup by calling from_dict on the json representation
        hsmha_group_model = HSMHAGroup.from_dict(hsmha_group_model_json)
        assert hsmha_group_model != False

        # Construct a model instance of HSMHAGroup by calling from_dict on the json representation
        hsmha_group_model_dict = HSMHAGroup.from_dict(hsmha_group_model_json).__dict__
        hsmha_group_model2 = HSMHAGroup(**hsmha_group_model_dict)

        # Verify the model instances are equivalent
        assert hsmha_group_model == hsmha_group_model2

        # Convert model instance back to dict and verify no loss of data
        hsmha_group_model_json2 = hsmha_group_model.to_dict()
        assert hsmha_group_model_json2 == hsmha_group_model_json


class TestModel_HSMHAGroupCollection:
    """
    Test Class for HSMHAGroupCollection
    """

    def test_hsmha_group_collection_serialization(self):
        """
        Test serialization/deserialization for HSMHAGroupCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hsmha_group_model = {}  # HSMHAGroup
        hsmha_group_model['name'] = 'production-ha-group'
        hsmha_group_model['description'] = 'Primary HA Group for prod'
        hsmha_group_model['provisioning_state'] = 'completed'
        hsmha_group_model['health_state'] = 'healthy'
        hsmha_group_model['health_as_of'] = '2026-07-09T16:00:00Z'
        hsmha_group_model['group_label'] = 'prod_ha_group'
        hsmha_group_model['group_serial'] = '11323465009866'
        hsmha_group_model['member_serials'] = ['123456', '123457']
        hsmha_group_model['created_at'] = '2026-07-09T15:00:00Z'
        hsmha_group_model['updated_at'] = '2026-07-09T16:00:00Z'
        hsmha_group_model['created_by'] = 'iam-ServiceId-abc123'
        hsmha_group_model['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a json representation of a HSMHAGroupCollection model
        hsmha_group_collection_model_json = {}
        hsmha_group_collection_model_json['ha_groups'] = [hsmha_group_model]

        # Construct a model instance of HSMHAGroupCollection by calling from_dict on the json representation
        hsmha_group_collection_model = HSMHAGroupCollection.from_dict(hsmha_group_collection_model_json)
        assert hsmha_group_collection_model != False

        # Construct a model instance of HSMHAGroupCollection by calling from_dict on the json representation
        hsmha_group_collection_model_dict = HSMHAGroupCollection.from_dict(hsmha_group_collection_model_json).__dict__
        hsmha_group_collection_model2 = HSMHAGroupCollection(**hsmha_group_collection_model_dict)

        # Verify the model instances are equivalent
        assert hsmha_group_collection_model == hsmha_group_collection_model2

        # Convert model instance back to dict and verify no loss of data
        hsmha_group_collection_model_json2 = hsmha_group_collection_model.to_dict()
        assert hsmha_group_collection_model_json2 == hsmha_group_collection_model_json


class TestModel_HSMHAGroupPatch:
    """
    Test Class for HSMHAGroupPatch
    """

    def test_hsmha_group_patch_serialization(self):
        """
        Test serialization/deserialization for HSMHAGroupPatch
        """

        # Construct a json representation of a HSMHAGroupPatch model
        hsmha_group_patch_model_json = {}
        hsmha_group_patch_model_json['name'] = 'dr-ha-group'
        hsmha_group_patch_model_json['description'] = 'DR HA Group for failover'
        hsmha_group_patch_model_json['member_serials'] = ['123456', '123457', '123458']

        # Construct a model instance of HSMHAGroupPatch by calling from_dict on the json representation
        hsmha_group_patch_model = HSMHAGroupPatch.from_dict(hsmha_group_patch_model_json)
        assert hsmha_group_patch_model != False

        # Construct a model instance of HSMHAGroupPatch by calling from_dict on the json representation
        hsmha_group_patch_model_dict = HSMHAGroupPatch.from_dict(hsmha_group_patch_model_json).__dict__
        hsmha_group_patch_model2 = HSMHAGroupPatch(**hsmha_group_patch_model_dict)

        # Verify the model instances are equivalent
        assert hsmha_group_patch_model == hsmha_group_patch_model2

        # Convert model instance back to dict and verify no loss of data
        hsmha_group_patch_model_json2 = hsmha_group_patch_model.to_dict()
        assert hsmha_group_patch_model_json2 == hsmha_group_patch_model_json


class TestModel_HSMPathReset:
    """
    Test Class for HSMPathReset
    """

    def test_hsm_path_reset_serialization(self):
        """
        Test serialization/deserialization for HSMPathReset
        """

        # Construct a json representation of a HSMPathReset model
        hsm_path_reset_model_json = {}
        hsm_path_reset_model_json['provisioning_state'] = 'completed'

        # Construct a model instance of HSMPathReset by calling from_dict on the json representation
        hsm_path_reset_model = HSMPathReset.from_dict(hsm_path_reset_model_json)
        assert hsm_path_reset_model != False

        # Construct a model instance of HSMPathReset by calling from_dict on the json representation
        hsm_path_reset_model_dict = HSMPathReset.from_dict(hsm_path_reset_model_json).__dict__
        hsm_path_reset_model2 = HSMPathReset(**hsm_path_reset_model_dict)

        # Verify the model instances are equivalent
        assert hsm_path_reset_model == hsm_path_reset_model2

        # Convert model instance back to dict and verify no loss of data
        hsm_path_reset_model_json2 = hsm_path_reset_model.to_dict()
        assert hsm_path_reset_model_json2 == hsm_path_reset_model_json


class TestModel_HealthSnapshotClientCert:
    """
    Test Class for HealthSnapshotClientCert
    """

    def test_health_snapshot_client_cert_serialization(self):
        """
        Test serialization/deserialization for HealthSnapshotClientCert
        """

        # Construct a json representation of a HealthSnapshotClientCert model
        health_snapshot_client_cert_model_json = {}
        health_snapshot_client_cert_model_json['id'] = '7c9e6679-7425-40de-944b-e07fc1f90ae7'
        health_snapshot_client_cert_model_json['name'] = 'hsm-client-cert-prod'
        health_snapshot_client_cert_model_json['health_state'] = 'valid'

        # Construct a model instance of HealthSnapshotClientCert by calling from_dict on the json representation
        health_snapshot_client_cert_model = HealthSnapshotClientCert.from_dict(health_snapshot_client_cert_model_json)
        assert health_snapshot_client_cert_model != False

        # Construct a model instance of HealthSnapshotClientCert by calling from_dict on the json representation
        health_snapshot_client_cert_model_dict = HealthSnapshotClientCert.from_dict(health_snapshot_client_cert_model_json).__dict__
        health_snapshot_client_cert_model2 = HealthSnapshotClientCert(**health_snapshot_client_cert_model_dict)

        # Verify the model instances are equivalent
        assert health_snapshot_client_cert_model == health_snapshot_client_cert_model2

        # Convert model instance back to dict and verify no loss of data
        health_snapshot_client_cert_model_json2 = health_snapshot_client_cert_model.to_dict()
        assert health_snapshot_client_cert_model_json2 == health_snapshot_client_cert_model_json


class TestModel_HealthSnapshotConnection:
    """
    Test Class for HealthSnapshotConnection
    """

    def test_health_snapshot_connection_serialization(self):
        """
        Test serialization/deserialization for HealthSnapshotConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        health_snapshot_server_ca_model = {}  # HealthSnapshotServerCa
        health_snapshot_server_ca_model['id'] = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'
        health_snapshot_server_ca_model['name'] = 'HSM1_Server_CA'
        health_snapshot_server_ca_model['health_state'] = 'valid'

        # Construct a json representation of a HealthSnapshotConnection model
        health_snapshot_connection_model_json = {}
        health_snapshot_connection_model_json['id'] = 'fa3d1234-0000-0000-0000-000000000001'
        health_snapshot_connection_model_json['name'] = 'hsm-node-1'
        health_snapshot_connection_model_json['health_state'] = 'healthy'
        health_snapshot_connection_model_json['server_cas'] = [health_snapshot_server_ca_model]

        # Construct a model instance of HealthSnapshotConnection by calling from_dict on the json representation
        health_snapshot_connection_model = HealthSnapshotConnection.from_dict(health_snapshot_connection_model_json)
        assert health_snapshot_connection_model != False

        # Construct a model instance of HealthSnapshotConnection by calling from_dict on the json representation
        health_snapshot_connection_model_dict = HealthSnapshotConnection.from_dict(health_snapshot_connection_model_json).__dict__
        health_snapshot_connection_model2 = HealthSnapshotConnection(**health_snapshot_connection_model_dict)

        # Verify the model instances are equivalent
        assert health_snapshot_connection_model == health_snapshot_connection_model2

        # Convert model instance back to dict and verify no loss of data
        health_snapshot_connection_model_json2 = health_snapshot_connection_model.to_dict()
        assert health_snapshot_connection_model_json2 == health_snapshot_connection_model_json


class TestModel_HealthSnapshotHSMHAGroup:
    """
    Test Class for HealthSnapshotHSMHAGroup
    """

    def test_health_snapshot_hsmha_group_serialization(self):
        """
        Test serialization/deserialization for HealthSnapshotHSMHAGroup
        """

        # Construct a json representation of a HealthSnapshotHSMHAGroup model
        health_snapshot_hsmha_group_model_json = {}
        health_snapshot_hsmha_group_model_json['id'] = 'ee52ebb6-1728-4580-8ede-13f6504e3ae0'
        health_snapshot_hsmha_group_model_json['name'] = 'production-ha-group'
        health_snapshot_hsmha_group_model_json['health_state'] = 'healthy'

        # Construct a model instance of HealthSnapshotHSMHAGroup by calling from_dict on the json representation
        health_snapshot_hsmha_group_model = HealthSnapshotHSMHAGroup.from_dict(health_snapshot_hsmha_group_model_json)
        assert health_snapshot_hsmha_group_model != False

        # Construct a model instance of HealthSnapshotHSMHAGroup by calling from_dict on the json representation
        health_snapshot_hsmha_group_model_dict = HealthSnapshotHSMHAGroup.from_dict(health_snapshot_hsmha_group_model_json).__dict__
        health_snapshot_hsmha_group_model2 = HealthSnapshotHSMHAGroup(**health_snapshot_hsmha_group_model_dict)

        # Verify the model instances are equivalent
        assert health_snapshot_hsmha_group_model == health_snapshot_hsmha_group_model2

        # Convert model instance back to dict and verify no loss of data
        health_snapshot_hsmha_group_model_json2 = health_snapshot_hsmha_group_model.to_dict()
        assert health_snapshot_hsmha_group_model_json2 == health_snapshot_hsmha_group_model_json


class TestModel_HealthSnapshotServerCa:
    """
    Test Class for HealthSnapshotServerCa
    """

    def test_health_snapshot_server_ca_serialization(self):
        """
        Test serialization/deserialization for HealthSnapshotServerCa
        """

        # Construct a json representation of a HealthSnapshotServerCa model
        health_snapshot_server_ca_model_json = {}
        health_snapshot_server_ca_model_json['id'] = '5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f'
        health_snapshot_server_ca_model_json['name'] = 'HSM1_Server_CA'
        health_snapshot_server_ca_model_json['health_state'] = 'valid'

        # Construct a model instance of HealthSnapshotServerCa by calling from_dict on the json representation
        health_snapshot_server_ca_model = HealthSnapshotServerCa.from_dict(health_snapshot_server_ca_model_json)
        assert health_snapshot_server_ca_model != False

        # Construct a model instance of HealthSnapshotServerCa by calling from_dict on the json representation
        health_snapshot_server_ca_model_dict = HealthSnapshotServerCa.from_dict(health_snapshot_server_ca_model_json).__dict__
        health_snapshot_server_ca_model2 = HealthSnapshotServerCa(**health_snapshot_server_ca_model_dict)

        # Verify the model instances are equivalent
        assert health_snapshot_server_ca_model == health_snapshot_server_ca_model2

        # Convert model instance back to dict and verify no loss of data
        health_snapshot_server_ca_model_json2 = health_snapshot_server_ca_model.to_dict()
        assert health_snapshot_server_ca_model_json2 == health_snapshot_server_ca_model_json


class TestModel_IbmCloudDatabaseDestination:
    """
    Test Class for IbmCloudDatabaseDestination
    """

    def test_ibm_cloud_database_destination_serialization(self):
        """
        Test serialization/deserialization for IbmCloudDatabaseDestination
        """

        # Construct a json representation of a IbmCloudDatabaseDestination model
        ibm_cloud_database_destination_model_json = {}
        ibm_cloud_database_destination_model_json['id'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        ibm_cloud_database_destination_model_json['name'] = 'testString'
        ibm_cloud_database_destination_model_json['type'] = 'ibm_cloud_database'
        ibm_cloud_database_destination_model_json['description'] = 'testString'
        ibm_cloud_database_destination_model_json['state'] = 'not_started'
        ibm_cloud_database_destination_model_json['created_at'] = '2019-01-01T12:00:00Z'
        ibm_cloud_database_destination_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        ibm_cloud_database_destination_model_json['crn'] = 'testString'

        # Construct a model instance of IbmCloudDatabaseDestination by calling from_dict on the json representation
        ibm_cloud_database_destination_model = IbmCloudDatabaseDestination.from_dict(ibm_cloud_database_destination_model_json)
        assert ibm_cloud_database_destination_model != False

        # Construct a model instance of IbmCloudDatabaseDestination by calling from_dict on the json representation
        ibm_cloud_database_destination_model_dict = IbmCloudDatabaseDestination.from_dict(ibm_cloud_database_destination_model_json).__dict__
        ibm_cloud_database_destination_model2 = IbmCloudDatabaseDestination(**ibm_cloud_database_destination_model_dict)

        # Verify the model instances are equivalent
        assert ibm_cloud_database_destination_model == ibm_cloud_database_destination_model2

        # Convert model instance back to dict and verify no loss of data
        ibm_cloud_database_destination_model_json2 = ibm_cloud_database_destination_model.to_dict()
        assert ibm_cloud_database_destination_model_json2 == ibm_cloud_database_destination_model_json


class TestModel_Instance:
    """
    Test Class for Instance
    """

    def test_instance_serialization(self):
        """
        Test serialization/deserialization for Instance
        """

        # Construct dict forms of any model objects needed in order to build this model.

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
        instance_model_json['id'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        instance_model_json['name'] = 'testString'
        instance_model_json['instance_crn'] = 'crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::'
        instance_model_json['plan'] = 'dedicated'
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


class TestModel_Path:
    """
    Test Class for Path
    """

    def test_path_serialization(self):
        """
        Test serialization/deserialization for Path
        """

        # Construct a json representation of a Path model
        path_model_json = {}
        path_model_json['name'] = 'hsm-node-1'
        path_model_json['description'] = 'Primary HSM node for prod'
        path_model_json['crn'] = 'crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1'
        path_model_json['provisioning_state'] = 'completed'
        path_model_json['health_state'] = 'healthy'
        path_model_json['health_as_of'] = '2026-07-09T15:30:00Z'
        path_model_json['created_at'] = '2026-07-09T15:00:00Z'
        path_model_json['updated_at'] = '2026-07-09T15:30:00Z'
        path_model_json['created_by'] = 'iam-ServiceId-abc123'
        path_model_json['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a model instance of Path by calling from_dict on the json representation
        path_model = Path.from_dict(path_model_json)
        assert path_model != False

        # Construct a model instance of Path by calling from_dict on the json representation
        path_model_dict = Path.from_dict(path_model_json).__dict__
        path_model2 = Path(**path_model_dict)

        # Verify the model instances are equivalent
        assert path_model == path_model2

        # Convert model instance back to dict and verify no loss of data
        path_model_json2 = path_model.to_dict()
        assert path_model_json2 == path_model_json


class TestModel_PathCollection:
    """
    Test Class for PathCollection
    """

    def test_path_collection_serialization(self):
        """
        Test serialization/deserialization for PathCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        path_model = {}  # Path
        path_model['name'] = 'hsm-node-1'
        path_model['description'] = 'Primary HSM node for prod'
        path_model['crn'] = 'crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1'
        path_model['provisioning_state'] = 'completed'
        path_model['health_state'] = 'healthy'
        path_model['health_as_of'] = '2026-07-09T15:30:00Z'
        path_model['created_at'] = '2026-07-09T15:00:00Z'
        path_model['updated_at'] = '2026-07-09T15:30:00Z'
        path_model['created_by'] = 'iam-ServiceId-abc123'
        path_model['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a json representation of a PathCollection model
        path_collection_model_json = {}
        path_collection_model_json['paths'] = [path_model]

        # Construct a model instance of PathCollection by calling from_dict on the json representation
        path_collection_model = PathCollection.from_dict(path_collection_model_json)
        assert path_collection_model != False

        # Construct a model instance of PathCollection by calling from_dict on the json representation
        path_collection_model_dict = PathCollection.from_dict(path_collection_model_json).__dict__
        path_collection_model2 = PathCollection(**path_collection_model_dict)

        # Verify the model instances are equivalent
        assert path_collection_model == path_collection_model2

        # Convert model instance back to dict and verify no loss of data
        path_collection_model_json2 = path_collection_model.to_dict()
        assert path_collection_model_json2 == path_collection_model_json


class TestModel_PathPatch:
    """
    Test Class for PathPatch
    """

    def test_path_patch_serialization(self):
        """
        Test serialization/deserialization for PathPatch
        """

        # Construct a json representation of a PathPatch model
        path_patch_model_json = {}
        path_patch_model_json['name'] = 'testString'
        path_patch_model_json['description'] = 'testString'

        # Construct a model instance of PathPatch by calling from_dict on the json representation
        path_patch_model = PathPatch.from_dict(path_patch_model_json)
        assert path_patch_model != False

        # Construct a model instance of PathPatch by calling from_dict on the json representation
        path_patch_model_dict = PathPatch.from_dict(path_patch_model_json).__dict__
        path_patch_model2 = PathPatch(**path_patch_model_dict)

        # Verify the model instances are equivalent
        assert path_patch_model == path_patch_model2

        # Convert model instance back to dict and verify no loss of data
        path_patch_model_json2 = path_patch_model.to_dict()
        assert path_patch_model_json2 == path_patch_model_json


class TestModel_ServerCa:
    """
    Test Class for ServerCa
    """

    def test_server_ca_serialization(self):
        """
        Test serialization/deserialization for ServerCa
        """

        # Construct a json representation of a ServerCa model
        server_ca_model_json = {}
        server_ca_model_json['name'] = 'HSM1_Server_CA'
        server_ca_model_json['description'] = 'Primary CA for HSM node 1'
        server_ca_model_json['certificate'] = '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        server_ca_model_json['expires_at'] = '2028-07-09T15:10:00Z'
        server_ca_model_json['status'] = 'active'
        server_ca_model_json['health_state'] = 'valid'
        server_ca_model_json['health_as_of'] = '2026-07-09T15:30:00Z'
        server_ca_model_json['created_at'] = '2026-07-09T15:10:00Z'
        server_ca_model_json['updated_at'] = '2026-07-09T15:20:00Z'
        server_ca_model_json['created_by'] = 'iam-ServiceId-abc123'
        server_ca_model_json['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a model instance of ServerCa by calling from_dict on the json representation
        server_ca_model = ServerCa.from_dict(server_ca_model_json)
        assert server_ca_model != False

        # Construct a model instance of ServerCa by calling from_dict on the json representation
        server_ca_model_dict = ServerCa.from_dict(server_ca_model_json).__dict__
        server_ca_model2 = ServerCa(**server_ca_model_dict)

        # Verify the model instances are equivalent
        assert server_ca_model == server_ca_model2

        # Convert model instance back to dict and verify no loss of data
        server_ca_model_json2 = server_ca_model.to_dict()
        assert server_ca_model_json2 == server_ca_model_json


class TestModel_ServerCaCollection:
    """
    Test Class for ServerCaCollection
    """

    def test_server_ca_collection_serialization(self):
        """
        Test serialization/deserialization for ServerCaCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        server_ca_model = {}  # ServerCa
        server_ca_model['name'] = 'HSM1_Server_CA'
        server_ca_model['description'] = 'Primary CA for HSM node 1'
        server_ca_model['certificate'] = '-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----'
        server_ca_model['expires_at'] = '2028-07-09T15:10:00Z'
        server_ca_model['status'] = 'active'
        server_ca_model['health_state'] = 'valid'
        server_ca_model['health_as_of'] = '2026-07-09T15:30:00Z'
        server_ca_model['created_at'] = '2026-07-09T15:10:00Z'
        server_ca_model['updated_at'] = '2026-07-09T15:20:00Z'
        server_ca_model['created_by'] = 'iam-ServiceId-abc123'
        server_ca_model['updated_by'] = 'iam-ServiceId-abc123'

        # Construct a json representation of a ServerCaCollection model
        server_ca_collection_model_json = {}
        server_ca_collection_model_json['server_cas'] = [server_ca_model]

        # Construct a model instance of ServerCaCollection by calling from_dict on the json representation
        server_ca_collection_model = ServerCaCollection.from_dict(server_ca_collection_model_json)
        assert server_ca_collection_model != False

        # Construct a model instance of ServerCaCollection by calling from_dict on the json representation
        server_ca_collection_model_dict = ServerCaCollection.from_dict(server_ca_collection_model_json).__dict__
        server_ca_collection_model2 = ServerCaCollection(**server_ca_collection_model_dict)

        # Verify the model instances are equivalent
        assert server_ca_collection_model == server_ca_collection_model2

        # Convert model instance back to dict and verify no loss of data
        server_ca_collection_model_json2 = server_ca_collection_model.to_dict()
        assert server_ca_collection_model_json2 == server_ca_collection_model_json


class TestModel_ServerCaPatch:
    """
    Test Class for ServerCaPatch
    """

    def test_server_ca_patch_serialization(self):
        """
        Test serialization/deserialization for ServerCaPatch
        """

        # Construct a json representation of a ServerCaPatch model
        server_ca_patch_model_json = {}
        server_ca_patch_model_json['name'] = 'testString'
        server_ca_patch_model_json['description'] = 'testString'
        server_ca_patch_model_json['status'] = 'active'

        # Construct a model instance of ServerCaPatch by calling from_dict on the json representation
        server_ca_patch_model = ServerCaPatch.from_dict(server_ca_patch_model_json)
        assert server_ca_patch_model != False

        # Construct a model instance of ServerCaPatch by calling from_dict on the json representation
        server_ca_patch_model_dict = ServerCaPatch.from_dict(server_ca_patch_model_json).__dict__
        server_ca_patch_model2 = ServerCaPatch(**server_ca_patch_model_dict)

        # Verify the model instances are equivalent
        assert server_ca_patch_model == server_ca_patch_model2

        # Convert model instance back to dict and verify no loss of data
        server_ca_patch_model_json2 = server_ca_patch_model.to_dict()
        assert server_ca_patch_model_json2 == server_ca_patch_model_json


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


class TestModel_VpeProvisioningResponse:
    """
    Test Class for VpeProvisioningResponse
    """

    def test_vpe_provisioning_response_serialization(self):
        """
        Test serialization/deserialization for VpeProvisioningResponse
        """

        # Construct a json representation of a VpeProvisioningResponse model
        vpe_provisioning_response_model_json = {}
        vpe_provisioning_response_model_json['provisioning_state'] = 'provisioning'

        # Construct a model instance of VpeProvisioningResponse by calling from_dict on the json representation
        vpe_provisioning_response_model = VpeProvisioningResponse.from_dict(vpe_provisioning_response_model_json)
        assert vpe_provisioning_response_model != False

        # Construct a model instance of VpeProvisioningResponse by calling from_dict on the json representation
        vpe_provisioning_response_model_dict = VpeProvisioningResponse.from_dict(vpe_provisioning_response_model_json).__dict__
        vpe_provisioning_response_model2 = VpeProvisioningResponse(**vpe_provisioning_response_model_dict)

        # Verify the model instances are equivalent
        assert vpe_provisioning_response_model == vpe_provisioning_response_model2

        # Convert model instance back to dict and verify no loss of data
        vpe_provisioning_response_model_json2 = vpe_provisioning_response_model.to_dict()
        assert vpe_provisioning_response_model_json2 == vpe_provisioning_response_model_json


class TestModel_VpeStatusResult:
    """
    Test Class for VpeStatusResult
    """

    def test_vpe_status_result_serialization(self):
        """
        Test serialization/deserialization for VpeStatusResult
        """

        # Construct a json representation of a VpeStatusResult model
        vpe_status_result_model_json = {}
        vpe_status_result_model_json['health_state'] = 'healthy'
        vpe_status_result_model_json['health_time_stamp'] = '2026-11-13T07:14:16Z'
        vpe_status_result_model_json['provisioning_state'] = 'completed'

        # Construct a model instance of VpeStatusResult by calling from_dict on the json representation
        vpe_status_result_model = VpeStatusResult.from_dict(vpe_status_result_model_json)
        assert vpe_status_result_model != False

        # Construct a model instance of VpeStatusResult by calling from_dict on the json representation
        vpe_status_result_model_dict = VpeStatusResult.from_dict(vpe_status_result_model_json).__dict__
        vpe_status_result_model2 = VpeStatusResult(**vpe_status_result_model_dict)

        # Verify the model instances are equivalent
        assert vpe_status_result_model == vpe_status_result_model2

        # Convert model instance back to dict and verify no loss of data
        vpe_status_result_model_json2 = vpe_status_result_model.to_dict()
        assert vpe_status_result_model_json2 == vpe_status_result_model_json


class TestModel_CreateDestinationRequestIbmCloudDatabaseDestinationPrototype:
    """
    Test Class for CreateDestinationRequestIbmCloudDatabaseDestinationPrototype
    """

    def test_create_destination_request_ibm_cloud_database_destination_prototype_serialization(self):
        """
        Test serialization/deserialization for CreateDestinationRequestIbmCloudDatabaseDestinationPrototype
        """

        # Construct a json representation of a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype model
        create_destination_request_ibm_cloud_database_destination_prototype_model_json = {}
        create_destination_request_ibm_cloud_database_destination_prototype_model_json['name'] = 'testString'
        create_destination_request_ibm_cloud_database_destination_prototype_model_json['type'] = 'ibm_cloud_database'
        create_destination_request_ibm_cloud_database_destination_prototype_model_json['description'] = 'Production PostgreSQL database'
        create_destination_request_ibm_cloud_database_destination_prototype_model_json['crn'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/e91c8f42b3d74e1a9c2f05d8b67a3e10:3f8b1c7a-9d42-4e6f-b8a5-2c1d9e7f4b83::'

        # Construct a model instance of CreateDestinationRequestIbmCloudDatabaseDestinationPrototype by calling from_dict on the json representation
        create_destination_request_ibm_cloud_database_destination_prototype_model = CreateDestinationRequestIbmCloudDatabaseDestinationPrototype.from_dict(create_destination_request_ibm_cloud_database_destination_prototype_model_json)
        assert create_destination_request_ibm_cloud_database_destination_prototype_model != False

        # Construct a model instance of CreateDestinationRequestIbmCloudDatabaseDestinationPrototype by calling from_dict on the json representation
        create_destination_request_ibm_cloud_database_destination_prototype_model_dict = CreateDestinationRequestIbmCloudDatabaseDestinationPrototype.from_dict(create_destination_request_ibm_cloud_database_destination_prototype_model_json).__dict__
        create_destination_request_ibm_cloud_database_destination_prototype_model2 = CreateDestinationRequestIbmCloudDatabaseDestinationPrototype(**create_destination_request_ibm_cloud_database_destination_prototype_model_dict)

        # Verify the model instances are equivalent
        assert create_destination_request_ibm_cloud_database_destination_prototype_model == create_destination_request_ibm_cloud_database_destination_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        create_destination_request_ibm_cloud_database_destination_prototype_model_json2 = create_destination_request_ibm_cloud_database_destination_prototype_model.to_dict()
        assert create_destination_request_ibm_cloud_database_destination_prototype_model_json2 == create_destination_request_ibm_cloud_database_destination_prototype_model_json


class TestModel_TokenPlainAdminToken:
    """
    Test Class for TokenPlainAdminToken
    """

    def test_token_plain_admin_token_serialization(self):
        """
        Test serialization/deserialization for TokenPlainAdminToken
        """

        # Construct a json representation of a TokenPlainAdminToken model
        token_plain_admin_token_model_json = {}
        token_plain_admin_token_model_json['token'] = 'hvs.CAESIC202dQW-jogohoywlivU-AMllTdeNT0QBiob9OBmyfnGigKImh2cy5yUkxpcmVaZURzTmw5cgtevFoyelBpYkguYW82SlMQyr0Q'

        # Construct a model instance of TokenPlainAdminToken by calling from_dict on the json representation
        token_plain_admin_token_model = TokenPlainAdminToken.from_dict(token_plain_admin_token_model_json)
        assert token_plain_admin_token_model != False

        # Construct a model instance of TokenPlainAdminToken by calling from_dict on the json representation
        token_plain_admin_token_model_dict = TokenPlainAdminToken.from_dict(token_plain_admin_token_model_json).__dict__
        token_plain_admin_token_model2 = TokenPlainAdminToken(**token_plain_admin_token_model_dict)

        # Verify the model instances are equivalent
        assert token_plain_admin_token_model == token_plain_admin_token_model2

        # Convert model instance back to dict and verify no loss of data
        token_plain_admin_token_model_json2 = token_plain_admin_token_model.to_dict()
        assert token_plain_admin_token_model_json2 == token_plain_admin_token_model_json


class TestModel_TokenWrappedAdminToken:
    """
    Test Class for TokenWrappedAdminToken
    """

    def test_token_wrapped_admin_token_serialization(self):
        """
        Test serialization/deserialization for TokenWrappedAdminToken
        """

        # Construct a json representation of a TokenWrappedAdminToken model
        token_wrapped_admin_token_model_json = {}
        token_wrapped_admin_token_model_json['wrapped_token'] = 'hvs.CAESIC202dQW-jogohoywlivU-AMllTdeNT0QBiob99htyfnGigKImh2cy5yUkhydtvaZURzTmw5cFV5dFoyelBpYkguYW82SlKhye5c'

        # Construct a model instance of TokenWrappedAdminToken by calling from_dict on the json representation
        token_wrapped_admin_token_model = TokenWrappedAdminToken.from_dict(token_wrapped_admin_token_model_json)
        assert token_wrapped_admin_token_model != False

        # Construct a model instance of TokenWrappedAdminToken by calling from_dict on the json representation
        token_wrapped_admin_token_model_dict = TokenWrappedAdminToken.from_dict(token_wrapped_admin_token_model_json).__dict__
        token_wrapped_admin_token_model2 = TokenWrappedAdminToken(**token_wrapped_admin_token_model_dict)

        # Verify the model instances are equivalent
        assert token_wrapped_admin_token_model == token_wrapped_admin_token_model2

        # Convert model instance back to dict and verify no loss of data
        token_wrapped_admin_token_model_json2 = token_wrapped_admin_token_model.to_dict()
        assert token_wrapped_admin_token_model_json2 == token_wrapped_admin_token_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
