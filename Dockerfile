FROM webviz/base_image:latest

COPY --chown=appuser . dash_app
RUN mv ./dash_app/gunicorn_conf.py ./gunicorn_conf.py
RUN pip install dash_app/.
RUN pip install azure-storage-blob

CMD gunicorn \
    --config="./gunicorn_conf.py" \
    "dash_app.webviz_app:server"