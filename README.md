# Happitu Super Awesome API

## Required tools
- Postman
- Python 3.9 or 3.10
- Docker
- CLI
- Git

## The Exercise
   
In this exercise, you'll be evaluated on your ability to use Git, Docker, ECS, and ALB. You must perform the following tasks:

### Setup

1. Clone repo
2. Create a Python virtual command
3. Install dependencies

Confirm the project is running locally by hitting the test endpoint. 

```
POST http://localhost:8000/test

{
  target_number: 5
}
```

### Challenge 1: Find the closest number

Open exercise in `excersise/function.py`

Background: You have a list of integers and a target number. Your task is to find the number in the list that is closest to the target number.

Challenge: Write a function that takes a list of integers and a single integer target. The function should return the number that is closest to the target. 
If there are two numbers equally close, return the smaller one.

Constraints:

The list numbers will have at least one and no more than 100 integers.
Each integer in numbers will be between -1000 and 1000.
The target will be an integer between -1000 and 1000.

Example: 
```
numbers = [2, 5, 6, 7, 8, 8, 1]
target = 9
```

### Challenge 2: Build a project

This challenge aims to build and deploy the provided docker image to ECS. You will be provided credentials to an AWS account with an existing ECS cluster to deploy to. You have completed the exercise if all health checks persist for 5 minutes, and you can successfully hit the API through the load balancer.

Update the following service with the changes in Challenge 1:

```
Cluster: hap-assessment
Service: hap-assessment-service
```


🚨🚨🚨 **NOTE** that instances are using the Linux/ARM64 architecture, not Linux/x86_64.

Tasks:
1. Create a new repository in ECR
2. Create a new task definition that uses the image you just uploaded. 
		- *Note 1: the service is assigned a target and autoscaling group. The task should take that into account.*
		- *Note 2: the task name must be test*
3. Update the `hap-assessment-service` to run your new task
4. Validate that the service is running
5. Make a request to `http://hap-test-1644500963.us-east-2.elb.amazonaws.com/test` with the following payload:

```
{
    "target_number": 9
}
```

6. Revalidate that the service is running and healthy

