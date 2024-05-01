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
    /// Provides an OpenSearch script resource.
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
    ///     // Create a script
    ///     var testScript = new Opensearch.Script("testScript", new()
    ///     {
    ///         Lang = "painless",
    ///         ScriptId = "my_script",
    ///         Source = "Math.log(_score * 2) + params.my_modifier",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import opensearch:index/script:Script test_script my_script
    /// ```
    /// </summary>
    [OpensearchResourceType("opensearch:index/script:Script")]
    public partial class Script : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies the language the script is written in. Defaults to painless.
        /// </summary>
        [Output("lang")]
        public Output<string?> Lang { get; private set; } = null!;

        /// <summary>
        /// Identifier for the stored script. Must be unique within the cluster.
        /// </summary>
        [Output("scriptId")]
        public Output<string> ScriptId { get; private set; } = null!;

        /// <summary>
        /// The source of the stored script
        /// </summary>
        [Output("source")]
        public Output<string> Source { get; private set; } = null!;


        /// <summary>
        /// Create a Script resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Script(string name, ScriptArgs args, CustomResourceOptions? options = null)
            : base("opensearch:index/script:Script", name, args ?? new ScriptArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Script(string name, Input<string> id, ScriptState? state = null, CustomResourceOptions? options = null)
            : base("opensearch:index/script:Script", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Script resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Script Get(string name, Input<string> id, ScriptState? state = null, CustomResourceOptions? options = null)
        {
            return new Script(name, id, state, options);
        }
    }

    public sealed class ScriptArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the language the script is written in. Defaults to painless.
        /// </summary>
        [Input("lang")]
        public Input<string>? Lang { get; set; }

        /// <summary>
        /// Identifier for the stored script. Must be unique within the cluster.
        /// </summary>
        [Input("scriptId", required: true)]
        public Input<string> ScriptId { get; set; } = null!;

        /// <summary>
        /// The source of the stored script
        /// </summary>
        [Input("source", required: true)]
        public Input<string> Source { get; set; } = null!;

        public ScriptArgs()
        {
        }
        public static new ScriptArgs Empty => new ScriptArgs();
    }

    public sealed class ScriptState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the language the script is written in. Defaults to painless.
        /// </summary>
        [Input("lang")]
        public Input<string>? Lang { get; set; }

        /// <summary>
        /// Identifier for the stored script. Must be unique within the cluster.
        /// </summary>
        [Input("scriptId")]
        public Input<string>? ScriptId { get; set; }

        /// <summary>
        /// The source of the stored script
        /// </summary>
        [Input("source")]
        public Input<string>? Source { get; set; }

        public ScriptState()
        {
        }
        public static new ScriptState Empty => new ScriptState();
    }
}
