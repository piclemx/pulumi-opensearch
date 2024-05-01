// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * A data stream lets you store append-only time series data across multiple (hidden, auto-generated) indices while giving you a single named resource for requests
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * const fooComposableIndexTemplate = new opensearch.ComposableIndexTemplate("fooComposableIndexTemplate", {body: `{
 *   "index_patterns": ["foo-data-stream*"],
 *   "data_stream": {}
 * }
 * `});
 * const fooDataStream = new opensearch.DataStream("fooDataStream", {}, {
 *     dependsOn: [fooComposableIndexTemplate],
 * });
 * ```
 */
export class DataStream extends pulumi.CustomResource {
    /**
     * Get an existing DataStream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataStreamState, opts?: pulumi.CustomResourceOptions): DataStream {
        return new DataStream(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/dataStream:DataStream';

    /**
     * Returns true if the given object is an instance of DataStream.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataStream {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataStream.__pulumiType;
    }

    /**
     * Name of the data stream to create, must have a matching
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a DataStream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DataStreamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DataStreamArgs | DataStreamState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DataStreamState | undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as DataStreamArgs | undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DataStream.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DataStream resources.
 */
export interface DataStreamState {
    /**
     * Name of the data stream to create, must have a matching
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DataStream resource.
 */
export interface DataStreamArgs {
    /**
     * Name of the data stream to create, must have a matching
     */
    name?: pulumi.Input<string>;
}