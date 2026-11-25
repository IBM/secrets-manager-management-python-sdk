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
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            response_wrapping=True,
        )

        assert response.get_status_code() == 201
        token = response.get_result()
        assert token is not None

    @needscredentials
    def test_get_instance(self):
        response = self.secrets_manager_instance_management_service.get_instance(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
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
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
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
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            destination_patch=destination_patch_model,
        )

        assert response.get_status_code() == 200
        ibm_cloud_database_destination = response.get_result()
        assert ibm_cloud_database_destination is not None

    @needscredentials
    def test_list_instance_hsm_destinations(self):
        response = self.secrets_manager_instance_management_service.list_instance_hsm_destinations(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
        )

        assert response.get_status_code() == 200
        hsm_destination_collection = response.get_result()
        assert hsm_destination_collection is not None

    @needscredentials
    def test_create_instance_hsm_destination(self):
        response = self.secrets_manager_instance_management_service.create_instance_hsm_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            name='prod-hsm-destination',
            vendor='thales_luna',
            description='Primary Thales Luna destination',
        )

        assert response.get_status_code() == 201
        hsm_destination = response.get_result()
        assert hsm_destination is not None

    @needscredentials
    def test_get_instance_hsm_destination(self):
        response = self.secrets_manager_instance_management_service.get_instance_hsm_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 200
        hsm_destination = response.get_result()
        assert hsm_destination is not None

    @needscredentials
    def test_update_instance_hsm_destination(self):
        # Construct a dict representation of a HSMDestinationPatch model
        hsm_destination_patch_model = {
            'name': 'my-hsm-destination',
            'description': 'testString',
        }

        response = self.secrets_manager_instance_management_service.update_instance_hsm_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            hsm_destination_patch=hsm_destination_patch_model,
        )

        assert response.get_status_code() == 200
        hsm_destination = response.get_result()
        assert hsm_destination is not None

    @needscredentials
    def test_get_hsm_destination_health_snapshot(self):
        response = self.secrets_manager_instance_management_service.get_hsm_destination_health_snapshot(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 200
        destination_health_snapshot = response.get_result()
        assert destination_health_snapshot is not None

    @needscredentials
    def test_run_hsm_destination_health_check(self):
        response = self.secrets_manager_instance_management_service.run_hsm_destination_health_check(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 202
        async_health_check_ack_response = response.get_result()
        assert async_health_check_ack_response is not None

    @needscredentials
    def test_apply_hsm_destination(self):
        response = self.secrets_manager_instance_management_service.apply_hsm_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 202
        async_health_ack_response = response.get_result()
        assert async_health_ack_response is not None

    @needscredentials
    def test_list_instance_hsm_destination_ha_groups(self):
        response = self.secrets_manager_instance_management_service.list_instance_hsm_destination_ha_groups(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 200
        hsmha_group_collection = response.get_result()
        assert hsmha_group_collection is not None

    @needscredentials
    def test_create_instance_hsm_destination_ha_group(self):
        response = self.secrets_manager_instance_management_service.create_instance_hsm_destination_ha_group(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            name='production-ha-group',
            group_label='prod_ha_group',
            group_serial='11323465009866',
            member_serials=['123456', '123457'],
            description='Primary HA Group for prod',
        )

        assert response.get_status_code() == 201
        hsmha_group = response.get_result()
        assert hsmha_group is not None

    @needscredentials
    def test_get_instance_hsm_destination_ha_group(self):
        response = self.secrets_manager_instance_management_service.get_instance_hsm_destination_ha_group(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            ha_group_id='ee52ebb6-1728-4580-8ede-13f6504e3ae0',
        )

        assert response.get_status_code() == 200
        hsmha_group = response.get_result()
        assert hsmha_group is not None

    @needscredentials
    def test_update_instance_hsm_destination_ha_group(self):
        # Construct a dict representation of a HSMHAGroupPatch model
        hsmha_group_patch_model = {
            'name': 'dr-ha-group',
            'description': 'DR HA Group for failover',
            'member_serials': ['123456', '123457', '123458'],
        }

        response = self.secrets_manager_instance_management_service.update_instance_hsm_destination_ha_group(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            ha_group_id='ee52ebb6-1728-4580-8ede-13f6504e3ae0',
            hsmha_group_patch=hsmha_group_patch_model,
        )

        assert response.get_status_code() == 200
        hsmha_group = response.get_result()
        assert hsmha_group is not None

    @needscredentials
    def test_list_instance_hsm_destination_paths(self):
        response = self.secrets_manager_instance_management_service.list_instance_hsm_destination_paths(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 200
        path_collection = response.get_result()
        assert path_collection is not None

    @needscredentials
    def test_create_instance_hsm_destination_path(self):
        response = self.secrets_manager_instance_management_service.create_instance_hsm_destination_path(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            name='hsm-node-1',
            crn='crn:v1:staging:public:databases-for-postgresql:us-south:a/791f5fb10986423e97aa8512f18b7e65:11111111-0000-4000-8000-111111111111::',
            description='testString',
        )

        assert response.get_status_code() == 201
        path = response.get_result()
        assert path is not None

    @needscredentials
    def test_get_instance_hsm_destination_path(self):
        response = self.secrets_manager_instance_management_service.get_instance_hsm_destination_path(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
        )

        assert response.get_status_code() == 200
        path = response.get_result()
        assert path is not None

    @needscredentials
    def test_update_instance_hsm_destination_path(self):
        # Construct a dict representation of a PathPatch model
        path_patch_model = {
            'name': 'hsm-node-1-renamed',
            'description': 'testString',
        }

        response = self.secrets_manager_instance_management_service.update_instance_hsm_destination_path(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
            path_patch=path_patch_model,
        )

        assert response.get_status_code() == 200
        path = response.get_result()
        assert path is not None

    @needscredentials
    def test_create_path_build(self):
        response = self.secrets_manager_instance_management_service.create_path_build(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
        )

        assert response.get_status_code() == 202
        vpe_provisioning_response = response.get_result()
        assert vpe_provisioning_response is not None

    @needscredentials
    def test_get_path_vpe_status(self):
        response = self.secrets_manager_instance_management_service.get_path_vpe_status(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
        )

        assert response.get_status_code() == 200
        vpe_status_result = response.get_result()
        assert vpe_status_result is not None

    @needscredentials
    def test_reset_hsm_destination_path(self):
        response = self.secrets_manager_instance_management_service.reset_hsm_destination_path(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
        )

        assert response.get_status_code() == 200
        hsm_path_reset = response.get_result()
        assert hsm_path_reset is not None

    @needscredentials
    def test_list_instance_hsm_destination_path_server_cas(self):
        response = self.secrets_manager_instance_management_service.list_instance_hsm_destination_path_server_cas(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
        )

        assert response.get_status_code() == 200
        server_ca_collection = response.get_result()
        assert server_ca_collection is not None

    @needscredentials
    def test_create_instance_hsm_destination_path_server_ca(self):
        response = self.secrets_manager_instance_management_service.create_instance_hsm_destination_path_server_ca(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
            name='HSM1_Server_CA',
            certificate='-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----',
            description='testString',
        )

        assert response.get_status_code() == 201
        server_ca = response.get_result()
        assert server_ca is not None

    @needscredentials
    def test_get_instance_hsm_destination_path_server_ca(self):
        response = self.secrets_manager_instance_management_service.get_instance_hsm_destination_path_server_ca(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
            server_ca_id='5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f',
        )

        assert response.get_status_code() == 200
        server_ca = response.get_result()
        assert server_ca is not None

    @needscredentials
    def test_update_instance_hsm_destination_path_server_ca(self):
        # Construct a dict representation of a ServerCaPatch model
        server_ca_patch_model = {
            'name': 'HSM1_Server_CA_renamed',
            'description': 'testString',
            'status': 'active',
        }

        response = self.secrets_manager_instance_management_service.update_instance_hsm_destination_path_server_ca(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
            server_ca_id='5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f',
            server_ca_patch=server_ca_patch_model,
        )

        assert response.get_status_code() == 200
        server_ca = response.get_result()
        assert server_ca is not None

    @needscredentials
    def test_list_instance_hsm_destination_client_certificates(self):
        response = self.secrets_manager_instance_management_service.list_instance_hsm_destination_client_certificates(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 200
        client_certificate_collection = response.get_result()
        assert client_certificate_collection is not None

    @needscredentials
    def test_create_instance_hsm_destination_client_certificate(self):
        response = self.secrets_manager_instance_management_service.create_instance_hsm_destination_client_certificate(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            name='hsm-client-cert-prod',
            description='testString',
        )

        assert response.get_status_code() == 201
        client_certificate = response.get_result()
        assert client_certificate is not None

    @needscredentials
    def test_get_instance_hsm_destination_client_certificate(self):
        response = self.secrets_manager_instance_management_service.get_instance_hsm_destination_client_certificate(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            cert_id='7c9e6679-7425-40de-944b-e07fc1f90ae7',
        )

        assert response.get_status_code() == 200
        client_certificate = response.get_result()
        assert client_certificate is not None

    @needscredentials
    def test_update_instance_hsm_destination_client_certificate(self):
        # Construct a dict representation of a ClientCertificatePatch model
        client_certificate_patch_model = {
            'name': 'hsm-client-cert-renamed',
            'description': 'testString',
            'status': 'testString',
            'signed_cert': 'testString',
        }

        response = self.secrets_manager_instance_management_service.update_instance_hsm_destination_client_certificate(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            cert_id='7c9e6679-7425-40de-944b-e07fc1f90ae7',
            client_certificate_patch=client_certificate_patch_model,
        )

        assert response.get_status_code() == 200
        client_certificate = response.get_result()
        assert client_certificate is not None

    @needscredentials
    def test_delete_vault_admintokens(self):
        response = self.secrets_manager_instance_management_service.delete_vault_admintokens(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_instance_destination(self):
        response = self.secrets_manager_instance_management_service.delete_instance_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 202
        ibm_cloud_database_destination = response.get_result()
        assert ibm_cloud_database_destination is not None

    @needscredentials
    def test_delete_instance_hsm_destination(self):
        response = self.secrets_manager_instance_management_service.delete_instance_hsm_destination(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
        )

        assert response.get_status_code() == 202
        async_delete_response = response.get_result()
        assert async_delete_response is not None

    @needscredentials
    def test_delete_instance_hsm_destination_ha_group(self):
        response = self.secrets_manager_instance_management_service.delete_instance_hsm_destination_ha_group(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            ha_group_id='ee52ebb6-1728-4580-8ede-13f6504e3ae0',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_instance_hsm_destination_path(self):
        response = self.secrets_manager_instance_management_service.delete_instance_hsm_destination_path(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
        )

        assert response.get_status_code() == 202
        path = response.get_result()
        assert path is not None

    @needscredentials
    def test_delete_instance_hsm_destination_path_server_ca(self):
        response = self.secrets_manager_instance_management_service.delete_instance_hsm_destination_path_server_ca(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            path_id='fa3d1234-0000-0000-0000-000000000001',
            server_ca_id='5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_instance_hsm_destination_client_certificate(self):
        response = self.secrets_manager_instance_management_service.delete_instance_hsm_destination_client_certificate(
            instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            destination_id='437bc8d5-da05-4df6-8d3d-08af5507e863',
            cert_id='7c9e6679-7425-40de-944b-e07fc1f90ae7',
        )

        assert response.get_status_code() == 204
