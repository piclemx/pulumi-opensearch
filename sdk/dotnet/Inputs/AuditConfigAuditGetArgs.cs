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

    public sealed class AuditConfigAuditGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("disabledRestCategories")]
        private InputList<string>? _disabledRestCategories;
        public InputList<string> DisabledRestCategories
        {
            get => _disabledRestCategories ?? (_disabledRestCategories = new InputList<string>());
            set => _disabledRestCategories = value;
        }

        [Input("disabledTransportCategories")]
        private InputList<string>? _disabledTransportCategories;
        public InputList<string> DisabledTransportCategories
        {
            get => _disabledTransportCategories ?? (_disabledTransportCategories = new InputList<string>());
            set => _disabledTransportCategories = value;
        }

        [Input("enableRest")]
        public Input<bool>? EnableRest { get; set; }

        [Input("enableTransport")]
        public Input<bool>? EnableTransport { get; set; }

        [Input("excludeSensitiveHeaders")]
        public Input<bool>? ExcludeSensitiveHeaders { get; set; }

        [Input("ignoreRequests")]
        private InputList<string>? _ignoreRequests;
        public InputList<string> IgnoreRequests
        {
            get => _ignoreRequests ?? (_ignoreRequests = new InputList<string>());
            set => _ignoreRequests = value;
        }

        [Input("ignoreUsers")]
        private InputList<string>? _ignoreUsers;
        public InputList<string> IgnoreUsers
        {
            get => _ignoreUsers ?? (_ignoreUsers = new InputList<string>());
            set => _ignoreUsers = value;
        }

        [Input("logRequestBody")]
        public Input<bool>? LogRequestBody { get; set; }

        [Input("resolveBulkRequests")]
        public Input<bool>? ResolveBulkRequests { get; set; }

        [Input("resolveIndices")]
        public Input<bool>? ResolveIndices { get; set; }

        public AuditConfigAuditGetArgs()
        {
        }
        public static new AuditConfigAuditGetArgs Empty => new AuditConfigAuditGetArgs();
    }
}
