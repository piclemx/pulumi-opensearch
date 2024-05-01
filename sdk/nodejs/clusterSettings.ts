// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a cluster's (persistent) settings.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * const global = new opensearch.ClusterSettings("global", {
 *     actionAutoCreateIndex: "my-index-000001,index10,-index1*,+ind*",
 *     clusterMaxShardsPerNode: 10,
 * });
 * ```
 */
export class ClusterSettings extends pulumi.CustomResource {
    /**
     * Get an existing ClusterSettings resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterSettingsState, opts?: pulumi.CustomResourceOptions): ClusterSettings {
        return new ClusterSettings(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/clusterSettings:ClusterSettings';

    /**
     * Returns true if the given object is an instance of ClusterSettings.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterSettings {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterSettings.__pulumiType;
    }

    /**
     * Whether to automatically create an index if it doesn’t already exist and apply any configured index template
     */
    public readonly actionAutoCreateIndex!: pulumi.Output<string | undefined>;
    /**
     * When set to true, you must specify the index name to delete an index and it is not possible to delete all indices with _all or use wildcards
     */
    public readonly actionDestructiveRequiresName!: pulumi.Output<boolean | undefined>;
    /**
     * Make the whole cluster read only and metadata is not allowed to be modified
     */
    public readonly clusterBlocksReadOnly!: pulumi.Output<boolean | undefined>;
    /**
     * Make the whole cluster read only, but allows to delete indices to free up resources
     */
    public readonly clusterBlocksReadOnlyAllowDelete!: pulumi.Output<boolean | undefined>;
    /**
     * If false, you cannot close open indices
     */
    public readonly clusterIndicesCloseEnable!: pulumi.Output<boolean | undefined>;
    /**
     * A time string controlling how often OpenSearch should check on disk usage for each node in the cluster
     */
    public readonly clusterInfoUpdateInterval!: pulumi.Output<string | undefined>;
    /**
     * The total number of primary and replica shards for the cluster, this number is multiplied by the number of non-frozen data nodes; shards for closed indices do not count toward this limit
     */
    public readonly clusterMaxShardsPerNode!: pulumi.Output<number | undefined>;
    /**
     * The total number of primary and replica frozen shards, for the cluster; Ssards for closed indices do not count toward this limit, a cluster with no frozen data nodes is unlimited.
     */
    public readonly clusterMaxShardsPerNodeFrozen!: pulumi.Output<number | undefined>;
    /**
     * Specifies which operations are rejected when there is no active master in a cluster (all, write)
     */
    public readonly clusterNoMasterBlock!: pulumi.Output<string | undefined>;
    /**
     * Whether allocation for persistent tasks is active (all, none)
     */
    public readonly clusterPersistentTasksAllocationEnable!: pulumi.Output<string | undefined>;
    /**
     * A time string controling how often assignment checks are performed to react to whether persistent tasks can be assigned to nodes
     */
    public readonly clusterPersistentTasksAllocationRecheckInterval!: pulumi.Output<string | undefined>;
    /**
     * Specify when shard rebalancing is allowed (always, indices*primaries*active, indices*all*active)
     */
    public readonly clusterRoutingAllocationAllowRebalance!: pulumi.Output<string | undefined>;
    /**
     * Use custom node attributes to take hardware configuration into account when allocating shards
     */
    public readonly clusterRoutingAllocationAwarenessAttributes!: pulumi.Output<string | undefined>;
    /**
     * Weight factor for the number of shards per index allocated on a node, increasing this raises the tendency to equalize the number of shards per index across all nodes
     */
    public readonly clusterRoutingAllocationBalanceIndex!: pulumi.Output<number | undefined>;
    /**
     * Weight factor for the total number of shards allocated on a node, increasing this raises the tendency to equalize the number of shards across all nodes
     */
    public readonly clusterRoutingAllocationBalanceShard!: pulumi.Output<number | undefined>;
    /**
     * Minimal optimization value of operations that should be performed, raising this will cause the cluster to be less aggressive about optimizing the shard balance
     */
    public readonly clusterRoutingAllocationBalanceThreshold!: pulumi.Output<number | undefined>;
    /**
     * How many concurrent shard rebalances are allowed cluster wide
     */
    public readonly clusterRoutingAllocationClusterConcurrentRebalance!: pulumi.Output<number | undefined>;
    /**
     * Whether the allocator will take into account shards that are currently being relocated to the target node when computing a node’s disk usage
     */
    public readonly clusterRoutingAllocationDiskIncludeRelocations!: pulumi.Output<boolean | undefined>;
    /**
     * Whether the disk allocation decider is active
     */
    public readonly clusterRoutingAllocationDiskThresholdEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Allocator will attempt to relocate shards away from a node whose disk usage is above this percentage disk used
     */
    public readonly clusterRoutingAllocationDiskWatermarkHigh!: pulumi.Output<string | undefined>;
    /**
     * Allocator will not allocate shards to nodes that have more than this percentage disk used
     */
    public readonly clusterRoutingAllocationDiskWatermarkLow!: pulumi.Output<string | undefined>;
    /**
     * Enable or disable allocation for specific kinds of shards (all, primaries, new_primaries, none)
     */
    public readonly clusterRoutingAllocationEnable!: pulumi.Output<string | undefined>;
    /**
     * How many incoming recoveries where the target shard (likely the replica unless a shard is relocating) are allocated on the node
     */
    public readonly clusterRoutingAllocationNodeConcurrentIncomingRecoveries!: pulumi.Output<number | undefined>;
    /**
     * How many outgoing recoveries where the source shard (likely the primary unless a shard is relocating) are allocated on the node
     */
    public readonly clusterRoutingAllocationNodeConcurrentOutgoingRecoveries!: pulumi.Output<number | undefined>;
    /**
     * A shortcut to set both incoming and outgoing recoveries
     */
    public readonly clusterRoutingAllocationNodeConcurrentRecoveries!: pulumi.Output<number | undefined>;
    /**
     * Set a (usually) higher rate for primary recovery on node restart (usually from disk, so fast)
     */
    public readonly clusterRoutingAllocationNodeInitialPrimariesRecoveries!: pulumi.Output<number | undefined>;
    /**
     * Perform a check to prevent allocation of multiple instances of the same shard on a single host, if multiple nodes are started on the host
     */
    public readonly clusterRoutingAllocationSameShardHost!: pulumi.Output<boolean | undefined>;
    /**
     * Maximum number of primary and replica shards allocated to each node
     */
    public readonly clusterRoutingAllocationTotalShardsPerNode!: pulumi.Output<number | undefined>;
    /**
     * Allow rebalancing for specific kinds of shards (all, primaries, replicas, none)
     */
    public readonly clusterRoutingRebalanceEnable!: pulumi.Output<string | undefined>;
    /**
     * The percentage of memory above which if loading a field into the field data cache would cause the cache to exceed this limit, an error is returned
     */
    public readonly indicesBreakerFielddataLimit!: pulumi.Output<string | undefined>;
    /**
     * A constant that all field data estimations are multiplied by
     */
    public readonly indicesBreakerFielddataOverhead!: pulumi.Output<number | undefined>;
    /**
     * The percentabge of memory above which per-request data structures (e.g. calculating aggregations) are prevented from exceeding
     */
    public readonly indicesBreakerRequestLimit!: pulumi.Output<string | undefined>;
    /**
     * A constant that all request estimations are multiplied by
     */
    public readonly indicesBreakerRequestOverhead!: pulumi.Output<number | undefined>;
    /**
     * The percentage of total amount of memory that can be used across all breakers
     */
    public readonly indicesBreakerTotalLimit!: pulumi.Output<string | undefined>;
    /**
     * Maximum total inbound and outbound recovery traffic for each node, in mb
     */
    public readonly indicesRecoveryMaxBytesPerSec!: pulumi.Output<string | undefined>;
    /**
     * The percentage limit of memory usage on a node of all currently active incoming requests on transport or HTTP level
     */
    public readonly networkBreakerInflightRequestsLimit!: pulumi.Output<string | undefined>;
    /**
     * A constant that all in flight requests estimations are multiplied by
     */
    public readonly networkBreakerInflightRequestsOverhead!: pulumi.Output<number | undefined>;
    /**
     * Limit for the number of unique dynamic scripts within a certain interval that are allowed to be compiled, expressed as compilations divided by a time string
     */
    public readonly scriptMaxCompilationsRate!: pulumi.Output<string | undefined>;
    /**
     * A time string setting a cluster-wide default timeout for all search requests
     */
    public readonly searchDefaultSearchTimeout!: pulumi.Output<string | undefined>;

    /**
     * Create a ClusterSettings resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ClusterSettingsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterSettingsArgs | ClusterSettingsState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ClusterSettingsState | undefined;
            resourceInputs["actionAutoCreateIndex"] = state ? state.actionAutoCreateIndex : undefined;
            resourceInputs["actionDestructiveRequiresName"] = state ? state.actionDestructiveRequiresName : undefined;
            resourceInputs["clusterBlocksReadOnly"] = state ? state.clusterBlocksReadOnly : undefined;
            resourceInputs["clusterBlocksReadOnlyAllowDelete"] = state ? state.clusterBlocksReadOnlyAllowDelete : undefined;
            resourceInputs["clusterIndicesCloseEnable"] = state ? state.clusterIndicesCloseEnable : undefined;
            resourceInputs["clusterInfoUpdateInterval"] = state ? state.clusterInfoUpdateInterval : undefined;
            resourceInputs["clusterMaxShardsPerNode"] = state ? state.clusterMaxShardsPerNode : undefined;
            resourceInputs["clusterMaxShardsPerNodeFrozen"] = state ? state.clusterMaxShardsPerNodeFrozen : undefined;
            resourceInputs["clusterNoMasterBlock"] = state ? state.clusterNoMasterBlock : undefined;
            resourceInputs["clusterPersistentTasksAllocationEnable"] = state ? state.clusterPersistentTasksAllocationEnable : undefined;
            resourceInputs["clusterPersistentTasksAllocationRecheckInterval"] = state ? state.clusterPersistentTasksAllocationRecheckInterval : undefined;
            resourceInputs["clusterRoutingAllocationAllowRebalance"] = state ? state.clusterRoutingAllocationAllowRebalance : undefined;
            resourceInputs["clusterRoutingAllocationAwarenessAttributes"] = state ? state.clusterRoutingAllocationAwarenessAttributes : undefined;
            resourceInputs["clusterRoutingAllocationBalanceIndex"] = state ? state.clusterRoutingAllocationBalanceIndex : undefined;
            resourceInputs["clusterRoutingAllocationBalanceShard"] = state ? state.clusterRoutingAllocationBalanceShard : undefined;
            resourceInputs["clusterRoutingAllocationBalanceThreshold"] = state ? state.clusterRoutingAllocationBalanceThreshold : undefined;
            resourceInputs["clusterRoutingAllocationClusterConcurrentRebalance"] = state ? state.clusterRoutingAllocationClusterConcurrentRebalance : undefined;
            resourceInputs["clusterRoutingAllocationDiskIncludeRelocations"] = state ? state.clusterRoutingAllocationDiskIncludeRelocations : undefined;
            resourceInputs["clusterRoutingAllocationDiskThresholdEnabled"] = state ? state.clusterRoutingAllocationDiskThresholdEnabled : undefined;
            resourceInputs["clusterRoutingAllocationDiskWatermarkHigh"] = state ? state.clusterRoutingAllocationDiskWatermarkHigh : undefined;
            resourceInputs["clusterRoutingAllocationDiskWatermarkLow"] = state ? state.clusterRoutingAllocationDiskWatermarkLow : undefined;
            resourceInputs["clusterRoutingAllocationEnable"] = state ? state.clusterRoutingAllocationEnable : undefined;
            resourceInputs["clusterRoutingAllocationNodeConcurrentIncomingRecoveries"] = state ? state.clusterRoutingAllocationNodeConcurrentIncomingRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationNodeConcurrentOutgoingRecoveries"] = state ? state.clusterRoutingAllocationNodeConcurrentOutgoingRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationNodeConcurrentRecoveries"] = state ? state.clusterRoutingAllocationNodeConcurrentRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationNodeInitialPrimariesRecoveries"] = state ? state.clusterRoutingAllocationNodeInitialPrimariesRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationSameShardHost"] = state ? state.clusterRoutingAllocationSameShardHost : undefined;
            resourceInputs["clusterRoutingAllocationTotalShardsPerNode"] = state ? state.clusterRoutingAllocationTotalShardsPerNode : undefined;
            resourceInputs["clusterRoutingRebalanceEnable"] = state ? state.clusterRoutingRebalanceEnable : undefined;
            resourceInputs["indicesBreakerFielddataLimit"] = state ? state.indicesBreakerFielddataLimit : undefined;
            resourceInputs["indicesBreakerFielddataOverhead"] = state ? state.indicesBreakerFielddataOverhead : undefined;
            resourceInputs["indicesBreakerRequestLimit"] = state ? state.indicesBreakerRequestLimit : undefined;
            resourceInputs["indicesBreakerRequestOverhead"] = state ? state.indicesBreakerRequestOverhead : undefined;
            resourceInputs["indicesBreakerTotalLimit"] = state ? state.indicesBreakerTotalLimit : undefined;
            resourceInputs["indicesRecoveryMaxBytesPerSec"] = state ? state.indicesRecoveryMaxBytesPerSec : undefined;
            resourceInputs["networkBreakerInflightRequestsLimit"] = state ? state.networkBreakerInflightRequestsLimit : undefined;
            resourceInputs["networkBreakerInflightRequestsOverhead"] = state ? state.networkBreakerInflightRequestsOverhead : undefined;
            resourceInputs["scriptMaxCompilationsRate"] = state ? state.scriptMaxCompilationsRate : undefined;
            resourceInputs["searchDefaultSearchTimeout"] = state ? state.searchDefaultSearchTimeout : undefined;
        } else {
            const args = argsOrState as ClusterSettingsArgs | undefined;
            resourceInputs["actionAutoCreateIndex"] = args ? args.actionAutoCreateIndex : undefined;
            resourceInputs["actionDestructiveRequiresName"] = args ? args.actionDestructiveRequiresName : undefined;
            resourceInputs["clusterBlocksReadOnly"] = args ? args.clusterBlocksReadOnly : undefined;
            resourceInputs["clusterBlocksReadOnlyAllowDelete"] = args ? args.clusterBlocksReadOnlyAllowDelete : undefined;
            resourceInputs["clusterIndicesCloseEnable"] = args ? args.clusterIndicesCloseEnable : undefined;
            resourceInputs["clusterInfoUpdateInterval"] = args ? args.clusterInfoUpdateInterval : undefined;
            resourceInputs["clusterMaxShardsPerNode"] = args ? args.clusterMaxShardsPerNode : undefined;
            resourceInputs["clusterMaxShardsPerNodeFrozen"] = args ? args.clusterMaxShardsPerNodeFrozen : undefined;
            resourceInputs["clusterNoMasterBlock"] = args ? args.clusterNoMasterBlock : undefined;
            resourceInputs["clusterPersistentTasksAllocationEnable"] = args ? args.clusterPersistentTasksAllocationEnable : undefined;
            resourceInputs["clusterPersistentTasksAllocationRecheckInterval"] = args ? args.clusterPersistentTasksAllocationRecheckInterval : undefined;
            resourceInputs["clusterRoutingAllocationAllowRebalance"] = args ? args.clusterRoutingAllocationAllowRebalance : undefined;
            resourceInputs["clusterRoutingAllocationAwarenessAttributes"] = args ? args.clusterRoutingAllocationAwarenessAttributes : undefined;
            resourceInputs["clusterRoutingAllocationBalanceIndex"] = args ? args.clusterRoutingAllocationBalanceIndex : undefined;
            resourceInputs["clusterRoutingAllocationBalanceShard"] = args ? args.clusterRoutingAllocationBalanceShard : undefined;
            resourceInputs["clusterRoutingAllocationBalanceThreshold"] = args ? args.clusterRoutingAllocationBalanceThreshold : undefined;
            resourceInputs["clusterRoutingAllocationClusterConcurrentRebalance"] = args ? args.clusterRoutingAllocationClusterConcurrentRebalance : undefined;
            resourceInputs["clusterRoutingAllocationDiskIncludeRelocations"] = args ? args.clusterRoutingAllocationDiskIncludeRelocations : undefined;
            resourceInputs["clusterRoutingAllocationDiskThresholdEnabled"] = args ? args.clusterRoutingAllocationDiskThresholdEnabled : undefined;
            resourceInputs["clusterRoutingAllocationDiskWatermarkHigh"] = args ? args.clusterRoutingAllocationDiskWatermarkHigh : undefined;
            resourceInputs["clusterRoutingAllocationDiskWatermarkLow"] = args ? args.clusterRoutingAllocationDiskWatermarkLow : undefined;
            resourceInputs["clusterRoutingAllocationEnable"] = args ? args.clusterRoutingAllocationEnable : undefined;
            resourceInputs["clusterRoutingAllocationNodeConcurrentIncomingRecoveries"] = args ? args.clusterRoutingAllocationNodeConcurrentIncomingRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationNodeConcurrentOutgoingRecoveries"] = args ? args.clusterRoutingAllocationNodeConcurrentOutgoingRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationNodeConcurrentRecoveries"] = args ? args.clusterRoutingAllocationNodeConcurrentRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationNodeInitialPrimariesRecoveries"] = args ? args.clusterRoutingAllocationNodeInitialPrimariesRecoveries : undefined;
            resourceInputs["clusterRoutingAllocationSameShardHost"] = args ? args.clusterRoutingAllocationSameShardHost : undefined;
            resourceInputs["clusterRoutingAllocationTotalShardsPerNode"] = args ? args.clusterRoutingAllocationTotalShardsPerNode : undefined;
            resourceInputs["clusterRoutingRebalanceEnable"] = args ? args.clusterRoutingRebalanceEnable : undefined;
            resourceInputs["indicesBreakerFielddataLimit"] = args ? args.indicesBreakerFielddataLimit : undefined;
            resourceInputs["indicesBreakerFielddataOverhead"] = args ? args.indicesBreakerFielddataOverhead : undefined;
            resourceInputs["indicesBreakerRequestLimit"] = args ? args.indicesBreakerRequestLimit : undefined;
            resourceInputs["indicesBreakerRequestOverhead"] = args ? args.indicesBreakerRequestOverhead : undefined;
            resourceInputs["indicesBreakerTotalLimit"] = args ? args.indicesBreakerTotalLimit : undefined;
            resourceInputs["indicesRecoveryMaxBytesPerSec"] = args ? args.indicesRecoveryMaxBytesPerSec : undefined;
            resourceInputs["networkBreakerInflightRequestsLimit"] = args ? args.networkBreakerInflightRequestsLimit : undefined;
            resourceInputs["networkBreakerInflightRequestsOverhead"] = args ? args.networkBreakerInflightRequestsOverhead : undefined;
            resourceInputs["scriptMaxCompilationsRate"] = args ? args.scriptMaxCompilationsRate : undefined;
            resourceInputs["searchDefaultSearchTimeout"] = args ? args.searchDefaultSearchTimeout : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ClusterSettings.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ClusterSettings resources.
 */
export interface ClusterSettingsState {
    /**
     * Whether to automatically create an index if it doesn’t already exist and apply any configured index template
     */
    actionAutoCreateIndex?: pulumi.Input<string>;
    /**
     * When set to true, you must specify the index name to delete an index and it is not possible to delete all indices with _all or use wildcards
     */
    actionDestructiveRequiresName?: pulumi.Input<boolean>;
    /**
     * Make the whole cluster read only and metadata is not allowed to be modified
     */
    clusterBlocksReadOnly?: pulumi.Input<boolean>;
    /**
     * Make the whole cluster read only, but allows to delete indices to free up resources
     */
    clusterBlocksReadOnlyAllowDelete?: pulumi.Input<boolean>;
    /**
     * If false, you cannot close open indices
     */
    clusterIndicesCloseEnable?: pulumi.Input<boolean>;
    /**
     * A time string controlling how often OpenSearch should check on disk usage for each node in the cluster
     */
    clusterInfoUpdateInterval?: pulumi.Input<string>;
    /**
     * The total number of primary and replica shards for the cluster, this number is multiplied by the number of non-frozen data nodes; shards for closed indices do not count toward this limit
     */
    clusterMaxShardsPerNode?: pulumi.Input<number>;
    /**
     * The total number of primary and replica frozen shards, for the cluster; Ssards for closed indices do not count toward this limit, a cluster with no frozen data nodes is unlimited.
     */
    clusterMaxShardsPerNodeFrozen?: pulumi.Input<number>;
    /**
     * Specifies which operations are rejected when there is no active master in a cluster (all, write)
     */
    clusterNoMasterBlock?: pulumi.Input<string>;
    /**
     * Whether allocation for persistent tasks is active (all, none)
     */
    clusterPersistentTasksAllocationEnable?: pulumi.Input<string>;
    /**
     * A time string controling how often assignment checks are performed to react to whether persistent tasks can be assigned to nodes
     */
    clusterPersistentTasksAllocationRecheckInterval?: pulumi.Input<string>;
    /**
     * Specify when shard rebalancing is allowed (always, indices*primaries*active, indices*all*active)
     */
    clusterRoutingAllocationAllowRebalance?: pulumi.Input<string>;
    /**
     * Use custom node attributes to take hardware configuration into account when allocating shards
     */
    clusterRoutingAllocationAwarenessAttributes?: pulumi.Input<string>;
    /**
     * Weight factor for the number of shards per index allocated on a node, increasing this raises the tendency to equalize the number of shards per index across all nodes
     */
    clusterRoutingAllocationBalanceIndex?: pulumi.Input<number>;
    /**
     * Weight factor for the total number of shards allocated on a node, increasing this raises the tendency to equalize the number of shards across all nodes
     */
    clusterRoutingAllocationBalanceShard?: pulumi.Input<number>;
    /**
     * Minimal optimization value of operations that should be performed, raising this will cause the cluster to be less aggressive about optimizing the shard balance
     */
    clusterRoutingAllocationBalanceThreshold?: pulumi.Input<number>;
    /**
     * How many concurrent shard rebalances are allowed cluster wide
     */
    clusterRoutingAllocationClusterConcurrentRebalance?: pulumi.Input<number>;
    /**
     * Whether the allocator will take into account shards that are currently being relocated to the target node when computing a node’s disk usage
     */
    clusterRoutingAllocationDiskIncludeRelocations?: pulumi.Input<boolean>;
    /**
     * Whether the disk allocation decider is active
     */
    clusterRoutingAllocationDiskThresholdEnabled?: pulumi.Input<boolean>;
    /**
     * Allocator will attempt to relocate shards away from a node whose disk usage is above this percentage disk used
     */
    clusterRoutingAllocationDiskWatermarkHigh?: pulumi.Input<string>;
    /**
     * Allocator will not allocate shards to nodes that have more than this percentage disk used
     */
    clusterRoutingAllocationDiskWatermarkLow?: pulumi.Input<string>;
    /**
     * Enable or disable allocation for specific kinds of shards (all, primaries, new_primaries, none)
     */
    clusterRoutingAllocationEnable?: pulumi.Input<string>;
    /**
     * How many incoming recoveries where the target shard (likely the replica unless a shard is relocating) are allocated on the node
     */
    clusterRoutingAllocationNodeConcurrentIncomingRecoveries?: pulumi.Input<number>;
    /**
     * How many outgoing recoveries where the source shard (likely the primary unless a shard is relocating) are allocated on the node
     */
    clusterRoutingAllocationNodeConcurrentOutgoingRecoveries?: pulumi.Input<number>;
    /**
     * A shortcut to set both incoming and outgoing recoveries
     */
    clusterRoutingAllocationNodeConcurrentRecoveries?: pulumi.Input<number>;
    /**
     * Set a (usually) higher rate for primary recovery on node restart (usually from disk, so fast)
     */
    clusterRoutingAllocationNodeInitialPrimariesRecoveries?: pulumi.Input<number>;
    /**
     * Perform a check to prevent allocation of multiple instances of the same shard on a single host, if multiple nodes are started on the host
     */
    clusterRoutingAllocationSameShardHost?: pulumi.Input<boolean>;
    /**
     * Maximum number of primary and replica shards allocated to each node
     */
    clusterRoutingAllocationTotalShardsPerNode?: pulumi.Input<number>;
    /**
     * Allow rebalancing for specific kinds of shards (all, primaries, replicas, none)
     */
    clusterRoutingRebalanceEnable?: pulumi.Input<string>;
    /**
     * The percentage of memory above which if loading a field into the field data cache would cause the cache to exceed this limit, an error is returned
     */
    indicesBreakerFielddataLimit?: pulumi.Input<string>;
    /**
     * A constant that all field data estimations are multiplied by
     */
    indicesBreakerFielddataOverhead?: pulumi.Input<number>;
    /**
     * The percentabge of memory above which per-request data structures (e.g. calculating aggregations) are prevented from exceeding
     */
    indicesBreakerRequestLimit?: pulumi.Input<string>;
    /**
     * A constant that all request estimations are multiplied by
     */
    indicesBreakerRequestOverhead?: pulumi.Input<number>;
    /**
     * The percentage of total amount of memory that can be used across all breakers
     */
    indicesBreakerTotalLimit?: pulumi.Input<string>;
    /**
     * Maximum total inbound and outbound recovery traffic for each node, in mb
     */
    indicesRecoveryMaxBytesPerSec?: pulumi.Input<string>;
    /**
     * The percentage limit of memory usage on a node of all currently active incoming requests on transport or HTTP level
     */
    networkBreakerInflightRequestsLimit?: pulumi.Input<string>;
    /**
     * A constant that all in flight requests estimations are multiplied by
     */
    networkBreakerInflightRequestsOverhead?: pulumi.Input<number>;
    /**
     * Limit for the number of unique dynamic scripts within a certain interval that are allowed to be compiled, expressed as compilations divided by a time string
     */
    scriptMaxCompilationsRate?: pulumi.Input<string>;
    /**
     * A time string setting a cluster-wide default timeout for all search requests
     */
    searchDefaultSearchTimeout?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ClusterSettings resource.
 */
export interface ClusterSettingsArgs {
    /**
     * Whether to automatically create an index if it doesn’t already exist and apply any configured index template
     */
    actionAutoCreateIndex?: pulumi.Input<string>;
    /**
     * When set to true, you must specify the index name to delete an index and it is not possible to delete all indices with _all or use wildcards
     */
    actionDestructiveRequiresName?: pulumi.Input<boolean>;
    /**
     * Make the whole cluster read only and metadata is not allowed to be modified
     */
    clusterBlocksReadOnly?: pulumi.Input<boolean>;
    /**
     * Make the whole cluster read only, but allows to delete indices to free up resources
     */
    clusterBlocksReadOnlyAllowDelete?: pulumi.Input<boolean>;
    /**
     * If false, you cannot close open indices
     */
    clusterIndicesCloseEnable?: pulumi.Input<boolean>;
    /**
     * A time string controlling how often OpenSearch should check on disk usage for each node in the cluster
     */
    clusterInfoUpdateInterval?: pulumi.Input<string>;
    /**
     * The total number of primary and replica shards for the cluster, this number is multiplied by the number of non-frozen data nodes; shards for closed indices do not count toward this limit
     */
    clusterMaxShardsPerNode?: pulumi.Input<number>;
    /**
     * The total number of primary and replica frozen shards, for the cluster; Ssards for closed indices do not count toward this limit, a cluster with no frozen data nodes is unlimited.
     */
    clusterMaxShardsPerNodeFrozen?: pulumi.Input<number>;
    /**
     * Specifies which operations are rejected when there is no active master in a cluster (all, write)
     */
    clusterNoMasterBlock?: pulumi.Input<string>;
    /**
     * Whether allocation for persistent tasks is active (all, none)
     */
    clusterPersistentTasksAllocationEnable?: pulumi.Input<string>;
    /**
     * A time string controling how often assignment checks are performed to react to whether persistent tasks can be assigned to nodes
     */
    clusterPersistentTasksAllocationRecheckInterval?: pulumi.Input<string>;
    /**
     * Specify when shard rebalancing is allowed (always, indices*primaries*active, indices*all*active)
     */
    clusterRoutingAllocationAllowRebalance?: pulumi.Input<string>;
    /**
     * Use custom node attributes to take hardware configuration into account when allocating shards
     */
    clusterRoutingAllocationAwarenessAttributes?: pulumi.Input<string>;
    /**
     * Weight factor for the number of shards per index allocated on a node, increasing this raises the tendency to equalize the number of shards per index across all nodes
     */
    clusterRoutingAllocationBalanceIndex?: pulumi.Input<number>;
    /**
     * Weight factor for the total number of shards allocated on a node, increasing this raises the tendency to equalize the number of shards across all nodes
     */
    clusterRoutingAllocationBalanceShard?: pulumi.Input<number>;
    /**
     * Minimal optimization value of operations that should be performed, raising this will cause the cluster to be less aggressive about optimizing the shard balance
     */
    clusterRoutingAllocationBalanceThreshold?: pulumi.Input<number>;
    /**
     * How many concurrent shard rebalances are allowed cluster wide
     */
    clusterRoutingAllocationClusterConcurrentRebalance?: pulumi.Input<number>;
    /**
     * Whether the allocator will take into account shards that are currently being relocated to the target node when computing a node’s disk usage
     */
    clusterRoutingAllocationDiskIncludeRelocations?: pulumi.Input<boolean>;
    /**
     * Whether the disk allocation decider is active
     */
    clusterRoutingAllocationDiskThresholdEnabled?: pulumi.Input<boolean>;
    /**
     * Allocator will attempt to relocate shards away from a node whose disk usage is above this percentage disk used
     */
    clusterRoutingAllocationDiskWatermarkHigh?: pulumi.Input<string>;
    /**
     * Allocator will not allocate shards to nodes that have more than this percentage disk used
     */
    clusterRoutingAllocationDiskWatermarkLow?: pulumi.Input<string>;
    /**
     * Enable or disable allocation for specific kinds of shards (all, primaries, new_primaries, none)
     */
    clusterRoutingAllocationEnable?: pulumi.Input<string>;
    /**
     * How many incoming recoveries where the target shard (likely the replica unless a shard is relocating) are allocated on the node
     */
    clusterRoutingAllocationNodeConcurrentIncomingRecoveries?: pulumi.Input<number>;
    /**
     * How many outgoing recoveries where the source shard (likely the primary unless a shard is relocating) are allocated on the node
     */
    clusterRoutingAllocationNodeConcurrentOutgoingRecoveries?: pulumi.Input<number>;
    /**
     * A shortcut to set both incoming and outgoing recoveries
     */
    clusterRoutingAllocationNodeConcurrentRecoveries?: pulumi.Input<number>;
    /**
     * Set a (usually) higher rate for primary recovery on node restart (usually from disk, so fast)
     */
    clusterRoutingAllocationNodeInitialPrimariesRecoveries?: pulumi.Input<number>;
    /**
     * Perform a check to prevent allocation of multiple instances of the same shard on a single host, if multiple nodes are started on the host
     */
    clusterRoutingAllocationSameShardHost?: pulumi.Input<boolean>;
    /**
     * Maximum number of primary and replica shards allocated to each node
     */
    clusterRoutingAllocationTotalShardsPerNode?: pulumi.Input<number>;
    /**
     * Allow rebalancing for specific kinds of shards (all, primaries, replicas, none)
     */
    clusterRoutingRebalanceEnable?: pulumi.Input<string>;
    /**
     * The percentage of memory above which if loading a field into the field data cache would cause the cache to exceed this limit, an error is returned
     */
    indicesBreakerFielddataLimit?: pulumi.Input<string>;
    /**
     * A constant that all field data estimations are multiplied by
     */
    indicesBreakerFielddataOverhead?: pulumi.Input<number>;
    /**
     * The percentabge of memory above which per-request data structures (e.g. calculating aggregations) are prevented from exceeding
     */
    indicesBreakerRequestLimit?: pulumi.Input<string>;
    /**
     * A constant that all request estimations are multiplied by
     */
    indicesBreakerRequestOverhead?: pulumi.Input<number>;
    /**
     * The percentage of total amount of memory that can be used across all breakers
     */
    indicesBreakerTotalLimit?: pulumi.Input<string>;
    /**
     * Maximum total inbound and outbound recovery traffic for each node, in mb
     */
    indicesRecoveryMaxBytesPerSec?: pulumi.Input<string>;
    /**
     * The percentage limit of memory usage on a node of all currently active incoming requests on transport or HTTP level
     */
    networkBreakerInflightRequestsLimit?: pulumi.Input<string>;
    /**
     * A constant that all in flight requests estimations are multiplied by
     */
    networkBreakerInflightRequestsOverhead?: pulumi.Input<number>;
    /**
     * Limit for the number of unique dynamic scripts within a certain interval that are allowed to be compiled, expressed as compilations divided by a time string
     */
    scriptMaxCompilationsRate?: pulumi.Input<string>;
    /**
     * A time string setting a cluster-wide default timeout for all search requests
     */
    searchDefaultSearchTimeout?: pulumi.Input<string>;
}
