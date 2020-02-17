FROM webviz/base_image:latest
RUN pip install --no-cache-dir redis

COPY --chown=appuser . dash_app
RUN mv ./dash_app/gunicorn_conf.py ./gunicorn_conf.py

CMD gunicorn \
    --config="./gunicorn_conf.py" \
    "dash_app.webviz_app:server"