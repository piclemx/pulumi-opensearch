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
    /// Provides an OpenSearch anonaly detection. Please refer to the OpenSearch anomaly detection documentation for details.
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
    ///     var foo = new Opensearch.AnomalyDetection("foo", new()
    ///     {
    ///         Body = @"{
    ///   ""name"": ""foo"",
    ///   ""description"": ""Test detector"",
    ///   ""time_field"": ""@timestamp"",
    ///   ""indices"": [
    ///     ""security-auditlog*""
    ///   ],
    ///   ""feature_attributes"": [
    ///     {
    ///       ""feature_name"": ""test"",
    ///       ""feature_enabled"": true,
    ///       ""aggregation_query"": {
    ///         ""test"": {
    ///           ""value_count"": {
    ///             ""field"": ""audit_category.keyword""
    ///           }
    ///         }
    ///       }
    ///     }
    ///   ],
    ///   ""filter_query"": {
    ///     ""bool"": {
    ///       ""filter"": [
    ///         {
    ///           ""range"": {
    ///             ""value"": {
    ///               ""gt"": 1
    ///             }
    ///           }
    ///         }
    ///       ],
    ///       ""adjust_pure_negative"": true,
    ///       ""boost"": 1
    ///     }
    ///   },
    ///   ""detection_interval"": {
    ///     ""period"": {
    ///       ""interval"": 1,
    ///       ""unit"": ""Minutes""
    ///     }
    ///   },
    ///   ""window_delay"": {
    ///     ""period"": {
    ///       ""interval"": 1,
    ///       ""unit"": ""Minutes""
    ///     }
    ///   },
    ///   ""result_index"" : ""opensearch-ad-plugin-result-test""
    /// }
    /// 
    /// ",
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [OpensearchResourceType("opensearch:index/anomalyDetection:AnomalyDetection")]
    public partial class AnomalyDetection : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The anomaly detection document
        /// </summary>
        [Output("body")]
        public Output<string> Body { get; private set; } = null!;


        /// <summary>
        /// Create a AnomalyDetection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AnomalyDetection(string name, AnomalyDetectionArgs args, CustomResourceOptions? options = null)
            : base("opensearch:index/anomalyDetection:AnomalyDetection", name, args ?? new AnomalyDetectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AnomalyDetection(string name, Input<string> id, AnomalyDetectionState? state = null, CustomResourceOptions? options = null)
            : base("opensearch:index/anomalyDetection:AnomalyDetection", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AnomalyDetection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AnomalyDetection Get(string name, Input<string> id, AnomalyDetectionState? state = null, CustomResourceOptions? options = null)
        {
            return new AnomalyDetection(name, id, state, options);
        }
    }

    public sealed class AnomalyDetectionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The anomaly detection document
        /// </summary>
        [Input("body", required: true)]
        public Input<string> Body { get; set; } = null!;

        public AnomalyDetectionArgs()
        {
        }
        public static new AnomalyDetectionArgs Empty => new AnomalyDetectionArgs();
    }

    public sealed class AnomalyDetectionState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The anomaly detection document
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        public AnomalyDetectionState()
        {
        }
        public static new AnomalyDetectionState Empty => new AnomalyDetectionState();
    }
}
