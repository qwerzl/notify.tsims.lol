FROM python
WORKDIR /app
COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN pip install poetry
RUN poetry install --no-dev

COPY . /app
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]