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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/admintokens')
        mock_response = '{"token": "hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Invoke method
        response = _service.create_vault_admintoken(
            id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/admintokens')
        mock_response = '{"token": "hvs.CAESIIG_PILmULFYOsEyWHxkZ2mF2a8V...example...p3ZnpWbDF1RUNjUkNTZEg"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Invoke method
        response = _service.delete_instance_admintokens(
            id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/admintokens')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "name": "name", "instance_crn": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": "dedicated", "vault_cluster": {"status": "healthy", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}, "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Invoke method
        response = _service.get_instance(
            id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "name": "name", "instance_crn": "crn:v1:bluemix:public:secrets-manager:us-south:a/791f3fb10486421e97aa8512f18b7e65:b49ad24d-81d4-5ebc-b9b9-b0937d1c84d5::", "plan": "dedicated", "vault_cluster": {"status": "healthy", "version": "1.21.2+ent.hsm"}, "endpoints": {"public": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}, "private": {"vault_api": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud", "vault_ui": "https://f85f512b-e21b-4a9a-ac45-7bbc2f5cew2e.us-south.secrets-manager.appdomain.cloud/ui"}}, "encryption": {"mode": "service_managed", "provider": "key_protect", "key_crn": "crn:v1:bluemix:public:kms:us-south:a/791f5fb10986423e97aa8512f18b7e65:31639268-42e8-4420-9872-590a6ee20506:key:b4af8f76-e6ea-4dc5-89cc-5f1b9bb207cc"}, "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations')
        mock_response = '{"destinations": [{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "crn": "crn"}], "total": 0}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations')
        mock_response = '{"destinations": [{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "crn": "crn"}], "total": 0}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations')
        mock_response = '{"destinations": [{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "href": "https://us-south.secrets-manager.cloud.ibm.com/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/ce8aa9a4-8cde-4b63-8156-d4a8b252beeb", "name": "name", "type": "ibm_cloud_database", "description": "description", "state": "not_started", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "crn": "crn"}], "total": 0}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations')
        responses.add(
            responses.POST,
            url,
            status=201,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Invoke method
        response = _service.create_instance_destination(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))

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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations')
        responses.add(
            responses.POST,
            url,
            status=201,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.GET,
            url,
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.GET,
            url,
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.PATCH,
            url,
            status=200,
        )

        # Construct a dict representation of a InlineObject model
        inline_object_model = {}
        inline_object_model['name'] = 'production-postgres-db'
        inline_object_model['description'] = 'Updated description for production database'

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'
        inline_object = inline_object_model

        # Invoke method
        response = _service.update_instance_destination(
            instance_id,
            destination_id,
            inline_object=inline_object,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == inline_object

    def test_update_instance_destination_all_params_with_retries(self):
        # Enable retries and run test_update_instance_destination_all_params.
        _service.enable_retries()
        self.test_update_instance_destination_all_params()

        # Disable retries and run test_update_instance_destination_all_params.
        _service.disable_retries()
        self.test_update_instance_destination_all_params()

    @responses.activate
    def test_update_instance_destination_required_params(self):
        """
        test_update_instance_destination_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.PATCH,
            url,
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.update_instance_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_instance_destination_required_params_with_retries(self):
        # Enable retries and run test_update_instance_destination_required_params.
        _service.enable_retries()
        self.test_update_instance_destination_required_params()

        # Disable retries and run test_update_instance_destination_required_params.
        _service.disable_retries()
        self.test_update_instance_destination_required_params()

    @responses.activate
    def test_update_instance_destination_value_error(self):
        """
        test_update_instance_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.PATCH,
            url,
            status=200,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_id": destination_id,
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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
        destination_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'

        # Invoke method
        response = _service.delete_instance_destination(
            instance_id,
            destination_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

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
        url = preprocess_url('/v2/instances/bfc50c2e-d66d-4f37-9ccf-9713f8325b39/destinations/b2c3d4e5-f6a7-8901-bcde-f12345678901')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'bfc50c2e-d66d-4f37-9ccf-9713f8325b39'
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
# Start of Model Tests
##############################################################################
# region


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
        destination_model_json['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        destination_model_json['name'] = 'testString'
        destination_model_json['type'] = 'ibm_cloud_database'
        destination_model_json['description'] = 'testString'
        destination_model_json['state'] = 'not_started'
        destination_model_json['created_at'] = '2019-01-01T12:00:00Z'
        destination_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of Destination by calling from_dict on the json representation
        destination_model = Destination.from_dict(destination_model_json)
        assert destination_model != False

        # Construct a copy of the model instance by calling from_dict on the output of to_dict
        destination_model_json2 = destination_model.to_dict()
        destination_model2 = Destination.from_dict(destination_model_json2)

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

        destination_model = {}  # IbmCloudDatabaseDestination
        destination_model['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        destination_model['name'] = 'testString'
        destination_model['type'] = 'ibm_cloud_database'
        destination_model['description'] = 'testString'
        destination_model['state'] = 'not_started'
        destination_model['created_at'] = '2019-01-01T12:00:00Z'
        destination_model['updated_at'] = '2019-01-01T12:00:00Z'
        destination_model['crn'] = 'testString'

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
        instance_model_json['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
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


class TestModel_InlineObject:
    """
    Test Class for InlineObject
    """

    def test_inline_object_serialization(self):
        """
        Test serialization/deserialization for InlineObject
        """

        # Construct a json representation of a InlineObject model
        inline_object_model_json = {}
        inline_object_model_json['name'] = 'production-postgres-db'
        inline_object_model_json['description'] = 'Updated description for production database'

        # Construct a model instance of InlineObject by calling from_dict on the json representation
        inline_object_model = InlineObject.from_dict(inline_object_model_json)
        assert inline_object_model != False

        # Construct a model instance of InlineObject by calling from_dict on the json representation
        inline_object_model_dict = InlineObject.from_dict(inline_object_model_json).__dict__
        inline_object_model2 = InlineObject(**inline_object_model_dict)

        # Verify the model instances are equivalent
        assert inline_object_model == inline_object_model2

        # Convert model instance back to dict and verify no loss of data
        inline_object_model_json2 = inline_object_model.to_dict()
        assert inline_object_model_json2 == inline_object_model_json


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


class TestModel_CreateInstanceDestinationRequest:
    """
    Test Class for CreateInstanceDestinationRequest
    """

    def test_create_instance_destination_request_serialization(self):
        """
        Test serialization/deserialization for CreateInstanceDestinationRequest
        """

        # Construct a json representation of a CreateInstanceDestinationRequest model
        create_instance_destination_request_model_json = {}

        # Construct a model instance of CreateInstanceDestinationRequest by calling from_dict on the json representation
        create_instance_destination_request_model = CreateInstanceDestinationRequest.from_dict(create_instance_destination_request_model_json)
        assert create_instance_destination_request_model != False

        # Construct a model instance of CreateInstanceDestinationRequest by calling from_dict on the json representation
        create_instance_destination_request_model_dict = CreateInstanceDestinationRequest.from_dict(create_instance_destination_request_model_json).__dict__
        create_instance_destination_request_model2 = CreateInstanceDestinationRequest(**create_instance_destination_request_model_dict)

        # Verify the model instances are equivalent
        assert create_instance_destination_request_model == create_instance_destination_request_model2

        # Convert model instance back to dict and verify no loss of data
        create_instance_destination_request_model_json2 = create_instance_destination_request_model.to_dict()
        assert create_instance_destination_request_model_json2 == create_instance_destination_request_model_json


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
        ibm_cloud_database_destination_model_json['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
