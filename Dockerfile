FROM python:3.7-alpine as base
FROM base as builder

COPY requirements.txt /requirements.txt
RUN apk add --no-cache \
    python-dev build-base \
    && pip install --no-cache-dir --install-option="--prefix=/install" -r /requirements.txt \
    && apk del python-dev build-base \
    && rm -rf /var/cache/apk/* /root/.cache /tmp/*

FROM base
COPY --from=builder /install /usr/local
COPY src /opt/msvc

WORKDIR /opt/msvc/
EXPOSE 9080
CMD gunicorn --bind 0.0.0.0:9080 -w 2 -t 30 -k gevent --access-logfile - --error-logfile - wsgi:app
