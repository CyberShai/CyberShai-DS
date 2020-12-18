# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

ENV APP_HOME /app
WORKDIR $APP_HOME

# Install manually all the missing libraries
RUN apt-get update

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy local code to the container image.
COPY . .

# Expose port
EXPOSE 8080

# Run the web service on container startup. 
CMD uvicorn --host=0.0.0.0 --port 8080 app.main:app