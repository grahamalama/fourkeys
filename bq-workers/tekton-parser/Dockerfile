FROM python:3.12 AS deps
COPY bq-workers.tekton-parser/binary.pex /binary.pex
RUN PEX_TOOLS=1 /usr/local/bin/python3.12 /binary.pex venv --scope=deps --compile /bin/app

FROM python:3.12 AS srcs
COPY bq-workers.tekton-parser/binary.pex /binary.pex
RUN PEX_TOOLS=1 /usr/local/bin/python3.12 /binary.pex venv --scope=srcs --compile /bin/app

FROM python:3.12-slim

ENV PYTHONUNBUFFERED True

COPY --from=deps /bin/app /bin/app
COPY --from=srcs /bin/app /bin/app
COPY common/gunicorn.conf.py /conf/gunicorn.conf.py

ENTRYPOINT ["/bin/app/pex"]