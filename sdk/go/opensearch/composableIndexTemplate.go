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

// Provides an Composable index template resource. This resource uses the `/_index_template` endpoint of the API that is available since version 2.0.0. Use `IndexTemplate` if you are using older versions or if you want to keep using legacy Index Templates.
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
//			_, err := opensearch.NewComposableIndexTemplate(ctx, "template1", &opensearch.ComposableIndexTemplateArgs{
//				Body: pulumi.String(`{
//	  "index_patterns": ["te*", "bar*"],
//	  "template": {
//	    "settings": {
//	      "index": {
//	        "number_of_shards": "1"
//	      }
//	    },
//	    "mappings": {
//	      "properties": {
//	        "host_name": {
//	          "type": "keyword"
//	        },
//	        "created_at": {
//	          "type": "date",
//	          "format": "EEE MMM dd HH:mm:ss Z yyyy"
//	        }
//	      }
//	    },
//	    "aliases": {
//	      "mydata": { }
//	    }
//	  },
//	  "priority": 200,
//	  "version": 3
//	}
//
// `),
//
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
//	$ pulumi import opensearch:index/composableIndexTemplate:ComposableIndexTemplate template_1 template_1
//
// ```
type ComposableIndexTemplate struct {
	pulumi.CustomResourceState

	// The JSON body of the index template.
	Body pulumi.StringOutput `pulumi:"body"`
	// The name of the index template.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewComposableIndexTemplate registers a new resource with the given unique name, arguments, and options.
func NewComposableIndexTemplate(ctx *pulumi.Context,
	name string, args *ComposableIndexTemplateArgs, opts ...pulumi.ResourceOption) (*ComposableIndexTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Body == nil {
		return nil, errors.New("invalid value for required argument 'Body'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ComposableIndexTemplate
	err := ctx.RegisterResource("opensearch:index/composableIndexTemplate:ComposableIndexTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComposableIndexTemplate gets an existing ComposableIndexTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComposableIndexTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComposableIndexTemplateState, opts ...pulumi.ResourceOption) (*ComposableIndexTemplate, error) {
	var resource ComposableIndexTemplate
	err := ctx.ReadResource("opensearch:index/composableIndexTemplate:ComposableIndexTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ComposableIndexTemplate resources.
type composableIndexTemplateState struct {
	// The JSON body of the index template.
	Body *string `pulumi:"body"`
	// The name of the index template.
	Name *string `pulumi:"name"`
}

type ComposableIndexTemplateState struct {
	// The JSON body of the index template.
	Body pulumi.StringPtrInput
	// The name of the index template.
	Name pulumi.StringPtrInput
}

func (ComposableIndexTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*composableIndexTemplateState)(nil)).Elem()
}

type composableIndexTemplateArgs struct {
	// The JSON body of the index template.
	Body string `pulumi:"body"`
	// The name of the index template.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a ComposableIndexTemplate resource.
type ComposableIndexTemplateArgs struct {
	// The JSON body of the index template.
	Body pulumi.StringInput
	// The name of the index template.
	Name pulumi.StringPtrInput
}

func (ComposableIndexTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*composableIndexTemplateArgs)(nil)).Elem()
}

type ComposableIndexTemplateInput interface {
	pulumi.Input

	ToComposableIndexTemplateOutput() ComposableIndexTemplateOutput
	ToComposableIndexTemplateOutputWithContext(ctx context.Context) ComposableIndexTemplateOutput
}

func (*ComposableIndexTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**ComposableIndexTemplate)(nil)).Elem()
}

func (i *ComposableIndexTemplate) ToComposableIndexTemplateOutput() ComposableIndexTemplateOutput {
	return i.ToComposableIndexTemplateOutputWithContext(context.Background())
}

func (i *ComposableIndexTemplate) ToComposableIndexTemplateOutputWithContext(ctx context.Context) ComposableIndexTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComposableIndexTemplateOutput)
}

// ComposableIndexTemplateArrayInput is an input type that accepts ComposableIndexTemplateArray and ComposableIndexTemplateArrayOutput values.
// You can construct a concrete instance of `ComposableIndexTemplateArrayInput` via:
//
//	ComposableIndexTemplateArray{ ComposableIndexTemplateArgs{...} }
type ComposableIndexTemplateArrayInput interface {
	pulumi.Input

	ToComposableIndexTemplateArrayOutput() ComposableIndexTemplateArrayOutput
	ToComposableIndexTemplateArrayOutputWithContext(context.Context) ComposableIndexTemplateArrayOutput
}

type ComposableIndexTemplateArray []ComposableIndexTemplateInput

func (ComposableIndexTemplateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ComposableIndexTemplate)(nil)).Elem()
}

func (i ComposableIndexTemplateArray) ToComposableIndexTemplateArrayOutput() ComposableIndexTemplateArrayOutput {
	return i.ToComposableIndexTemplateArrayOutputWithContext(context.Background())
}

func (i ComposableIndexTemplateArray) ToComposableIndexTemplateArrayOutputWithContext(ctx context.Context) ComposableIndexTemplateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComposableIndexTemplateArrayOutput)
}

// ComposableIndexTemplateMapInput is an input type that accepts ComposableIndexTemplateMap and ComposableIndexTemplateMapOutput values.
// You can construct a concrete instance of `ComposableIndexTemplateMapInput` via:
//
//	ComposableIndexTemplateMap{ "key": ComposableIndexTemplateArgs{...} }
type ComposableIndexTemplateMapInput interface {
	pulumi.Input

	ToComposableIndexTemplateMapOutput() ComposableIndexTemplateMapOutput
	ToComposableIndexTemplateMapOutputWithContext(context.Context) ComposableIndexTemplateMapOutput
}

type ComposableIndexTemplateMap map[string]ComposableIndexTemplateInput

func (ComposableIndexTemplateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ComposableIndexTemplate)(nil)).Elem()
}

func (i ComposableIndexTemplateMap) ToComposableIndexTemplateMapOutput() ComposableIndexTemplateMapOutput {
	return i.ToComposableIndexTemplateMapOutputWithContext(context.Background())
}

func (i ComposableIndexTemplateMap) ToComposableIndexTemplateMapOutputWithContext(ctx context.Context) ComposableIndexTemplateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComposableIndexTemplateMapOutput)
}

type ComposableIndexTemplateOutput struct{ *pulumi.OutputState }

func (ComposableIndexTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ComposableIndexTemplate)(nil)).Elem()
}

func (o ComposableIndexTemplateOutput) ToComposableIndexTemplateOutput() ComposableIndexTemplateOutput {
	return o
}

func (o ComposableIndexTemplateOutput) ToComposableIndexTemplateOutputWithContext(ctx context.Context) ComposableIndexTemplateOutput {
	return o
}

// The JSON body of the index template.
func (o ComposableIndexTemplateOutput) Body() pulumi.StringOutput {
	return o.ApplyT(func(v *ComposableIndexTemplate) pulumi.StringOutput { return v.Body }).(pulumi.StringOutput)
}

// The name of the index template.
func (o ComposableIndexTemplateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ComposableIndexTemplate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

type ComposableIndexTemplateArrayOutput struct{ *pulumi.OutputState }

func (ComposableIndexTemplateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ComposableIndexTemplate)(nil)).Elem()
}

func (o ComposableIndexTemplateArrayOutput) ToComposableIndexTemplateArrayOutput() ComposableIndexTemplateArrayOutput {
	return o
}

func (o ComposableIndexTemplateArrayOutput) ToComposableIndexTemplateArrayOutputWithContext(ctx context.Context) ComposableIndexTemplateArrayOutput {
	return o
}

func (o ComposableIndexTemplateArrayOutput) Index(i pulumi.IntInput) ComposableIndexTemplateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ComposableIndexTemplate {
		return vs[0].([]*ComposableIndexTemplate)[vs[1].(int)]
	}).(ComposableIndexTemplateOutput)
}

type ComposableIndexTemplateMapOutput struct{ *pulumi.OutputState }

func (ComposableIndexTemplateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ComposableIndexTemplate)(nil)).Elem()
}

func (o ComposableIndexTemplateMapOutput) ToComposableIndexTemplateMapOutput() ComposableIndexTemplateMapOutput {
	return o
}

func (o ComposableIndexTemplateMapOutput) ToComposableIndexTemplateMapOutputWithContext(ctx context.Context) ComposableIndexTemplateMapOutput {
	return o
}

func (o ComposableIndexTemplateMapOutput) MapIndex(k pulumi.StringInput) ComposableIndexTemplateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ComposableIndexTemplate {
		return vs[0].(map[string]*ComposableIndexTemplate)[vs[1].(string)]
	}).(ComposableIndexTemplateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ComposableIndexTemplateInput)(nil)).Elem(), &ComposableIndexTemplate{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComposableIndexTemplateArrayInput)(nil)).Elem(), ComposableIndexTemplateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComposableIndexTemplateMapInput)(nil)).Elem(), ComposableIndexTemplateMap{})
	pulumi.RegisterOutputType(ComposableIndexTemplateOutput{})
	pulumi.RegisterOutputType(ComposableIndexTemplateArrayOutput{})
	pulumi.RegisterOutputType(ComposableIndexTemplateMapOutput{})
}
