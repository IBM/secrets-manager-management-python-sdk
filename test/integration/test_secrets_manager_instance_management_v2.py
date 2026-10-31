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
Integration Tests for SecretsManagerInstanceManagementV2
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_secrets_manager_sdk_instance_management.secrets_manager_instance_management_v2 import *

# Config file name
config_file = 'secrets_manager_instance_management_v2.env'


class TestSecretsManagerInstanceManagementV2:
    """
    Integration Test Class for SecretsManagerInstanceManagementV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.secrets_manager_instance_management_service = SecretsManagerInstanceManagementV2.new_instance(
            )
            assert cls.secrets_manager_instance_management_service is not None

            cls.config = read_external_sources(SecretsManagerInstanceManagementV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.secrets_manager_instance_management_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_vault_admintoken(self):
        response = self.secrets_manager_instance_management_service.create_vault_admintoken(
            id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            response_wrapping=True,
        )

        assert response.get_status_code() == 201
        token = response.get_result()
        assert token is not None

    @needscredentials
    def test_get_instance(self):
        response = self.secrets_manager_instance_management_service.get_instance(
            id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
        )

        assert response.get_status_code() == 200
        instance = response.get_result()
        assert instance is not None

    @needscredentials
    def test_list_instance_destinations(self):
        response = self.secrets_manager_instance_management_service.list_instance_destinations(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            state='not_started',
        )

        assert response.get_status_code() == 200
        destination_collection = response.get_result()
        assert destination_collection is not None

    @needscredentials
    def test_create_instance_destination(self):
        # Construct a dict representation of a CreateDestinationRequestIbmCloudDatabaseDestinationPrototype model
        create_destination_request_model = {
            'name': 'my-postgres',
            'type': 'ibm_cloud_database',
            'description': 'Production PostgreSQL database',
            'crn': 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/e91c8f42b3d74e1a9c2f05d8b67a3e10:3f8b1c7a-9d42-4e6f-b8a5-2c1d9e7f4b83::',
        }

        response = self.secrets_manager_instance_management_service.create_instance_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_prototype=create_destination_request_model,
        )

        assert response.get_status_code() == 202
        ibm_cloud_database_destination = response.get_result()
        assert ibm_cloud_database_destination is not None

    @needscredentials
    def test_get_instance_destination(self):
        response = self.secrets_manager_instance_management_service.get_instance_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='d6354cf6-e746-469d-ac1b-fd3158292c28',
        )

        assert response.get_status_code() == 200
        ibm_cloud_database_destination = response.get_result()
        assert ibm_cloud_database_destination is not None

    @needscredentials
    def test_update_instance_destination(self):
        # Construct a dict representation of a DestinationPatch model
        destination_patch_model = {
            'name': 'my-postgres-updated',
            'description': 'Production PostgreSQL database',
        }

        response = self.secrets_manager_instance_management_service.update_instance_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='d6354cf6-e746-469d-ac1b-fd3158292c28',
            destination_patch=destination_patch_model,
        )

        assert response.get_status_code() == 200
        ibm_cloud_database_destination = response.get_result()
        assert ibm_cloud_database_destination is not None

    @needscredentials
    def test_delete_instance_admintokens(self):
        response = self.secrets_manager_instance_management_service.delete_instance_admintokens(
            id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_instance_destination(self):
        response = self.secrets_manager_instance_management_service.delete_instance_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='d6354cf6-e746-469d-ac1b-fd3158292c28',
        )

        assert response.get_status_code() == 202
        ibm_cloud_database_destination = response.get_result()
        assert ibm_cloud_database_destination is not None
