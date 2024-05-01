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

// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/piclemx/pulumi-opensearch/sdk/go/opensearch"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := opensearch.NewAuditConfig(ctx, "test", &opensearch.AuditConfigArgs{
//				Audit: &opensearch.AuditConfigAuditArgs{
//					DisabledRestCategories: pulumi.StringArray{
//						pulumi.String("GRANTED_PRIVILEGES"),
//						pulumi.String("AUTHENTICATED"),
//					},
//					DisabledTransportCategories: pulumi.StringArray{
//						pulumi.String("GRANTED_PRIVILEGES"),
//						pulumi.String("AUTHENTICATED"),
//					},
//					EnableRest:              pulumi.Bool(true),
//					EnableTransport:         pulumi.Bool(true),
//					ExcludeSensitiveHeaders: pulumi.Bool(true),
//					IgnoreRequests: pulumi.StringArray{
//						pulumi.String("SearchRequest"),
//						pulumi.String("indices:data/read/*"),
//						pulumi.String("/_cluster/health"),
//					},
//					IgnoreUsers: pulumi.StringArray{
//						pulumi.String("dashboardserver"),
//					},
//					LogRequestBody:      pulumi.Bool(true),
//					ResolveBulkRequests: pulumi.Bool(true),
//					ResolveIndices:      pulumi.Bool(true),
//				},
//				Compliance: &opensearch.AuditConfigComplianceArgs{
//					Enabled:        pulumi.Bool(true),
//					ExternalConfig: pulumi.Bool(false),
//					InternalConfig: pulumi.Bool(true),
//					ReadIgnoreUsers: pulumi.StringArray{
//						pulumi.String("read-ignore-1"),
//					},
//					ReadMetadataOnly: pulumi.Bool(true),
//					ReadWatchedFields: opensearch.AuditConfigComplianceReadWatchedFieldArray{
//						&opensearch.AuditConfigComplianceReadWatchedFieldArgs{
//							Fields: pulumi.StringArray{
//								pulumi.String("field-1"),
//								pulumi.String("field-2"),
//							},
//							Index: pulumi.String("read-index-1"),
//						},
//						&opensearch.AuditConfigComplianceReadWatchedFieldArgs{
//							Fields: pulumi.StringArray{
//								pulumi.String("field-3"),
//							},
//							Index: pulumi.String("read-index-2"),
//						},
//					},
//					WriteIgnoreUsers: pulumi.StringArray{
//						pulumi.String("write-ignore-1"),
//					},
//					WriteLogDiffs:     pulumi.Bool(false),
//					WriteMetadataOnly: pulumi.Bool(true),
//					WriteWatchedIndices: pulumi.StringArray{
//						pulumi.String("write-index-1"),
//						pulumi.String("write-index-2"),
//						pulumi.String("log-*"),
//						pulumi.String("*"),
//					},
//				},
//				Enabled: pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// # Import by name
//
// ```sh
//
//	$ pulumi import opensearch:index/auditConfig:AuditConfig test_config my-config
//
// ```
type AuditConfig struct {
	pulumi.CustomResourceState

	Audit      AuditConfigAuditPtrOutput      `pulumi:"audit"`
	Compliance AuditConfigCompliancePtrOutput `pulumi:"compliance"`
	Enabled    pulumi.BoolOutput              `pulumi:"enabled"`
}

// NewAuditConfig registers a new resource with the given unique name, arguments, and options.
func NewAuditConfig(ctx *pulumi.Context,
	name string, args *AuditConfigArgs, opts ...pulumi.ResourceOption) (*AuditConfig, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Enabled == nil {
		return nil, errors.New("invalid value for required argument 'Enabled'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AuditConfig
	err := ctx.RegisterResource("opensearch:index/auditConfig:AuditConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAuditConfig gets an existing AuditConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAuditConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AuditConfigState, opts ...pulumi.ResourceOption) (*AuditConfig, error) {
	var resource AuditConfig
	err := ctx.ReadResource("opensearch:index/auditConfig:AuditConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AuditConfig resources.
type auditConfigState struct {
	Audit      *AuditConfigAudit      `pulumi:"audit"`
	Compliance *AuditConfigCompliance `pulumi:"compliance"`
	Enabled    *bool                  `pulumi:"enabled"`
}

type AuditConfigState struct {
	Audit      AuditConfigAuditPtrInput
	Compliance AuditConfigCompliancePtrInput
	Enabled    pulumi.BoolPtrInput
}

func (AuditConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*auditConfigState)(nil)).Elem()
}

type auditConfigArgs struct {
	Audit      *AuditConfigAudit      `pulumi:"audit"`
	Compliance *AuditConfigCompliance `pulumi:"compliance"`
	Enabled    bool                   `pulumi:"enabled"`
}

// The set of arguments for constructing a AuditConfig resource.
type AuditConfigArgs struct {
	Audit      AuditConfigAuditPtrInput
	Compliance AuditConfigCompliancePtrInput
	Enabled    pulumi.BoolInput
}

func (AuditConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*auditConfigArgs)(nil)).Elem()
}

type AuditConfigInput interface {
	pulumi.Input

	ToAuditConfigOutput() AuditConfigOutput
	ToAuditConfigOutputWithContext(ctx context.Context) AuditConfigOutput
}

func (*AuditConfig) ElementType() reflect.Type {
	return reflect.TypeOf((**AuditConfig)(nil)).Elem()
}

func (i *AuditConfig) ToAuditConfigOutput() AuditConfigOutput {
	return i.ToAuditConfigOutputWithContext(context.Background())
}

func (i *AuditConfig) ToAuditConfigOutputWithContext(ctx context.Context) AuditConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuditConfigOutput)
}

// AuditConfigArrayInput is an input type that accepts AuditConfigArray and AuditConfigArrayOutput values.
// You can construct a concrete instance of `AuditConfigArrayInput` via:
//
//	AuditConfigArray{ AuditConfigArgs{...} }
type AuditConfigArrayInput interface {
	pulumi.Input

	ToAuditConfigArrayOutput() AuditConfigArrayOutput
	ToAuditConfigArrayOutputWithContext(context.Context) AuditConfigArrayOutput
}

type AuditConfigArray []AuditConfigInput

func (AuditConfigArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AuditConfig)(nil)).Elem()
}

func (i AuditConfigArray) ToAuditConfigArrayOutput() AuditConfigArrayOutput {
	return i.ToAuditConfigArrayOutputWithContext(context.Background())
}

func (i AuditConfigArray) ToAuditConfigArrayOutputWithContext(ctx context.Context) AuditConfigArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuditConfigArrayOutput)
}

// AuditConfigMapInput is an input type that accepts AuditConfigMap and AuditConfigMapOutput values.
// You can construct a concrete instance of `AuditConfigMapInput` via:
//
//	AuditConfigMap{ "key": AuditConfigArgs{...} }
type AuditConfigMapInput interface {
	pulumi.Input

	ToAuditConfigMapOutput() AuditConfigMapOutput
	ToAuditConfigMapOutputWithContext(context.Context) AuditConfigMapOutput
}

type AuditConfigMap map[string]AuditConfigInput

func (AuditConfigMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AuditConfig)(nil)).Elem()
}

func (i AuditConfigMap) ToAuditConfigMapOutput() AuditConfigMapOutput {
	return i.ToAuditConfigMapOutputWithContext(context.Background())
}

func (i AuditConfigMap) ToAuditConfigMapOutputWithContext(ctx context.Context) AuditConfigMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuditConfigMapOutput)
}

type AuditConfigOutput struct{ *pulumi.OutputState }

func (AuditConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AuditConfig)(nil)).Elem()
}

func (o AuditConfigOutput) ToAuditConfigOutput() AuditConfigOutput {
	return o
}

func (o AuditConfigOutput) ToAuditConfigOutputWithContext(ctx context.Context) AuditConfigOutput {
	return o
}

func (o AuditConfigOutput) Audit() AuditConfigAuditPtrOutput {
	return o.ApplyT(func(v *AuditConfig) AuditConfigAuditPtrOutput { return v.Audit }).(AuditConfigAuditPtrOutput)
}

func (o AuditConfigOutput) Compliance() AuditConfigCompliancePtrOutput {
	return o.ApplyT(func(v *AuditConfig) AuditConfigCompliancePtrOutput { return v.Compliance }).(AuditConfigCompliancePtrOutput)
}

func (o AuditConfigOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v *AuditConfig) pulumi.BoolOutput { return v.Enabled }).(pulumi.BoolOutput)
}

type AuditConfigArrayOutput struct{ *pulumi.OutputState }

func (AuditConfigArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AuditConfig)(nil)).Elem()
}

func (o AuditConfigArrayOutput) ToAuditConfigArrayOutput() AuditConfigArrayOutput {
	return o
}

func (o AuditConfigArrayOutput) ToAuditConfigArrayOutputWithContext(ctx context.Context) AuditConfigArrayOutput {
	return o
}

func (o AuditConfigArrayOutput) Index(i pulumi.IntInput) AuditConfigOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AuditConfig {
		return vs[0].([]*AuditConfig)[vs[1].(int)]
	}).(AuditConfigOutput)
}

type AuditConfigMapOutput struct{ *pulumi.OutputState }

func (AuditConfigMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AuditConfig)(nil)).Elem()
}

func (o AuditConfigMapOutput) ToAuditConfigMapOutput() AuditConfigMapOutput {
	return o
}

func (o AuditConfigMapOutput) ToAuditConfigMapOutputWithContext(ctx context.Context) AuditConfigMapOutput {
	return o
}

func (o AuditConfigMapOutput) MapIndex(k pulumi.StringInput) AuditConfigOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AuditConfig {
		return vs[0].(map[string]*AuditConfig)[vs[1].(string)]
	}).(AuditConfigOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AuditConfigInput)(nil)).Elem(), &AuditConfig{})
	pulumi.RegisterInputType(reflect.TypeOf((*AuditConfigArrayInput)(nil)).Elem(), AuditConfigArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AuditConfigMapInput)(nil)).Elem(), AuditConfigMap{})
	pulumi.RegisterOutputType(AuditConfigOutput{})
	pulumi.RegisterOutputType(AuditConfigArrayOutput{})
	pulumi.RegisterOutputType(AuditConfigMapOutput{})
}