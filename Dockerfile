#Start from the official Python base image.
FROM python:3.11

#release port 8080 so that it is available
EXPOSE 8080

#Set the current working directory to /code.
#This is where we'll put the requirements.txt file and the app directory.
WORKDIR app

#Copy only the file with the requirements first.
#As this file doesn't change often, Docker will detect it and use the cache for this step,
#enabling the cache for the next step too.
COPY requirements.txt requirements.txt

#Install the package dependencies in the requirements file.
RUN pip3 install -r requirements.txt

#Copy the ./app directory inside the /code directory.
COPY . /app

#Set the command to start the uvicorn server.
CMD ["uvicorn", "app.main:app","--host", "127.0.0.1", "--port", "8080"]
