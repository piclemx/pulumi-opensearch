// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Component templates are building blocks for constructing index templates that specify index mappings, settings, and aliases. You cannot directly apply a component template to a data stream or index. To be applied, a component template must be included in an index template’s `composedOf` list.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as opensearch from "@piclemx/pulumi-opensearch";
 *
 * const test = new opensearch.ComponentTemplate("test", {body: `{
 *   "template": {
 *     "settings": {
 *       "index": {
 *         "number_of_shards": "1"
 *       }
 *     },
 *     "mappings": {
 *       "properties": {
 *         "host_name": {
 *           "type": "keyword"
 *         },
 *         "created_at": {
 *           "type": "date",
 *           "format": "EEE MMM dd HH:mm:ss Z yyyy"
 *         }
 *       }
 *     },
 *     "aliases": {
 *       "mydata": { }
 *     }
 *   }
 * }
 *
 * `});
 * ```
 *
 * ## Import
 *
 * Import by name
 *
 * ```sh
 *  $ pulumi import opensearch:index/componentTemplate:ComponentTemplate test terraform-test
 * ```
 */
export class ComponentTemplate extends pulumi.CustomResource {
    /**
     * Get an existing ComponentTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComponentTemplateState, opts?: pulumi.CustomResourceOptions): ComponentTemplate {
        return new ComponentTemplate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'opensearch:index/componentTemplate:ComponentTemplate';

    /**
     * Returns true if the given object is an instance of ComponentTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ComponentTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ComponentTemplate.__pulumiType;
    }

    /**
     * The JSON body of the template.
     */
    public readonly body!: pulumi.Output<string>;
    /**
     * Name of the component template to create.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a ComponentTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ComponentTemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ComponentTemplateArgs | ComponentTemplateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ComponentTemplateState | undefined;
            resourceInputs["body"] = state ? state.body : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as ComponentTemplateArgs | undefined;
            if ((!args || args.body === undefined) && !opts.urn) {
                throw new Error("Missing required property 'body'");
            }
            resourceInputs["body"] = args ? args.body : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ComponentTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ComponentTemplate resources.
 */
export interface ComponentTemplateState {
    /**
     * The JSON body of the template.
     */
    body?: pulumi.Input<string>;
    /**
     * Name of the component template to create.
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ComponentTemplate resource.
 */
export interface ComponentTemplateArgs {
    /**
     * The JSON body of the template.
     */
    body: pulumi.Input<string>;
    /**
     * Name of the component template to create.
     */
    name?: pulumi.Input<string>;
}