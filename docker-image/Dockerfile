FROM python:2.7

ADD locust-tasks /locust-tasks
ADD run.sh .

# Install the required dependencies via pip
RUN pip install -r /locust-tasks/requirements.txt

# Expose the required Locust ports
EXPOSE 5557 5558 8089

# Set script to be executable
RUN chmod 755 run.sh

# Start Locust using LOCUS_OPTS environment variable
ENTRYPOINT ["bash", "./run.sh"]