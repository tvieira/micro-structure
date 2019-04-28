# Copyright 2019 Tiago M. Vieira <tiago@tvieira.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
COPY src /opt/microservices

WORKDIR /opt/microservices/
EXPOSE 9080
CMD gunicorn --bind 0.0.0.0:9080 -w 2 -t 30 -k gevent --access-logfile - --error-logfile - wsgi:app
