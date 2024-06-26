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
    public static class GetHost
    {
        /// <summary>
        /// `opensearch.getHost` can be used to retrieve the host URL for the provider's current cluster.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Opensearch = Pulumi.Opensearch;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = Opensearch.GetHost.Invoke(new()
        ///     {
        ///         Active = true,
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetHostResult> InvokeAsync(GetHostArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetHostResult>("opensearch:index/getHost:getHost", args ?? new GetHostArgs(), options.WithDefaults());

        /// <summary>
        /// `opensearch.getHost` can be used to retrieve the host URL for the provider's current cluster.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Opensearch = Pulumi.Opensearch;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = Opensearch.GetHost.Invoke(new()
        ///     {
        ///         Active = true,
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetHostResult> Invoke(GetHostInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetHostResult>("opensearch:index/getHost:getHost", args ?? new GetHostInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetHostArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// should be set to `true`
        /// </summary>
        [Input("active", required: true)]
        public bool Active { get; set; }

        public GetHostArgs()
        {
        }
        public static new GetHostArgs Empty => new GetHostArgs();
    }

    public sealed class GetHostInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// should be set to `true`
        /// </summary>
        [Input("active", required: true)]
        public Input<bool> Active { get; set; } = null!;

        public GetHostInvokeArgs()
        {
        }
        public static new GetHostInvokeArgs Empty => new GetHostInvokeArgs();
    }


    [OutputType]
    public sealed class GetHostResult
    {
        /// <summary>
        /// should be set to `true`
        /// </summary>
        public readonly bool Active;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// the url of the active cluster
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private GetHostResult(
            bool active,

            string id,

            string url)
        {
            Active = active;
            Id = id;
            Url = url;
        }
    }
}
