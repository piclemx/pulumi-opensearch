# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ComposableIndexTemplateArgs', 'ComposableIndexTemplate']

@pulumi.input_type
class ComposableIndexTemplateArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ComposableIndexTemplate resource.
        :param pulumi.Input[str] body: The JSON body of the index template.
        :param pulumi.Input[str] name: The name of the index template.
        """
        pulumi.set(__self__, "body", body)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        The JSON body of the index template.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the index template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ComposableIndexTemplateState:
    def __init__(__self__, *,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ComposableIndexTemplate resources.
        :param pulumi.Input[str] body: The JSON body of the index template.
        :param pulumi.Input[str] name: The name of the index template.
        """
        if body is not None:
            pulumi.set(__self__, "body", body)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON body of the index template.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the index template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ComposableIndexTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Composable index template resource. This resource uses the `/_index_template` endpoint of the API that is available since version 2.0.0. Use `IndexTemplate` if you are using older versions or if you want to keep using legacy Index Templates.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        template1 = opensearch.ComposableIndexTemplate("template1", body=\"\"\"{
          "index_patterns": ["te*", "bar*"],
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
          },
          "priority": 200,
          "version": 3
        }

        \"\"\")
        ```

        ## Import

        ```sh
         $ pulumi import opensearch:index/composableIndexTemplate:ComposableIndexTemplate template_1 template_1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The JSON body of the index template.
        :param pulumi.Input[str] name: The name of the index template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComposableIndexTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Composable index template resource. This resource uses the `/_index_template` endpoint of the API that is available since version 2.0.0. Use `IndexTemplate` if you are using older versions or if you want to keep using legacy Index Templates.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        template1 = opensearch.ComposableIndexTemplate("template1", body=\"\"\"{
          "index_patterns": ["te*", "bar*"],
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
          },
          "priority": 200,
          "version": 3
        }

        \"\"\")
        ```

        ## Import

        ```sh
         $ pulumi import opensearch:index/composableIndexTemplate:ComposableIndexTemplate template_1 template_1
        ```

        :param str resource_name: The name of the resource.
        :param ComposableIndexTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComposableIndexTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
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
            __props__ = ComposableIndexTemplateArgs.__new__(ComposableIndexTemplateArgs)

            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
            __props__.__dict__["name"] = name
        super(ComposableIndexTemplate, __self__).__init__(
            'opensearch:index/composableIndexTemplate:ComposableIndexTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            body: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ComposableIndexTemplate':
        """
        Get an existing ComposableIndexTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The JSON body of the index template.
        :param pulumi.Input[str] name: The name of the index template.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComposableIndexTemplateState.__new__(_ComposableIndexTemplateState)

        __props__.__dict__["body"] = body
        __props__.__dict__["name"] = name
        return ComposableIndexTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        The JSON body of the index template.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the index template.
        """
        return pulumi.get(self, "name")
