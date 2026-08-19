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
            id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
        )

        assert response.get_status_code() == 201
        token = response.get_result()
        assert token is not None

    @needscredentials
    def test_get_instance(self):
        response = self.secrets_manager_instance_management_service.get_instance(
            id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
        )

        assert response.get_status_code() == 200
        instance = response.get_result()
        assert instance is not None

    @needscredentials
    def test_list_instance_destinations(self):
        response = self.secrets_manager_instance_management_service.list_instance_destinations(
            instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            state='not_started',
        )

        assert response.get_status_code() == 200
        destination_collection = response.get_result()
        assert destination_collection is not None

    @needscredentials
    def test_create_instance_destination(self):
        response = self.secrets_manager_instance_management_service.create_instance_destination(
            instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
        )

        assert response.get_status_code() == 201

    @needscredentials
    def test_get_instance_destination(self):
        response = self.secrets_manager_instance_management_service.get_instance_destination(
            instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_update_instance_destination(self):
        # Construct a dict representation of a InlineObject model
        inline_object_model = {
            'name': 'production-postgres-db',
            'description': 'Updated description for production database',
        }

        response = self.secrets_manager_instance_management_service.update_instance_destination(
            instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            inline_object=inline_object_model,
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_delete_instance_admintokens(self):
        response = self.secrets_manager_instance_management_service.delete_instance_admintokens(
            id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_instance_destination(self):
        response = self.secrets_manager_instance_management_service.delete_instance_destination(
            instance_id='bfc50c2e-d66d-4f37-9ccf-9713f8325b39',
            destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
        )

        assert response.get_status_code() == 204
