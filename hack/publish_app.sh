#!/bin/bash

#######################################################################################
### The STORAGE_ACCOUNT_KEY is a secret used for accessing the storage account
### and should never be shared with anyone
###

if [[ -z "$STORAGE_ACCOUNT_KEY" ]]; then
    echo "Please provide STORAGE_ACCOUNT_KEY" >&2
    exit 1
fi

#######################################################################################
### Generates the app from webviz yaml config file. This requires access to
### raw resource files used by the reports
###

WORKDIR="./generated_app"
WEBVIZ_STORAGE="webviz_storage"
SOURCE_FOLDER="${WORKDIR}/${WEBVIZ_STORAGE}"
WEBVIZ_CONFIG="../webviz-subsurface-testdata/webviz_examples/webviz-full-demo.yml"

echo "Generate app"
rm -rf generated_app && webviz build "${WEBVIZ_CONFIG}" --theme equinor --portable "${WORKDIR}"

#######################################################################################
### Radix needs to be able to load aggregated files. Unless agregated files are small enough to
### be kept inside the built docker container image, the data needs to be separate from the
### container. In this case we are using the storage account
###

STORAGE_ACCOUNT_NAME="webvizonradix"
STORAGE_ACCOUNT="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
CONTAINER_NAME="js-webwiz-hm"

echo "Copy generated data to storage account"
az storage blob upload-batch -d "${CONTAINER_NAME}" -s "${SOURCE_FOLDER}" --account-name "${STORAGE_ACCOUNT_NAME}" --account-key "${STORAGE_ACCOUNT_KEY}" --destination-path "${WEBVIZ_STORAGE}"

#######################################################################################
### Modifying the generated assets
###

cp -rf ./generated_app/assets/ ./assets/
cp ./generated_app/.dockerignore ./.dockerignore
cp ./generated_app/theme_settings.json ./theme_settings.json
