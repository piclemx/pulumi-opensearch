// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides an OpenSearch anonaly detection. Please refer to the OpenSearch anomaly detection documentation for details.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * const foo = new opensearch.AnomalyDetection("foo", {body: `{
 *   "name": "foo",
 *   "description": "Test detector",
 *   "time_field": "@timestamp",
 *   "indices": [
 *     "security-auditlog*"
 *   ],
 *   "feature_attributes": [
 *     {
 *       "feature_name": "test",
 *       "feature_enabled": true,
 *       "aggregation_query": {
 *         "test": {
 *           "value_count": {
 *             "field": "audit_category.keyword"
 *           }
 *         }
 *       }
 *     }
 *   ],
 *   "filter_query": {
 *     "bool": {
 *       "filter": [
 *         {
 *           "range": {
 *             "value": {
 *               "gt": 1
 *             }
 *           }
 *         }
 *       ],
 *       "adjust_pure_negative": true,
 *       "boost": 1
 *     }
 *   },
 *   "detection_interval": {
 *     "period": {
 *       "interval": 1,
 *       "unit": "Minutes"
 *     }
 *   },
 *   "window_delay": {
 *     "period": {
 *       "interval": 1,
 *       "unit": "Minutes"
 *     }
 *   },
 *   "result_index" : "opensearch-ad-plugin-result-test"
 * }
 *
 * `});
 * ```
 */
export class AnomalyDetection extends pulumi.CustomResource {
    /**
     * Get an existing AnomalyDetection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AnomalyDetectionState, opts?: pulumi.CustomResourceOptions): AnomalyDetection {
        return new AnomalyDetection(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/anomalyDetection:AnomalyDetection';

    /**
     * Returns true if the given object is an instance of AnomalyDetection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AnomalyDetection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AnomalyDetection.__pulumiType;
    }

    /**
     * The anomaly detection document
     */
    public readonly body!: pulumi.Output<string>;

    /**
     * Create a AnomalyDetection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AnomalyDetectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AnomalyDetectionArgs | AnomalyDetectionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AnomalyDetectionState | undefined;
            resourceInputs["body"] = state ? state.body : undefined;
        } else {
            const args = argsOrState as AnomalyDetectionArgs | undefined;
            if ((!args || args.body === undefined) && !opts.urn) {
                throw new Error("Missing required property 'body'");
            }
            resourceInputs["body"] = args ? args.body : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AnomalyDetection.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AnomalyDetection resources.
 */
export interface AnomalyDetectionState {
    /**
     * The anomaly detection document
     */
    body?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AnomalyDetection resource.
 */
export interface AnomalyDetectionArgs {
    /**
     * The anomaly detection document
     */
    body: pulumi.Input<string>;
}
