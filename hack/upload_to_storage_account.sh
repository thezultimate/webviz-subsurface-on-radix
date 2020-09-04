#!/bin/bash

if [[ -z "$STORAGE_ACCOUNT_NAME" ]]; then
    echo "Please provide STORAGE_ACCOUNT_NAME" >&2
    exit 1
fi

if [[ -z "$CONTAINER_NAME" ]]; then
    echo "Please provide CONTAINER_NAME" >&2
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

echo "Copy generated data to storage account"
az storage blob upload-batch --account-name "${STORAGE_ACCOUNT_NAME}" -d "${CONTAINER_NAME}" -s "${SOURCE_FOLDER}" --auth-mode login --destination-path "${DESTINATION_FOLDER}"
