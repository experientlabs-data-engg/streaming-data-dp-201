# Use a base image with Java pre-installed
FROM eclipse-temurin:17-jre

# Set environment variables
ARG KAFKA_VERSION=3.9.0
ENV KAFKA_VERSION=${KAFKA_VERSION}
ENV KAFKA_UI_VERSION=0.7.2
ENV KAFKA_HOME=/home/kafka
ENV KAFKA_UI_HOME=/home/kafka-ui
ENV KAFKA_UI_JAR=/home/kafka-ui/kafka-ui.jar
ENV VENV_PATH=/home/kafkauser/environments

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    sudo \
    git

# Create a user and group
ARG USERNAME=kafkauser
ARG USER_UID=1001
ARG USER_GID=1001

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Download and extract Kafka
#RUN wget https://dlcdn.apache.org/kafka/${KAFKA_VERSION}/kafka_2.13-${KAFKA_VERSION}.tgz -O /tmp/kafka.tgz && \
#    tar -xzf /tmp/kafka.tgz -C /opt && \
#    mv /opt/kafka_2.13-${KAFKA_VERSION} ${KAFKA_HOME} && \
#    rm /tmp/kafka.tgz

# Copy and extract Kafka tar
COPY downloads/kafka_2.13-3.9.0.tgz /tmp/kafka.tgz
RUN ls -lh /tmp/kafka.tgz
RUN tar --version
RUN tar -xzf /tmp/kafka.tgz -C /opt && \
    mv /opt/kafka_2.13-${KAFKA_VERSION} ${KAFKA_HOME} && \
    rm /tmp/kafka.tgz

# Set ownership for Kafka directories
RUN chown -R $USER_UID:$USER_GID ${KAFKA_HOME}

# Download Kafka UI JAR file
#RUN mkdir -p ${KAFKA_UI_HOME} && \
#    wget https://github.com/provectus/kafka-ui/releases/download/v${KAFKA_UI_VERSION}/kafka-ui-api-v${KAFKA_UI_VERSION}.jar -O ${KAFKA_UI_JAR} && \
#    chown -R $USER_UID:$USER_GID $KAFKA_UI_HOME

# Copy and extract Kafka tar
COPY downloads/kafka-ui-api-v0.7.2.jar ${KAFKA_UI_JAR}
RUN chown -R $USER_UID:$USER_GID $KAFKA_UI_HOME



RUN mkdir -p /var/lib/kafka/data && \
  chown -R $USER_UID:$USER_GID /var/lib/kafka/data

## Download and install Nessie
#RUN mkdir -p /nessie && \
#    cd /nessie && \
#    curl -L -o nessie-server.tar.gz https://github.com/projectnessie/nessie/releases/download/nessie-0.60.0/nessie-quarkus-0.60.0-runner.tar.gz && \
#    tar -xzf nessie-server.tar.gz && \
#    rm nessie-server.tar.gz

# Create a virtual environment and install dependencies
RUN python3 -m venv $VENV_PATH/kafka_venv && \
    $VENV_PATH/kafka_venv/bin/pip install --upgrade pip && \
    $VENV_PATH/kafka_venv/bin/pip install poetry
COPY s3d_producer/pyproject.toml /home/kafkauser/app/pyproject.toml

# Set the working directory
WORKDIR /home/kafkauser/app
RUN $VENV_PATH/kafka_venv/bin/poetry install --no-root

# Set ownership for the virtual environment
RUN chown -R $USER_UID:$USER_GID ${VENV_PATH}

# Expose ports
EXPOSE 9092 8765 8080 19120

# Copy startup script
COPY scripts/start.sh /start.sh
RUN chmod +x /start.sh

# Set the entrypoint
ENTRYPOINT ["/start.sh"]

# Switch to the kafkauser
USER $USERNAME

