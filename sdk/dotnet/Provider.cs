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
    /// The provider type for the opensearch package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [OpensearchResourceType("pulumi:providers:opensearch")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// The access key for use with AWS OpenSearch Service domains
        /// </summary>
        [Output("awsAccessKey")]
        public Output<string?> AwsAccessKey { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        /// </summary>
        [Output("awsAssumeRoleArn")]
        public Output<string?> AwsAssumeRoleArn { get; private set; } = null!;

        /// <summary>
        /// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        /// </summary>
        [Output("awsAssumeRoleExternalId")]
        public Output<string?> AwsAssumeRoleExternalId { get; private set; } = null!;

        /// <summary>
        /// The AWS profile for use with AWS OpenSearch Service domains
        /// </summary>
        [Output("awsProfile")]
        public Output<string?> AwsProfile { get; private set; } = null!;

        /// <summary>
        /// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
        /// OpenSearch endpoint exposed on a custom DNS domain.
        /// </summary>
        [Output("awsRegion")]
        public Output<string?> AwsRegion { get; private set; } = null!;

        /// <summary>
        /// The secret key for use with AWS OpenSearch Service domains
        /// </summary>
        [Output("awsSecretKey")]
        public Output<string?> AwsSecretKey { get; private set; } = null!;

        /// <summary>
        /// AWS service name used in the credential scope of signed requests to OpenSearch.
        /// </summary>
        [Output("awsSignatureService")]
        public Output<string?> AwsSignatureService { get; private set; } = null!;

        /// <summary>
        /// The session token for use with AWS OpenSearch Service domains
        /// </summary>
        [Output("awsToken")]
        public Output<string?> AwsToken { get; private set; } = null!;

        /// <summary>
        /// A Custom CA certificate
        /// </summary>
        [Output("cacertFile")]
        public Output<string?> CacertFile { get; private set; } = null!;

        /// <summary>
        /// A X509 certificate to connect to OpenSearch
        /// </summary>
        [Output("clientCertPath")]
        public Output<string?> ClientCertPath { get; private set; } = null!;

        /// <summary>
        /// A X509 key to connect to OpenSearch
        /// </summary>
        [Output("clientKeyPath")]
        public Output<string?> ClientKeyPath { get; private set; } = null!;

        /// <summary>
        /// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
        /// documentation on connecting to OpenSearch via an SSH tunnel.
        /// </summary>
        [Output("hostOverride")]
        public Output<string?> HostOverride { get; private set; } = null!;

        /// <summary>
        /// OpenSearch Version
        /// </summary>
        [Output("opensearchVersion")]
        public Output<string?> OpensearchVersion { get; private set; } = null!;

        /// <summary>
        /// Password to use to connect to OpenSearch using basic auth
        /// </summary>
        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        /// <summary>
        /// Proxy URL to use for requests to OpenSearch.
        /// </summary>
        [Output("proxy")]
        public Output<string?> Proxy { get; private set; } = null!;

        /// <summary>
        /// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        /// </summary>
        [Output("token")]
        public Output<string?> Token { get; private set; } = null!;

        /// <summary>
        /// The type of token, usually ApiKey or Bearer
        /// </summary>
        [Output("tokenName")]
        public Output<string?> TokenName { get; private set; } = null!;

        /// <summary>
        /// OpenSearch URL
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;

        /// <summary>
        /// Username to use to connect to OpenSearch using basic auth
        /// </summary>
        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, CustomResourceOptions? options = null)
            : base("opensearch", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
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
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access key for use with AWS OpenSearch Service domains
        /// </summary>
        [Input("awsAccessKey")]
        public Input<string>? AwsAccessKey { get; set; }

        /// <summary>
        /// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        /// </summary>
        [Input("awsAssumeRoleArn")]
        public Input<string>? AwsAssumeRoleArn { get; set; }

        /// <summary>
        /// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        /// </summary>
        [Input("awsAssumeRoleExternalId")]
        public Input<string>? AwsAssumeRoleExternalId { get; set; }

        /// <summary>
        /// The AWS profile for use with AWS OpenSearch Service domains
        /// </summary>
        [Input("awsProfile")]
        public Input<string>? AwsProfile { get; set; }

        /// <summary>
        /// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
        /// OpenSearch endpoint exposed on a custom DNS domain.
        /// </summary>
        [Input("awsRegion")]
        public Input<string>? AwsRegion { get; set; }

        /// <summary>
        /// The secret key for use with AWS OpenSearch Service domains
        /// </summary>
        [Input("awsSecretKey")]
        public Input<string>? AwsSecretKey { get; set; }

        /// <summary>
        /// AWS service name used in the credential scope of signed requests to OpenSearch.
        /// </summary>
        [Input("awsSignatureService")]
        public Input<string>? AwsSignatureService { get; set; }

        /// <summary>
        /// The session token for use with AWS OpenSearch Service domains
        /// </summary>
        [Input("awsToken")]
        public Input<string>? AwsToken { get; set; }

        /// <summary>
        /// A Custom CA certificate
        /// </summary>
        [Input("cacertFile")]
        public Input<string>? CacertFile { get; set; }

        /// <summary>
        /// A X509 certificate to connect to OpenSearch
        /// </summary>
        [Input("clientCertPath")]
        public Input<string>? ClientCertPath { get; set; }

        /// <summary>
        /// A X509 key to connect to OpenSearch
        /// </summary>
        [Input("clientKeyPath")]
        public Input<string>? ClientKeyPath { get; set; }

        /// <summary>
        /// Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
        /// cluster.
        /// </summary>
        [Input("healthcheck", json: true)]
        public Input<bool>? Healthcheck { get; set; }

        /// <summary>
        /// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
        /// documentation on connecting to OpenSearch via an SSH tunnel.
        /// </summary>
        [Input("hostOverride")]
        public Input<string>? HostOverride { get; set; }

        /// <summary>
        /// Disable SSL verification of API calls
        /// </summary>
        [Input("insecure", json: true)]
        public Input<bool>? Insecure { get; set; }

        /// <summary>
        /// OpenSearch Version
        /// </summary>
        [Input("opensearchVersion")]
        public Input<string>? OpensearchVersion { get; set; }

        /// <summary>
        /// Password to use to connect to OpenSearch using basic auth
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// Proxy URL to use for requests to OpenSearch.
        /// </summary>
        [Input("proxy")]
        public Input<string>? Proxy { get; set; }

        /// <summary>
        /// Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.&lt;region&gt;.es.amazonaws.com`), or
        /// `aws_region` must be specified explicitly.
        /// </summary>
        [Input("signAwsRequests", json: true)]
        public Input<bool>? SignAwsRequests { get; set; }

        /// <summary>
        /// Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
        /// </summary>
        [Input("sniff", json: true)]
        public Input<bool>? Sniff { get; set; }

        /// <summary>
        /// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        /// <summary>
        /// The type of token, usually ApiKey or Bearer
        /// </summary>
        [Input("tokenName")]
        public Input<string>? TokenName { get; set; }

        /// <summary>
        /// OpenSearch URL
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        /// <summary>
        /// Username to use to connect to OpenSearch using basic auth
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        /// <summary>
        /// Version ping timeout in seconds
        /// </summary>
        [Input("versionPingTimeout", json: true)]
        public Input<int>? VersionPingTimeout { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
