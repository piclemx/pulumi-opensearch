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

// Provides an OpenSearch security role mapping. Please refer to the OpenSearch Access Control documentation for details.
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
//			_, err := opensearch.NewRolesMapping(ctx, "mapper", &opensearch.RolesMappingArgs{
//				BackendRoles: pulumi.StringArray{
//					pulumi.String("arn:aws:iam::123456789012:role/lambda-call-opensearch"),
//					pulumi.String("arn:aws:iam::123456789012:role/run-containers"),
//				},
//				Description: pulumi.String("Mapping AWS IAM roles to ES role"),
//				RoleName:    pulumi.String("logs_writer"),
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
//	$ pulumi import opensearch:index/rolesMapping:RolesMapping mapper logs_writer
//
// ```
type RolesMapping struct {
	pulumi.CustomResourceState

	// A list of backend roles.
	AndBackendRoles pulumi.StringArrayOutput `pulumi:"andBackendRoles"`
	// A list of backend roles.
	BackendRoles pulumi.StringArrayOutput `pulumi:"backendRoles"`
	// Description of the role mapping.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A list of host names.
	Hosts pulumi.StringArrayOutput `pulumi:"hosts"`
	// The name of the security role.
	RoleName pulumi.StringOutput `pulumi:"roleName"`
	// A list of users.
	Users pulumi.StringArrayOutput `pulumi:"users"`
}

// NewRolesMapping registers a new resource with the given unique name, arguments, and options.
func NewRolesMapping(ctx *pulumi.Context,
	name string, args *RolesMappingArgs, opts ...pulumi.ResourceOption) (*RolesMapping, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RoleName == nil {
		return nil, errors.New("invalid value for required argument 'RoleName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RolesMapping
	err := ctx.RegisterResource("opensearch:index/rolesMapping:RolesMapping", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRolesMapping gets an existing RolesMapping resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRolesMapping(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RolesMappingState, opts ...pulumi.ResourceOption) (*RolesMapping, error) {
	var resource RolesMapping
	err := ctx.ReadResource("opensearch:index/rolesMapping:RolesMapping", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RolesMapping resources.
type rolesMappingState struct {
	// A list of backend roles.
	AndBackendRoles []string `pulumi:"andBackendRoles"`
	// A list of backend roles.
	BackendRoles []string `pulumi:"backendRoles"`
	// Description of the role mapping.
	Description *string `pulumi:"description"`
	// A list of host names.
	Hosts []string `pulumi:"hosts"`
	// The name of the security role.
	RoleName *string `pulumi:"roleName"`
	// A list of users.
	Users []string `pulumi:"users"`
}

type RolesMappingState struct {
	// A list of backend roles.
	AndBackendRoles pulumi.StringArrayInput
	// A list of backend roles.
	BackendRoles pulumi.StringArrayInput
	// Description of the role mapping.
	Description pulumi.StringPtrInput
	// A list of host names.
	Hosts pulumi.StringArrayInput
	// The name of the security role.
	RoleName pulumi.StringPtrInput
	// A list of users.
	Users pulumi.StringArrayInput
}

func (RolesMappingState) ElementType() reflect.Type {
	return reflect.TypeOf((*rolesMappingState)(nil)).Elem()
}

type rolesMappingArgs struct {
	// A list of backend roles.
	AndBackendRoles []string `pulumi:"andBackendRoles"`
	// A list of backend roles.
	BackendRoles []string `pulumi:"backendRoles"`
	// Description of the role mapping.
	Description *string `pulumi:"description"`
	// A list of host names.
	Hosts []string `pulumi:"hosts"`
	// The name of the security role.
	RoleName string `pulumi:"roleName"`
	// A list of users.
	Users []string `pulumi:"users"`
}

// The set of arguments for constructing a RolesMapping resource.
type RolesMappingArgs struct {
	// A list of backend roles.
	AndBackendRoles pulumi.StringArrayInput
	// A list of backend roles.
	BackendRoles pulumi.StringArrayInput
	// Description of the role mapping.
	Description pulumi.StringPtrInput
	// A list of host names.
	Hosts pulumi.StringArrayInput
	// The name of the security role.
	RoleName pulumi.StringInput
	// A list of users.
	Users pulumi.StringArrayInput
}

func (RolesMappingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rolesMappingArgs)(nil)).Elem()
}

type RolesMappingInput interface {
	pulumi.Input

	ToRolesMappingOutput() RolesMappingOutput
	ToRolesMappingOutputWithContext(ctx context.Context) RolesMappingOutput
}

func (*RolesMapping) ElementType() reflect.Type {
	return reflect.TypeOf((**RolesMapping)(nil)).Elem()
}

func (i *RolesMapping) ToRolesMappingOutput() RolesMappingOutput {
	return i.ToRolesMappingOutputWithContext(context.Background())
}

func (i *RolesMapping) ToRolesMappingOutputWithContext(ctx context.Context) RolesMappingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RolesMappingOutput)
}

// RolesMappingArrayInput is an input type that accepts RolesMappingArray and RolesMappingArrayOutput values.
// You can construct a concrete instance of `RolesMappingArrayInput` via:
//
//	RolesMappingArray{ RolesMappingArgs{...} }
type RolesMappingArrayInput interface {
	pulumi.Input

	ToRolesMappingArrayOutput() RolesMappingArrayOutput
	ToRolesMappingArrayOutputWithContext(context.Context) RolesMappingArrayOutput
}

type RolesMappingArray []RolesMappingInput

func (RolesMappingArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RolesMapping)(nil)).Elem()
}

func (i RolesMappingArray) ToRolesMappingArrayOutput() RolesMappingArrayOutput {
	return i.ToRolesMappingArrayOutputWithContext(context.Background())
}

func (i RolesMappingArray) ToRolesMappingArrayOutputWithContext(ctx context.Context) RolesMappingArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RolesMappingArrayOutput)
}

// RolesMappingMapInput is an input type that accepts RolesMappingMap and RolesMappingMapOutput values.
// You can construct a concrete instance of `RolesMappingMapInput` via:
//
//	RolesMappingMap{ "key": RolesMappingArgs{...} }
type RolesMappingMapInput interface {
	pulumi.Input

	ToRolesMappingMapOutput() RolesMappingMapOutput
	ToRolesMappingMapOutputWithContext(context.Context) RolesMappingMapOutput
}

type RolesMappingMap map[string]RolesMappingInput

func (RolesMappingMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RolesMapping)(nil)).Elem()
}

func (i RolesMappingMap) ToRolesMappingMapOutput() RolesMappingMapOutput {
	return i.ToRolesMappingMapOutputWithContext(context.Background())
}

func (i RolesMappingMap) ToRolesMappingMapOutputWithContext(ctx context.Context) RolesMappingMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RolesMappingMapOutput)
}

type RolesMappingOutput struct{ *pulumi.OutputState }

func (RolesMappingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RolesMapping)(nil)).Elem()
}

func (o RolesMappingOutput) ToRolesMappingOutput() RolesMappingOutput {
	return o
}

func (o RolesMappingOutput) ToRolesMappingOutputWithContext(ctx context.Context) RolesMappingOutput {
	return o
}

// A list of backend roles.
func (o RolesMappingOutput) AndBackendRoles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *RolesMapping) pulumi.StringArrayOutput { return v.AndBackendRoles }).(pulumi.StringArrayOutput)
}

// A list of backend roles.
func (o RolesMappingOutput) BackendRoles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *RolesMapping) pulumi.StringArrayOutput { return v.BackendRoles }).(pulumi.StringArrayOutput)
}

// Description of the role mapping.
func (o RolesMappingOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RolesMapping) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// A list of host names.
func (o RolesMappingOutput) Hosts() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *RolesMapping) pulumi.StringArrayOutput { return v.Hosts }).(pulumi.StringArrayOutput)
}

// The name of the security role.
func (o RolesMappingOutput) RoleName() pulumi.StringOutput {
	return o.ApplyT(func(v *RolesMapping) pulumi.StringOutput { return v.RoleName }).(pulumi.StringOutput)
}

// A list of users.
func (o RolesMappingOutput) Users() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *RolesMapping) pulumi.StringArrayOutput { return v.Users }).(pulumi.StringArrayOutput)
}

type RolesMappingArrayOutput struct{ *pulumi.OutputState }

func (RolesMappingArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RolesMapping)(nil)).Elem()
}

func (o RolesMappingArrayOutput) ToRolesMappingArrayOutput() RolesMappingArrayOutput {
	return o
}

func (o RolesMappingArrayOutput) ToRolesMappingArrayOutputWithContext(ctx context.Context) RolesMappingArrayOutput {
	return o
}

func (o RolesMappingArrayOutput) Index(i pulumi.IntInput) RolesMappingOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RolesMapping {
		return vs[0].([]*RolesMapping)[vs[1].(int)]
	}).(RolesMappingOutput)
}

type RolesMappingMapOutput struct{ *pulumi.OutputState }

func (RolesMappingMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RolesMapping)(nil)).Elem()
}

func (o RolesMappingMapOutput) ToRolesMappingMapOutput() RolesMappingMapOutput {
	return o
}

func (o RolesMappingMapOutput) ToRolesMappingMapOutputWithContext(ctx context.Context) RolesMappingMapOutput {
	return o
}

func (o RolesMappingMapOutput) MapIndex(k pulumi.StringInput) RolesMappingOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RolesMapping {
		return vs[0].(map[string]*RolesMapping)[vs[1].(string)]
	}).(RolesMappingOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RolesMappingInput)(nil)).Elem(), &RolesMapping{})
	pulumi.RegisterInputType(reflect.TypeOf((*RolesMappingArrayInput)(nil)).Elem(), RolesMappingArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RolesMappingMapInput)(nil)).Elem(), RolesMappingMap{})
	pulumi.RegisterOutputType(RolesMappingOutput{})
	pulumi.RegisterOutputType(RolesMappingArrayOutput{})
	pulumi.RegisterOutputType(RolesMappingMapOutput{})
}
