#!/bin/bash

if [[ -z "$STORAGE_CONNECTION_STRING" ]]; then
    echo "Please provide STORAGE_CONNECTION_STRING" >&2
    exit 1
fi

if [[ -z "$SOURCE_FOLDER" ]]; then
    echo "Please provide SOURCE_FOLDER" >&2
    exit 1
fi

if [[ -z "$DESTINATION_FOLDER" ]]; then
    echo "Please provide DESTINATION_FOLDER" >&2
    exit 1
fi

STORAGE_ACCOUNT_NAME="webvizonradix"
STORAGE_ACCOUNT="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
CONTAINER_NAME="webviz-data"

echo "Copy generated data to storage account"
az storage blob upload-batch -d "${CONTAINER_NAME}" -s "${SOURCE_FOLDER}" --connection-string "${STORAGE_CONNECTION_STRING}" --destination "${DESTINATION_FOLDER}"
