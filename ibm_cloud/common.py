# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.

"""Common functionality for IBM Cloud SDK."""

def get_sdk_headers(service_name=None, service_version=None, operation_id=None):
    """Get SDK specific headers to be included in every API call."""
    return {
        'User-Agent': 'ibm-secrets-manager-vaas-sdk-python/0.0.1',
        'X-SDK-Analytics': f'service_name={service_name};service_version={service_version};operation_id={operation_id}'
    }
