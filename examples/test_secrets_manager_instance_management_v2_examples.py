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
Examples for SecretsManagerInstanceManagementV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_secrets_manager_sdk_instance_management.secrets_manager_instance_management_v2 import *

#
# This file provides an example of how to use the secrets-manager-instance-management service.
#
# The following configuration properties are assumed to be defined:
# SECRETS_MANAGER_INSTANCE_MANAGEMENT_URL=<service base url>
# SECRETS_MANAGER_INSTANCE_MANAGEMENT_AUTH_TYPE=iam
# SECRETS_MANAGER_INSTANCE_MANAGEMENT_APIKEY=<IAM apikey>
# SECRETS_MANAGER_INSTANCE_MANAGEMENT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'secrets_manager_instance_management_v2.env'

secrets_manager_instance_management_service = None

config = None


##############################################################################
# Start of Examples for Service: SecretsManagerInstanceManagementV2
##############################################################################
# region
class TestSecretsManagerInstanceManagementV2Examples:
    """
    Example Test Class for SecretsManagerInstanceManagementV2
    """

    @classmethod
    def setup_class(cls):
        global secrets_manager_instance_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            secrets_manager_instance_management_service = SecretsManagerInstanceManagementV2.new_instance(
            )

            # end-common
            assert secrets_manager_instance_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(SecretsManagerInstanceManagementV2.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_vault_admintoken_example(self):
        """
        create_vault_admintoken request example
        """
        try:
            print('\ncreate_vault_admintoken() result:')

            # begin-create_vault_admintoken

            response = secrets_manager_instance_management_service.create_vault_admintoken(
                id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            )
            token = response.get_result()

            print(json.dumps(token, indent=2))

            # end-create_vault_admintoken

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_example(self):
        """
        get_instance request example
        """
        try:
            print('\nget_instance() result:')

            # begin-get_instance

            response = secrets_manager_instance_management_service.get_instance(
                id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            )
            instance = response.get_result()

            print(json.dumps(instance, indent=2))

            # end-get_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_destinations_example(self):
        """
        list_instance_destinations request example
        """
        try:
            print('\nlist_instance_destinations() result:')

            # begin-list_instance_destinations

            response = secrets_manager_instance_management_service.list_instance_destinations(
                instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            )
            destination_collection = response.get_result()

            print(json.dumps(destination_collection, indent=2))

            # end-list_instance_destinations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_instance_destination_example(self):
        """
        create_instance_destination request example
        """
        try:
            # begin-create_instance_destination

            response = secrets_manager_instance_management_service.create_instance_destination(
                instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            )

            # end-create_instance_destination
            print('\ncreate_instance_destination() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_destination_example(self):
        """
        get_instance_destination request example
        """
        try:
            # begin-get_instance_destination

            response = secrets_manager_instance_management_service.get_instance_destination(
                instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )

            # end-get_instance_destination
            print('\nget_instance_destination() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_destination_example(self):
        """
        update_instance_destination request example
        """
        try:
            # begin-update_instance_destination

            response = secrets_manager_instance_management_service.update_instance_destination(
                instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )

            # end-update_instance_destination
            print('\nupdate_instance_destination() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_admintokens_example(self):
        """
        delete_instance_admintokens request example
        """
        try:
            # begin-delete_instance_admintokens

            response = secrets_manager_instance_management_service.delete_instance_admintokens(
                id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            )

            # end-delete_instance_admintokens
            print('\ndelete_instance_admintokens() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_destination_example(self):
        """
        delete_instance_destination request example
        """
        try:
            # begin-delete_instance_destination

            response = secrets_manager_instance_management_service.delete_instance_destination(
                instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )

            # end-delete_instance_destination
            print('\ndelete_instance_destination() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: SecretsManagerInstanceManagementV2
##############################################################################
