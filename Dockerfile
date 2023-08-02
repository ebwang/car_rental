FROM python:3.11.2
RUN mkdir -p /app/car_rental
COPY /car_rental /app/car_rental
COPY pyproject.toml /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root
CMD ["/usr/local/bin/uvicorn", "car_rental.api:api"]