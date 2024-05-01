// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package opensearch

import (
	"context"
	"reflect"

	"github.com/piclemx/pulumi-opensearch/sdk/go/opensearch/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A data stream lets you store append-only time series data across multiple (hidden, auto-generated) indices while giving you a single named resource for requests
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
//			fooComposableIndexTemplate, err := opensearch.NewComposableIndexTemplate(ctx, "fooComposableIndexTemplate", &opensearch.ComposableIndexTemplateArgs{
//				Body: pulumi.String("{\n  \"index_patterns\": [\"foo-data-stream*\"],\n  \"data_stream\": {}\n}\n"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = opensearch.NewDataStream(ctx, "fooDataStream", nil, pulumi.DependsOn([]pulumi.Resource{
//				fooComposableIndexTemplate,
//			}))
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type DataStream struct {
	pulumi.CustomResourceState

	// Name of the data stream to create, must have a matching
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewDataStream registers a new resource with the given unique name, arguments, and options.
func NewDataStream(ctx *pulumi.Context,
	name string, args *DataStreamArgs, opts ...pulumi.ResourceOption) (*DataStream, error) {
	if args == nil {
		args = &DataStreamArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DataStream
	err := ctx.RegisterResource("opensearch:index/dataStream:DataStream", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataStream gets an existing DataStream resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataStream(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataStreamState, opts ...pulumi.ResourceOption) (*DataStream, error) {
	var resource DataStream
	err := ctx.ReadResource("opensearch:index/dataStream:DataStream", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataStream resources.
type dataStreamState struct {
	// Name of the data stream to create, must have a matching
	Name *string `pulumi:"name"`
}

type DataStreamState struct {
	// Name of the data stream to create, must have a matching
	Name pulumi.StringPtrInput
}

func (DataStreamState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataStreamState)(nil)).Elem()
}

type dataStreamArgs struct {
	// Name of the data stream to create, must have a matching
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a DataStream resource.
type DataStreamArgs struct {
	// Name of the data stream to create, must have a matching
	Name pulumi.StringPtrInput
}

func (DataStreamArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataStreamArgs)(nil)).Elem()
}

type DataStreamInput interface {
	pulumi.Input

	ToDataStreamOutput() DataStreamOutput
	ToDataStreamOutputWithContext(ctx context.Context) DataStreamOutput
}

func (*DataStream) ElementType() reflect.Type {
	return reflect.TypeOf((**DataStream)(nil)).Elem()
}

func (i *DataStream) ToDataStreamOutput() DataStreamOutput {
	return i.ToDataStreamOutputWithContext(context.Background())
}

func (i *DataStream) ToDataStreamOutputWithContext(ctx context.Context) DataStreamOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataStreamOutput)
}

// DataStreamArrayInput is an input type that accepts DataStreamArray and DataStreamArrayOutput values.
// You can construct a concrete instance of `DataStreamArrayInput` via:
//
//	DataStreamArray{ DataStreamArgs{...} }
type DataStreamArrayInput interface {
	pulumi.Input

	ToDataStreamArrayOutput() DataStreamArrayOutput
	ToDataStreamArrayOutputWithContext(context.Context) DataStreamArrayOutput
}

type DataStreamArray []DataStreamInput

func (DataStreamArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataStream)(nil)).Elem()
}

func (i DataStreamArray) ToDataStreamArrayOutput() DataStreamArrayOutput {
	return i.ToDataStreamArrayOutputWithContext(context.Background())
}

func (i DataStreamArray) ToDataStreamArrayOutputWithContext(ctx context.Context) DataStreamArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataStreamArrayOutput)
}

// DataStreamMapInput is an input type that accepts DataStreamMap and DataStreamMapOutput values.
// You can construct a concrete instance of `DataStreamMapInput` via:
//
//	DataStreamMap{ "key": DataStreamArgs{...} }
type DataStreamMapInput interface {
	pulumi.Input

	ToDataStreamMapOutput() DataStreamMapOutput
	ToDataStreamMapOutputWithContext(context.Context) DataStreamMapOutput
}

type DataStreamMap map[string]DataStreamInput

func (DataStreamMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataStream)(nil)).Elem()
}

func (i DataStreamMap) ToDataStreamMapOutput() DataStreamMapOutput {
	return i.ToDataStreamMapOutputWithContext(context.Background())
}

func (i DataStreamMap) ToDataStreamMapOutputWithContext(ctx context.Context) DataStreamMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataStreamMapOutput)
}

type DataStreamOutput struct{ *pulumi.OutputState }

func (DataStreamOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataStream)(nil)).Elem()
}

func (o DataStreamOutput) ToDataStreamOutput() DataStreamOutput {
	return o
}

func (o DataStreamOutput) ToDataStreamOutputWithContext(ctx context.Context) DataStreamOutput {
	return o
}

// Name of the data stream to create, must have a matching
func (o DataStreamOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DataStream) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

type DataStreamArrayOutput struct{ *pulumi.OutputState }

func (DataStreamArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataStream)(nil)).Elem()
}

func (o DataStreamArrayOutput) ToDataStreamArrayOutput() DataStreamArrayOutput {
	return o
}

func (o DataStreamArrayOutput) ToDataStreamArrayOutputWithContext(ctx context.Context) DataStreamArrayOutput {
	return o
}

func (o DataStreamArrayOutput) Index(i pulumi.IntInput) DataStreamOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DataStream {
		return vs[0].([]*DataStream)[vs[1].(int)]
	}).(DataStreamOutput)
}

type DataStreamMapOutput struct{ *pulumi.OutputState }

func (DataStreamMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataStream)(nil)).Elem()
}

func (o DataStreamMapOutput) ToDataStreamMapOutput() DataStreamMapOutput {
	return o
}

func (o DataStreamMapOutput) ToDataStreamMapOutputWithContext(ctx context.Context) DataStreamMapOutput {
	return o
}

func (o DataStreamMapOutput) MapIndex(k pulumi.StringInput) DataStreamOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DataStream {
		return vs[0].(map[string]*DataStream)[vs[1].(string)]
	}).(DataStreamOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataStreamInput)(nil)).Elem(), &DataStream{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataStreamArrayInput)(nil)).Elem(), DataStreamArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataStreamMapInput)(nil)).Elem(), DataStreamMap{})
	pulumi.RegisterOutputType(DataStreamOutput{})
	pulumi.RegisterOutputType(DataStreamArrayOutput{})
	pulumi.RegisterOutputType(DataStreamMapOutput{})
}
