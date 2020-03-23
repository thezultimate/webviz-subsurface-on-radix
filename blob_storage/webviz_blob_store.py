import os, uuid
import io
import glob
import shutil
import functools
import hashlib
import inspect
import pathlib
import os.path as path
from collections import defaultdict
from typing import Callable, List, Union, Any

import pandas as pd

from webviz_config.webviz_store import WebvizStorage
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class WebvizBlobStorage(WebvizStorage):
    def get_stored_data(
        self, func: Callable, *args: Any, **kwargs: Any
    ) -> Union[pd.DataFrame, pathlib.Path, io.BytesIO]:
        
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
        
        local_path = "webviz_storage"
        absolute_path = path.join(path.dirname(path.realpath(local_path)), local_path)

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        argspec = inspect.getfullargspec(func)
        for arg_name, arg in zip(argspec.args, args):
            kwargs[arg_name] = arg

        WebvizStorage.complete_kwargs(func, kwargs)
        return_type = inspect.getfullargspec(func).annotations["return"]

        hashed_args = hashlib.sha256(repr(WebvizStorage._dict_to_tuples(kwargs)).encode()).hexdigest()
        filename = f"{func.__module__}-{func.__name__}-{hashed_args}"

        if return_type == pathlib.Path:
            output = func(**kwargs)
            filename = f"{func.__module__}-{func.__name__}-{hashed_args}{output.suffix}"
        if return_type == pd.DataFrame:
            filename = f"{func.__module__}-{func.__name__}-{hashed_args}.parquet"

        download_file_path = os.path.join(absolute_path, filename)
        print("\nDownloading blob to \n\t" + download_file_path)

        blob_client = blob_service_client.get_blob_client(container_name, filename)
        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

        try:
            if return_type == pd.DataFrame:
                return pd.read_parquet(f"{download_file_path}")
            if return_type == pathlib.Path:
                return pathlib.Path(glob.glob(f"{download_file_path}*")[0])
            if return_type == io.BytesIO:
                return io.BytesIO(pathlib.Path(download_file_path).read_bytes())
            raise ValueError(f"Unknown return type {return_type}")

        except OSError:
            raise OSError(
                f"Could not find file {download_file_path}, which should be the "
                "stored output of the function call "
                f"{WebvizStorage.string(func, kwargs)}."
            )

WEBVIZ_BLOB_STORAGE = WebvizBlobStorage()