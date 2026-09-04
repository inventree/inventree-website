---
author: SchrodingersGat
title: InvenTree MCP Plugin
---

The InvenTree development team is excited to introduce [InvenTreeMCP](https://github.com/inventree/inventree-mcp), a new plugin which exposes your InvenTree inventory data to AI agents and other MCP-aware applications via the [Model Context Protocol](https://modelcontextprotocol.io) (MCP).

### What is it for?

MCP is an open standard which allows AI assistants - such as Claude - to interact with external tools and data sources in a structured way. InvenTreeMCP implements an MCP server as an InvenTree plugin, allowing any MCP client to query your InvenTree instance directly, over a Streamable HTTP endpoint.

This means you can ask an AI assistant questions about your inventory - stock levels, open orders, BOM structures, and more - and have it query your live InvenTree data to provide an answer, without needing to write any custom integration code.

Under the hood, InvenTreeMCP is implemented as a thin layer on top of the existing InvenTree API. Every request made by an MCP client passes through the same permission checks and filtering as a normal API call, so users only ever see the data they are already allowed to access.

### What tools does it expose?

InvenTreeMCP currently exposes read access to the core InvenTree data model, including:

- Parts and part categories
- Stock items and stock locations
- Purchase, sales, return and build orders (and their line items)
- Companies and contacts
- Manufacturer and supplier parts
- Bill of materials (BOM) items
- Attachments and parameters
- Stock tracking history and test results
- Project codes

Tool schemas and available filters are generated automatically from InvenTree's existing API serializers, so the tools exposed to MCP clients stay in sync with the underlying data model as InvenTree evolves.

### How can it be used?

InvenTreeMCP can be installed like any other InvenTree plugin:

1. Install the plugin, e.g. via pip: `pip install inventree-mcp`
2. Enable the plugin under *Admin > Plugins*
3. Generate an API token in InvenTree for your MCP client to use

Once installed and enabled, the MCP server is available at a URL such as `https://<your-inventree-server>/plugin/inventree-mcp/mcp/`. Most MCP clients which support remote (Streamable HTTP) servers can be pointed directly at this endpoint, authenticating with an InvenTree API token, e.g.:

```json
{
  "mcpServers": {
    "inventree": {
      "url": "https://<your-inventree-server>/plugin/inventree-mcp/mcp/",
      "headers": {
        "Authorization": "Token <your-api-token>"
      }
    }
  }
}
```

For clients which only support local (stdio) MCP servers, the [`mcp-remote`](https://github.com/geelen/mcp-remote) bridge can be used to connect to the same endpoint.

In addition to API tokens, the plugin also supports authentication via username/password, or OAuth2 bearer tokens with optional scope restrictions - useful if you want to issue narrowly-scoped credentials to a particular agent.

By default, the plugin runs in *read only* mode, which blocks any write operations regardless of the permissions of the authenticating user. This is a sensible default while you get a feel for how your AI tooling of choice interacts with your InvenTree data.

### Feedback Welcome

InvenTreeMCP is a brand new plugin, and this is very much a first step towards richer AI integration with InvenTree. We would love to hear how you're using it, and what's working (or not working) for your setup.

If you run into any bugs, or have trouble with installation or configuration, please [open an issue](https://github.com/inventree/inventree-mcp/issues) on the GitHub repository.

If there are additional tools or data types you'd like to see exposed via MCP, we'd also love to hear your suggestions - feel free to raise a feature request on the same [issue tracker](https://github.com/inventree/inventree-mcp/issues).
