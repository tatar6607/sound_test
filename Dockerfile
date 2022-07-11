FROM python:3.7.9

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./requirements.txt ./
# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --workers 1 --threads 8 --timeout 0 main:app
