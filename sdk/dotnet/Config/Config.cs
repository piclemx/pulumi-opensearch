// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Piclemx.Opensearch
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("opensearch");

        private static readonly __Value<string?> _awsAccessKey = new __Value<string?>(() => __config.Get("awsAccessKey"));
        /// <summary>
        /// The access key for use with AWS OpenSearch Service domains
        /// </summary>
        public static string? AwsAccessKey
        {
            get => _awsAccessKey.Get();
            set => _awsAccessKey.Set(value);
        }

        private static readonly __Value<string?> _awsAssumeRoleArn = new __Value<string?>(() => __config.Get("awsAssumeRoleArn"));
        /// <summary>
        /// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        /// </summary>
        public static string? AwsAssumeRoleArn
        {
            get => _awsAssumeRoleArn.Get();
            set => _awsAssumeRoleArn.Set(value);
        }

        private static readonly __Value<string?> _awsAssumeRoleExternalId = new __Value<string?>(() => __config.Get("awsAssumeRoleExternalId"));
        /// <summary>
        /// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        /// </summary>
        public static string? AwsAssumeRoleExternalId
        {
            get => _awsAssumeRoleExternalId.Get();
            set => _awsAssumeRoleExternalId.Set(value);
        }

        private static readonly __Value<string?> _awsProfile = new __Value<string?>(() => __config.Get("awsProfile"));
        /// <summary>
        /// The AWS profile for use with AWS OpenSearch Service domains
        /// </summary>
        public static string? AwsProfile
        {
            get => _awsProfile.Get();
            set => _awsProfile.Set(value);
        }

        private static readonly __Value<string?> _awsRegion = new __Value<string?>(() => __config.Get("awsRegion"));
        /// <summary>
        /// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
        /// OpenSearch endpoint exposed on a custom DNS domain.
        /// </summary>
        public static string? AwsRegion
        {
            get => _awsRegion.Get();
            set => _awsRegion.Set(value);
        }

        private static readonly __Value<string?> _awsSecretKey = new __Value<string?>(() => __config.Get("awsSecretKey"));
        /// <summary>
        /// The secret key for use with AWS OpenSearch Service domains
        /// </summary>
        public static string? AwsSecretKey
        {
            get => _awsSecretKey.Get();
            set => _awsSecretKey.Set(value);
        }

        private static readonly __Value<string?> _awsSignatureService = new __Value<string?>(() => __config.Get("awsSignatureService"));
        /// <summary>
        /// AWS service name used in the credential scope of signed requests to OpenSearch.
        /// </summary>
        public static string? AwsSignatureService
        {
            get => _awsSignatureService.Get();
            set => _awsSignatureService.Set(value);
        }

        private static readonly __Value<string?> _awsToken = new __Value<string?>(() => __config.Get("awsToken"));
        /// <summary>
        /// The session token for use with AWS OpenSearch Service domains
        /// </summary>
        public static string? AwsToken
        {
            get => _awsToken.Get();
            set => _awsToken.Set(value);
        }

        private static readonly __Value<string?> _cacertFile = new __Value<string?>(() => __config.Get("cacertFile"));
        /// <summary>
        /// A Custom CA certificate
        /// </summary>
        public static string? CacertFile
        {
            get => _cacertFile.Get();
            set => _cacertFile.Set(value);
        }

        private static readonly __Value<string?> _clientCertPath = new __Value<string?>(() => __config.Get("clientCertPath"));
        /// <summary>
        /// A X509 certificate to connect to OpenSearch
        /// </summary>
        public static string? ClientCertPath
        {
            get => _clientCertPath.Get();
            set => _clientCertPath.Set(value);
        }

        private static readonly __Value<string?> _clientKeyPath = new __Value<string?>(() => __config.Get("clientKeyPath"));
        /// <summary>
        /// A X509 key to connect to OpenSearch
        /// </summary>
        public static string? ClientKeyPath
        {
            get => _clientKeyPath.Get();
            set => _clientKeyPath.Set(value);
        }

        private static readonly __Value<bool?> _healthcheck = new __Value<bool?>(() => __config.GetBoolean("healthcheck"));
        /// <summary>
        /// Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
        /// cluster.
        /// </summary>
        public static bool? Healthcheck
        {
            get => _healthcheck.Get();
            set => _healthcheck.Set(value);
        }

        private static readonly __Value<string?> _hostOverride = new __Value<string?>(() => __config.Get("hostOverride"));
        /// <summary>
        /// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
        /// documentation on connecting to OpenSearch via an SSH tunnel.
        /// </summary>
        public static string? HostOverride
        {
            get => _hostOverride.Get();
            set => _hostOverride.Set(value);
        }

        private static readonly __Value<bool?> _insecure = new __Value<bool?>(() => __config.GetBoolean("insecure"));
        /// <summary>
        /// Disable SSL verification of API calls
        /// </summary>
        public static bool? Insecure
        {
            get => _insecure.Get();
            set => _insecure.Set(value);
        }

        private static readonly __Value<string?> _opensearchVersion = new __Value<string?>(() => __config.Get("opensearchVersion"));
        /// <summary>
        /// OpenSearch Version
        /// </summary>
        public static string? OpensearchVersion
        {
            get => _opensearchVersion.Get();
            set => _opensearchVersion.Set(value);
        }

        private static readonly __Value<string?> _password = new __Value<string?>(() => __config.Get("password"));
        /// <summary>
        /// Password to use to connect to OpenSearch using basic auth
        /// </summary>
        public static string? Password
        {
            get => _password.Get();
            set => _password.Set(value);
        }

        private static readonly __Value<string?> _proxy = new __Value<string?>(() => __config.Get("proxy"));
        /// <summary>
        /// Proxy URL to use for requests to OpenSearch.
        /// </summary>
        public static string? Proxy
        {
            get => _proxy.Get();
            set => _proxy.Set(value);
        }

        private static readonly __Value<bool?> _signAwsRequests = new __Value<bool?>(() => __config.GetBoolean("signAwsRequests"));
        /// <summary>
        /// Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.&lt;region&gt;.es.amazonaws.com`), or
        /// `aws_region` must be specified explicitly.
        /// </summary>
        public static bool? SignAwsRequests
        {
            get => _signAwsRequests.Get();
            set => _signAwsRequests.Set(value);
        }

        private static readonly __Value<bool?> _sniff = new __Value<bool?>(() => __config.GetBoolean("sniff"));
        /// <summary>
        /// Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
        /// </summary>
        public static bool? Sniff
        {
            get => _sniff.Get();
            set => _sniff.Set(value);
        }

        private static readonly __Value<string?> _token = new __Value<string?>(() => __config.Get("token"));
        /// <summary>
        /// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        /// </summary>
        public static string? Token
        {
            get => _token.Get();
            set => _token.Set(value);
        }

        private static readonly __Value<string?> _tokenName = new __Value<string?>(() => __config.Get("tokenName"));
        /// <summary>
        /// The type of token, usually ApiKey or Bearer
        /// </summary>
        public static string? TokenName
        {
            get => _tokenName.Get();
            set => _tokenName.Set(value);
        }

        private static readonly __Value<string?> _url = new __Value<string?>(() => __config.Get("url"));
        /// <summary>
        /// OpenSearch URL
        /// </summary>
        public static string? Url
        {
            get => _url.Get();
            set => _url.Set(value);
        }

        private static readonly __Value<string?> _username = new __Value<string?>(() => __config.Get("username"));
        /// <summary>
        /// Username to use to connect to OpenSearch using basic auth
        /// </summary>
        public static string? Username
        {
            get => _username.Get();
            set => _username.Set(value);
        }

        private static readonly __Value<int?> _versionPingTimeout = new __Value<int?>(() => __config.GetInt32("versionPingTimeout"));
        /// <summary>
        /// Version ping timeout in seconds
        /// </summary>
        public static int? VersionPingTimeout
        {
            get => _versionPingTimeout.Get();
            set => _versionPingTimeout.Set(value);
        }

    }
}
