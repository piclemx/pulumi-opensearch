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

    public sealed class AuditConfigComplianceGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("externalConfig")]
        public Input<bool>? ExternalConfig { get; set; }

        [Input("internalConfig")]
        public Input<bool>? InternalConfig { get; set; }

        [Input("readIgnoreUsers")]
        private InputList<string>? _readIgnoreUsers;
        public InputList<string> ReadIgnoreUsers
        {
            get => _readIgnoreUsers ?? (_readIgnoreUsers = new InputList<string>());
            set => _readIgnoreUsers = value;
        }

        [Input("readMetadataOnly")]
        public Input<bool>? ReadMetadataOnly { get; set; }

        [Input("readWatchedFields")]
        private InputList<Inputs.AuditConfigComplianceReadWatchedFieldGetArgs>? _readWatchedFields;
        public InputList<Inputs.AuditConfigComplianceReadWatchedFieldGetArgs> ReadWatchedFields
        {
            get => _readWatchedFields ?? (_readWatchedFields = new InputList<Inputs.AuditConfigComplianceReadWatchedFieldGetArgs>());
            set => _readWatchedFields = value;
        }

        [Input("writeIgnoreUsers")]
        private InputList<string>? _writeIgnoreUsers;
        public InputList<string> WriteIgnoreUsers
        {
            get => _writeIgnoreUsers ?? (_writeIgnoreUsers = new InputList<string>());
            set => _writeIgnoreUsers = value;
        }

        [Input("writeLogDiffs")]
        public Input<bool>? WriteLogDiffs { get; set; }

        [Input("writeMetadataOnly")]
        public Input<bool>? WriteMetadataOnly { get; set; }

        [Input("writeWatchedIndices")]
        private InputList<string>? _writeWatchedIndices;
        public InputList<string> WriteWatchedIndices
        {
            get => _writeWatchedIndices ?? (_writeWatchedIndices = new InputList<string>());
            set => _writeWatchedIndices = value;
        }

        public AuditConfigComplianceGetArgs()
        {
        }
        public static new AuditConfigComplianceGetArgs Empty => new AuditConfigComplianceGetArgs();
    }
}
