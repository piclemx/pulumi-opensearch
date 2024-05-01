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

// Provides an OpenSearch Index State Management (ISM) policy. Please refer to the OpenSearch ISM documentation for details.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"fmt"
//	"os"
//
//	"github.com/piclemx/pulumi-opensearch/sdk/go/opensearch"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func readFileOrPanic(path string) pulumi.StringPtrInput {
//		data, err := os.ReadFile(path)
//		if err != nil {
//			panic(err.Error())
//		}
//		return pulumi.String(string(data))
//	}
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := opensearch.NewIsmPolicy(ctx, "cleanup", &opensearch.IsmPolicyArgs{
//				PolicyId: pulumi.String("delete_after_15d"),
//				Body:     readFileOrPanic(fmt.Sprintf("%v/policies/delete_after_15d.json", path.Module)),
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
//	$ pulumi import opensearch:index/ismPolicy:IsmPolicy cleanup delete_after_15d
//
// ```
type IsmPolicy struct {
	pulumi.CustomResourceState

	// The policy document.
	Body pulumi.StringOutput `pulumi:"body"`
	// The id of the ISM policy.
	PolicyId pulumi.StringOutput `pulumi:"policyId"`
	// The primary term of the ISM policy version.
	PrimaryTerm pulumi.IntOutput `pulumi:"primaryTerm"`
	// The sequence number of the ISM policy version.
	SeqNo pulumi.IntOutput `pulumi:"seqNo"`
}

// NewIsmPolicy registers a new resource with the given unique name, arguments, and options.
func NewIsmPolicy(ctx *pulumi.Context,
	name string, args *IsmPolicyArgs, opts ...pulumi.ResourceOption) (*IsmPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Body == nil {
		return nil, errors.New("invalid value for required argument 'Body'")
	}
	if args.PolicyId == nil {
		return nil, errors.New("invalid value for required argument 'PolicyId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource IsmPolicy
	err := ctx.RegisterResource("opensearch:index/ismPolicy:IsmPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIsmPolicy gets an existing IsmPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIsmPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IsmPolicyState, opts ...pulumi.ResourceOption) (*IsmPolicy, error) {
	var resource IsmPolicy
	err := ctx.ReadResource("opensearch:index/ismPolicy:IsmPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IsmPolicy resources.
type ismPolicyState struct {
	// The policy document.
	Body *string `pulumi:"body"`
	// The id of the ISM policy.
	PolicyId *string `pulumi:"policyId"`
	// The primary term of the ISM policy version.
	PrimaryTerm *int `pulumi:"primaryTerm"`
	// The sequence number of the ISM policy version.
	SeqNo *int `pulumi:"seqNo"`
}

type IsmPolicyState struct {
	// The policy document.
	Body pulumi.StringPtrInput
	// The id of the ISM policy.
	PolicyId pulumi.StringPtrInput
	// The primary term of the ISM policy version.
	PrimaryTerm pulumi.IntPtrInput
	// The sequence number of the ISM policy version.
	SeqNo pulumi.IntPtrInput
}

func (IsmPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*ismPolicyState)(nil)).Elem()
}

type ismPolicyArgs struct {
	// The policy document.
	Body string `pulumi:"body"`
	// The id of the ISM policy.
	PolicyId string `pulumi:"policyId"`
	// The primary term of the ISM policy version.
	PrimaryTerm *int `pulumi:"primaryTerm"`
	// The sequence number of the ISM policy version.
	SeqNo *int `pulumi:"seqNo"`
}

// The set of arguments for constructing a IsmPolicy resource.
type IsmPolicyArgs struct {
	// The policy document.
	Body pulumi.StringInput
	// The id of the ISM policy.
	PolicyId pulumi.StringInput
	// The primary term of the ISM policy version.
	PrimaryTerm pulumi.IntPtrInput
	// The sequence number of the ISM policy version.
	SeqNo pulumi.IntPtrInput
}

func (IsmPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ismPolicyArgs)(nil)).Elem()
}

type IsmPolicyInput interface {
	pulumi.Input

	ToIsmPolicyOutput() IsmPolicyOutput
	ToIsmPolicyOutputWithContext(ctx context.Context) IsmPolicyOutput
}

func (*IsmPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**IsmPolicy)(nil)).Elem()
}

func (i *IsmPolicy) ToIsmPolicyOutput() IsmPolicyOutput {
	return i.ToIsmPolicyOutputWithContext(context.Background())
}

func (i *IsmPolicy) ToIsmPolicyOutputWithContext(ctx context.Context) IsmPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IsmPolicyOutput)
}

// IsmPolicyArrayInput is an input type that accepts IsmPolicyArray and IsmPolicyArrayOutput values.
// You can construct a concrete instance of `IsmPolicyArrayInput` via:
//
//	IsmPolicyArray{ IsmPolicyArgs{...} }
type IsmPolicyArrayInput interface {
	pulumi.Input

	ToIsmPolicyArrayOutput() IsmPolicyArrayOutput
	ToIsmPolicyArrayOutputWithContext(context.Context) IsmPolicyArrayOutput
}

type IsmPolicyArray []IsmPolicyInput

func (IsmPolicyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IsmPolicy)(nil)).Elem()
}

func (i IsmPolicyArray) ToIsmPolicyArrayOutput() IsmPolicyArrayOutput {
	return i.ToIsmPolicyArrayOutputWithContext(context.Background())
}

func (i IsmPolicyArray) ToIsmPolicyArrayOutputWithContext(ctx context.Context) IsmPolicyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IsmPolicyArrayOutput)
}

// IsmPolicyMapInput is an input type that accepts IsmPolicyMap and IsmPolicyMapOutput values.
// You can construct a concrete instance of `IsmPolicyMapInput` via:
//
//	IsmPolicyMap{ "key": IsmPolicyArgs{...} }
type IsmPolicyMapInput interface {
	pulumi.Input

	ToIsmPolicyMapOutput() IsmPolicyMapOutput
	ToIsmPolicyMapOutputWithContext(context.Context) IsmPolicyMapOutput
}

type IsmPolicyMap map[string]IsmPolicyInput

func (IsmPolicyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IsmPolicy)(nil)).Elem()
}

func (i IsmPolicyMap) ToIsmPolicyMapOutput() IsmPolicyMapOutput {
	return i.ToIsmPolicyMapOutputWithContext(context.Background())
}

func (i IsmPolicyMap) ToIsmPolicyMapOutputWithContext(ctx context.Context) IsmPolicyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IsmPolicyMapOutput)
}

type IsmPolicyOutput struct{ *pulumi.OutputState }

func (IsmPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IsmPolicy)(nil)).Elem()
}

func (o IsmPolicyOutput) ToIsmPolicyOutput() IsmPolicyOutput {
	return o
}

func (o IsmPolicyOutput) ToIsmPolicyOutputWithContext(ctx context.Context) IsmPolicyOutput {
	return o
}

// The policy document.
func (o IsmPolicyOutput) Body() pulumi.StringOutput {
	return o.ApplyT(func(v *IsmPolicy) pulumi.StringOutput { return v.Body }).(pulumi.StringOutput)
}

// The id of the ISM policy.
func (o IsmPolicyOutput) PolicyId() pulumi.StringOutput {
	return o.ApplyT(func(v *IsmPolicy) pulumi.StringOutput { return v.PolicyId }).(pulumi.StringOutput)
}

// The primary term of the ISM policy version.
func (o IsmPolicyOutput) PrimaryTerm() pulumi.IntOutput {
	return o.ApplyT(func(v *IsmPolicy) pulumi.IntOutput { return v.PrimaryTerm }).(pulumi.IntOutput)
}

// The sequence number of the ISM policy version.
func (o IsmPolicyOutput) SeqNo() pulumi.IntOutput {
	return o.ApplyT(func(v *IsmPolicy) pulumi.IntOutput { return v.SeqNo }).(pulumi.IntOutput)
}

type IsmPolicyArrayOutput struct{ *pulumi.OutputState }

func (IsmPolicyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IsmPolicy)(nil)).Elem()
}

func (o IsmPolicyArrayOutput) ToIsmPolicyArrayOutput() IsmPolicyArrayOutput {
	return o
}

func (o IsmPolicyArrayOutput) ToIsmPolicyArrayOutputWithContext(ctx context.Context) IsmPolicyArrayOutput {
	return o
}

func (o IsmPolicyArrayOutput) Index(i pulumi.IntInput) IsmPolicyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IsmPolicy {
		return vs[0].([]*IsmPolicy)[vs[1].(int)]
	}).(IsmPolicyOutput)
}

type IsmPolicyMapOutput struct{ *pulumi.OutputState }

func (IsmPolicyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IsmPolicy)(nil)).Elem()
}

func (o IsmPolicyMapOutput) ToIsmPolicyMapOutput() IsmPolicyMapOutput {
	return o
}

func (o IsmPolicyMapOutput) ToIsmPolicyMapOutputWithContext(ctx context.Context) IsmPolicyMapOutput {
	return o
}

func (o IsmPolicyMapOutput) MapIndex(k pulumi.StringInput) IsmPolicyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IsmPolicy {
		return vs[0].(map[string]*IsmPolicy)[vs[1].(string)]
	}).(IsmPolicyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IsmPolicyInput)(nil)).Elem(), &IsmPolicy{})
	pulumi.RegisterInputType(reflect.TypeOf((*IsmPolicyArrayInput)(nil)).Elem(), IsmPolicyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IsmPolicyMapInput)(nil)).Elem(), IsmPolicyMap{})
	pulumi.RegisterOutputType(IsmPolicyOutput{})
	pulumi.RegisterOutputType(IsmPolicyArrayOutput{})
	pulumi.RegisterOutputType(IsmPolicyMapOutput{})
}