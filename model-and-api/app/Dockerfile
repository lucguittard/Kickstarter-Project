# Start with a base image
FROM python:3-onbuild

# Copy our application code
WORKDIR /var/app
COPY . .
COPY requirements.txt .

# Fetch app specific dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Start the app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]


# Inside of app/ directory, run:
#  $ docker build -t <your-dockerhub-username>/model_api .
#  $ docker run -p 5000:5000 lsguittard/model_api

# Repeating the request below should yield same output as that from Flask:
#  $ curl -X GET "http://0.0.0.0:5000/api" -H "Content-Type: application/json" --data '{"backers_count":"500", "goal":"1000", "spotlight":"0", "staff_pick":"1"}'

# Finally, push the image to Docker Hub account:
#  $ docker push <your-dockerhub-username>/model_api

# Pushing the image is useful when deploying to AWS Elastic Beanstalk

# Can now go to AWS BeanStalk for app setup -> will be uploading
#  the Dockerrun.aws.json file there
# After deployment, can access your app via the URL/API given on-screen

# Can then repeat once more the below request and get the same outputs as with Flask and Docker:
# $ curl -X GET "http://<insert your api-URL here>/api" -H "Content-Type: application/json" --data '{"backers_count":"500", "goal":"1000", "spotlight":"0", "staff_pick":"1"}'