FROM node:12.18.2-alpine3.11 as build-frontend

WORKDIR /app

COPY  package.json yarn.lock ./
RUN yarn --ignore-optional --network-timeout 300000 --frozen-lockfile

COPY ./frontend ./frontend
RUN yarn build

FROM python:3.7.8 as build-backend
ENV PYTHONUNBUFFERED=1 POETRY_VERSION=1.1.4

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN pip3 install --no-cache-dir --upgrade pip uwsgi && \
    poetry config virtualenvs.create false && poetry install --no-interaction && \
    rm -rf /root/.cache/

COPY ./backend/ /app/backend/
COPY --from=build-frontend /app/frontend/dist/ /app/frontend/dist/
COPY Makefile /app/

WORKDIR /app/backend/

RUN SECRET_KEY=fake python ./manage.py collectstatic --no-input

EXPOSE 9000
ENTRYPOINT []
CMD ["uwsgi", "/app/backend/uwsgi.ini"]