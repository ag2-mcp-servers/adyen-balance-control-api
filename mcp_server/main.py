# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T08:59:40+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity, HTTPBasic

from models import BalanceTransferRequest, BalanceTransferResponse

app = MCPProxy(
    contact={
        'email': 'developer-experience@adyen.com',
        'name': 'Adyen Developer Experience team',
        'url': 'https://www.adyen.help/hc/en-us/community/topics',
        'x-twitter': 'Adyen',
    },
    description='The Balance Control API lets you transfer funds between merchant accounts that belong to the same legal entity and are under the same company account.\n\n## Authentication\nTo connect to the Balance Control API, you must authenticate your requests with an [API key or basic auth username and password](https://docs.adyen.com/development-resources/api-authentication). To learn how you can generate these, see [API credentials](https://docs.adyen.com/development-resources/api-credentials).Here is an example of authenticating a request with an API key:\n\n```\ncurl\n-H "X-API-Key: Your_API_key" \\\n-H "Content-Type: application/json" \\\n...\n```\nNote that when going live, you need to generate API credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).\n\n## Versioning\nThe Balance Control API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.\n\nFor example:\n\n```\nhttps://pal-test.adyen.com/pal/servlet/BalanceControl/v1/balanceTransfer\n```\n',
    termsOfService='https://www.adyen.com/legal/terms-and-conditions',
    title='Adyen Balance Control API',
    version='1',
    servers=[{'url': 'https://pal-test.adyen.com/pal/servlet/BalanceControl/v1'}],
)


@app.post(
    '/balanceTransfer',
    description=""" Starts a balance transfer request between merchant accounts. The following conditions must be met before you can successfully transfer balances:

* The source and destination merchant accounts must be under the same company account and legal entity.

* The source merchant account must have sufficient funds.

* The source and destination merchant accounts must have at least one common processing currency.

When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel.
 """,
    tags=['balance_transfer_management'],
    security=[
        HTTPBasic(name="None"),
        APIKeyHeader(name="X-API-Key"),
    ],
)
def post_balance_transfer(body: BalanceTransferRequest = None):
    """
    Start a balance transfer
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
