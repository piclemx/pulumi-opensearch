// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides an OpenSearch monitor. Please refer to the OpenSearch monitor documentation for details.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * const moviesLastHour = new opensearch.Monitor("moviesLastHour", {body: `{
 *   "name": "test-monitor",
 *   "type": "monitor",
 *   "enabled": true,
 *   "schedule": {
 *     "period": {
 *       "interval": 1,
 *       "unit": "MINUTES"
 *     }
 *   },
 *   "inputs": [{
 *     "search": {
 *       "indices": ["movies"],
 *       "query": {
 *         "size": 0,
 *         "aggregations": {},
 *         "query": {
 *           "bool": {
 *             "adjust_pure_negative":true,
 *             "boost":1,
 *             "filter": [{
 *               "range": {
 *                 "@timestamp": {
 *                   "boost":1,
 *                   "from":"||-1h",
 *                   "to":"",
 *                   "include_lower":true,
 *                   "include_upper":true,
 *                   "format": "epoch_millis"
 *                 }
 *               }
 *             }]
 *           }
 *         }
 *       }
 *     }
 *   }],
 *   "triggers": [
 *     {
 *       "name" : "Errors",
 *       "severity" : "1",
 *       "condition" : {
 *         "script" : {
 *           "source" : "ctx.results[0].hits.total.value > 0",
 *           "lang" : "painless"
 *         }
 *       },
 *       "actions" : [
 *         {
 *           "name" : "Slack",
 *           "destination_id" : "${opensearch_channel_configuration.slack_on_call_channel.id}",
 *           "message_template" : {
 *             "source" : "bogus",
 *             "lang" : "mustache"
 *           },
 *           "throttle_enabled" : false,
 *           "subject_template" : {
 *             "source" : "Production Errors",
 *             "lang" : "mustache"
 *           }
 *         }
 *       ]
 *     }
 *   ]
 * }
 *
 * `});
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import opensearch:index/monitor:Monitor alert lgOZb3UB96pyyRQv0ppQ
 * ```
 */
export class Monitor extends pulumi.CustomResource {
    /**
     * Get an existing Monitor resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MonitorState, opts?: pulumi.CustomResourceOptions): Monitor {
        return new Monitor(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/monitor:Monitor';

    /**
     * Returns true if the given object is an instance of Monitor.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Monitor {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Monitor.__pulumiType;
    }

    /**
     * The monitor document
     */
    public readonly body!: pulumi.Output<string>;

    /**
     * Create a Monitor resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MonitorArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MonitorArgs | MonitorState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MonitorState | undefined;
            resourceInputs["body"] = state ? state.body : undefined;
        } else {
            const args = argsOrState as MonitorArgs | undefined;
            if ((!args || args.body === undefined) && !opts.urn) {
                throw new Error("Missing required property 'body'");
            }
            resourceInputs["body"] = args ? args.body : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Monitor.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Monitor resources.
 */
export interface MonitorState {
    /**
     * The monitor document
     */
    body?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Monitor resource.
 */
export interface MonitorArgs {
    /**
     * The monitor document
     */
    body: pulumi.Input<string>;
}
