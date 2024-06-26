# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 username: pulumi.Input[str],
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 backend_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] username: The name of the security user.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attributes: A map of arbitrary key value string pairs stored alongside of users.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] backend_roles: A list of backend roles.
        :param pulumi.Input[str] description: Description of the user.
        :param pulumi.Input[str] password: The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        :param pulumi.Input[str] password_hash: The pre-hashed password for the user, cannot be specified with `password`.
        """
        pulumi.set(__self__, "username", username)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if backend_roles is not None:
            pulumi.set(__self__, "backend_roles", backend_roles)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if password_hash is not None:
            pulumi.set(__self__, "password_hash", password_hash)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The name of the security user.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of arbitrary key value string pairs stored alongside of users.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="backendRoles")
    def backend_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of backend roles.
        """
        return pulumi.get(self, "backend_roles")

    @backend_roles.setter
    def backend_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "backend_roles", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the user.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The pre-hashed password for the user, cannot be specified with `password`.
        """
        return pulumi.get(self, "password_hash")

    @password_hash.setter
    def password_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_hash", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 backend_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attributes: A map of arbitrary key value string pairs stored alongside of users.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] backend_roles: A list of backend roles.
        :param pulumi.Input[str] description: Description of the user.
        :param pulumi.Input[str] password: The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        :param pulumi.Input[str] password_hash: The pre-hashed password for the user, cannot be specified with `password`.
        :param pulumi.Input[str] username: The name of the security user.
        """
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if backend_roles is not None:
            pulumi.set(__self__, "backend_roles", backend_roles)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if password_hash is not None:
            pulumi.set(__self__, "password_hash", password_hash)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of arbitrary key value string pairs stored alongside of users.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="backendRoles")
    def backend_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of backend roles.
        """
        return pulumi.get(self, "backend_roles")

    @backend_roles.setter
    def backend_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "backend_roles", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the user.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The pre-hashed password for the user, cannot be specified with `password`.
        """
        return pulumi.get(self, "password_hash")

    @password_hash.setter
    def password_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_hash", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security user.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 backend_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an OpenSearch security user. Please refer to the OpenSearch Access Control documentation for details.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        # Create a user
        mapper = opensearch.User("mapper",
            username="app-reasdder",
            password="SuperSekret123!",
            description="a reader role for our app")
        # And a full user, role and role mapping example:
        reader_role = opensearch.Role("readerRole",
            role_name="app_reader",
            description="App Reader Role",
            index_permissions=[opensearch.RoleIndexPermissionArgs(
                index_patterns=["app-*"],
                allowed_actions=[
                    "get",
                    "read",
                    "search",
                ],
            )])
        reader_user = opensearch.User("readerUser",
            username="app-reader",
            password=var["password"])
        reader_roles_mapping = opensearch.RolesMapping("readerRolesMapping",
            role_name=reader_role.id,
            description="App Reader Role",
            users=[reader_user.id])
        ```

        ## Import

        ```sh
         $ pulumi import opensearch:index/user:User reader app_reader
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attributes: A map of arbitrary key value string pairs stored alongside of users.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] backend_roles: A list of backend roles.
        :param pulumi.Input[str] description: Description of the user.
        :param pulumi.Input[str] password: The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        :param pulumi.Input[str] password_hash: The pre-hashed password for the user, cannot be specified with `password`.
        :param pulumi.Input[str] username: The name of the security user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an OpenSearch security user. Please refer to the OpenSearch Access Control documentation for details.

        ## Example Usage

        ```python
        import pulumi
        import piclemx_pulumi_opensearch as opensearch

        # Create a user
        mapper = opensearch.User("mapper",
            username="app-reasdder",
            password="SuperSekret123!",
            description="a reader role for our app")
        # And a full user, role and role mapping example:
        reader_role = opensearch.Role("readerRole",
            role_name="app_reader",
            description="App Reader Role",
            index_permissions=[opensearch.RoleIndexPermissionArgs(
                index_patterns=["app-*"],
                allowed_actions=[
                    "get",
                    "read",
                    "search",
                ],
            )])
        reader_user = opensearch.User("readerUser",
            username="app-reader",
            password=var["password"])
        reader_roles_mapping = opensearch.RolesMapping("readerRolesMapping",
            role_name=reader_role.id,
            description="App Reader Role",
            users=[reader_user.id])
        ```

        ## Import

        ```sh
         $ pulumi import opensearch:index/user:User reader app_reader
        ```

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 backend_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["backend_roles"] = backend_roles
            __props__.__dict__["description"] = description
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["password_hash"] = None if password_hash is None else pulumi.Output.secret(password_hash)
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password", "passwordHash"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(User, __self__).__init__(
            'opensearch:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            backend_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            password_hash: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attributes: A map of arbitrary key value string pairs stored alongside of users.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] backend_roles: A list of backend roles.
        :param pulumi.Input[str] description: Description of the user.
        :param pulumi.Input[str] password: The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        :param pulumi.Input[str] password_hash: The pre-hashed password for the user, cannot be specified with `password`.
        :param pulumi.Input[str] username: The name of the security user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["attributes"] = attributes
        __props__.__dict__["backend_roles"] = backend_roles
        __props__.__dict__["description"] = description
        __props__.__dict__["password"] = password
        __props__.__dict__["password_hash"] = password_hash
        __props__.__dict__["username"] = username
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of arbitrary key value string pairs stored alongside of users.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="backendRoles")
    def backend_roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of backend roles.
        """
        return pulumi.get(self, "backend_roles")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the user.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The plain text password for the user, cannot be specified with `password_hash`. Some implementations may enforce a password policy. Invalid passwords may cause a non-descriptive HTTP 400 Bad Request error. For AWS OpenSearch domains "password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character".
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> pulumi.Output[Optional[str]]:
        """
        The pre-hashed password for the user, cannot be specified with `password`.
        """
        return pulumi.get(self, "password_hash")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The name of the security user.
        """
        return pulumi.get(self, "username")

