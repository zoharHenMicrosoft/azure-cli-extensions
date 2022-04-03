# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_kusto.generated._client_factory import (
    cf_cluster,
    cf_cluster_principal_assignment,
    cf_database,
    cf_attached_database_configuration,
    cf_managed_private_endpoint,
    cf_database_principal_assignment,
    cf_script,
    cf_private_endpoint_connection,
    cf_private_link_resource,
    cf_data_connection,
    cf_operation_result,
    cf_operation_result_location,
)


kusto_attached_database_configuration = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._attached_database_configurations_operations#AttachedDatabaseConfigurationsOperations.{}',
    client_factory=cf_attached_database_configuration,
)


kusto_cluster = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._clusters_operations#ClustersOperations.{}',
    client_factory=cf_cluster,
)


kusto_cluster_principal_assignment = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._cluster_principal_assignments_operations#ClusterPrincipalAssignmentsOperations.{}',
    client_factory=cf_cluster_principal_assignment,
)


kusto_data_connection = CliCommandType(
    operations_tmpl=(
        'azext_kusto.vendored_sdks.kusto.operations._data_connections_operations#DataConnectionsOperations.{}'
    ),
    client_factory=cf_data_connection,
)


kusto_database = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._databases_operations#DatabasesOperations.{}',
    client_factory=cf_database,
)


kusto_database_principal_assignment = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._database_principal_assignments_operations#DatabasePrincipalAssignmentsOperations.{}',
    client_factory=cf_database_principal_assignment,
)


kusto_managed_private_endpoint = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._managed_private_endpoints_operations#ManagedPrivateEndpointsOperations.{}',
    client_factory=cf_managed_private_endpoint,
)


kusto_operation_result = CliCommandType(
    operations_tmpl=(
        'azext_kusto.vendored_sdks.kusto.operations._operations_results_operations#OperationsResultsOperations.{}'
    ),
    client_factory=cf_operation_result,
)


kusto_operation_result_location = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._operations_results_location_operations#OperationsResultsLocationOperations.{}',
    client_factory=cf_operation_result_location,
)


kusto_private_endpoint_connection = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._private_endpoint_connections_operations#PrivateEndpointConnectionsOperations.{}',
    client_factory=cf_private_endpoint_connection,
)


kusto_private_link_resource = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._private_link_resources_operations#PrivateLinkResourcesOperations.{}',
    client_factory=cf_private_link_resource,
)


kusto_script = CliCommandType(
    operations_tmpl='azext_kusto.vendored_sdks.kusto.operations._scripts_operations#ScriptsOperations.{}',
    client_factory=cf_script,
)


def load_command_table(self, _):

    with self.command_group(
        'kusto attached-database-configuration',
        kusto_attached_database_configuration,
        client_factory=cf_attached_database_configuration,
    ) as g:
        g.custom_command('list', 'kusto_attached_database_configuration_list')
        g.custom_show_command('show', 'kusto_attached_database_configuration_show')
        g.custom_command('create', 'kusto_attached_database_configuration_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_attached_database_configuration_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'kusto_attached_database_configuration_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'kusto_attached_database_configuration_show')

    with self.command_group('kusto cluster', kusto_cluster, client_factory=cf_cluster) as g:
        g.custom_command('list', 'kusto_cluster_list')
        g.custom_show_command('show', 'kusto_cluster_show')
        g.custom_command('create', 'kusto_cluster_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_cluster_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_cluster_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('add-language-extension', 'kusto_cluster_add_language_extension', supports_no_wait=True)
        g.custom_command('detach-follower-database', 'kusto_cluster_detach_follower_database', supports_no_wait=True)
        g.custom_command('diagnose-virtual-network', 'kusto_cluster_diagnose_virtual_network', supports_no_wait=True)
        g.custom_command('list-follower-database', 'kusto_cluster_list_follower_database')
        g.custom_command('list-language-extension', 'kusto_cluster_list_language_extension')
        g.custom_command(
            'list-outbound-network-dependency-endpoint', 'kusto_cluster_list_outbound_network_dependency_endpoint'
        )
        g.custom_command('list-sku', 'kusto_cluster_list_sku')
        g.custom_command('remove-language-extension', 'kusto_cluster_remove_language_extension', supports_no_wait=True)
        g.custom_command('start', 'kusto_cluster_start', supports_no_wait=True)
        g.custom_command('stop', 'kusto_cluster_stop', supports_no_wait=True)
        g.custom_wait_command('wait', 'kusto_cluster_show')

    with self.command_group(
        'kusto cluster-principal-assignment',
        kusto_cluster_principal_assignment,
        client_factory=cf_cluster_principal_assignment,
    ) as g:
        g.custom_command('list', 'kusto_cluster_principal_assignment_list')
        g.custom_show_command('show', 'kusto_cluster_principal_assignment_show')
        g.custom_command('create', 'kusto_cluster_principal_assignment_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_cluster_principal_assignment_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'kusto_cluster_principal_assignment_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'kusto_cluster_principal_assignment_show')

    with self.command_group('kusto data-connection', kusto_data_connection, client_factory=cf_data_connection) as g:
        g.custom_command('list', 'kusto_data_connection_list')
        g.custom_show_command('show', 'kusto_data_connection_show')
        g.custom_command('event-grid create', 'kusto_data_connection_event_grid_create', supports_no_wait=True)
        g.custom_command('event-hub create', 'kusto_data_connection_event_hub_create', supports_no_wait=True)
        g.custom_command('iot-hub create', 'kusto_data_connection_iot_hub_create', supports_no_wait=True)
        g.custom_command('event-grid update', 'kusto_data_connection_event_grid_update', supports_no_wait=True)
        g.custom_command('event-hub update', 'kusto_data_connection_event_hub_update', supports_no_wait=True)
        g.custom_command('iot-hub update', 'kusto_data_connection_iot_hub_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_data_connection_delete', supports_no_wait=True, confirmation=True)
        g.custom_command(
            'event-grid data-connection-validation',
            'kusto_data_connection_event_grid_data_connection_validation',
            supports_no_wait=True,
        )
        g.custom_command(
            'event-hub data-connection-validation',
            'kusto_data_connection_event_hub_data_connection_validation',
            supports_no_wait=True,
        )
        g.custom_command(
            'iot-hub data-connection-validation',
            'kusto_data_connection_iot_hub_data_connection_validation',
            supports_no_wait=True,
        )
        g.custom_wait_command('wait', 'kusto_data_connection_show')

    with self.command_group('kusto database', kusto_database, client_factory=cf_database) as g:
        g.custom_command('list', 'kusto_database_list')
        g.custom_show_command('show', 'kusto_database_show')
        g.custom_command('create', 'kusto_database_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_database_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_database_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('add-principal', 'kusto_database_add_principal')
        g.custom_command('list-principal', 'kusto_database_list_principal')
        g.custom_command('remove-principal', 'kusto_database_remove_principal')
        g.custom_wait_command('wait', 'kusto_database_show')

    with self.command_group(
        'kusto database-principal-assignment',
        kusto_database_principal_assignment,
        client_factory=cf_database_principal_assignment,
    ) as g:
        g.custom_command('list', 'kusto_database_principal_assignment_list')
        g.custom_show_command('show', 'kusto_database_principal_assignment_show')
        g.custom_command('create', 'kusto_database_principal_assignment_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_database_principal_assignment_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'kusto_database_principal_assignment_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'kusto_database_principal_assignment_show')

    with self.command_group(
        'kusto managed-private-endpoint', kusto_managed_private_endpoint, client_factory=cf_managed_private_endpoint
    ) as g:
        g.custom_command('list', 'kusto_managed_private_endpoint_list')
        g.custom_show_command('show', 'kusto_managed_private_endpoint_show')
        g.custom_command('create', 'kusto_managed_private_endpoint_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_managed_private_endpoint_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_managed_private_endpoint_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'kusto_managed_private_endpoint_show')

    with self.command_group('kusto operation-result', kusto_operation_result, client_factory=cf_operation_result) as g:
        g.custom_show_command('show', 'kusto_operation_result_show')

    with self.command_group(
        'kusto operation-result-location', kusto_operation_result_location, client_factory=cf_operation_result_location
    ) as g:
        g.custom_show_command('show', 'kusto_operation_result_location_show')

    with self.command_group(
        'kusto private-endpoint-connection',
        kusto_private_endpoint_connection,
        client_factory=cf_private_endpoint_connection,
    ) as g:
        g.custom_command('list', 'kusto_private_endpoint_connection_list')
        g.custom_show_command('show', 'kusto_private_endpoint_connection_show')
        g.custom_command('create', 'kusto_private_endpoint_connection_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_private_endpoint_connection_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command('delete', 'kusto_private_endpoint_connection_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'kusto_private_endpoint_connection_show')

    with self.command_group(
        'kusto private-link-resource', kusto_private_link_resource, client_factory=cf_private_link_resource
    ) as g:
        g.custom_command('list', 'kusto_private_link_resource_list')
        g.custom_show_command('show', 'kusto_private_link_resource_show')

    with self.command_group('kusto script', kusto_script, client_factory=cf_script) as g:
        g.custom_command('list', 'kusto_script_list')
        g.custom_show_command('show', 'kusto_script_show')
        g.custom_command('create', 'kusto_script_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_script_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_script_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'kusto_script_show')

    with self.command_group('kusto', is_experimental=True):
        pass
