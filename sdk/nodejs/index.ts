// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { AnomalyDetectionArgs, AnomalyDetectionState } from "./anomalyDetection";
export type AnomalyDetection = import("./anomalyDetection").AnomalyDetection;
export const AnomalyDetection: typeof import("./anomalyDetection").AnomalyDetection = null as any;
utilities.lazyLoad(exports, ["AnomalyDetection"], () => require("./anomalyDetection"));

export { AuditConfigArgs, AuditConfigState } from "./auditConfig";
export type AuditConfig = import("./auditConfig").AuditConfig;
export const AuditConfig: typeof import("./auditConfig").AuditConfig = null as any;
utilities.lazyLoad(exports, ["AuditConfig"], () => require("./auditConfig"));

export { ChannelConfigurationArgs, ChannelConfigurationState } from "./channelConfiguration";
export type ChannelConfiguration = import("./channelConfiguration").ChannelConfiguration;
export const ChannelConfiguration: typeof import("./channelConfiguration").ChannelConfiguration = null as any;
utilities.lazyLoad(exports, ["ChannelConfiguration"], () => require("./channelConfiguration"));

export { ClusterSettingsArgs, ClusterSettingsState } from "./clusterSettings";
export type ClusterSettings = import("./clusterSettings").ClusterSettings;
export const ClusterSettings: typeof import("./clusterSettings").ClusterSettings = null as any;
utilities.lazyLoad(exports, ["ClusterSettings"], () => require("./clusterSettings"));

export { ComponentTemplateArgs, ComponentTemplateState } from "./componentTemplate";
export type ComponentTemplate = import("./componentTemplate").ComponentTemplate;
export const ComponentTemplate: typeof import("./componentTemplate").ComponentTemplate = null as any;
utilities.lazyLoad(exports, ["ComponentTemplate"], () => require("./componentTemplate"));

export { ComposableIndexTemplateArgs, ComposableIndexTemplateState } from "./composableIndexTemplate";
export type ComposableIndexTemplate = import("./composableIndexTemplate").ComposableIndexTemplate;
export const ComposableIndexTemplate: typeof import("./composableIndexTemplate").ComposableIndexTemplate = null as any;
utilities.lazyLoad(exports, ["ComposableIndexTemplate"], () => require("./composableIndexTemplate"));

export { DashboardObjectArgs, DashboardObjectState } from "./dashboardObject";
export type DashboardObject = import("./dashboardObject").DashboardObject;
export const DashboardObject: typeof import("./dashboardObject").DashboardObject = null as any;
utilities.lazyLoad(exports, ["DashboardObject"], () => require("./dashboardObject"));

export { DashboardTenantArgs, DashboardTenantState } from "./dashboardTenant";
export type DashboardTenant = import("./dashboardTenant").DashboardTenant;
export const DashboardTenant: typeof import("./dashboardTenant").DashboardTenant = null as any;
utilities.lazyLoad(exports, ["DashboardTenant"], () => require("./dashboardTenant"));

export { DataStreamArgs, DataStreamState } from "./dataStream";
export type DataStream = import("./dataStream").DataStream;
export const DataStream: typeof import("./dataStream").DataStream = null as any;
utilities.lazyLoad(exports, ["DataStream"], () => require("./dataStream"));

export { GetHostArgs, GetHostResult, GetHostOutputArgs } from "./getHost";
export const getHost: typeof import("./getHost").getHost = null as any;
export const getHostOutput: typeof import("./getHost").getHostOutput = null as any;
utilities.lazyLoad(exports, ["getHost","getHostOutput"], () => require("./getHost"));

export { IndexTemplateArgs, IndexTemplateState } from "./indexTemplate";
export type IndexTemplate = import("./indexTemplate").IndexTemplate;
export const IndexTemplate: typeof import("./indexTemplate").IndexTemplate = null as any;
utilities.lazyLoad(exports, ["IndexTemplate"], () => require("./indexTemplate"));

export { IndexArgs, IndexState } from "./index_";
export type Index = import("./index_").Index;
export const Index: typeof import("./index_").Index = null as any;
utilities.lazyLoad(exports, ["Index"], () => require("./index_"));

export { IngestPipelineArgs, IngestPipelineState } from "./ingestPipeline";
export type IngestPipeline = import("./ingestPipeline").IngestPipeline;
export const IngestPipeline: typeof import("./ingestPipeline").IngestPipeline = null as any;
utilities.lazyLoad(exports, ["IngestPipeline"], () => require("./ingestPipeline"));

export { IsmPolicyArgs, IsmPolicyState } from "./ismPolicy";
export type IsmPolicy = import("./ismPolicy").IsmPolicy;
export const IsmPolicy: typeof import("./ismPolicy").IsmPolicy = null as any;
utilities.lazyLoad(exports, ["IsmPolicy"], () => require("./ismPolicy"));

export { IsmPolicyMappingArgs, IsmPolicyMappingState } from "./ismPolicyMapping";
export type IsmPolicyMapping = import("./ismPolicyMapping").IsmPolicyMapping;
export const IsmPolicyMapping: typeof import("./ismPolicyMapping").IsmPolicyMapping = null as any;
utilities.lazyLoad(exports, ["IsmPolicyMapping"], () => require("./ismPolicyMapping"));

export { MonitorArgs, MonitorState } from "./monitor";
export type Monitor = import("./monitor").Monitor;
export const Monitor: typeof import("./monitor").Monitor = null as any;
utilities.lazyLoad(exports, ["Monitor"], () => require("./monitor"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { RoleArgs, RoleState } from "./role";
export type Role = import("./role").Role;
export const Role: typeof import("./role").Role = null as any;
utilities.lazyLoad(exports, ["Role"], () => require("./role"));

export { RolesMappingArgs, RolesMappingState } from "./rolesMapping";
export type RolesMapping = import("./rolesMapping").RolesMapping;
export const RolesMapping: typeof import("./rolesMapping").RolesMapping = null as any;
utilities.lazyLoad(exports, ["RolesMapping"], () => require("./rolesMapping"));

export { ScriptArgs, ScriptState } from "./script";
export type Script = import("./script").Script;
export const Script: typeof import("./script").Script = null as any;
utilities.lazyLoad(exports, ["Script"], () => require("./script"));

export { SmPolicyArgs, SmPolicyState } from "./smPolicy";
export type SmPolicy = import("./smPolicy").SmPolicy;
export const SmPolicy: typeof import("./smPolicy").SmPolicy = null as any;
utilities.lazyLoad(exports, ["SmPolicy"], () => require("./smPolicy"));

export { SnapshotRepositoryArgs, SnapshotRepositoryState } from "./snapshotRepository";
export type SnapshotRepository = import("./snapshotRepository").SnapshotRepository;
export const SnapshotRepository: typeof import("./snapshotRepository").SnapshotRepository = null as any;
utilities.lazyLoad(exports, ["SnapshotRepository"], () => require("./snapshotRepository"));

export { UserArgs, UserState } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "opensearch:index/anomalyDetection:AnomalyDetection":
                return new AnomalyDetection(name, <any>undefined, { urn })
            case "opensearch:index/auditConfig:AuditConfig":
                return new AuditConfig(name, <any>undefined, { urn })
            case "opensearch:index/channelConfiguration:ChannelConfiguration":
                return new ChannelConfiguration(name, <any>undefined, { urn })
            case "opensearch:index/clusterSettings:ClusterSettings":
                return new ClusterSettings(name, <any>undefined, { urn })
            case "opensearch:index/componentTemplate:ComponentTemplate":
                return new ComponentTemplate(name, <any>undefined, { urn })
            case "opensearch:index/composableIndexTemplate:ComposableIndexTemplate":
                return new ComposableIndexTemplate(name, <any>undefined, { urn })
            case "opensearch:index/dashboardObject:DashboardObject":
                return new DashboardObject(name, <any>undefined, { urn })
            case "opensearch:index/dashboardTenant:DashboardTenant":
                return new DashboardTenant(name, <any>undefined, { urn })
            case "opensearch:index/dataStream:DataStream":
                return new DataStream(name, <any>undefined, { urn })
            case "opensearch:index/index:Index":
                return new Index(name, <any>undefined, { urn })
            case "opensearch:index/indexTemplate:IndexTemplate":
                return new IndexTemplate(name, <any>undefined, { urn })
            case "opensearch:index/ingestPipeline:IngestPipeline":
                return new IngestPipeline(name, <any>undefined, { urn })
            case "opensearch:index/ismPolicy:IsmPolicy":
                return new IsmPolicy(name, <any>undefined, { urn })
            case "opensearch:index/ismPolicyMapping:IsmPolicyMapping":
                return new IsmPolicyMapping(name, <any>undefined, { urn })
            case "opensearch:index/monitor:Monitor":
                return new Monitor(name, <any>undefined, { urn })
            case "opensearch:index/role:Role":
                return new Role(name, <any>undefined, { urn })
            case "opensearch:index/rolesMapping:RolesMapping":
                return new RolesMapping(name, <any>undefined, { urn })
            case "opensearch:index/script:Script":
                return new Script(name, <any>undefined, { urn })
            case "opensearch:index/smPolicy:SmPolicy":
                return new SmPolicy(name, <any>undefined, { urn })
            case "opensearch:index/snapshotRepository:SnapshotRepository":
                return new SnapshotRepository(name, <any>undefined, { urn })
            case "opensearch:index/user:User":
                return new User(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("opensearch", "index/anomalyDetection", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/auditConfig", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/channelConfiguration", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/clusterSettings", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/componentTemplate", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/composableIndexTemplate", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/dashboardObject", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/dashboardTenant", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/dataStream", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/index", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/indexTemplate", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/ingestPipeline", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/ismPolicy", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/ismPolicyMapping", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/monitor", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/role", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/rolesMapping", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/script", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/smPolicy", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/snapshotRepository", _module)
pulumi.runtime.registerResourceModule("opensearch", "index/user", _module)
pulumi.runtime.registerResourcePackage("opensearch", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:opensearch") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});