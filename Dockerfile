FROM public.ecr.aws/lambda/python:3.12

# Write Docker commands to package your Python application with its dependencies
# so that it can

# tips: a python 'requirements.txt' file to insall the Python dependencies with pip
# can be generated using 'poetry export --without-hashes > lambda_app/requirements.txt'
# before building the image with 'docker build ...'

COPY requirements.txt /var/task
# Copy function code
COPY src/app/app.py /var/task

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]