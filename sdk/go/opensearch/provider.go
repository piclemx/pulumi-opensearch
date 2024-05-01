// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package opensearch

import (
	"context"
	"reflect"

	"errors"
	"github.com/piclemx/pulumi-opensearch/sdk/go/opensearch/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the opensearch package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// The access key for use with AWS OpenSearch Service domains
	AwsAccessKey pulumi.StringPtrOutput `pulumi:"awsAccessKey"`
	// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
	AwsAssumeRoleArn pulumi.StringPtrOutput `pulumi:"awsAssumeRoleArn"`
	// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
	AwsAssumeRoleExternalId pulumi.StringPtrOutput `pulumi:"awsAssumeRoleExternalId"`
	// The AWS profile for use with AWS OpenSearch Service domains
	AwsProfile pulumi.StringPtrOutput `pulumi:"awsProfile"`
	// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
	// OpenSearch endpoint exposed on a custom DNS domain.
	AwsRegion pulumi.StringPtrOutput `pulumi:"awsRegion"`
	// The secret key for use with AWS OpenSearch Service domains
	AwsSecretKey pulumi.StringPtrOutput `pulumi:"awsSecretKey"`
	// AWS service name used in the credential scope of signed requests to OpenSearch.
	AwsSignatureService pulumi.StringPtrOutput `pulumi:"awsSignatureService"`
	// The session token for use with AWS OpenSearch Service domains
	AwsToken pulumi.StringPtrOutput `pulumi:"awsToken"`
	// A Custom CA certificate
	CacertFile pulumi.StringPtrOutput `pulumi:"cacertFile"`
	// A X509 certificate to connect to OpenSearch
	ClientCertPath pulumi.StringPtrOutput `pulumi:"clientCertPath"`
	// A X509 key to connect to OpenSearch
	ClientKeyPath pulumi.StringPtrOutput `pulumi:"clientKeyPath"`
	// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
	// documentation on connecting to OpenSearch via an SSH tunnel.
	HostOverride pulumi.StringPtrOutput `pulumi:"hostOverride"`
	// OpenSearch Version
	OpensearchVersion pulumi.StringPtrOutput `pulumi:"opensearchVersion"`
	// Password to use to connect to OpenSearch using basic auth
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// Proxy URL to use for requests to OpenSearch.
	Proxy pulumi.StringPtrOutput `pulumi:"proxy"`
	// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
	Token pulumi.StringPtrOutput `pulumi:"token"`
	// The type of token, usually ApiKey or Bearer
	TokenName pulumi.StringPtrOutput `pulumi:"tokenName"`
	// OpenSearch URL
	Url pulumi.StringOutput `pulumi:"url"`
	// Username to use to connect to OpenSearch using basic auth
	Username pulumi.StringPtrOutput `pulumi:"username"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Url == nil {
		return nil, errors.New("invalid value for required argument 'Url'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:opensearch", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// The access key for use with AWS OpenSearch Service domains
	AwsAccessKey *string `pulumi:"awsAccessKey"`
	// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
	AwsAssumeRoleArn *string `pulumi:"awsAssumeRoleArn"`
	// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
	AwsAssumeRoleExternalId *string `pulumi:"awsAssumeRoleExternalId"`
	// The AWS profile for use with AWS OpenSearch Service domains
	AwsProfile *string `pulumi:"awsProfile"`
	// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
	// OpenSearch endpoint exposed on a custom DNS domain.
	AwsRegion *string `pulumi:"awsRegion"`
	// The secret key for use with AWS OpenSearch Service domains
	AwsSecretKey *string `pulumi:"awsSecretKey"`
	// AWS service name used in the credential scope of signed requests to OpenSearch.
	AwsSignatureService *string `pulumi:"awsSignatureService"`
	// The session token for use with AWS OpenSearch Service domains
	AwsToken *string `pulumi:"awsToken"`
	// A Custom CA certificate
	CacertFile *string `pulumi:"cacertFile"`
	// A X509 certificate to connect to OpenSearch
	ClientCertPath *string `pulumi:"clientCertPath"`
	// A X509 key to connect to OpenSearch
	ClientKeyPath *string `pulumi:"clientKeyPath"`
	// Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
	// cluster.
	Healthcheck *bool `pulumi:"healthcheck"`
	// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
	// documentation on connecting to OpenSearch via an SSH tunnel.
	HostOverride *string `pulumi:"hostOverride"`
	// Disable SSL verification of API calls
	Insecure *bool `pulumi:"insecure"`
	// OpenSearch Version
	OpensearchVersion *string `pulumi:"opensearchVersion"`
	// Password to use to connect to OpenSearch using basic auth
	Password *string `pulumi:"password"`
	// Proxy URL to use for requests to OpenSearch.
	Proxy *string `pulumi:"proxy"`
	// Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.<region>.es.amazonaws.com`), or
	// `aws_region` must be specified explicitly.
	SignAwsRequests *bool `pulumi:"signAwsRequests"`
	// Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
	Sniff *bool `pulumi:"sniff"`
	// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
	Token *string `pulumi:"token"`
	// The type of token, usually ApiKey or Bearer
	TokenName *string `pulumi:"tokenName"`
	// OpenSearch URL
	Url string `pulumi:"url"`
	// Username to use to connect to OpenSearch using basic auth
	Username *string `pulumi:"username"`
	// Version ping timeout in seconds
	VersionPingTimeout *int `pulumi:"versionPingTimeout"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// The access key for use with AWS OpenSearch Service domains
	AwsAccessKey pulumi.StringPtrInput
	// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
	AwsAssumeRoleArn pulumi.StringPtrInput
	// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
	AwsAssumeRoleExternalId pulumi.StringPtrInput
	// The AWS profile for use with AWS OpenSearch Service domains
	AwsProfile pulumi.StringPtrInput
	// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
	// OpenSearch endpoint exposed on a custom DNS domain.
	AwsRegion pulumi.StringPtrInput
	// The secret key for use with AWS OpenSearch Service domains
	AwsSecretKey pulumi.StringPtrInput
	// AWS service name used in the credential scope of signed requests to OpenSearch.
	AwsSignatureService pulumi.StringPtrInput
	// The session token for use with AWS OpenSearch Service domains
	AwsToken pulumi.StringPtrInput
	// A Custom CA certificate
	CacertFile pulumi.StringPtrInput
	// A X509 certificate to connect to OpenSearch
	ClientCertPath pulumi.StringPtrInput
	// A X509 key to connect to OpenSearch
	ClientKeyPath pulumi.StringPtrInput
	// Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
	// cluster.
	Healthcheck pulumi.BoolPtrInput
	// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
	// documentation on connecting to OpenSearch via an SSH tunnel.
	HostOverride pulumi.StringPtrInput
	// Disable SSL verification of API calls
	Insecure pulumi.BoolPtrInput
	// OpenSearch Version
	OpensearchVersion pulumi.StringPtrInput
	// Password to use to connect to OpenSearch using basic auth
	Password pulumi.StringPtrInput
	// Proxy URL to use for requests to OpenSearch.
	Proxy pulumi.StringPtrInput
	// Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.<region>.es.amazonaws.com`), or
	// `aws_region` must be specified explicitly.
	SignAwsRequests pulumi.BoolPtrInput
	// Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
	Sniff pulumi.BoolPtrInput
	// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
	Token pulumi.StringPtrInput
	// The type of token, usually ApiKey or Bearer
	TokenName pulumi.StringPtrInput
	// OpenSearch URL
	Url pulumi.StringInput
	// Username to use to connect to OpenSearch using basic auth
	Username pulumi.StringPtrInput
	// Version ping timeout in seconds
	VersionPingTimeout pulumi.IntPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// The access key for use with AWS OpenSearch Service domains
func (o ProviderOutput) AwsAccessKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsAccessKey }).(pulumi.StringPtrOutput)
}

// Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
func (o ProviderOutput) AwsAssumeRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsAssumeRoleArn }).(pulumi.StringPtrOutput)
}

// External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
func (o ProviderOutput) AwsAssumeRoleExternalId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsAssumeRoleExternalId }).(pulumi.StringPtrOutput)
}

// The AWS profile for use with AWS OpenSearch Service domains
func (o ProviderOutput) AwsProfile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsProfile }).(pulumi.StringPtrOutput)
}

// The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
// OpenSearch endpoint exposed on a custom DNS domain.
func (o ProviderOutput) AwsRegion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsRegion }).(pulumi.StringPtrOutput)
}

// The secret key for use with AWS OpenSearch Service domains
func (o ProviderOutput) AwsSecretKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsSecretKey }).(pulumi.StringPtrOutput)
}

// AWS service name used in the credential scope of signed requests to OpenSearch.
func (o ProviderOutput) AwsSignatureService() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsSignatureService }).(pulumi.StringPtrOutput)
}

// The session token for use with AWS OpenSearch Service domains
func (o ProviderOutput) AwsToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.AwsToken }).(pulumi.StringPtrOutput)
}

// A Custom CA certificate
func (o ProviderOutput) CacertFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.CacertFile }).(pulumi.StringPtrOutput)
}

// A X509 certificate to connect to OpenSearch
func (o ProviderOutput) ClientCertPath() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ClientCertPath }).(pulumi.StringPtrOutput)
}

// A X509 key to connect to OpenSearch
func (o ProviderOutput) ClientKeyPath() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ClientKeyPath }).(pulumi.StringPtrOutput)
}

// If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
// documentation on connecting to OpenSearch via an SSH tunnel.
func (o ProviderOutput) HostOverride() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.HostOverride }).(pulumi.StringPtrOutput)
}

// OpenSearch Version
func (o ProviderOutput) OpensearchVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.OpensearchVersion }).(pulumi.StringPtrOutput)
}

// Password to use to connect to OpenSearch using basic auth
func (o ProviderOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

// Proxy URL to use for requests to OpenSearch.
func (o ProviderOutput) Proxy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Proxy }).(pulumi.StringPtrOutput)
}

// A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
func (o ProviderOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Token }).(pulumi.StringPtrOutput)
}

// The type of token, usually ApiKey or Bearer
func (o ProviderOutput) TokenName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.TokenName }).(pulumi.StringPtrOutput)
}

// OpenSearch URL
func (o ProviderOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

// Username to use to connect to OpenSearch using basic auth
func (o ProviderOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Username }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
