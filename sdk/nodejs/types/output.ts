// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface AuditConfigAudit {
    disabledRestCategories?: string[];
    disabledTransportCategories?: string[];
    enableRest?: boolean;
    enableTransport?: boolean;
    excludeSensitiveHeaders?: boolean;
    ignoreRequests?: string[];
    ignoreUsers?: string[];
    logRequestBody?: boolean;
    resolveBulkRequests?: boolean;
    resolveIndices?: boolean;
}

export interface AuditConfigCompliance {
    enabled?: boolean;
    externalConfig?: boolean;
    internalConfig?: boolean;
    readIgnoreUsers?: string[];
    readMetadataOnly?: boolean;
    readWatchedFields?: outputs.AuditConfigComplianceReadWatchedField[];
    writeIgnoreUsers?: string[];
    writeLogDiffs?: boolean;
    writeMetadataOnly?: boolean;
    writeWatchedIndices?: string[];
}

export interface AuditConfigComplianceReadWatchedField {
    fields: string[];
    index: string;
}

export interface RoleIndexPermission {
    /**
     * A list of allowed actions.
     */
    allowedActions?: string[];
    /**
     * A selector for document-level security (json formatted using jsonencode).
     */
    documentLevelSecurity?: string;
    /**
     * A list of selectors for field-level security.
     */
    fieldLevelSecurities?: string[];
    /**
     * A list of glob patterns for the index names.
     */
    indexPatterns?: string[];
    /**
     * A list of masked fields
     */
    maskedFields?: string[];
}

export interface RoleTenantPermission {
    /**
     * A list of allowed actions.
     */
    allowedActions?: string[];
    /**
     * A list of glob patterns for the tenant names
     */
    tenantPatterns?: string[];
}

