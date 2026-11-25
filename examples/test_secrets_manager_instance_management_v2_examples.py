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
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
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
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
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
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
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
            print('\ncreate_instance_destination() result:')

            # begin-create_instance_destination

            create_destination_request_model = {
                'name': 'my-postgres',
                'type': 'ibm_cloud_database',
                'description': 'Production PostgreSQL database',
                'crn': 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/e91c8f42b3d74e1a9c2f05d8b67a3e10:3f8b1c7a-9d42-4e6f-b8a5-2c1d9e7f4b83::',
            }

            response = secrets_manager_instance_management_service.create_instance_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_prototype=create_destination_request_model,
            )
            ibm_cloud_database_destination = response.get_result()

            print(json.dumps(ibm_cloud_database_destination, indent=2))

            # end-create_instance_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_destination_example(self):
        """
        get_instance_destination request example
        """
        try:
            print('\nget_instance_destination() result:')

            # begin-get_instance_destination

            response = secrets_manager_instance_management_service.get_instance_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            ibm_cloud_database_destination = response.get_result()

            print(json.dumps(ibm_cloud_database_destination, indent=2))

            # end-get_instance_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_destination_example(self):
        """
        update_instance_destination request example
        """
        try:
            print('\nupdate_instance_destination() result:')

            # begin-update_instance_destination

            destination_patch_model = {
                'name': 'my-postgres-updated',
                'description': 'Production PostgreSQL database',
            }

            response = secrets_manager_instance_management_service.update_instance_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                destination_patch=destination_patch_model,
            )
            ibm_cloud_database_destination = response.get_result()

            print(json.dumps(ibm_cloud_database_destination, indent=2))

            # end-update_instance_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_hsm_destinations_example(self):
        """
        list_instance_hsm_destinations request example
        """
        try:
            print('\nlist_instance_hsm_destinations() result:')

            # begin-list_instance_hsm_destinations

            response = secrets_manager_instance_management_service.list_instance_hsm_destinations(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            )
            hsm_destination_collection = response.get_result()

            print(json.dumps(hsm_destination_collection, indent=2))

            # end-list_instance_hsm_destinations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_instance_hsm_destination_example(self):
        """
        create_instance_hsm_destination request example
        """
        try:
            print('\ncreate_instance_hsm_destination() result:')

            # begin-create_instance_hsm_destination

            response = secrets_manager_instance_management_service.create_instance_hsm_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                name='prod-hsm-destination',
                vendor='thales_luna',
                description='Primary Thales Luna destination',
            )
            hsm_destination = response.get_result()

            print(json.dumps(hsm_destination, indent=2))

            # end-create_instance_hsm_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_hsm_destination_example(self):
        """
        get_instance_hsm_destination request example
        """
        try:
            print('\nget_instance_hsm_destination() result:')

            # begin-get_instance_hsm_destination

            response = secrets_manager_instance_management_service.get_instance_hsm_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            hsm_destination = response.get_result()

            print(json.dumps(hsm_destination, indent=2))

            # end-get_instance_hsm_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_hsm_destination_example(self):
        """
        update_instance_hsm_destination request example
        """
        try:
            print('\nupdate_instance_hsm_destination() result:')

            # begin-update_instance_hsm_destination

            hsm_destination_patch_model = {
                'name': 'my-hsm-destination',
            }

            response = secrets_manager_instance_management_service.update_instance_hsm_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                hsm_destination_patch=hsm_destination_patch_model,
            )
            hsm_destination = response.get_result()

            print(json.dumps(hsm_destination, indent=2))

            # end-update_instance_hsm_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_hsm_destination_health_snapshot_example(self):
        """
        get_hsm_destination_health_snapshot request example
        """
        try:
            print('\nget_hsm_destination_health_snapshot() result:')

            # begin-get_hsm_destination_health_snapshot

            response = secrets_manager_instance_management_service.get_hsm_destination_health_snapshot(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            destination_health_snapshot = response.get_result()

            print(json.dumps(destination_health_snapshot, indent=2))

            # end-get_hsm_destination_health_snapshot

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_run_hsm_destination_health_check_example(self):
        """
        run_hsm_destination_health_check request example
        """
        try:
            print('\nrun_hsm_destination_health_check() result:')

            # begin-run_hsm_destination_health_check

            response = secrets_manager_instance_management_service.run_hsm_destination_health_check(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            async_health_check_ack_response = response.get_result()

            print(json.dumps(async_health_check_ack_response, indent=2))

            # end-run_hsm_destination_health_check

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_apply_hsm_destination_example(self):
        """
        apply_hsm_destination request example
        """
        try:
            print('\napply_hsm_destination() result:')

            # begin-apply_hsm_destination

            response = secrets_manager_instance_management_service.apply_hsm_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            async_health_ack_response = response.get_result()

            print(json.dumps(async_health_ack_response, indent=2))

            # end-apply_hsm_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_hsm_destination_ha_groups_example(self):
        """
        list_instance_hsm_destination_ha_groups request example
        """
        try:
            print('\nlist_instance_hsm_destination_ha_groups() result:')

            # begin-list_instance_hsm_destination_ha_groups

            response = secrets_manager_instance_management_service.list_instance_hsm_destination_ha_groups(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            hsmha_group_collection = response.get_result()

            print(json.dumps(hsmha_group_collection, indent=2))

            # end-list_instance_hsm_destination_ha_groups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_instance_hsm_destination_ha_group_example(self):
        """
        create_instance_hsm_destination_ha_group request example
        """
        try:
            print('\ncreate_instance_hsm_destination_ha_group() result:')

            # begin-create_instance_hsm_destination_ha_group

            response = secrets_manager_instance_management_service.create_instance_hsm_destination_ha_group(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                name='production-ha-group',
                group_label='prod_ha_group',
                group_serial='11323465009866',
                member_serials=['123456', '123457'],
                description='Primary HA Group for prod',
            )
            hsmha_group = response.get_result()

            print(json.dumps(hsmha_group, indent=2))

            # end-create_instance_hsm_destination_ha_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_hsm_destination_ha_group_example(self):
        """
        get_instance_hsm_destination_ha_group request example
        """
        try:
            print('\nget_instance_hsm_destination_ha_group() result:')

            # begin-get_instance_hsm_destination_ha_group

            response = secrets_manager_instance_management_service.get_instance_hsm_destination_ha_group(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                ha_group_id='ee52ebb6-1728-4580-8ede-13f6504e3ae0',
            )
            hsmha_group = response.get_result()

            print(json.dumps(hsmha_group, indent=2))

            # end-get_instance_hsm_destination_ha_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_hsm_destination_ha_group_example(self):
        """
        update_instance_hsm_destination_ha_group request example
        """
        try:
            print('\nupdate_instance_hsm_destination_ha_group() result:')

            # begin-update_instance_hsm_destination_ha_group

            hsmha_group_patch_model = {
                'name': 'dr-ha-group',
            }

            response = secrets_manager_instance_management_service.update_instance_hsm_destination_ha_group(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                ha_group_id='ee52ebb6-1728-4580-8ede-13f6504e3ae0',
                hsmha_group_patch=hsmha_group_patch_model,
            )
            hsmha_group = response.get_result()

            print(json.dumps(hsmha_group, indent=2))

            # end-update_instance_hsm_destination_ha_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_hsm_destination_paths_example(self):
        """
        list_instance_hsm_destination_paths request example
        """
        try:
            print('\nlist_instance_hsm_destination_paths() result:')

            # begin-list_instance_hsm_destination_paths

            response = secrets_manager_instance_management_service.list_instance_hsm_destination_paths(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            path_collection = response.get_result()

            print(json.dumps(path_collection, indent=2))

            # end-list_instance_hsm_destination_paths

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_instance_hsm_destination_path_example(self):
        """
        create_instance_hsm_destination_path request example
        """
        try:
            print('\ncreate_instance_hsm_destination_path() result:')

            # begin-create_instance_hsm_destination_path

            response = secrets_manager_instance_management_service.create_instance_hsm_destination_path(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                name='hsm-node-1',
                crn='crn:v1:bluemix:public:is:eu-fr2:a/customer123::private-path-service-gateway:hsm1',
            )
            path = response.get_result()

            print(json.dumps(path, indent=2))

            # end-create_instance_hsm_destination_path

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_hsm_destination_path_example(self):
        """
        get_instance_hsm_destination_path request example
        """
        try:
            print('\nget_instance_hsm_destination_path() result:')

            # begin-get_instance_hsm_destination_path

            response = secrets_manager_instance_management_service.get_instance_hsm_destination_path(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
            )
            path = response.get_result()

            print(json.dumps(path, indent=2))

            # end-get_instance_hsm_destination_path

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_hsm_destination_path_example(self):
        """
        update_instance_hsm_destination_path request example
        """
        try:
            print('\nupdate_instance_hsm_destination_path() result:')

            # begin-update_instance_hsm_destination_path

            path_patch_model = {
                'name': 'hsm-node-1-renamed',
            }

            response = secrets_manager_instance_management_service.update_instance_hsm_destination_path(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
                path_patch=path_patch_model,
            )
            path = response.get_result()

            print(json.dumps(path, indent=2))

            # end-update_instance_hsm_destination_path

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_path_build_example(self):
        """
        create_path_build request example
        """
        try:
            print('\ncreate_path_build() result:')

            # begin-create_path_build

            response = secrets_manager_instance_management_service.create_path_build(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
            )
            vpe_provisioning_response = response.get_result()

            print(json.dumps(vpe_provisioning_response, indent=2))

            # end-create_path_build

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_path_vpe_status_example(self):
        """
        get_path_vpe_status request example
        """
        try:
            print('\nget_path_vpe_status() result:')

            # begin-get_path_vpe_status

            response = secrets_manager_instance_management_service.get_path_vpe_status(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
            )
            vpe_status_result = response.get_result()

            print(json.dumps(vpe_status_result, indent=2))

            # end-get_path_vpe_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_reset_hsm_destination_path_example(self):
        """
        reset_hsm_destination_path request example
        """
        try:
            print('\nreset_hsm_destination_path() result:')

            # begin-reset_hsm_destination_path

            response = secrets_manager_instance_management_service.reset_hsm_destination_path(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
            )
            hsm_path_reset = response.get_result()

            print(json.dumps(hsm_path_reset, indent=2))

            # end-reset_hsm_destination_path

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_hsm_destination_path_server_cas_example(self):
        """
        list_instance_hsm_destination_path_server_cas request example
        """
        try:
            print('\nlist_instance_hsm_destination_path_server_cas() result:')

            # begin-list_instance_hsm_destination_path_server_cas

            response = secrets_manager_instance_management_service.list_instance_hsm_destination_path_server_cas(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
            )
            server_ca_collection = response.get_result()

            print(json.dumps(server_ca_collection, indent=2))

            # end-list_instance_hsm_destination_path_server_cas

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_instance_hsm_destination_path_server_ca_example(self):
        """
        create_instance_hsm_destination_path_server_ca request example
        """
        try:
            print('\ncreate_instance_hsm_destination_path_server_ca() result:')

            # begin-create_instance_hsm_destination_path_server_ca

            response = secrets_manager_instance_management_service.create_instance_hsm_destination_path_server_ca(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
                name='HSM1_Server_CA',
                certificate='-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWg...\n-----END CERTIFICATE-----',
            )
            server_ca = response.get_result()

            print(json.dumps(server_ca, indent=2))

            # end-create_instance_hsm_destination_path_server_ca

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_hsm_destination_path_server_ca_example(self):
        """
        get_instance_hsm_destination_path_server_ca request example
        """
        try:
            print('\nget_instance_hsm_destination_path_server_ca() result:')

            # begin-get_instance_hsm_destination_path_server_ca

            response = secrets_manager_instance_management_service.get_instance_hsm_destination_path_server_ca(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
                server_ca_id='5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f',
            )
            server_ca = response.get_result()

            print(json.dumps(server_ca, indent=2))

            # end-get_instance_hsm_destination_path_server_ca

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_hsm_destination_path_server_ca_example(self):
        """
        update_instance_hsm_destination_path_server_ca request example
        """
        try:
            print('\nupdate_instance_hsm_destination_path_server_ca() result:')

            # begin-update_instance_hsm_destination_path_server_ca

            server_ca_patch_model = {
                'name': 'HSM1_Server_CA_renamed',
            }

            response = secrets_manager_instance_management_service.update_instance_hsm_destination_path_server_ca(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
                server_ca_id='5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f',
                server_ca_patch=server_ca_patch_model,
            )
            server_ca = response.get_result()

            print(json.dumps(server_ca, indent=2))

            # end-update_instance_hsm_destination_path_server_ca

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_hsm_destination_client_certificates_example(self):
        """
        list_instance_hsm_destination_client_certificates request example
        """
        try:
            print('\nlist_instance_hsm_destination_client_certificates() result:')

            # begin-list_instance_hsm_destination_client_certificates

            response = secrets_manager_instance_management_service.list_instance_hsm_destination_client_certificates(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            client_certificate_collection = response.get_result()

            print(json.dumps(client_certificate_collection, indent=2))

            # end-list_instance_hsm_destination_client_certificates

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_instance_hsm_destination_client_certificate_example(self):
        """
        create_instance_hsm_destination_client_certificate request example
        """
        try:
            print('\ncreate_instance_hsm_destination_client_certificate() result:')

            # begin-create_instance_hsm_destination_client_certificate

            response = secrets_manager_instance_management_service.create_instance_hsm_destination_client_certificate(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                name='hsm-client-cert-prod',
            )
            client_certificate = response.get_result()

            print(json.dumps(client_certificate, indent=2))

            # end-create_instance_hsm_destination_client_certificate

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_hsm_destination_client_certificate_example(self):
        """
        get_instance_hsm_destination_client_certificate request example
        """
        try:
            print('\nget_instance_hsm_destination_client_certificate() result:')

            # begin-get_instance_hsm_destination_client_certificate

            response = secrets_manager_instance_management_service.get_instance_hsm_destination_client_certificate(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                cert_id='7c9e6679-7425-40de-944b-e07fc1f90ae7',
            )
            client_certificate = response.get_result()

            print(json.dumps(client_certificate, indent=2))

            # end-get_instance_hsm_destination_client_certificate

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_hsm_destination_client_certificate_example(self):
        """
        update_instance_hsm_destination_client_certificate request example
        """
        try:
            print('\nupdate_instance_hsm_destination_client_certificate() result:')

            # begin-update_instance_hsm_destination_client_certificate

            client_certificate_patch_model = {
                'name': 'hsm-client-cert-renamed',
            }

            response = secrets_manager_instance_management_service.update_instance_hsm_destination_client_certificate(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                cert_id='7c9e6679-7425-40de-944b-e07fc1f90ae7',
                client_certificate_patch=client_certificate_patch_model,
            )
            client_certificate = response.get_result()

            print(json.dumps(client_certificate, indent=2))

            # end-update_instance_hsm_destination_client_certificate

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_vault_admintokens_example(self):
        """
        delete_vault_admintokens request example
        """
        try:
            # begin-delete_vault_admintokens

            response = secrets_manager_instance_management_service.delete_vault_admintokens(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
            )

            # end-delete_vault_admintokens
            print('\ndelete_vault_admintokens() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_destination_example(self):
        """
        delete_instance_destination request example
        """
        try:
            print('\ndelete_instance_destination() result:')

            # begin-delete_instance_destination

            response = secrets_manager_instance_management_service.delete_instance_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            ibm_cloud_database_destination = response.get_result()

            print(json.dumps(ibm_cloud_database_destination, indent=2))

            # end-delete_instance_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_hsm_destination_example(self):
        """
        delete_instance_hsm_destination request example
        """
        try:
            print('\ndelete_instance_hsm_destination() result:')

            # begin-delete_instance_hsm_destination

            response = secrets_manager_instance_management_service.delete_instance_hsm_destination(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
            )
            async_delete_response = response.get_result()

            print(json.dumps(async_delete_response, indent=2))

            # end-delete_instance_hsm_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_hsm_destination_ha_group_example(self):
        """
        delete_instance_hsm_destination_ha_group request example
        """
        try:
            # begin-delete_instance_hsm_destination_ha_group

            response = secrets_manager_instance_management_service.delete_instance_hsm_destination_ha_group(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                ha_group_id='ee52ebb6-1728-4580-8ede-13f6504e3ae0',
            )

            # end-delete_instance_hsm_destination_ha_group
            print('\ndelete_instance_hsm_destination_ha_group() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_hsm_destination_path_example(self):
        """
        delete_instance_hsm_destination_path request example
        """
        try:
            print('\ndelete_instance_hsm_destination_path() result:')

            # begin-delete_instance_hsm_destination_path

            response = secrets_manager_instance_management_service.delete_instance_hsm_destination_path(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
            )
            path = response.get_result()

            print(json.dumps(path, indent=2))

            # end-delete_instance_hsm_destination_path

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_hsm_destination_path_server_ca_example(self):
        """
        delete_instance_hsm_destination_path_server_ca request example
        """
        try:
            # begin-delete_instance_hsm_destination_path_server_ca

            response = secrets_manager_instance_management_service.delete_instance_hsm_destination_path_server_ca(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                path_id='fa3d1234-0000-0000-0000-000000000001',
                server_ca_id='5d1f3c2e-8a4b-4c6d-9e7f-0a1b2c3d4e5f',
            )

            # end-delete_instance_hsm_destination_path_server_ca
            print('\ndelete_instance_hsm_destination_path_server_ca() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_instance_hsm_destination_client_certificate_example(self):
        """
        delete_instance_hsm_destination_client_certificate request example
        """
        try:
            # begin-delete_instance_hsm_destination_client_certificate

            response = secrets_manager_instance_management_service.delete_instance_hsm_destination_client_certificate(
                instance_id='fe5c5c27-3e44-474a-9484-55892e12d6d1',
                destination_id='b2c3d4e5-f6a7-8901-bcde-f12345678901',
                cert_id='7c9e6679-7425-40de-944b-e07fc1f90ae7',
            )

            # end-delete_instance_hsm_destination_client_certificate
            print('\ndelete_instance_hsm_destination_client_certificate() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: SecretsManagerInstanceManagementV2
##############################################################################
