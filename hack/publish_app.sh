#!/bin/bash

if [[ -z "$STORAGE_ACCOUNT_KEY" ]]; then
    echo "Please provide STORAGE_ACCOUNT_KEY" >&2
    exit 1
fi

WORKDIR="./generated_app"
WEBVIZ_STORAGE="webviz_storage"
SOURCE_FOLDER="${WORKDIR}/${WEBVIZ_STORAGE}"

echo "Generate app"
rm -rf generated_app && webviz build ../webviz-subsurface-testdata/webviz_examples/webviz-full-demo.yml --theme equinor --portable ./generated_app

STORAGE_ACCOUNT_NAME="webvizonradix"
STORAGE_ACCOUNT="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
CONTAINER_NAME="js-webwiz-hm"

echo "Copy generated data to storage account"
az storage blob upload-batch -d "${CONTAINER_NAME}" -s "${SOURCE_FOLDER}" --account-name "${STORAGE_ACCOUNT_NAME}" --account-key "${STORAGE_ACCOUNT_KEY}" --destination-path "${WEBVIZ_STORAGE}"

mv ./generated_app/assets/ ./assets
mv ./generated_app/.dockerignore ./.dockerignore
mv ./generated_app/theme_settings.json ./theme_settings.json
