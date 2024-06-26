# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AnomalyDetectionArgs', 'AnomalyDetection']

@pulumi.input_type
class AnomalyDetectionArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[str]):
        """
        The set of arguments for constructing a AnomalyDetection resource.
        :param pulumi.Input[str] body: The anomaly detection document
        """
        pulumi.set(__self__, "body", body)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        The anomaly detection document
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)


@pulumi.input_type
class _AnomalyDetectionState:
    def __init__(__self__, *,
                 body: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AnomalyDetection resources.
        :param pulumi.Input[str] body: The anomaly detection document
        """
        if body is not None:
            pulumi.set(__self__, "body", body)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        The anomaly detection document
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)


class AnomalyDetection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an OpenSearch anonaly detection. Please refer to the OpenSearch anomaly detection documentation for details.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        foo = opensearch.AnomalyDetection("foo", body=\"\"\"{
          "name": "foo",
          "description": "Test detector",
          "time_field": "@timestamp",
          "indices": [
            "security-auditlog*"
          ],
          "feature_attributes": [
            {
              "feature_name": "test",
              "feature_enabled": true,
              "aggregation_query": {
                "test": {
                  "value_count": {
                    "field": "audit_category.keyword"
                  }
                }
              }
            }
          ],
          "filter_query": {
            "bool": {
              "filter": [
                {
                  "range": {
                    "value": {
                      "gt": 1
                    }
                  }
                }
              ],
              "adjust_pure_negative": true,
              "boost": 1
            }
          },
          "detection_interval": {
            "period": {
              "interval": 1,
              "unit": "Minutes"
            }
          },
          "window_delay": {
            "period": {
              "interval": 1,
              "unit": "Minutes"
            }
          },
          "result_index" : "opensearch-ad-plugin-result-test"
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The anomaly detection document
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnomalyDetectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an OpenSearch anonaly detection. Please refer to the OpenSearch anomaly detection documentation for details.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        foo = opensearch.AnomalyDetection("foo", body=\"\"\"{
          "name": "foo",
          "description": "Test detector",
          "time_field": "@timestamp",
          "indices": [
            "security-auditlog*"
          ],
          "feature_attributes": [
            {
              "feature_name": "test",
              "feature_enabled": true,
              "aggregation_query": {
                "test": {
                  "value_count": {
                    "field": "audit_category.keyword"
                  }
                }
              }
            }
          ],
          "filter_query": {
            "bool": {
              "filter": [
                {
                  "range": {
                    "value": {
                      "gt": 1
                    }
                  }
                }
              ],
              "adjust_pure_negative": true,
              "boost": 1
            }
          },
          "detection_interval": {
            "period": {
              "interval": 1,
              "unit": "Minutes"
            }
          },
          "window_delay": {
            "period": {
              "interval": 1,
              "unit": "Minutes"
            }
          },
          "result_index" : "opensearch-ad-plugin-result-test"
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param AnomalyDetectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnomalyDetectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnomalyDetectionArgs.__new__(AnomalyDetectionArgs)

            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
        super(AnomalyDetection, __self__).__init__(
            'opensearch:index/anomalyDetection:AnomalyDetection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            body: Optional[pulumi.Input[str]] = None) -> 'AnomalyDetection':
        """
        Get an existing AnomalyDetection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The anomaly detection document
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnomalyDetectionState.__new__(_AnomalyDetectionState)

        __props__.__dict__["body"] = body
        return AnomalyDetection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        The anomaly detection document
        """
        return pulumi.get(self, "body")

