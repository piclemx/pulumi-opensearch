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

// Provides an OpenSearch snapshot repository resource.
//
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
//			_, err := opensearch.NewSnapshotRepository(ctx, "repo", &opensearch.SnapshotRepositoryArgs{
//				Settings: pulumi.Map{
//					"bucket":   pulumi.Any("es-index-backups"),
//					"region":   pulumi.Any("us-east-1"),
//					"role_arn": pulumi.Any("arn:aws:iam::123456789012:role/MyRole"),
//				},
//				Type: pulumi.String("s3"),
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
// ```sh
//
//	$ pulumi import opensearch:index/snapshotRepository:SnapshotRepository repo es-index-backups
//
// ```
type SnapshotRepository struct {
	pulumi.CustomResourceState

	// The name of the repository.
	Name pulumi.StringOutput `pulumi:"name"`
	// The settings map applicable for the backend, see official documentation for plugins.
	Settings pulumi.MapOutput `pulumi:"settings"`
	// The name of the repository backend (required plugins must be installed).
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewSnapshotRepository registers a new resource with the given unique name, arguments, and options.
func NewSnapshotRepository(ctx *pulumi.Context,
	name string, args *SnapshotRepositoryArgs, opts ...pulumi.ResourceOption) (*SnapshotRepository, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SnapshotRepository
	err := ctx.RegisterResource("opensearch:index/snapshotRepository:SnapshotRepository", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshotRepository gets an existing SnapshotRepository resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshotRepository(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotRepositoryState, opts ...pulumi.ResourceOption) (*SnapshotRepository, error) {
	var resource SnapshotRepository
	err := ctx.ReadResource("opensearch:index/snapshotRepository:SnapshotRepository", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SnapshotRepository resources.
type snapshotRepositoryState struct {
	// The name of the repository.
	Name *string `pulumi:"name"`
	// The settings map applicable for the backend, see official documentation for plugins.
	Settings map[string]interface{} `pulumi:"settings"`
	// The name of the repository backend (required plugins must be installed).
	Type *string `pulumi:"type"`
}

type SnapshotRepositoryState struct {
	// The name of the repository.
	Name pulumi.StringPtrInput
	// The settings map applicable for the backend, see official documentation for plugins.
	Settings pulumi.MapInput
	// The name of the repository backend (required plugins must be installed).
	Type pulumi.StringPtrInput
}

func (SnapshotRepositoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotRepositoryState)(nil)).Elem()
}

type snapshotRepositoryArgs struct {
	// The name of the repository.
	Name *string `pulumi:"name"`
	// The settings map applicable for the backend, see official documentation for plugins.
	Settings map[string]interface{} `pulumi:"settings"`
	// The name of the repository backend (required plugins must be installed).
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a SnapshotRepository resource.
type SnapshotRepositoryArgs struct {
	// The name of the repository.
	Name pulumi.StringPtrInput
	// The settings map applicable for the backend, see official documentation for plugins.
	Settings pulumi.MapInput
	// The name of the repository backend (required plugins must be installed).
	Type pulumi.StringInput
}

func (SnapshotRepositoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotRepositoryArgs)(nil)).Elem()
}

type SnapshotRepositoryInput interface {
	pulumi.Input

	ToSnapshotRepositoryOutput() SnapshotRepositoryOutput
	ToSnapshotRepositoryOutputWithContext(ctx context.Context) SnapshotRepositoryOutput
}

func (*SnapshotRepository) ElementType() reflect.Type {
	return reflect.TypeOf((**SnapshotRepository)(nil)).Elem()
}

func (i *SnapshotRepository) ToSnapshotRepositoryOutput() SnapshotRepositoryOutput {
	return i.ToSnapshotRepositoryOutputWithContext(context.Background())
}

func (i *SnapshotRepository) ToSnapshotRepositoryOutputWithContext(ctx context.Context) SnapshotRepositoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SnapshotRepositoryOutput)
}

// SnapshotRepositoryArrayInput is an input type that accepts SnapshotRepositoryArray and SnapshotRepositoryArrayOutput values.
// You can construct a concrete instance of `SnapshotRepositoryArrayInput` via:
//
//	SnapshotRepositoryArray{ SnapshotRepositoryArgs{...} }
type SnapshotRepositoryArrayInput interface {
	pulumi.Input

	ToSnapshotRepositoryArrayOutput() SnapshotRepositoryArrayOutput
	ToSnapshotRepositoryArrayOutputWithContext(context.Context) SnapshotRepositoryArrayOutput
}

type SnapshotRepositoryArray []SnapshotRepositoryInput

func (SnapshotRepositoryArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SnapshotRepository)(nil)).Elem()
}

func (i SnapshotRepositoryArray) ToSnapshotRepositoryArrayOutput() SnapshotRepositoryArrayOutput {
	return i.ToSnapshotRepositoryArrayOutputWithContext(context.Background())
}

func (i SnapshotRepositoryArray) ToSnapshotRepositoryArrayOutputWithContext(ctx context.Context) SnapshotRepositoryArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SnapshotRepositoryArrayOutput)
}

// SnapshotRepositoryMapInput is an input type that accepts SnapshotRepositoryMap and SnapshotRepositoryMapOutput values.
// You can construct a concrete instance of `SnapshotRepositoryMapInput` via:
//
//	SnapshotRepositoryMap{ "key": SnapshotRepositoryArgs{...} }
type SnapshotRepositoryMapInput interface {
	pulumi.Input

	ToSnapshotRepositoryMapOutput() SnapshotRepositoryMapOutput
	ToSnapshotRepositoryMapOutputWithContext(context.Context) SnapshotRepositoryMapOutput
}

type SnapshotRepositoryMap map[string]SnapshotRepositoryInput

func (SnapshotRepositoryMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SnapshotRepository)(nil)).Elem()
}

func (i SnapshotRepositoryMap) ToSnapshotRepositoryMapOutput() SnapshotRepositoryMapOutput {
	return i.ToSnapshotRepositoryMapOutputWithContext(context.Background())
}

func (i SnapshotRepositoryMap) ToSnapshotRepositoryMapOutputWithContext(ctx context.Context) SnapshotRepositoryMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SnapshotRepositoryMapOutput)
}

type SnapshotRepositoryOutput struct{ *pulumi.OutputState }

func (SnapshotRepositoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SnapshotRepository)(nil)).Elem()
}

func (o SnapshotRepositoryOutput) ToSnapshotRepositoryOutput() SnapshotRepositoryOutput {
	return o
}

func (o SnapshotRepositoryOutput) ToSnapshotRepositoryOutputWithContext(ctx context.Context) SnapshotRepositoryOutput {
	return o
}

// The name of the repository.
func (o SnapshotRepositoryOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *SnapshotRepository) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The settings map applicable for the backend, see official documentation for plugins.
func (o SnapshotRepositoryOutput) Settings() pulumi.MapOutput {
	return o.ApplyT(func(v *SnapshotRepository) pulumi.MapOutput { return v.Settings }).(pulumi.MapOutput)
}

// The name of the repository backend (required plugins must be installed).
func (o SnapshotRepositoryOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *SnapshotRepository) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type SnapshotRepositoryArrayOutput struct{ *pulumi.OutputState }

func (SnapshotRepositoryArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SnapshotRepository)(nil)).Elem()
}

func (o SnapshotRepositoryArrayOutput) ToSnapshotRepositoryArrayOutput() SnapshotRepositoryArrayOutput {
	return o
}

func (o SnapshotRepositoryArrayOutput) ToSnapshotRepositoryArrayOutputWithContext(ctx context.Context) SnapshotRepositoryArrayOutput {
	return o
}

func (o SnapshotRepositoryArrayOutput) Index(i pulumi.IntInput) SnapshotRepositoryOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SnapshotRepository {
		return vs[0].([]*SnapshotRepository)[vs[1].(int)]
	}).(SnapshotRepositoryOutput)
}

type SnapshotRepositoryMapOutput struct{ *pulumi.OutputState }

func (SnapshotRepositoryMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SnapshotRepository)(nil)).Elem()
}

func (o SnapshotRepositoryMapOutput) ToSnapshotRepositoryMapOutput() SnapshotRepositoryMapOutput {
	return o
}

func (o SnapshotRepositoryMapOutput) ToSnapshotRepositoryMapOutputWithContext(ctx context.Context) SnapshotRepositoryMapOutput {
	return o
}

func (o SnapshotRepositoryMapOutput) MapIndex(k pulumi.StringInput) SnapshotRepositoryOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SnapshotRepository {
		return vs[0].(map[string]*SnapshotRepository)[vs[1].(string)]
	}).(SnapshotRepositoryOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SnapshotRepositoryInput)(nil)).Elem(), &SnapshotRepository{})
	pulumi.RegisterInputType(reflect.TypeOf((*SnapshotRepositoryArrayInput)(nil)).Elem(), SnapshotRepositoryArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SnapshotRepositoryMapInput)(nil)).Elem(), SnapshotRepositoryMap{})
	pulumi.RegisterOutputType(SnapshotRepositoryOutput{})
	pulumi.RegisterOutputType(SnapshotRepositoryArrayOutput{})
	pulumi.RegisterOutputType(SnapshotRepositoryMapOutput{})
}