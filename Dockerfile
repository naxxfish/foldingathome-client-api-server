FROM python:3.8
RUN pip install pipenv
ENV PROJECT_DIR /usr/local/src/app/
WORKDIR ${PROJECT_DIR}
COPY Pipfile* ${PROJECT_DIR}
RUN pipenv install --system --deploy
COPY . ${PROJECT_DIR}/
EXPOSE 8000
CMD pipenv run gunicorn --bind 0.0.0.0:8000 wsgi:app