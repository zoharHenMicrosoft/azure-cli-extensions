# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AzureScaleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Scale type.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    NONE = "none"

class AzureSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """SKU name.
    """

    DEV_NO_SLA_STANDARD_D11_V2 = "Dev(No SLA)_Standard_D11_v2"
    DEV_NO_SLA_STANDARD_E2_A_V4 = "Dev(No SLA)_Standard_E2a_v4"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D32_D_V4 = "Standard_D32d_v4"
    STANDARD_D16_D_V5 = "Standard_D16d_v5"
    STANDARD_D32_D_V5 = "Standard_D32d_v5"
    STANDARD_DS13_V2_1_TB_PS = "Standard_DS13_v2+1TB_PS"
    STANDARD_DS13_V2_2_TB_PS = "Standard_DS13_v2+2TB_PS"
    STANDARD_DS14_V2_3_TB_PS = "Standard_DS14_v2+3TB_PS"
    STANDARD_DS14_V2_4_TB_PS = "Standard_DS14_v2+4TB_PS"
    STANDARD_L4_S = "Standard_L4s"
    STANDARD_L8_S = "Standard_L8s"
    STANDARD_L16_S = "Standard_L16s"
    STANDARD_L8_S_V2 = "Standard_L8s_v2"
    STANDARD_L16_S_V2 = "Standard_L16s_v2"
    STANDARD_E64_I_V3 = "Standard_E64i_v3"
    STANDARD_E80_IDS_V4 = "Standard_E80ids_v4"
    STANDARD_E2_A_V4 = "Standard_E2a_v4"
    STANDARD_E4_A_V4 = "Standard_E4a_v4"
    STANDARD_E8_A_V4 = "Standard_E8a_v4"
    STANDARD_E16_A_V4 = "Standard_E16a_v4"
    STANDARD_E8_AS_V4_1_TB_PS = "Standard_E8as_v4+1TB_PS"
    STANDARD_E8_AS_V4_2_TB_PS = "Standard_E8as_v4+2TB_PS"
    STANDARD_E16_AS_V4_3_TB_PS = "Standard_E16as_v4+3TB_PS"
    STANDARD_E16_AS_V4_4_TB_PS = "Standard_E16as_v4+4TB_PS"
    STANDARD_E8_AS_V5_1_TB_PS = "Standard_E8as_v5+1TB_PS"
    STANDARD_E8_AS_V5_2_TB_PS = "Standard_E8as_v5+2TB_PS"
    STANDARD_E16_AS_V5_3_TB_PS = "Standard_E16as_v5+3TB_PS"
    STANDARD_E16_AS_V5_4_TB_PS = "Standard_E16as_v5+4TB_PS"
    STANDARD_E2_ADS_V5 = "Standard_E2ads_v5"
    STANDARD_E4_ADS_V5 = "Standard_E4ads_v5"
    STANDARD_E8_ADS_V5 = "Standard_E8ads_v5"
    STANDARD_E16_ADS_V5 = "Standard_E16ads_v5"
    STANDARD_E8_S_V4_1_TB_PS = "Standard_E8s_v4+1TB_PS"
    STANDARD_E8_S_V4_2_TB_PS = "Standard_E8s_v4+2TB_PS"
    STANDARD_E16_S_V4_3_TB_PS = "Standard_E16s_v4+3TB_PS"
    STANDARD_E16_S_V4_4_TB_PS = "Standard_E16s_v4+4TB_PS"
    STANDARD_E8_S_V5_1_TB_PS = "Standard_E8s_v5+1TB_PS"
    STANDARD_E8_S_V5_2_TB_PS = "Standard_E8s_v5+2TB_PS"
    STANDARD_E16_S_V5_3_TB_PS = "Standard_E16s_v5+3TB_PS"
    STANDARD_E16_S_V5_4_TB_PS = "Standard_E16s_v5+4TB_PS"

class AzureSkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """SKU tier.
    """

    BASIC = "Basic"
    STANDARD = "Standard"

class BlobStorageEventType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The name of blob storage event type to process.
    """

    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_RENAMED = "Microsoft.Storage.BlobRenamed"

class ClusterNetworkAccessFlag(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether or not to restrict outbound network access.  Value is optional but if passed in, must
    be 'Enabled' or 'Disabled'
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ClusterPrincipalRole(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Cluster principal role.
    """

    ALL_DATABASES_ADMIN = "AllDatabasesAdmin"
    ALL_DATABASES_VIEWER = "AllDatabasesViewer"

class Compression(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The compression type
    """

    NONE = "None"
    G_ZIP = "GZip"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DatabasePrincipalRole(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Database principal role.
    """

    ADMIN = "Admin"
    INGESTOR = "Ingestor"
    MONITOR = "Monitor"
    USER = "User"
    UNRESTRICTED_VIEWER = "UnrestrictedViewer"
    VIEWER = "Viewer"

class DatabasePrincipalType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Database principal type.
    """

    APP = "App"
    GROUP = "Group"
    USER = "User"

class DatabaseRouting(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indication for database routing information from the data connection, by default only database
    routing information is allowed
    """

    SINGLE = "Single"
    MULTI = "Multi"

class DataConnectionKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of the endpoint for the data connection
    """

    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"

class DefaultPrincipalsModificationKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default principals modification kind
    """

    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"

class EngineType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The engine type
    """

    V2 = "V2"
    V3 = "V3"

class EventGridDataFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"

class EventHubDataFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"

class IdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an
    implicitly created identity and a set of user-assigned identities. The type 'None' will remove
    all identities.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"

class IotHubDataFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"

class Kind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of the database
    """

    READ_WRITE = "ReadWrite"
    READ_ONLY_FOLLOWING = "ReadOnlyFollowing"

class LanguageExtensionName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Language extension that can run within KQL query.
    """

    PYTHON = "PYTHON"
    R = "R"

class PrincipalsModificationKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The principals modification kind of the database
    """

    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"

class PrincipalType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Principal type.
    """

    APP = "App"
    GROUP = "Group"
    USER = "User"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioned state of the resource.
    """

    RUNNING = "Running"
    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    MOVING = "Moving"

class PublicIpType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates what public IP type to create - IPv4 (default), or DualStack (both IPv4 and IPv6)
    """

    I_PV4 = "IPv4"
    DUAL_STACK = "DualStack"

class PublicNetworkAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Public network access to the cluster is enabled by default. When disabled, only private
    endpoint connection to the cluster is allowed
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class Reason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Message providing the reason why the given name is invalid.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class State(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the resource.
    """

    CREATING = "Creating"
    UNAVAILABLE = "Unavailable"
    RUNNING = "Running"
    DELETING = "Deleting"
    DELETED = "Deleted"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    STARTING = "Starting"
    UPDATING = "Updating"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of operation.
    """

    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    RUNNING = "Running"

class Type(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of resource, for instance Microsoft.Kusto/clusters/databases.
    """

    MICROSOFT_KUSTO_CLUSTERS_DATABASES = "Microsoft.Kusto/clusters/databases"
    MICROSOFT_KUSTO_CLUSTERS_ATTACHED_DATABASE_CONFIGURATIONS = "Microsoft.Kusto/clusters/attachedDatabaseConfigurations"
