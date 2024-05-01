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
    /// Provides an OpenSearch Index State Management (ISM) policy. Please refer to the OpenSearch ISM documentation for details.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.IO;
    /// using System.Linq;
    /// using Pulumi;
    /// using Opensearch = Piclemx.Opensearch;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Create an ISM policy
    ///     var cleanup = new Opensearch.IsmPolicy("cleanup", new()
    ///     {
    ///         PolicyId = "delete_after_15d",
    ///         Body = File.ReadAllText($"{path.Module}/policies/delete_after_15d.json"),
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import opensearch:index/ismPolicy:IsmPolicy cleanup delete_after_15d
    /// ```
    /// </summary>
    [OpensearchResourceType("opensearch:index/ismPolicy:IsmPolicy")]
    public partial class IsmPolicy : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The policy document.
        /// </summary>
        [Output("body")]
        public Output<string> Body { get; private set; } = null!;

        /// <summary>
        /// The id of the ISM policy.
        /// </summary>
        [Output("policyId")]
        public Output<string> PolicyId { get; private set; } = null!;

        /// <summary>
        /// The primary term of the ISM policy version.
        /// </summary>
        [Output("primaryTerm")]
        public Output<int> PrimaryTerm { get; private set; } = null!;

        /// <summary>
        /// The sequence number of the ISM policy version.
        /// </summary>
        [Output("seqNo")]
        public Output<int> SeqNo { get; private set; } = null!;


        /// <summary>
        /// Create a IsmPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IsmPolicy(string name, IsmPolicyArgs args, CustomResourceOptions? options = null)
            : base("opensearch:index/ismPolicy:IsmPolicy", name, args ?? new IsmPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IsmPolicy(string name, Input<string> id, IsmPolicyState? state = null, CustomResourceOptions? options = null)
            : base("opensearch:index/ismPolicy:IsmPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing IsmPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IsmPolicy Get(string name, Input<string> id, IsmPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new IsmPolicy(name, id, state, options);
        }
    }

    public sealed class IsmPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The policy document.
        /// </summary>
        [Input("body", required: true)]
        public Input<string> Body { get; set; } = null!;

        /// <summary>
        /// The id of the ISM policy.
        /// </summary>
        [Input("policyId", required: true)]
        public Input<string> PolicyId { get; set; } = null!;

        /// <summary>
        /// The primary term of the ISM policy version.
        /// </summary>
        [Input("primaryTerm")]
        public Input<int>? PrimaryTerm { get; set; }

        /// <summary>
        /// The sequence number of the ISM policy version.
        /// </summary>
        [Input("seqNo")]
        public Input<int>? SeqNo { get; set; }

        public IsmPolicyArgs()
        {
        }
        public static new IsmPolicyArgs Empty => new IsmPolicyArgs();
    }

    public sealed class IsmPolicyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The policy document.
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        /// <summary>
        /// The id of the ISM policy.
        /// </summary>
        [Input("policyId")]
        public Input<string>? PolicyId { get; set; }

        /// <summary>
        /// The primary term of the ISM policy version.
        /// </summary>
        [Input("primaryTerm")]
        public Input<int>? PrimaryTerm { get; set; }

        /// <summary>
        /// The sequence number of the ISM policy version.
        /// </summary>
        [Input("seqNo")]
        public Input<int>? SeqNo { get; set; }

        public IsmPolicyState()
        {
        }
        public static new IsmPolicyState Empty => new IsmPolicyState();
    }
}
