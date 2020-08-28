FROM webviz/base_image:latest

COPY --chown=appuser . dash_app
RUN mv ./dash_app/gunicorn_conf.py ./gunicorn_conf.py

RUN pip install dash_app/.
RUN pip install azure-storage-blob
RUN pip install pandas~=0.24

RUN pip install -r requirements.txt
RUN pip install webviz-subsurface --upgrade
RUN pip install webviz-subsurface-components --upgrade
RUN pip install webviz-core-components --upgrade
RUN pip install ecl --upgrade
RUN pip install libecl --upgrade

CMD gunicorn \
    --config="./gunicorn_conf.py" \
    "dash_app.webviz_app:server"