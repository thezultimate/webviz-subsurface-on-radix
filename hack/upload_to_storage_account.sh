#!/bin/bash

if [[ -z "$STORAGE_ACCOUNT_KEY" ]]; then
    echo "Please provide STORAGE_ACCOUNT_KEY" >&2
    exit 1
fi

if [[ -z "$SOURCE_FOLDER" ]]; then
    echo "Please provide SOURCE_FOLDER" >&2
    exit 1
fi

STORAGE_ACCOUNT_NAME="webvizonradix"
STORAGE_ACCOUNT="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
CONTAINER_NAME="webviz-data"

echo "Copy generated data to storage account"
az storage blob upload-batch -d "${CONTAINER_NAME}" -s "${SOURCE_FOLDER}" --account-name "${STORAGE_ACCOUNT_NAME}" --account-key "${STORAGE_ACCOUNT_KEY}" --destination "test"
