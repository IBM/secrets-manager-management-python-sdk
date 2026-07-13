# IBM Cloud Secrets Manager Management Python SDK
A Python client library to interact with the IBM Cloud® Secrets Manager Instance Management APIs.

> **Important:** This SDK is for use with instances of the IBM Cloud Secrets Manager **Vault Enterprise plan only**. It is not compatible with other Secrets Manager plans.

<details>
<summary>Table of Contents</summary>

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Authentication](#authentication)
* [Using the SDK](#using-the-sdk)
* [Issues](#issues)
* [Contributing](#contributing)
* [License](#license)

</details>

## Overview
The IBM Cloud Secrets Manager Management Python SDK allows developers to programmatically interact with the following IBM Cloud services:

| Service name                              | Imported class name                     |
|-------------------------------------------|-----------------------------------------|
| Secrets Manager Management | SecretsManagerInstanceManagementV2 |

## Prerequisites
- An [IBM Cloud account](https://cloud.ibm.com/registration).
- A [Secrets Manager service instance](https://cloud.ibm.com/catalog/services/secrets-manager) with the **Vault Enterprise plan**.
- An [IBM Cloud API key](https://cloud.ibm.com/iam/apikeys) that allows the SDK to access your account.
- Python 3.9 or above.

## Installation
To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-secrets-manager-instance-management-sdk"
```

or

```bash
easy_install --upgrade "ibm-secrets-manager-instance-management-sdk"
```

## Authentication
Secrets Manager uses token-based Identity and Access Management (IAM) authentication.

With IAM authentication, you supply an API key that is used to generate an access token. Then, the access token is included in each API request to Secrets Manager. Access tokens are valid for a limited amount of time and must be regenerated.
Authentication for this SDK is accomplished by using [IAM authenticators](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md#authentication). Import authenticators from `ibm_cloud_sdk_core.authenticators`.

### Examples
#### Programmatic credentials

```python
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator

secretsManagerInstanceManagement = SecretsManagerInstanceManagementV2(
    authenticator=IAMAuthenticator(apikey='<IBM_CLOUD_API_KEY>')
)
```

To learn more about IAM authenticators and how to use them in your Python application, see the [IBM Python SDK Core documentation](https://github.com/IBM/python-sdk-core/blob/master/Authentication.md).

## Using the SDK

### Basic usage

- Use the `set_service_url` method to set the endpoint URL that is specific to your Secrets Manager service instance. To find your endpoint URL, you can copy it from the **Endpoints** section on the **Overview** page in the Secrets Manager UI.

#### Examples

Construct a service client and use it to generate an admin token and get instance details.

Here's an example `secrets_manager_instance_management.py` file:

```python
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
from ibm_secrets_manager_instance_management_sdk.secrets_manager_instance_management_v2 import *

secretsManagerInstanceManagement = SecretsManagerInstanceManagementV2(
    authenticator=IAMAuthenticator(apikey='<IBM_CLOUD_API_KEY>')
)

secretsManagerInstanceManagement.set_service_url('<SERVICE_URL>')

# Generate admin token
response = secretsManagerInstanceManagement.admin_token_generate(
    instance_crn='<INSTANCE_CRN>'
)

print('Admin token generated!')

# Get instance details
response = secretsManagerInstanceManagement.instance_details(
    instance_crn='<INSTANCE_CRN>'
)

print('Instance details:')
print(response.result)
```

Replace the `apikey`, `SERVICE_URL`, and `INSTANCE_CRN` values. Then use the `python secrets_manager_instance_management.py` command to run your
application.

For more information and IBM Cloud SDK usage examples for Python, see
the [IBM Cloud SDK Common documentation](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md).

## Issues

If you encounter an issue with the project, you're welcome to submit
a [bug report](https://github.com/IBM/secrets-manager-management-python-sdk/issues) to help us improve.

## Contributing

For general contribution guidelines, see [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK project is released under the Apache 2.0 license. The license's full text can be found in [LICENSE](LICENSE).
