# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IngestPipelineArgs', 'IngestPipeline']

@pulumi.input_type
class IngestPipelineArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IngestPipeline resource.
        :param pulumi.Input[str] body: The JSON body of the ingest pipeline
        :param pulumi.Input[str] name: The name of the ingest pipeline
        """
        pulumi.set(__self__, "body", body)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        The JSON body of the ingest pipeline
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ingest pipeline
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _IngestPipelineState:
    def __init__(__self__, *,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IngestPipeline resources.
        :param pulumi.Input[str] body: The JSON body of the ingest pipeline
        :param pulumi.Input[str] name: The name of the ingest pipeline
        """
        if body is not None:
            pulumi.set(__self__, "body", body)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON body of the ingest pipeline
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ingest pipeline
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class IngestPipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an OpenSearch ingest pipeline resource.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        # Create a simple ingest pipeline
        test = opensearch.IngestPipeline("test", body=\"\"\"{
          "description" : "describe pipeline",
          "version": 123,
          "processors" : [
            {
              "set" : {
                "field": "foo",
                "value": "bar"
              }
            }
          ]
        }

        \"\"\")
        ```

        ## Import

        ```sh
         $ pulumi import opensearch:index/ingestPipeline:IngestPipeline test terraform-test
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The JSON body of the ingest pipeline
        :param pulumi.Input[str] name: The name of the ingest pipeline
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IngestPipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an OpenSearch ingest pipeline resource.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        # Create a simple ingest pipeline
        test = opensearch.IngestPipeline("test", body=\"\"\"{
          "description" : "describe pipeline",
          "version": 123,
          "processors" : [
            {
              "set" : {
                "field": "foo",
                "value": "bar"
              }
            }
          ]
        }

        \"\"\")
        ```

        ## Import

        ```sh
         $ pulumi import opensearch:index/ingestPipeline:IngestPipeline test terraform-test
        ```

        :param str resource_name: The name of the resource.
        :param IngestPipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IngestPipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
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
            __props__ = IngestPipelineArgs.__new__(IngestPipelineArgs)

            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
            __props__.__dict__["name"] = name
        super(IngestPipeline, __self__).__init__(
            'opensearch:index/ingestPipeline:IngestPipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            body: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'IngestPipeline':
        """
        Get an existing IngestPipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The JSON body of the ingest pipeline
        :param pulumi.Input[str] name: The name of the ingest pipeline
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IngestPipelineState.__new__(_IngestPipelineState)

        __props__.__dict__["body"] = body
        __props__.__dict__["name"] = name
        return IngestPipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        The JSON body of the ingest pipeline
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ingest pipeline
        """
        return pulumi.get(self, "name")
