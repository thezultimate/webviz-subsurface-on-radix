FROM webviz/base_image:latest

COPY --chown=appuser . dash_app
RUN mv ./dash_app/hack/blob_storage/ ./dash_app/blob_storage && \
    mv ./dash_app/hack/gunicorn_conf.py ./gunicorn_conf.py && \
    mv ./dash_app/hack/setup.py ./dash_app/setup.py

RUN pip install dash_app/. && \
    pip install azure-storage-blob && \
    pip install pandas~=0.24 && \
    pip install webviz-subsurface --upgrade && \
    pip install libecl --upgrade

CMD gunicorn \
    --config="./gunicorn_conf.py" \
    "dash_app.webviz_app:server"