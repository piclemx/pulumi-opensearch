# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ComponentTemplateArgs', 'ComponentTemplate']

@pulumi.input_type
class ComponentTemplateArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ComponentTemplate resource.
        :param pulumi.Input[str] body: The JSON body of the template.
        :param pulumi.Input[str] name: Name of the component template to create.
        """
        pulumi.set(__self__, "body", body)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        The JSON body of the template.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the component template to create.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ComponentTemplateState:
    def __init__(__self__, *,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ComponentTemplate resources.
        :param pulumi.Input[str] body: The JSON body of the template.
        :param pulumi.Input[str] name: Name of the component template to create.
        """
        if body is not None:
            pulumi.set(__self__, "body", body)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON body of the template.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the component template to create.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ComponentTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Component templates are building blocks for constructing index templates that specify index mappings, settings, and aliases. You cannot directly apply a component template to a data stream or index. To be applied, a component template must be included in an index template’s `composed_of` list.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        test = opensearch.ComponentTemplate("test", body=\"\"\"{
          "template": {
            "settings": {
              "index": {
                "number_of_shards": "1"
              }
            },
            "mappings": {
              "properties": {
                "host_name": {
                  "type": "keyword"
                },
                "created_at": {
                  "type": "date",
                  "format": "EEE MMM dd HH:mm:ss Z yyyy"
                }
              }
            },
            "aliases": {
              "mydata": { }
            }
          }
        }

        \"\"\")
        ```

        ## Import

        Import by name

        ```sh
         $ pulumi import opensearch:index/componentTemplate:ComponentTemplate test terraform-test
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The JSON body of the template.
        :param pulumi.Input[str] name: Name of the component template to create.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Component templates are building blocks for constructing index templates that specify index mappings, settings, and aliases. You cannot directly apply a component template to a data stream or index. To be applied, a component template must be included in an index template’s `composed_of` list.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        test = opensearch.ComponentTemplate("test", body=\"\"\"{
          "template": {
            "settings": {
              "index": {
                "number_of_shards": "1"
              }
            },
            "mappings": {
              "properties": {
                "host_name": {
                  "type": "keyword"
                },
                "created_at": {
                  "type": "date",
                  "format": "EEE MMM dd HH:mm:ss Z yyyy"
                }
              }
            },
            "aliases": {
              "mydata": { }
            }
          }
        }

        \"\"\")
        ```

        ## Import

        Import by name

        ```sh
         $ pulumi import opensearch:index/componentTemplate:ComponentTemplate test terraform-test
        ```

        :param str resource_name: The name of the resource.
        :param ComponentTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentTemplateArgs.__new__(ComponentTemplateArgs)

            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
            __props__.__dict__["name"] = name
        super(ComponentTemplate, __self__).__init__(
            'opensearch:index/componentTemplate:ComponentTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            body: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ComponentTemplate':
        """
        Get an existing ComponentTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The JSON body of the template.
        :param pulumi.Input[str] name: Name of the component template to create.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComponentTemplateState.__new__(_ComponentTemplateState)

        __props__.__dict__["body"] = body
        __props__.__dict__["name"] = name
        return ComponentTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        The JSON body of the template.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the component template to create.
        """
        return pulumi.get(self, "name")
