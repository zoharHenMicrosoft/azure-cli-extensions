# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import StorageAccountPreparer
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)

from .example_steps import step_attached_database_configuration_create
from .example_steps import step_attached_database_configuration_delete
from .example_steps import step_attached_database_configuration_list
from .example_steps import step_attached_database_configuration_show
from .example_steps import step_cluster_add_language_extension
from .example_steps import step_cluster_create
from .example_steps import step_cluster_delete
from .example_steps import step_cluster_detach_follower_database
from .example_steps import step_cluster_diagnose_virtual_network
from .example_steps import step_cluster_list
from .example_steps import step_cluster_list_by_resource_group
from .example_steps import step_cluster_list_follower_database
from .example_steps import step_cluster_list_language_extension
from .example_steps import step_cluster_list_outbound
from .example_steps import step_cluster_list_sku
from .example_steps import step_cluster_list_sku_by_resource_group
from .example_steps import step_cluster_principal_assignment_create
from .example_steps import step_cluster_principal_assignment_delete
from .example_steps import step_cluster_principal_assignment_list
from .example_steps import step_cluster_principal_assignment_show
from .example_steps import step_cluster_remove_language_extension
from .example_steps import step_cluster_show
from .example_steps import step_cluster_start
from .example_steps import step_cluster_stop
from .example_steps import step_cluster_update
from .example_steps import step_data_connection_delete
from .example_steps import step_data_connection_event_hub_create
from .example_steps import step_data_connection_event_hub_update
from .example_steps import step_data_connection_list
from .example_steps import step_data_connection_show
from .example_steps import step_data_connection_validation
from .example_steps import step_database_add_principal
from .example_steps import step_database_create
from .example_steps import step_database_delete
from .example_steps import step_database_list
from .example_steps import step_database_list_principal
from .example_steps import step_database_principal_assignment_create
from .example_steps import step_database_principal_assignment_delete
from .example_steps import step_database_principal_assignment_list
from .example_steps import step_database_principal_assignment_show
from .example_steps import step_database_remove_principal
from .example_steps import step_database_show
from .example_steps import step_database_update
from .example_steps import step_leader_cluster_create
from .example_steps import step_managed_private_endpoint_create
from .example_steps import step_managed_private_endpoint_delete
from .example_steps import step_managed_private_endpoint_list
from .example_steps import step_managed_private_endpoint_show
from .example_steps import step_managed_private_endpoint_update
from .example_steps import step_operation_result_show
from .example_steps import step_private_endpoint_connection_create
from .example_steps import step_private_endpoint_connection_delete
from .example_steps import step_private_endpoint_connection_list
from .example_steps import step_private_endpoint_connection_show
from .example_steps import step_private_link_resource_list
from .example_steps import step_private_link_resource_show
from .example_steps import step_script_create
from .example_steps import step_script_delete
from .example_steps import step_script_list
from .example_steps import step_script_show
from .example_steps import step_script_update

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    # Create 
    step_cluster_create(test, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus2", case_sensitive=False),
        test.check("enableAutoStop", True),
        test.check("enableDoubleEncryption", False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("publicNetworkAccess", "Enabled", case_sensitive=False),
        test.check("sku.name", "Standard_E2a_v4", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step_cluster_principal_assignment_create(test, checks=[])
    step_leader_cluster_create(test, checks=[])
    step_database_create(test, checks=[])
    step_database_principal_assignment_create(test, checks=[])
    step_database_add_principal(test, checks=[])
    step_attached_database_configuration_create(test, checks=[])
    step_data_connection_event_hub_create(test, checks=[])
    step_script_create(test, checks=[])
    step_managed_private_endpoint_create(test, checks=[])
    step_cluster_add_language_extension(test, checks=[])
    step_private_endpoint_connection_create(test, checks=[])
    # Show / List
    step_cluster_show(test, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "West US 2", case_sensitive=False),
        test.check("enableAutoStop", True),
        test.check("enableStreamingIngest", True),
        test.check("publicNetworkAccess", "Enabled", case_sensitive=False),
        test.check("sku.name", "Standard_D11_v2", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step_cluster_principal_assignment_show(test, checks=[])
    step_database_show(test, checks=[])
    step_script_show(test, checks=[])
    step_database_principal_assignment_show(test, checks=[])
    step_attached_database_configuration_show(test, checks=[
        test.check("location", "West US 2", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
        test.check("tableLevelSharingProperties.externalTablesToExclude[0]", "ExternalTable2", case_sensitive=False),
        test.check("tableLevelSharingProperties.externalTablesToInclude[0]", "ExternalTable1", case_sensitive=False),
        test.check("tableLevelSharingProperties.materializedViewsToExclude[0]", "MaterializedViewTable2", case_sensitive=False),
        test.check("tableLevelSharingProperties.materializedViewsToInclude[0]", "MaterializedViewTable1", case_sensitive=False),
        test.check("tableLevelSharingProperties.tablesToExclude[0]", "Table2", case_sensitive=False),
        test.check("tableLevelSharingProperties.tablesToInclude[0]", "Table1", case_sensitive=False),
    ])
    step_data_connection_show(test, checks=[
        test.check("location", "West US 2", case_sensitive=False),
        test.check("eventHubResourceId", "/subscriptions/{subscription_id}/resourceGroups/testrg/providers/Microsoft.EventHub/namespaces/testcli/eventhubs/eventhubTest1", case_sensitive=False)
    ])
    step_managed_private_endpoint_show(test, checks=[])
    step_private_endpoint_connection_show(test, checks=[])
    #step_private_link_resource_show(test, checks=[])
    step_cluster_list(test, checks=[])
    step_cluster_list_by_resource_group(test, checks=[
        test.check('length(@)', 2),
    ])
    step_cluster_principal_assignment_list(test, checks=[])
    step_script_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_list_sku(test, checks=[])
    step_cluster_list_sku_by_resource_group(test, checks=[])
    step_cluster_list_language_extension(test, checks=[
        test.check('length(@)', 2),
    ])
    step_database_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_list_follower_database(test, checks=[
        test.check('length(@)', 1),
    ])
    step_database_principal_assignment_list(test, checks=[])
    step_database_list_principal(test, checks=[
            test.check('length(@)', 3),
    ])
    step_attached_database_configuration_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_data_connection_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_managed_private_endpoint_list(test, checks=[])
    step_cluster_diagnose_virtual_network(test, checks=[])
    step_cluster_list_outbound(test, checks=[])
    step_private_endpoint_connection_list(test, checks=[])
    #step_private_link_resource_list(test, checks=[
    #    test.check('length(@)', 1),
    #])
    ####################step_operation_result_show(test, checks=[])
    # Update + validation
    step_data_connection_event_hub_update(test, checks=[])
    step_managed_private_endpoint_update(test, checks=[])
    step_data_connection_validation(test, checks=[])
    step_script_update(test, checks=[])
    step_database_update(test, checks=[])
    step_cluster_stop(test, checks=[])
    step_cluster_start(test, checks=[])
    step_cluster_update(test, checks=[
        test.check("name", "{myCluster1}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "West US 2", case_sensitive=False),
        test.check("enableAutoStop", True),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("engineType", "V3", case_sensitive=False),
        test.check("restrictOutboundNetworkAccess", "Disabled", case_sensitive=False),
    ])
    # Remove  
    step_cluster_remove_language_extension(test, checks=[])
    step_managed_private_endpoint_delete(test, checks=[])
    step_private_endpoint_connection_delete(test, checks=[])
    step_script_delete(test, checks=[])
    step_database_principal_assignment_delete(test, checks=[])
    step_cluster_principal_assignment_delete(test, checks=[])
    step_database_remove_principal(test, checks=[])
    step_cluster_detach_follower_database(test, checks=[])
    step_attached_database_configuration_delete(test, checks=[])
    step_data_connection_delete(test, checks=[])
    step_database_delete(test, checks=[])
    step_cluster_delete(test, checks=[])
    # Cleanup
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class KustoScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(KustoScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myCluster': 'kustoCluster',
            'myScript': 'kustoScript',
            'myCluster1': 'KustoClusterLeader',
            'myDataConnection': 'dataConnectionTest',
            'myAttachedDatabaseConfiguration': 'attachedDatabaseConfigurationsTest',
            'myManagedPrivateEndpoint': 'kustoManagedPrivateEndpoint4',
            'myPrivateEndpoint': 'kustoPrivateEndpoint4',
            'myPrivateLinkResource': 'privateLinkResource'
        })

    @AllowLargeResponse(size_kb=5000)
    @ResourceGroupPreparer(name_prefix='clitestkusto_kustorptest'[:7], key='rg', parameter_name='rg')
    @StorageAccountPreparer(name_prefix='clitestkusto_storageAccountTest'[:7], key='sa', resource_group_parameter_name='rg')
    @StorageAccountPreparer(name_prefix='clitestkusto_teststorageaccount'[:7], key='sa_2', resource_group_parameter_name='rg')
    def test_kusto_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
