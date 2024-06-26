// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides an OpenSearch dashboard tenant resource. Please refer to the OpenSearch documentation for details.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * // Create a tenant
 * const test = new opensearch.DashboardTenant("test", {
 *     description: "test tenant",
 *     tenantName: "test",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import opensearch:index/dashboardTenant:DashboardTenant writer test
 * ```
 */
export class DashboardTenant extends pulumi.CustomResource {
    /**
     * Get an existing DashboardTenant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DashboardTenantState, opts?: pulumi.CustomResourceOptions): DashboardTenant {
        return new DashboardTenant(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/dashboardTenant:DashboardTenant';

    /**
     * Returns true if the given object is an instance of DashboardTenant.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DashboardTenant {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DashboardTenant.__pulumiType;
    }

    /**
     * Description of the tenant.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly index!: pulumi.Output<string>;
    /**
     * The name of the tenant.
     */
    public readonly tenantName!: pulumi.Output<string>;

    /**
     * Create a DashboardTenant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DashboardTenantArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DashboardTenantArgs | DashboardTenantState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DashboardTenantState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["index"] = state ? state.index : undefined;
            resourceInputs["tenantName"] = state ? state.tenantName : undefined;
        } else {
            const args = argsOrState as DashboardTenantArgs | undefined;
            if ((!args || args.tenantName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tenantName'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["tenantName"] = args ? args.tenantName : undefined;
            resourceInputs["index"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DashboardTenant.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DashboardTenant resources.
 */
export interface DashboardTenantState {
    /**
     * Description of the tenant.
     */
    description?: pulumi.Input<string>;
    index?: pulumi.Input<string>;
    /**
     * The name of the tenant.
     */
    tenantName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DashboardTenant resource.
 */
export interface DashboardTenantArgs {
    /**
     * Description of the tenant.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the tenant.
     */
    tenantName: pulumi.Input<string>;
}
