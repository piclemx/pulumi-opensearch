---
title: Opensearch Installation & Configuration
meta_desc: Information on how to install the Opensearch provider.
layout: installation
---

## Installation

The Pulumi Opensearch provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@piclemx/pulumi-opensearch`](https://www.npmjs.com/package/@piclemx/pulumi-opensearch)
* Python: [`piclemx_pulumi_opensearch`](https://pypi.org/project/piclemx_pulumi_opensearch/)
* Go: [`github.com/piclemx/pulumi-opensearch/sdk/go/opensearch`](https://pkg.go.dev/github.com/piclemx/pulumi-opensearch/sdk/go/opensearch)
* .NET: [`Piclemx.Opensearch`](https://www.nuget.org/packages/Piclemx.Opensearch)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `opensearch` provider:

- `opensearch:apiKey` (environment: `opensearch_API_KEY`) - the API key for `opensearch`
- `opensearch:region` (environment: `opensearch_REGION`) - the region in which to deploy resources

### Provider Binary

The Opensearch provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource opensearch <version>
```

Replace the version string `<version>` with your desired version.
