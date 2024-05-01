// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Piclemx.Opensearch
{
    /// <summary>
    /// Manages a cluster's (persistent) settings.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Opensearch = Piclemx.Opensearch;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var @global = new Opensearch.ClusterSettings("global", new()
    ///     {
    ///         ActionAutoCreateIndex = "my-index-000001,index10,-index1*,+ind*",
    ///         ClusterMaxShardsPerNode = 10,
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [OpensearchResourceType("opensearch:index/clusterSettings:ClusterSettings")]
    public partial class ClusterSettings : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Whether to automatically create an index if it doesn’t already exist and apply any configured index template
        /// </summary>
        [Output("actionAutoCreateIndex")]
        public Output<string?> ActionAutoCreateIndex { get; private set; } = null!;

        /// <summary>
        /// When set to true, you must specify the index name to delete an index and it is not possible to delete all indices with _all or use wildcards
        /// </summary>
        [Output("actionDestructiveRequiresName")]
        public Output<bool?> ActionDestructiveRequiresName { get; private set; } = null!;

        /// <summary>
        /// Make the whole cluster read only and metadata is not allowed to be modified
        /// </summary>
        [Output("clusterBlocksReadOnly")]
        public Output<bool?> ClusterBlocksReadOnly { get; private set; } = null!;

        /// <summary>
        /// Make the whole cluster read only, but allows to delete indices to free up resources
        /// </summary>
        [Output("clusterBlocksReadOnlyAllowDelete")]
        public Output<bool?> ClusterBlocksReadOnlyAllowDelete { get; private set; } = null!;

        /// <summary>
        /// If false, you cannot close open indices
        /// </summary>
        [Output("clusterIndicesCloseEnable")]
        public Output<bool?> ClusterIndicesCloseEnable { get; private set; } = null!;

        /// <summary>
        /// A time string controlling how often OpenSearch should check on disk usage for each node in the cluster
        /// </summary>
        [Output("clusterInfoUpdateInterval")]
        public Output<string?> ClusterInfoUpdateInterval { get; private set; } = null!;

        /// <summary>
        /// The total number of primary and replica shards for the cluster, this number is multiplied by the number of non-frozen data nodes; shards for closed indices do not count toward this limit
        /// </summary>
        [Output("clusterMaxShardsPerNode")]
        public Output<int?> ClusterMaxShardsPerNode { get; private set; } = null!;

        /// <summary>
        /// The total number of primary and replica frozen shards, for the cluster; Ssards for closed indices do not count toward this limit, a cluster with no frozen data nodes is unlimited.
        /// </summary>
        [Output("clusterMaxShardsPerNodeFrozen")]
        public Output<int?> ClusterMaxShardsPerNodeFrozen { get; private set; } = null!;

        /// <summary>
        /// Specifies which operations are rejected when there is no active master in a cluster (all, write)
        /// </summary>
        [Output("clusterNoMasterBlock")]
        public Output<string?> ClusterNoMasterBlock { get; private set; } = null!;

        /// <summary>
        /// Whether allocation for persistent tasks is active (all, none)
        /// </summary>
        [Output("clusterPersistentTasksAllocationEnable")]
        public Output<string?> ClusterPersistentTasksAllocationEnable { get; private set; } = null!;

        /// <summary>
        /// A time string controling how often assignment checks are performed to react to whether persistent tasks can be assigned to nodes
        /// </summary>
        [Output("clusterPersistentTasksAllocationRecheckInterval")]
        public Output<string?> ClusterPersistentTasksAllocationRecheckInterval { get; private set; } = null!;

        /// <summary>
        /// Specify when shard rebalancing is allowed (always, indices*primaries*active, indices*all*active)
        /// </summary>
        [Output("clusterRoutingAllocationAllowRebalance")]
        public Output<string?> ClusterRoutingAllocationAllowRebalance { get; private set; } = null!;

        /// <summary>
        /// Use custom node attributes to take hardware configuration into account when allocating shards
        /// </summary>
        [Output("clusterRoutingAllocationAwarenessAttributes")]
        public Output<string?> ClusterRoutingAllocationAwarenessAttributes { get; private set; } = null!;

        /// <summary>
        /// Weight factor for the number of shards per index allocated on a node, increasing this raises the tendency to equalize the number of shards per index across all nodes
        /// </summary>
        [Output("clusterRoutingAllocationBalanceIndex")]
        public Output<double?> ClusterRoutingAllocationBalanceIndex { get; private set; } = null!;

        /// <summary>
        /// Weight factor for the total number of shards allocated on a node, increasing this raises the tendency to equalize the number of shards across all nodes
        /// </summary>
        [Output("clusterRoutingAllocationBalanceShard")]
        public Output<double?> ClusterRoutingAllocationBalanceShard { get; private set; } = null!;

        /// <summary>
        /// Minimal optimization value of operations that should be performed, raising this will cause the cluster to be less aggressive about optimizing the shard balance
        /// </summary>
        [Output("clusterRoutingAllocationBalanceThreshold")]
        public Output<double?> ClusterRoutingAllocationBalanceThreshold { get; private set; } = null!;

        /// <summary>
        /// How many concurrent shard rebalances are allowed cluster wide
        /// </summary>
        [Output("clusterRoutingAllocationClusterConcurrentRebalance")]
        public Output<int?> ClusterRoutingAllocationClusterConcurrentRebalance { get; private set; } = null!;

        /// <summary>
        /// Whether the allocator will take into account shards that are currently being relocated to the target node when computing a node’s disk usage
        /// </summary>
        [Output("clusterRoutingAllocationDiskIncludeRelocations")]
        public Output<bool?> ClusterRoutingAllocationDiskIncludeRelocations { get; private set; } = null!;

        /// <summary>
        /// Whether the disk allocation decider is active
        /// </summary>
        [Output("clusterRoutingAllocationDiskThresholdEnabled")]
        public Output<bool?> ClusterRoutingAllocationDiskThresholdEnabled { get; private set; } = null!;

        /// <summary>
        /// Allocator will attempt to relocate shards away from a node whose disk usage is above this percentage disk used
        /// </summary>
        [Output("clusterRoutingAllocationDiskWatermarkHigh")]
        public Output<string?> ClusterRoutingAllocationDiskWatermarkHigh { get; private set; } = null!;

        /// <summary>
        /// Allocator will not allocate shards to nodes that have more than this percentage disk used
        /// </summary>
        [Output("clusterRoutingAllocationDiskWatermarkLow")]
        public Output<string?> ClusterRoutingAllocationDiskWatermarkLow { get; private set; } = null!;

        /// <summary>
        /// Enable or disable allocation for specific kinds of shards (all, primaries, new_primaries, none)
        /// </summary>
        [Output("clusterRoutingAllocationEnable")]
        public Output<string?> ClusterRoutingAllocationEnable { get; private set; } = null!;

        /// <summary>
        /// How many incoming recoveries where the target shard (likely the replica unless a shard is relocating) are allocated on the node
        /// </summary>
        [Output("clusterRoutingAllocationNodeConcurrentIncomingRecoveries")]
        public Output<int?> ClusterRoutingAllocationNodeConcurrentIncomingRecoveries { get; private set; } = null!;

        /// <summary>
        /// How many outgoing recoveries where the source shard (likely the primary unless a shard is relocating) are allocated on the node
        /// </summary>
        [Output("clusterRoutingAllocationNodeConcurrentOutgoingRecoveries")]
        public Output<int?> ClusterRoutingAllocationNodeConcurrentOutgoingRecoveries { get; private set; } = null!;

        /// <summary>
        /// A shortcut to set both incoming and outgoing recoveries
        /// </summary>
        [Output("clusterRoutingAllocationNodeConcurrentRecoveries")]
        public Output<int?> ClusterRoutingAllocationNodeConcurrentRecoveries { get; private set; } = null!;

        /// <summary>
        /// Set a (usually) higher rate for primary recovery on node restart (usually from disk, so fast)
        /// </summary>
        [Output("clusterRoutingAllocationNodeInitialPrimariesRecoveries")]
        public Output<int?> ClusterRoutingAllocationNodeInitialPrimariesRecoveries { get; private set; } = null!;

        /// <summary>
        /// Perform a check to prevent allocation of multiple instances of the same shard on a single host, if multiple nodes are started on the host
        /// </summary>
        [Output("clusterRoutingAllocationSameShardHost")]
        public Output<bool?> ClusterRoutingAllocationSameShardHost { get; private set; } = null!;

        /// <summary>
        /// Maximum number of primary and replica shards allocated to each node
        /// </summary>
        [Output("clusterRoutingAllocationTotalShardsPerNode")]
        public Output<int?> ClusterRoutingAllocationTotalShardsPerNode { get; private set; } = null!;

        /// <summary>
        /// Allow rebalancing for specific kinds of shards (all, primaries, replicas, none)
        /// </summary>
        [Output("clusterRoutingRebalanceEnable")]
        public Output<string?> ClusterRoutingRebalanceEnable { get; private set; } = null!;

        /// <summary>
        /// The percentage of memory above which if loading a field into the field data cache would cause the cache to exceed this limit, an error is returned
        /// </summary>
        [Output("indicesBreakerFielddataLimit")]
        public Output<string?> IndicesBreakerFielddataLimit { get; private set; } = null!;

        /// <summary>
        /// A constant that all field data estimations are multiplied by
        /// </summary>
        [Output("indicesBreakerFielddataOverhead")]
        public Output<double?> IndicesBreakerFielddataOverhead { get; private set; } = null!;

        /// <summary>
        /// The percentabge of memory above which per-request data structures (e.g. calculating aggregations) are prevented from exceeding
        /// </summary>
        [Output("indicesBreakerRequestLimit")]
        public Output<string?> IndicesBreakerRequestLimit { get; private set; } = null!;

        /// <summary>
        /// A constant that all request estimations are multiplied by
        /// </summary>
        [Output("indicesBreakerRequestOverhead")]
        public Output<double?> IndicesBreakerRequestOverhead { get; private set; } = null!;

        /// <summary>
        /// The percentage of total amount of memory that can be used across all breakers
        /// </summary>
        [Output("indicesBreakerTotalLimit")]
        public Output<string?> IndicesBreakerTotalLimit { get; private set; } = null!;

        /// <summary>
        /// Maximum total inbound and outbound recovery traffic for each node, in mb
        /// </summary>
        [Output("indicesRecoveryMaxBytesPerSec")]
        public Output<string?> IndicesRecoveryMaxBytesPerSec { get; private set; } = null!;

        /// <summary>
        /// The percentage limit of memory usage on a node of all currently active incoming requests on transport or HTTP level
        /// </summary>
        [Output("networkBreakerInflightRequestsLimit")]
        public Output<string?> NetworkBreakerInflightRequestsLimit { get; private set; } = null!;

        /// <summary>
        /// A constant that all in flight requests estimations are multiplied by
        /// </summary>
        [Output("networkBreakerInflightRequestsOverhead")]
        public Output<double?> NetworkBreakerInflightRequestsOverhead { get; private set; } = null!;

        /// <summary>
        /// Limit for the number of unique dynamic scripts within a certain interval that are allowed to be compiled, expressed as compilations divided by a time string
        /// </summary>
        [Output("scriptMaxCompilationsRate")]
        public Output<string?> ScriptMaxCompilationsRate { get; private set; } = null!;

        /// <summary>
        /// A time string setting a cluster-wide default timeout for all search requests
        /// </summary>
        [Output("searchDefaultSearchTimeout")]
        public Output<string?> SearchDefaultSearchTimeout { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterSettings resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterSettings(string name, ClusterSettingsArgs? args = null, CustomResourceOptions? options = null)
            : base("opensearch:index/clusterSettings:ClusterSettings", name, args ?? new ClusterSettingsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterSettings(string name, Input<string> id, ClusterSettingsState? state = null, CustomResourceOptions? options = null)
            : base("opensearch:index/clusterSettings:ClusterSettings", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/piclemx/pulumi-opensearch",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ClusterSettings resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterSettings Get(string name, Input<string> id, ClusterSettingsState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterSettings(name, id, state, options);
        }
    }

    public sealed class ClusterSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to automatically create an index if it doesn’t already exist and apply any configured index template
        /// </summary>
        [Input("actionAutoCreateIndex")]
        public Input<string>? ActionAutoCreateIndex { get; set; }

        /// <summary>
        /// When set to true, you must specify the index name to delete an index and it is not possible to delete all indices with _all or use wildcards
        /// </summary>
        [Input("actionDestructiveRequiresName")]
        public Input<bool>? ActionDestructiveRequiresName { get; set; }

        /// <summary>
        /// Make the whole cluster read only and metadata is not allowed to be modified
        /// </summary>
        [Input("clusterBlocksReadOnly")]
        public Input<bool>? ClusterBlocksReadOnly { get; set; }

        /// <summary>
        /// Make the whole cluster read only, but allows to delete indices to free up resources
        /// </summary>
        [Input("clusterBlocksReadOnlyAllowDelete")]
        public Input<bool>? ClusterBlocksReadOnlyAllowDelete { get; set; }

        /// <summary>
        /// If false, you cannot close open indices
        /// </summary>
        [Input("clusterIndicesCloseEnable")]
        public Input<bool>? ClusterIndicesCloseEnable { get; set; }

        /// <summary>
        /// A time string controlling how often OpenSearch should check on disk usage for each node in the cluster
        /// </summary>
        [Input("clusterInfoUpdateInterval")]
        public Input<string>? ClusterInfoUpdateInterval { get; set; }

        /// <summary>
        /// The total number of primary and replica shards for the cluster, this number is multiplied by the number of non-frozen data nodes; shards for closed indices do not count toward this limit
        /// </summary>
        [Input("clusterMaxShardsPerNode")]
        public Input<int>? ClusterMaxShardsPerNode { get; set; }

        /// <summary>
        /// The total number of primary and replica frozen shards, for the cluster; Ssards for closed indices do not count toward this limit, a cluster with no frozen data nodes is unlimited.
        /// </summary>
        [Input("clusterMaxShardsPerNodeFrozen")]
        public Input<int>? ClusterMaxShardsPerNodeFrozen { get; set; }

        /// <summary>
        /// Specifies which operations are rejected when there is no active master in a cluster (all, write)
        /// </summary>
        [Input("clusterNoMasterBlock")]
        public Input<string>? ClusterNoMasterBlock { get; set; }

        /// <summary>
        /// Whether allocation for persistent tasks is active (all, none)
        /// </summary>
        [Input("clusterPersistentTasksAllocationEnable")]
        public Input<string>? ClusterPersistentTasksAllocationEnable { get; set; }

        /// <summary>
        /// A time string controling how often assignment checks are performed to react to whether persistent tasks can be assigned to nodes
        /// </summary>
        [Input("clusterPersistentTasksAllocationRecheckInterval")]
        public Input<string>? ClusterPersistentTasksAllocationRecheckInterval { get; set; }

        /// <summary>
        /// Specify when shard rebalancing is allowed (always, indices*primaries*active, indices*all*active)
        /// </summary>
        [Input("clusterRoutingAllocationAllowRebalance")]
        public Input<string>? ClusterRoutingAllocationAllowRebalance { get; set; }

        /// <summary>
        /// Use custom node attributes to take hardware configuration into account when allocating shards
        /// </summary>
        [Input("clusterRoutingAllocationAwarenessAttributes")]
        public Input<string>? ClusterRoutingAllocationAwarenessAttributes { get; set; }

        /// <summary>
        /// Weight factor for the number of shards per index allocated on a node, increasing this raises the tendency to equalize the number of shards per index across all nodes
        /// </summary>
        [Input("clusterRoutingAllocationBalanceIndex")]
        public Input<double>? ClusterRoutingAllocationBalanceIndex { get; set; }

        /// <summary>
        /// Weight factor for the total number of shards allocated on a node, increasing this raises the tendency to equalize the number of shards across all nodes
        /// </summary>
        [Input("clusterRoutingAllocationBalanceShard")]
        public Input<double>? ClusterRoutingAllocationBalanceShard { get; set; }

        /// <summary>
        /// Minimal optimization value of operations that should be performed, raising this will cause the cluster to be less aggressive about optimizing the shard balance
        /// </summary>
        [Input("clusterRoutingAllocationBalanceThreshold")]
        public Input<double>? ClusterRoutingAllocationBalanceThreshold { get; set; }

        /// <summary>
        /// How many concurrent shard rebalances are allowed cluster wide
        /// </summary>
        [Input("clusterRoutingAllocationClusterConcurrentRebalance")]
        public Input<int>? ClusterRoutingAllocationClusterConcurrentRebalance { get; set; }

        /// <summary>
        /// Whether the allocator will take into account shards that are currently being relocated to the target node when computing a node’s disk usage
        /// </summary>
        [Input("clusterRoutingAllocationDiskIncludeRelocations")]
        public Input<bool>? ClusterRoutingAllocationDiskIncludeRelocations { get; set; }

        /// <summary>
        /// Whether the disk allocation decider is active
        /// </summary>
        [Input("clusterRoutingAllocationDiskThresholdEnabled")]
        public Input<bool>? ClusterRoutingAllocationDiskThresholdEnabled { get; set; }

        /// <summary>
        /// Allocator will attempt to relocate shards away from a node whose disk usage is above this percentage disk used
        /// </summary>
        [Input("clusterRoutingAllocationDiskWatermarkHigh")]
        public Input<string>? ClusterRoutingAllocationDiskWatermarkHigh { get; set; }

        /// <summary>
        /// Allocator will not allocate shards to nodes that have more than this percentage disk used
        /// </summary>
        [Input("clusterRoutingAllocationDiskWatermarkLow")]
        public Input<string>? ClusterRoutingAllocationDiskWatermarkLow { get; set; }

        /// <summary>
        /// Enable or disable allocation for specific kinds of shards (all, primaries, new_primaries, none)
        /// </summary>
        [Input("clusterRoutingAllocationEnable")]
        public Input<string>? ClusterRoutingAllocationEnable { get; set; }

        /// <summary>
        /// How many incoming recoveries where the target shard (likely the replica unless a shard is relocating) are allocated on the node
        /// </summary>
        [Input("clusterRoutingAllocationNodeConcurrentIncomingRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeConcurrentIncomingRecoveries { get; set; }

        /// <summary>
        /// How many outgoing recoveries where the source shard (likely the primary unless a shard is relocating) are allocated on the node
        /// </summary>
        [Input("clusterRoutingAllocationNodeConcurrentOutgoingRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeConcurrentOutgoingRecoveries { get; set; }

        /// <summary>
        /// A shortcut to set both incoming and outgoing recoveries
        /// </summary>
        [Input("clusterRoutingAllocationNodeConcurrentRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeConcurrentRecoveries { get; set; }

        /// <summary>
        /// Set a (usually) higher rate for primary recovery on node restart (usually from disk, so fast)
        /// </summary>
        [Input("clusterRoutingAllocationNodeInitialPrimariesRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeInitialPrimariesRecoveries { get; set; }

        /// <summary>
        /// Perform a check to prevent allocation of multiple instances of the same shard on a single host, if multiple nodes are started on the host
        /// </summary>
        [Input("clusterRoutingAllocationSameShardHost")]
        public Input<bool>? ClusterRoutingAllocationSameShardHost { get; set; }

        /// <summary>
        /// Maximum number of primary and replica shards allocated to each node
        /// </summary>
        [Input("clusterRoutingAllocationTotalShardsPerNode")]
        public Input<int>? ClusterRoutingAllocationTotalShardsPerNode { get; set; }

        /// <summary>
        /// Allow rebalancing for specific kinds of shards (all, primaries, replicas, none)
        /// </summary>
        [Input("clusterRoutingRebalanceEnable")]
        public Input<string>? ClusterRoutingRebalanceEnable { get; set; }

        /// <summary>
        /// The percentage of memory above which if loading a field into the field data cache would cause the cache to exceed this limit, an error is returned
        /// </summary>
        [Input("indicesBreakerFielddataLimit")]
        public Input<string>? IndicesBreakerFielddataLimit { get; set; }

        /// <summary>
        /// A constant that all field data estimations are multiplied by
        /// </summary>
        [Input("indicesBreakerFielddataOverhead")]
        public Input<double>? IndicesBreakerFielddataOverhead { get; set; }

        /// <summary>
        /// The percentabge of memory above which per-request data structures (e.g. calculating aggregations) are prevented from exceeding
        /// </summary>
        [Input("indicesBreakerRequestLimit")]
        public Input<string>? IndicesBreakerRequestLimit { get; set; }

        /// <summary>
        /// A constant that all request estimations are multiplied by
        /// </summary>
        [Input("indicesBreakerRequestOverhead")]
        public Input<double>? IndicesBreakerRequestOverhead { get; set; }

        /// <summary>
        /// The percentage of total amount of memory that can be used across all breakers
        /// </summary>
        [Input("indicesBreakerTotalLimit")]
        public Input<string>? IndicesBreakerTotalLimit { get; set; }

        /// <summary>
        /// Maximum total inbound and outbound recovery traffic for each node, in mb
        /// </summary>
        [Input("indicesRecoveryMaxBytesPerSec")]
        public Input<string>? IndicesRecoveryMaxBytesPerSec { get; set; }

        /// <summary>
        /// The percentage limit of memory usage on a node of all currently active incoming requests on transport or HTTP level
        /// </summary>
        [Input("networkBreakerInflightRequestsLimit")]
        public Input<string>? NetworkBreakerInflightRequestsLimit { get; set; }

        /// <summary>
        /// A constant that all in flight requests estimations are multiplied by
        /// </summary>
        [Input("networkBreakerInflightRequestsOverhead")]
        public Input<double>? NetworkBreakerInflightRequestsOverhead { get; set; }

        /// <summary>
        /// Limit for the number of unique dynamic scripts within a certain interval that are allowed to be compiled, expressed as compilations divided by a time string
        /// </summary>
        [Input("scriptMaxCompilationsRate")]
        public Input<string>? ScriptMaxCompilationsRate { get; set; }

        /// <summary>
        /// A time string setting a cluster-wide default timeout for all search requests
        /// </summary>
        [Input("searchDefaultSearchTimeout")]
        public Input<string>? SearchDefaultSearchTimeout { get; set; }

        public ClusterSettingsArgs()
        {
        }
        public static new ClusterSettingsArgs Empty => new ClusterSettingsArgs();
    }

    public sealed class ClusterSettingsState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to automatically create an index if it doesn’t already exist and apply any configured index template
        /// </summary>
        [Input("actionAutoCreateIndex")]
        public Input<string>? ActionAutoCreateIndex { get; set; }

        /// <summary>
        /// When set to true, you must specify the index name to delete an index and it is not possible to delete all indices with _all or use wildcards
        /// </summary>
        [Input("actionDestructiveRequiresName")]
        public Input<bool>? ActionDestructiveRequiresName { get; set; }

        /// <summary>
        /// Make the whole cluster read only and metadata is not allowed to be modified
        /// </summary>
        [Input("clusterBlocksReadOnly")]
        public Input<bool>? ClusterBlocksReadOnly { get; set; }

        /// <summary>
        /// Make the whole cluster read only, but allows to delete indices to free up resources
        /// </summary>
        [Input("clusterBlocksReadOnlyAllowDelete")]
        public Input<bool>? ClusterBlocksReadOnlyAllowDelete { get; set; }

        /// <summary>
        /// If false, you cannot close open indices
        /// </summary>
        [Input("clusterIndicesCloseEnable")]
        public Input<bool>? ClusterIndicesCloseEnable { get; set; }

        /// <summary>
        /// A time string controlling how often OpenSearch should check on disk usage for each node in the cluster
        /// </summary>
        [Input("clusterInfoUpdateInterval")]
        public Input<string>? ClusterInfoUpdateInterval { get; set; }

        /// <summary>
        /// The total number of primary and replica shards for the cluster, this number is multiplied by the number of non-frozen data nodes; shards for closed indices do not count toward this limit
        /// </summary>
        [Input("clusterMaxShardsPerNode")]
        public Input<int>? ClusterMaxShardsPerNode { get; set; }

        /// <summary>
        /// The total number of primary and replica frozen shards, for the cluster; Ssards for closed indices do not count toward this limit, a cluster with no frozen data nodes is unlimited.
        /// </summary>
        [Input("clusterMaxShardsPerNodeFrozen")]
        public Input<int>? ClusterMaxShardsPerNodeFrozen { get; set; }

        /// <summary>
        /// Specifies which operations are rejected when there is no active master in a cluster (all, write)
        /// </summary>
        [Input("clusterNoMasterBlock")]
        public Input<string>? ClusterNoMasterBlock { get; set; }

        /// <summary>
        /// Whether allocation for persistent tasks is active (all, none)
        /// </summary>
        [Input("clusterPersistentTasksAllocationEnable")]
        public Input<string>? ClusterPersistentTasksAllocationEnable { get; set; }

        /// <summary>
        /// A time string controling how often assignment checks are performed to react to whether persistent tasks can be assigned to nodes
        /// </summary>
        [Input("clusterPersistentTasksAllocationRecheckInterval")]
        public Input<string>? ClusterPersistentTasksAllocationRecheckInterval { get; set; }

        /// <summary>
        /// Specify when shard rebalancing is allowed (always, indices*primaries*active, indices*all*active)
        /// </summary>
        [Input("clusterRoutingAllocationAllowRebalance")]
        public Input<string>? ClusterRoutingAllocationAllowRebalance { get; set; }

        /// <summary>
        /// Use custom node attributes to take hardware configuration into account when allocating shards
        /// </summary>
        [Input("clusterRoutingAllocationAwarenessAttributes")]
        public Input<string>? ClusterRoutingAllocationAwarenessAttributes { get; set; }

        /// <summary>
        /// Weight factor for the number of shards per index allocated on a node, increasing this raises the tendency to equalize the number of shards per index across all nodes
        /// </summary>
        [Input("clusterRoutingAllocationBalanceIndex")]
        public Input<double>? ClusterRoutingAllocationBalanceIndex { get; set; }

        /// <summary>
        /// Weight factor for the total number of shards allocated on a node, increasing this raises the tendency to equalize the number of shards across all nodes
        /// </summary>
        [Input("clusterRoutingAllocationBalanceShard")]
        public Input<double>? ClusterRoutingAllocationBalanceShard { get; set; }

        /// <summary>
        /// Minimal optimization value of operations that should be performed, raising this will cause the cluster to be less aggressive about optimizing the shard balance
        /// </summary>
        [Input("clusterRoutingAllocationBalanceThreshold")]
        public Input<double>? ClusterRoutingAllocationBalanceThreshold { get; set; }

        /// <summary>
        /// How many concurrent shard rebalances are allowed cluster wide
        /// </summary>
        [Input("clusterRoutingAllocationClusterConcurrentRebalance")]
        public Input<int>? ClusterRoutingAllocationClusterConcurrentRebalance { get; set; }

        /// <summary>
        /// Whether the allocator will take into account shards that are currently being relocated to the target node when computing a node’s disk usage
        /// </summary>
        [Input("clusterRoutingAllocationDiskIncludeRelocations")]
        public Input<bool>? ClusterRoutingAllocationDiskIncludeRelocations { get; set; }

        /// <summary>
        /// Whether the disk allocation decider is active
        /// </summary>
        [Input("clusterRoutingAllocationDiskThresholdEnabled")]
        public Input<bool>? ClusterRoutingAllocationDiskThresholdEnabled { get; set; }

        /// <summary>
        /// Allocator will attempt to relocate shards away from a node whose disk usage is above this percentage disk used
        /// </summary>
        [Input("clusterRoutingAllocationDiskWatermarkHigh")]
        public Input<string>? ClusterRoutingAllocationDiskWatermarkHigh { get; set; }

        /// <summary>
        /// Allocator will not allocate shards to nodes that have more than this percentage disk used
        /// </summary>
        [Input("clusterRoutingAllocationDiskWatermarkLow")]
        public Input<string>? ClusterRoutingAllocationDiskWatermarkLow { get; set; }

        /// <summary>
        /// Enable or disable allocation for specific kinds of shards (all, primaries, new_primaries, none)
        /// </summary>
        [Input("clusterRoutingAllocationEnable")]
        public Input<string>? ClusterRoutingAllocationEnable { get; set; }

        /// <summary>
        /// How many incoming recoveries where the target shard (likely the replica unless a shard is relocating) are allocated on the node
        /// </summary>
        [Input("clusterRoutingAllocationNodeConcurrentIncomingRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeConcurrentIncomingRecoveries { get; set; }

        /// <summary>
        /// How many outgoing recoveries where the source shard (likely the primary unless a shard is relocating) are allocated on the node
        /// </summary>
        [Input("clusterRoutingAllocationNodeConcurrentOutgoingRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeConcurrentOutgoingRecoveries { get; set; }

        /// <summary>
        /// A shortcut to set both incoming and outgoing recoveries
        /// </summary>
        [Input("clusterRoutingAllocationNodeConcurrentRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeConcurrentRecoveries { get; set; }

        /// <summary>
        /// Set a (usually) higher rate for primary recovery on node restart (usually from disk, so fast)
        /// </summary>
        [Input("clusterRoutingAllocationNodeInitialPrimariesRecoveries")]
        public Input<int>? ClusterRoutingAllocationNodeInitialPrimariesRecoveries { get; set; }

        /// <summary>
        /// Perform a check to prevent allocation of multiple instances of the same shard on a single host, if multiple nodes are started on the host
        /// </summary>
        [Input("clusterRoutingAllocationSameShardHost")]
        public Input<bool>? ClusterRoutingAllocationSameShardHost { get; set; }

        /// <summary>
        /// Maximum number of primary and replica shards allocated to each node
        /// </summary>
        [Input("clusterRoutingAllocationTotalShardsPerNode")]
        public Input<int>? ClusterRoutingAllocationTotalShardsPerNode { get; set; }

        /// <summary>
        /// Allow rebalancing for specific kinds of shards (all, primaries, replicas, none)
        /// </summary>
        [Input("clusterRoutingRebalanceEnable")]
        public Input<string>? ClusterRoutingRebalanceEnable { get; set; }

        /// <summary>
        /// The percentage of memory above which if loading a field into the field data cache would cause the cache to exceed this limit, an error is returned
        /// </summary>
        [Input("indicesBreakerFielddataLimit")]
        public Input<string>? IndicesBreakerFielddataLimit { get; set; }

        /// <summary>
        /// A constant that all field data estimations are multiplied by
        /// </summary>
        [Input("indicesBreakerFielddataOverhead")]
        public Input<double>? IndicesBreakerFielddataOverhead { get; set; }

        /// <summary>
        /// The percentabge of memory above which per-request data structures (e.g. calculating aggregations) are prevented from exceeding
        /// </summary>
        [Input("indicesBreakerRequestLimit")]
        public Input<string>? IndicesBreakerRequestLimit { get; set; }

        /// <summary>
        /// A constant that all request estimations are multiplied by
        /// </summary>
        [Input("indicesBreakerRequestOverhead")]
        public Input<double>? IndicesBreakerRequestOverhead { get; set; }

        /// <summary>
        /// The percentage of total amount of memory that can be used across all breakers
        /// </summary>
        [Input("indicesBreakerTotalLimit")]
        public Input<string>? IndicesBreakerTotalLimit { get; set; }

        /// <summary>
        /// Maximum total inbound and outbound recovery traffic for each node, in mb
        /// </summary>
        [Input("indicesRecoveryMaxBytesPerSec")]
        public Input<string>? IndicesRecoveryMaxBytesPerSec { get; set; }

        /// <summary>
        /// The percentage limit of memory usage on a node of all currently active incoming requests on transport or HTTP level
        /// </summary>
        [Input("networkBreakerInflightRequestsLimit")]
        public Input<string>? NetworkBreakerInflightRequestsLimit { get; set; }

        /// <summary>
        /// A constant that all in flight requests estimations are multiplied by
        /// </summary>
        [Input("networkBreakerInflightRequestsOverhead")]
        public Input<double>? NetworkBreakerInflightRequestsOverhead { get; set; }

        /// <summary>
        /// Limit for the number of unique dynamic scripts within a certain interval that are allowed to be compiled, expressed as compilations divided by a time string
        /// </summary>
        [Input("scriptMaxCompilationsRate")]
        public Input<string>? ScriptMaxCompilationsRate { get; set; }

        /// <summary>
        /// A time string setting a cluster-wide default timeout for all search requests
        /// </summary>
        [Input("searchDefaultSearchTimeout")]
        public Input<string>? SearchDefaultSearchTimeout { get; set; }

        public ClusterSettingsState()
        {
        }
        public static new ClusterSettingsState Empty => new ClusterSettingsState();
    }
}