# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 aws_access_key: Optional[pulumi.Input[str]] = None,
                 aws_assume_role_arn: Optional[pulumi.Input[str]] = None,
                 aws_assume_role_external_id: Optional[pulumi.Input[str]] = None,
                 aws_profile: Optional[pulumi.Input[str]] = None,
                 aws_region: Optional[pulumi.Input[str]] = None,
                 aws_secret_key: Optional[pulumi.Input[str]] = None,
                 aws_signature_service: Optional[pulumi.Input[str]] = None,
                 aws_token: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 client_cert_path: Optional[pulumi.Input[str]] = None,
                 client_key_path: Optional[pulumi.Input[str]] = None,
                 healthcheck: Optional[pulumi.Input[bool]] = None,
                 host_override: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 opensearch_version: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input[str]] = None,
                 sign_aws_requests: Optional[pulumi.Input[bool]] = None,
                 sniff: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 token_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 version_ping_timeout: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] url: OpenSearch URL
        :param pulumi.Input[str] aws_access_key: The access key for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] aws_assume_role_arn: Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        :param pulumi.Input[str] aws_assume_role_external_id: External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        :param pulumi.Input[str] aws_profile: The AWS profile for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] aws_region: The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
               OpenSearch endpoint exposed on a custom DNS domain.
        :param pulumi.Input[str] aws_secret_key: The secret key for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] aws_signature_service: AWS service name used in the credential scope of signed requests to OpenSearch.
        :param pulumi.Input[str] aws_token: The session token for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] cacert_file: A Custom CA certificate
        :param pulumi.Input[str] client_cert_path: A X509 certificate to connect to OpenSearch
        :param pulumi.Input[str] client_key_path: A X509 key to connect to OpenSearch
        :param pulumi.Input[bool] healthcheck: Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
               cluster.
        :param pulumi.Input[str] host_override: If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
               documentation on connecting to OpenSearch via an SSH tunnel.
        :param pulumi.Input[bool] insecure: Disable SSL verification of API calls
        :param pulumi.Input[str] opensearch_version: OpenSearch Version
        :param pulumi.Input[str] password: Password to use to connect to OpenSearch using basic auth
        :param pulumi.Input[str] proxy: Proxy URL to use for requests to OpenSearch.
        :param pulumi.Input[bool] sign_aws_requests: Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.<region>.es.amazonaws.com`), or
               `aws_region` must be specified explicitly.
        :param pulumi.Input[bool] sniff: Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
        :param pulumi.Input[str] token: A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        :param pulumi.Input[str] token_name: The type of token, usually ApiKey or Bearer
        :param pulumi.Input[str] username: Username to use to connect to OpenSearch using basic auth
        :param pulumi.Input[int] version_ping_timeout: Version ping timeout in seconds
        """
        pulumi.set(__self__, "url", url)
        if aws_access_key is not None:
            pulumi.set(__self__, "aws_access_key", aws_access_key)
        if aws_assume_role_arn is not None:
            pulumi.set(__self__, "aws_assume_role_arn", aws_assume_role_arn)
        if aws_assume_role_external_id is not None:
            pulumi.set(__self__, "aws_assume_role_external_id", aws_assume_role_external_id)
        if aws_profile is not None:
            pulumi.set(__self__, "aws_profile", aws_profile)
        if aws_region is not None:
            pulumi.set(__self__, "aws_region", aws_region)
        if aws_secret_key is not None:
            pulumi.set(__self__, "aws_secret_key", aws_secret_key)
        if aws_signature_service is not None:
            pulumi.set(__self__, "aws_signature_service", aws_signature_service)
        if aws_token is not None:
            pulumi.set(__self__, "aws_token", aws_token)
        if cacert_file is not None:
            pulumi.set(__self__, "cacert_file", cacert_file)
        if client_cert_path is not None:
            pulumi.set(__self__, "client_cert_path", client_cert_path)
        if client_key_path is not None:
            pulumi.set(__self__, "client_key_path", client_key_path)
        if healthcheck is not None:
            pulumi.set(__self__, "healthcheck", healthcheck)
        if host_override is not None:
            pulumi.set(__self__, "host_override", host_override)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if opensearch_version is not None:
            pulumi.set(__self__, "opensearch_version", opensearch_version)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if proxy is not None:
            pulumi.set(__self__, "proxy", proxy)
        if sign_aws_requests is not None:
            pulumi.set(__self__, "sign_aws_requests", sign_aws_requests)
        if sniff is not None:
            pulumi.set(__self__, "sniff", sniff)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if token_name is not None:
            pulumi.set(__self__, "token_name", token_name)
        if username is not None:
            pulumi.set(__self__, "username", username)
        if version_ping_timeout is not None:
            pulumi.set(__self__, "version_ping_timeout", version_ping_timeout)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        OpenSearch URL
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="awsAccessKey")
    def aws_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The access key for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_access_key")

    @aws_access_key.setter
    def aws_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_access_key", value)

    @property
    @pulumi.getter(name="awsAssumeRoleArn")
    def aws_assume_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        """
        return pulumi.get(self, "aws_assume_role_arn")

    @aws_assume_role_arn.setter
    def aws_assume_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_assume_role_arn", value)

    @property
    @pulumi.getter(name="awsAssumeRoleExternalId")
    def aws_assume_role_external_id(self) -> Optional[pulumi.Input[str]]:
        """
        External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        """
        return pulumi.get(self, "aws_assume_role_external_id")

    @aws_assume_role_external_id.setter
    def aws_assume_role_external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_assume_role_external_id", value)

    @property
    @pulumi.getter(name="awsProfile")
    def aws_profile(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS profile for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_profile")

    @aws_profile.setter
    def aws_profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_profile", value)

    @property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
        OpenSearch endpoint exposed on a custom DNS domain.
        """
        return pulumi.get(self, "aws_region")

    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_region", value)

    @property
    @pulumi.getter(name="awsSecretKey")
    def aws_secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        The secret key for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_secret_key")

    @aws_secret_key.setter
    def aws_secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_secret_key", value)

    @property
    @pulumi.getter(name="awsSignatureService")
    def aws_signature_service(self) -> Optional[pulumi.Input[str]]:
        """
        AWS service name used in the credential scope of signed requests to OpenSearch.
        """
        return pulumi.get(self, "aws_signature_service")

    @aws_signature_service.setter
    def aws_signature_service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_signature_service", value)

    @property
    @pulumi.getter(name="awsToken")
    def aws_token(self) -> Optional[pulumi.Input[str]]:
        """
        The session token for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_token")

    @aws_token.setter
    def aws_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_token", value)

    @property
    @pulumi.getter(name="cacertFile")
    def cacert_file(self) -> Optional[pulumi.Input[str]]:
        """
        A Custom CA certificate
        """
        return pulumi.get(self, "cacert_file")

    @cacert_file.setter
    def cacert_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cacert_file", value)

    @property
    @pulumi.getter(name="clientCertPath")
    def client_cert_path(self) -> Optional[pulumi.Input[str]]:
        """
        A X509 certificate to connect to OpenSearch
        """
        return pulumi.get(self, "client_cert_path")

    @client_cert_path.setter
    def client_cert_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_cert_path", value)

    @property
    @pulumi.getter(name="clientKeyPath")
    def client_key_path(self) -> Optional[pulumi.Input[str]]:
        """
        A X509 key to connect to OpenSearch
        """
        return pulumi.get(self, "client_key_path")

    @client_key_path.setter
    def client_key_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_key_path", value)

    @property
    @pulumi.getter
    def healthcheck(self) -> Optional[pulumi.Input[bool]]:
        """
        Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
        cluster.
        """
        return pulumi.get(self, "healthcheck")

    @healthcheck.setter
    def healthcheck(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "healthcheck", value)

    @property
    @pulumi.getter(name="hostOverride")
    def host_override(self) -> Optional[pulumi.Input[str]]:
        """
        If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
        documentation on connecting to OpenSearch via an SSH tunnel.
        """
        return pulumi.get(self, "host_override")

    @host_override.setter
    def host_override(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_override", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable SSL verification of API calls
        """
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)

    @property
    @pulumi.getter(name="opensearchVersion")
    def opensearch_version(self) -> Optional[pulumi.Input[str]]:
        """
        OpenSearch Version
        """
        return pulumi.get(self, "opensearch_version")

    @opensearch_version.setter
    def opensearch_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "opensearch_version", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password to use to connect to OpenSearch using basic auth
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input[str]]:
        """
        Proxy URL to use for requests to OpenSearch.
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy", value)

    @property
    @pulumi.getter(name="signAwsRequests")
    def sign_aws_requests(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.<region>.es.amazonaws.com`), or
        `aws_region` must be specified explicitly.
        """
        return pulumi.get(self, "sign_aws_requests")

    @sign_aws_requests.setter
    def sign_aws_requests(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sign_aws_requests", value)

    @property
    @pulumi.getter
    def sniff(self) -> Optional[pulumi.Input[bool]]:
        """
        Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
        """
        return pulumi.get(self, "sniff")

    @sniff.setter
    def sniff(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sniff", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="tokenName")
    def token_name(self) -> Optional[pulumi.Input[str]]:
        """
        The type of token, usually ApiKey or Bearer
        """
        return pulumi.get(self, "token_name")

    @token_name.setter
    def token_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_name", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username to use to connect to OpenSearch using basic auth
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="versionPingTimeout")
    def version_ping_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Version ping timeout in seconds
        """
        return pulumi.get(self, "version_ping_timeout")

    @version_ping_timeout.setter
    def version_ping_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version_ping_timeout", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_access_key: Optional[pulumi.Input[str]] = None,
                 aws_assume_role_arn: Optional[pulumi.Input[str]] = None,
                 aws_assume_role_external_id: Optional[pulumi.Input[str]] = None,
                 aws_profile: Optional[pulumi.Input[str]] = None,
                 aws_region: Optional[pulumi.Input[str]] = None,
                 aws_secret_key: Optional[pulumi.Input[str]] = None,
                 aws_signature_service: Optional[pulumi.Input[str]] = None,
                 aws_token: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 client_cert_path: Optional[pulumi.Input[str]] = None,
                 client_key_path: Optional[pulumi.Input[str]] = None,
                 healthcheck: Optional[pulumi.Input[bool]] = None,
                 host_override: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 opensearch_version: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input[str]] = None,
                 sign_aws_requests: Optional[pulumi.Input[bool]] = None,
                 sniff: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 token_name: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 version_ping_timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        The provider type for the opensearch package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_access_key: The access key for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] aws_assume_role_arn: Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        :param pulumi.Input[str] aws_assume_role_external_id: External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        :param pulumi.Input[str] aws_profile: The AWS profile for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] aws_region: The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
               OpenSearch endpoint exposed on a custom DNS domain.
        :param pulumi.Input[str] aws_secret_key: The secret key for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] aws_signature_service: AWS service name used in the credential scope of signed requests to OpenSearch.
        :param pulumi.Input[str] aws_token: The session token for use with AWS OpenSearch Service domains
        :param pulumi.Input[str] cacert_file: A Custom CA certificate
        :param pulumi.Input[str] client_cert_path: A X509 certificate to connect to OpenSearch
        :param pulumi.Input[str] client_key_path: A X509 key to connect to OpenSearch
        :param pulumi.Input[bool] healthcheck: Set the client healthcheck option for the OpenSearch client. Healthchecking is designed for direct access to the
               cluster.
        :param pulumi.Input[str] host_override: If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
               documentation on connecting to OpenSearch via an SSH tunnel.
        :param pulumi.Input[bool] insecure: Disable SSL verification of API calls
        :param pulumi.Input[str] opensearch_version: OpenSearch Version
        :param pulumi.Input[str] password: Password to use to connect to OpenSearch using basic auth
        :param pulumi.Input[str] proxy: Proxy URL to use for requests to OpenSearch.
        :param pulumi.Input[bool] sign_aws_requests: Enable signing of AWS OpenSearch requests. The `url` must refer to AWS ES domain (`*.<region>.es.amazonaws.com`), or
               `aws_region` must be specified explicitly.
        :param pulumi.Input[bool] sniff: Set the node sniffing option for the OpenSearch client. Client won't work with sniffing if nodes are not routable.
        :param pulumi.Input[str] token: A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        :param pulumi.Input[str] token_name: The type of token, usually ApiKey or Bearer
        :param pulumi.Input[str] url: OpenSearch URL
        :param pulumi.Input[str] username: Username to use to connect to OpenSearch using basic auth
        :param pulumi.Input[int] version_ping_timeout: Version ping timeout in seconds
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the opensearch package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_access_key: Optional[pulumi.Input[str]] = None,
                 aws_assume_role_arn: Optional[pulumi.Input[str]] = None,
                 aws_assume_role_external_id: Optional[pulumi.Input[str]] = None,
                 aws_profile: Optional[pulumi.Input[str]] = None,
                 aws_region: Optional[pulumi.Input[str]] = None,
                 aws_secret_key: Optional[pulumi.Input[str]] = None,
                 aws_signature_service: Optional[pulumi.Input[str]] = None,
                 aws_token: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 client_cert_path: Optional[pulumi.Input[str]] = None,
                 client_key_path: Optional[pulumi.Input[str]] = None,
                 healthcheck: Optional[pulumi.Input[bool]] = None,
                 host_override: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 opensearch_version: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 proxy: Optional[pulumi.Input[str]] = None,
                 sign_aws_requests: Optional[pulumi.Input[bool]] = None,
                 sniff: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 token_name: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 version_ping_timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["aws_access_key"] = aws_access_key
            __props__.__dict__["aws_assume_role_arn"] = aws_assume_role_arn
            __props__.__dict__["aws_assume_role_external_id"] = aws_assume_role_external_id
            __props__.__dict__["aws_profile"] = aws_profile
            __props__.__dict__["aws_region"] = aws_region
            __props__.__dict__["aws_secret_key"] = aws_secret_key
            __props__.__dict__["aws_signature_service"] = aws_signature_service
            __props__.__dict__["aws_token"] = aws_token
            __props__.__dict__["cacert_file"] = cacert_file
            __props__.__dict__["client_cert_path"] = client_cert_path
            __props__.__dict__["client_key_path"] = client_key_path
            __props__.__dict__["healthcheck"] = pulumi.Output.from_input(healthcheck).apply(pulumi.runtime.to_json) if healthcheck is not None else None
            __props__.__dict__["host_override"] = host_override
            __props__.__dict__["insecure"] = pulumi.Output.from_input(insecure).apply(pulumi.runtime.to_json) if insecure is not None else None
            __props__.__dict__["opensearch_version"] = opensearch_version
            __props__.__dict__["password"] = password
            __props__.__dict__["proxy"] = proxy
            __props__.__dict__["sign_aws_requests"] = pulumi.Output.from_input(sign_aws_requests).apply(pulumi.runtime.to_json) if sign_aws_requests is not None else None
            __props__.__dict__["sniff"] = pulumi.Output.from_input(sniff).apply(pulumi.runtime.to_json) if sniff is not None else None
            __props__.__dict__["token"] = token
            __props__.__dict__["token_name"] = token_name
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["username"] = username
            __props__.__dict__["version_ping_timeout"] = pulumi.Output.from_input(version_ping_timeout).apply(pulumi.runtime.to_json) if version_ping_timeout is not None else None
        super(Provider, __self__).__init__(
            'opensearch',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="awsAccessKey")
    def aws_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        The access key for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_access_key")

    @property
    @pulumi.getter(name="awsAssumeRoleArn")
    def aws_assume_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon Resource Name of an IAM Role to assume prior to making AWS API calls.
        """
        return pulumi.get(self, "aws_assume_role_arn")

    @property
    @pulumi.getter(name="awsAssumeRoleExternalId")
    def aws_assume_role_external_id(self) -> pulumi.Output[Optional[str]]:
        """
        External ID configured in the IAM policy of the IAM Role to assume prior to making AWS API calls.
        """
        return pulumi.get(self, "aws_assume_role_external_id")

    @property
    @pulumi.getter(name="awsProfile")
    def aws_profile(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS profile for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_profile")

    @property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS region for use in signing of AWS OpenSearch requests. Must be specified in order to use AWS URL signing with AWS
        OpenSearch endpoint exposed on a custom DNS domain.
        """
        return pulumi.get(self, "aws_region")

    @property
    @pulumi.getter(name="awsSecretKey")
    def aws_secret_key(self) -> pulumi.Output[Optional[str]]:
        """
        The secret key for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_secret_key")

    @property
    @pulumi.getter(name="awsSignatureService")
    def aws_signature_service(self) -> pulumi.Output[Optional[str]]:
        """
        AWS service name used in the credential scope of signed requests to OpenSearch.
        """
        return pulumi.get(self, "aws_signature_service")

    @property
    @pulumi.getter(name="awsToken")
    def aws_token(self) -> pulumi.Output[Optional[str]]:
        """
        The session token for use with AWS OpenSearch Service domains
        """
        return pulumi.get(self, "aws_token")

    @property
    @pulumi.getter(name="cacertFile")
    def cacert_file(self) -> pulumi.Output[Optional[str]]:
        """
        A Custom CA certificate
        """
        return pulumi.get(self, "cacert_file")

    @property
    @pulumi.getter(name="clientCertPath")
    def client_cert_path(self) -> pulumi.Output[Optional[str]]:
        """
        A X509 certificate to connect to OpenSearch
        """
        return pulumi.get(self, "client_cert_path")

    @property
    @pulumi.getter(name="clientKeyPath")
    def client_key_path(self) -> pulumi.Output[Optional[str]]:
        """
        A X509 key to connect to OpenSearch
        """
        return pulumi.get(self, "client_key_path")

    @property
    @pulumi.getter(name="hostOverride")
    def host_override(self) -> pulumi.Output[Optional[str]]:
        """
        If provided, sets the 'Host' header of requests and the 'ServerName' for certificate validation to this value. See the
        documentation on connecting to OpenSearch via an SSH tunnel.
        """
        return pulumi.get(self, "host_override")

    @property
    @pulumi.getter(name="opensearchVersion")
    def opensearch_version(self) -> pulumi.Output[Optional[str]]:
        """
        OpenSearch Version
        """
        return pulumi.get(self, "opensearch_version")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Password to use to connect to OpenSearch using basic auth
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional[str]]:
        """
        Proxy URL to use for requests to OpenSearch.
        """
        return pulumi.get(self, "proxy")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        A bearer token or ApiKey for an Authorization header, e.g. Active Directory API key.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="tokenName")
    def token_name(self) -> pulumi.Output[Optional[str]]:
        """
        The type of token, usually ApiKey or Bearer
        """
        return pulumi.get(self, "token_name")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        OpenSearch URL
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        """
        Username to use to connect to OpenSearch using basic auth
        """
        return pulumi.get(self, "username")

