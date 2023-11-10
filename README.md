# Happitu Super Awesome API

## Required tools
1. Postman
2. Python 3.9 or 3.10
3. Docker
4. AWS CLI

In this exercise, you'll be evaluated on your ability to use Git, Docker, ECS, and ALB. You must perform the following tasks:

1. Create a deployment branch
2. From said branch, create a docker image that will run the API that is already committed to this repo.
3. Upload the Docker image to ECR
4. Create a cluster, define a task using the image, and run the service. The service should be behind an ALB, and the deployment strategy can be a simple rolling update.

You have completed this exercise if all the health checks persist for 10 minutes.
