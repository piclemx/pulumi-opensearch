# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IsmPolicyMappingArgs', 'IsmPolicyMapping']

@pulumi.input_type
class IsmPolicyMappingArgs:
    def __init__(__self__, *,
                 indexes: pulumi.Input[str],
                 policy_id: pulumi.Input[str],
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 is_safe: Optional[pulumi.Input[bool]] = None,
                 managed_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IsmPolicyMapping resource.
        :param pulumi.Input[str] indexes: Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        :param pulumi.Input[str] policy_id: The name of the policy.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] includes: When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        :param pulumi.Input[str] state: After a change in policy takes place, specify the state for the index to transition to
        """
        pulumi.set(__self__, "indexes", indexes)
        pulumi.set(__self__, "policy_id", policy_id)
        if includes is not None:
            pulumi.set(__self__, "includes", includes)
        if is_safe is not None:
            pulumi.set(__self__, "is_safe", is_safe)
        if managed_indexes is not None:
            pulumi.set(__self__, "managed_indexes", managed_indexes)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def indexes(self) -> pulumi.Input[str]:
        """
        Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        """
        return pulumi.get(self, "indexes")

    @indexes.setter
    def indexes(self, value: pulumi.Input[str]):
        pulumi.set(self, "indexes", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[str]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter
    def includes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        """
        return pulumi.get(self, "includes")

    @includes.setter
    def includes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "includes", value)

    @property
    @pulumi.getter(name="isSafe")
    def is_safe(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_safe")

    @is_safe.setter
    def is_safe(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_safe", value)

    @property
    @pulumi.getter(name="managedIndexes")
    def managed_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "managed_indexes")

    @managed_indexes.setter
    def managed_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "managed_indexes", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        After a change in policy takes place, specify the state for the index to transition to
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class _IsmPolicyMappingState:
    def __init__(__self__, *,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 indexes: Optional[pulumi.Input[str]] = None,
                 is_safe: Optional[pulumi.Input[bool]] = None,
                 managed_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IsmPolicyMapping resources.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] includes: When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        :param pulumi.Input[str] indexes: Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        :param pulumi.Input[str] policy_id: The name of the policy.
        :param pulumi.Input[str] state: After a change in policy takes place, specify the state for the index to transition to
        """
        if includes is not None:
            pulumi.set(__self__, "includes", includes)
        if indexes is not None:
            pulumi.set(__self__, "indexes", indexes)
        if is_safe is not None:
            pulumi.set(__self__, "is_safe", is_safe)
        if managed_indexes is not None:
            pulumi.set(__self__, "managed_indexes", managed_indexes)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def includes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        """
        return pulumi.get(self, "includes")

    @includes.setter
    def includes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "includes", value)

    @property
    @pulumi.getter
    def indexes(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        """
        return pulumi.get(self, "indexes")

    @indexes.setter
    def indexes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "indexes", value)

    @property
    @pulumi.getter(name="isSafe")
    def is_safe(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_safe")

    @is_safe.setter
    def is_safe(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_safe", value)

    @property
    @pulumi.getter(name="managedIndexes")
    def managed_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "managed_indexes")

    @managed_indexes.setter
    def managed_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "managed_indexes", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        After a change in policy takes place, specify the state for the index to transition to
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class IsmPolicyMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 indexes: Optional[pulumi.Input[str]] = None,
                 is_safe: Optional[pulumi.Input[bool]] = None,
                 managed_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an OpenSearch Index State Management (ISM) policy. Please refer to the OpenSearch ISM documentation for details.

        !> `IsmPolicyMapping` is deprecated in OpenSearch 1.x please use the `IsmPolicy` resource and specify the `ism_template` attribute in the policies instead.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        test = opensearch.IsmPolicyMapping("test",
            indexes="test_index",
            policy_id="policy_1",
            state="delete")
        ```

        ## Import

        Import by poilcy_id

        ```sh
         $ pulumi import opensearch:index/ismPolicyMapping:IsmPolicyMapping test policy_1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] includes: When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        :param pulumi.Input[str] indexes: Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        :param pulumi.Input[str] policy_id: The name of the policy.
        :param pulumi.Input[str] state: After a change in policy takes place, specify the state for the index to transition to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IsmPolicyMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an OpenSearch Index State Management (ISM) policy. Please refer to the OpenSearch ISM documentation for details.

        !> `IsmPolicyMapping` is deprecated in OpenSearch 1.x please use the `IsmPolicy` resource and specify the `ism_template` attribute in the policies instead.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        test = opensearch.IsmPolicyMapping("test",
            indexes="test_index",
            policy_id="policy_1",
            state="delete")
        ```

        ## Import

        Import by poilcy_id

        ```sh
         $ pulumi import opensearch:index/ismPolicyMapping:IsmPolicyMapping test policy_1
        ```

        :param str resource_name: The name of the resource.
        :param IsmPolicyMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IsmPolicyMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 indexes: Optional[pulumi.Input[str]] = None,
                 is_safe: Optional[pulumi.Input[bool]] = None,
                 managed_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IsmPolicyMappingArgs.__new__(IsmPolicyMappingArgs)

            __props__.__dict__["includes"] = includes
            if indexes is None and not opts.urn:
                raise TypeError("Missing required property 'indexes'")
            __props__.__dict__["indexes"] = indexes
            __props__.__dict__["is_safe"] = is_safe
            __props__.__dict__["managed_indexes"] = managed_indexes
            if policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_id'")
            __props__.__dict__["policy_id"] = policy_id
            __props__.__dict__["state"] = state
        super(IsmPolicyMapping, __self__).__init__(
            'opensearch:index/ismPolicyMapping:IsmPolicyMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            includes: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
            indexes: Optional[pulumi.Input[str]] = None,
            is_safe: Optional[pulumi.Input[bool]] = None,
            managed_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            policy_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'IsmPolicyMapping':
        """
        Get an existing IsmPolicyMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] includes: When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        :param pulumi.Input[str] indexes: Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        :param pulumi.Input[str] policy_id: The name of the policy.
        :param pulumi.Input[str] state: After a change in policy takes place, specify the state for the index to transition to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IsmPolicyMappingState.__new__(_IsmPolicyMappingState)

        __props__.__dict__["includes"] = includes
        __props__.__dict__["indexes"] = indexes
        __props__.__dict__["is_safe"] = is_safe
        __props__.__dict__["managed_indexes"] = managed_indexes
        __props__.__dict__["policy_id"] = policy_id
        __props__.__dict__["state"] = state
        return IsmPolicyMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def includes(self) -> pulumi.Output[Optional[Sequence[Mapping[str, Any]]]]:
        """
        When updating multiple indices, you might want to include a state filter to only affect certain managed indices. The background process only applies the change if the index is currently in the state specified.
        """
        return pulumi.get(self, "includes")

    @property
    @pulumi.getter
    def indexes(self) -> pulumi.Output[str]:
        """
        Name of the index to apply the policy to. You can use an index pattern to update multiple indices at once.
        """
        return pulumi.get(self, "indexes")

    @property
    @pulumi.getter(name="isSafe")
    def is_safe(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_safe")

    @property
    @pulumi.getter(name="managedIndexes")
    def managed_indexes(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "managed_indexes")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        After a change in policy takes place, specify the state for the index to transition to
        """
        return pulumi.get(self, "state")
