FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Move pipfiles to project.
ADD Pipfile Pipfile.lock ./

RUN pip install -U pip pipenv

RUN pipenv install --system --deploy

RUN mkdir /app
COPY . /src/
WORKDIR /src

# Create empty env-file to avoid warnings
# RUN touch ./apps/config/.env

CMD ["uvicorn", "main:app", "--reload"]
