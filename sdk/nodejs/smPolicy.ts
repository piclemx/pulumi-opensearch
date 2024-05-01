// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides an OpenSearch Snapshot Management (SM) policy. Please refer to the OpenSearch SM documentation for details.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * // Create a snapshot repository. Make sure you also have created the bucket (eg. 
 * // via `terraform-aws-modules/s3-bucket/aws`) and matching IAM role.
 * const repo = new opensearch.SnapshotRepository("repo", {
 *     type: "s3",
 *     settings: {
 *         bucket: module.s3_snapshot.s3_bucket_id,
 *         region: module.s3_snapshot.s3_bucket_region,
 *         role_arn: aws_iam_role.snapshot_create.arn,
 *         server_side_encryption: true,
 *     },
 * });
 * // Create the SM policy
 * const snapshotToS3 = new opensearch.SmPolicy("snapshotToS3", {
 *     policyName: "snapshot_to_s3",
 *     body: repo.name.apply(name => JSON.stringify({
 *         enabled: true,
 *         description: "My snapshot policy",
 *         creation: {
 *             schedule: {
 *                 cron: {
 *                     expression: "0 0 * * *",
 *                     timezone: "UTC",
 *                 },
 *             },
 *             time_limit: "1h",
 *         },
 *         deletion: {
 *             schedule: {
 *                 cron: {
 *                     expression: "0 0 * * *",
 *                     timezone: "UTC",
 *                 },
 *             },
 *             condition: {
 *                 max_age: "14d",
 *                 max_count: 400,
 *                 min_count: 1,
 *             },
 *             time_limit: "1h",
 *         },
 *         snapshot_config: {
 *             timezone: "UTC",
 *             indices: "*",
 *             repository: name,
 *         },
 *     })),
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import opensearch:index/smPolicy:SmPolicy cleanup snapshot_to_s3
 * ```
 */
export class SmPolicy extends pulumi.CustomResource {
    /**
     * Get an existing SmPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SmPolicyState, opts?: pulumi.CustomResourceOptions): SmPolicy {
        return new SmPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/smPolicy:SmPolicy';

    /**
     * Returns true if the given object is an instance of SmPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SmPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SmPolicy.__pulumiType;
    }

    /**
     * The policy document.
     */
    public readonly body!: pulumi.Output<string>;
    /**
     * The name of the SM policy.
     */
    public readonly policyName!: pulumi.Output<string>;
    /**
     * The primary term of the SM policy version.
     */
    public readonly primaryTerm!: pulumi.Output<number>;
    /**
     * The sequence number of the SM policy version.
     */
    public readonly seqNo!: pulumi.Output<number>;

    /**
     * Create a SmPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SmPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SmPolicyArgs | SmPolicyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SmPolicyState | undefined;
            resourceInputs["body"] = state ? state.body : undefined;
            resourceInputs["policyName"] = state ? state.policyName : undefined;
            resourceInputs["primaryTerm"] = state ? state.primaryTerm : undefined;
            resourceInputs["seqNo"] = state ? state.seqNo : undefined;
        } else {
            const args = argsOrState as SmPolicyArgs | undefined;
            if ((!args || args.body === undefined) && !opts.urn) {
                throw new Error("Missing required property 'body'");
            }
            if ((!args || args.policyName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyName'");
            }
            resourceInputs["body"] = args ? args.body : undefined;
            resourceInputs["policyName"] = args ? args.policyName : undefined;
            resourceInputs["primaryTerm"] = args ? args.primaryTerm : undefined;
            resourceInputs["seqNo"] = args ? args.seqNo : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SmPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SmPolicy resources.
 */
export interface SmPolicyState {
    /**
     * The policy document.
     */
    body?: pulumi.Input<string>;
    /**
     * The name of the SM policy.
     */
    policyName?: pulumi.Input<string>;
    /**
     * The primary term of the SM policy version.
     */
    primaryTerm?: pulumi.Input<number>;
    /**
     * The sequence number of the SM policy version.
     */
    seqNo?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a SmPolicy resource.
 */
export interface SmPolicyArgs {
    /**
     * The policy document.
     */
    body: pulumi.Input<string>;
    /**
     * The name of the SM policy.
     */
    policyName: pulumi.Input<string>;
    /**
     * The primary term of the SM policy version.
     */
    primaryTerm?: pulumi.Input<number>;
    /**
     * The sequence number of the SM policy version.
     */
    seqNo?: pulumi.Input<number>;
}