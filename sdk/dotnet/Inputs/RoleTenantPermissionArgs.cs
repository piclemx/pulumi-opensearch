// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Piclemx.Opensearch.Inputs
{

    public sealed class RoleTenantPermissionArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedActions")]
        private InputList<string>? _allowedActions;

        /// <summary>
        /// A list of allowed actions.
        /// </summary>
        public InputList<string> AllowedActions
        {
            get => _allowedActions ?? (_allowedActions = new InputList<string>());
            set => _allowedActions = value;
        }

        [Input("tenantPatterns")]
        private InputList<string>? _tenantPatterns;

        /// <summary>
        /// A list of glob patterns for the tenant names
        /// </summary>
        public InputList<string> TenantPatterns
        {
            get => _tenantPatterns ?? (_tenantPatterns = new InputList<string>());
            set => _tenantPatterns = value;
        }

        public RoleTenantPermissionArgs()
        {
        }
        public static new RoleTenantPermissionArgs Empty => new RoleTenantPermissionArgs();
    }
}
