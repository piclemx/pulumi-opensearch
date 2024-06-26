// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface AuditConfigAudit {
    disabledRestCategories?: pulumi.Input<pulumi.Input<string>[]>;
    disabledTransportCategories?: pulumi.Input<pulumi.Input<string>[]>;
    enableRest?: pulumi.Input<boolean>;
    enableTransport?: pulumi.Input<boolean>;
    excludeSensitiveHeaders?: pulumi.Input<boolean>;
    ignoreRequests?: pulumi.Input<pulumi.Input<string>[]>;
    ignoreUsers?: pulumi.Input<pulumi.Input<string>[]>;
    logRequestBody?: pulumi.Input<boolean>;
    resolveBulkRequests?: pulumi.Input<boolean>;
    resolveIndices?: pulumi.Input<boolean>;
}

export interface AuditConfigCompliance {
    enabled?: pulumi.Input<boolean>;
    externalConfig?: pulumi.Input<boolean>;
    internalConfig?: pulumi.Input<boolean>;
    readIgnoreUsers?: pulumi.Input<pulumi.Input<string>[]>;
    readMetadataOnly?: pulumi.Input<boolean>;
    readWatchedFields?: pulumi.Input<pulumi.Input<inputs.AuditConfigComplianceReadWatchedField>[]>;
    writeIgnoreUsers?: pulumi.Input<pulumi.Input<string>[]>;
    writeLogDiffs?: pulumi.Input<boolean>;
    writeMetadataOnly?: pulumi.Input<boolean>;
    writeWatchedIndices?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface AuditConfigComplianceReadWatchedField {
    fields: pulumi.Input<pulumi.Input<string>[]>;
    index: pulumi.Input<string>;
}

export interface RoleIndexPermission {
    /**
     * A list of allowed actions.
     */
    allowedActions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A selector for document-level security (json formatted using jsonencode).
     */
    documentLevelSecurity?: pulumi.Input<string>;
    /**
     * A list of selectors for field-level security.
     */
    fieldLevelSecurities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of glob patterns for the index names.
     */
    indexPatterns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of masked fields
     */
    maskedFields?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface RoleTenantPermission {
    /**
     * A list of allowed actions.
     */
    allowedActions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of glob patterns for the tenant names
     */
    tenantPatterns?: pulumi.Input<pulumi.Input<string>[]>;
}
