#!/bin/bash

# Define the directories to clean
kafka_data="kafka_data"
mino_data="minio/data"

# Check the command-line argument
if [ "$1" == "start" ]; then
  # Clean the kafka data directory
  echo "Cleaning $kafka_data contents..."
  if [ -d "$kafka_data" ]; then
    echo "Keeping Kafka Data"
    find "$kafka_data" -mindepth 1 -delete
  else
    echo "$kafka_data does not exist. recreating and setting permissions"
    mkdir -p "$kafka_data"
    chmod -R 777 "$kafka_data"
  fi

  if [ $? -ne 0 ]; then
    echo "Error cleaning $kafka_data"
    exit 1
  fi
  # Clean mino data directory
  echo "Cleaning $mino_data..."
  if [ -d "$mino_data" ]; then
    rm -rf "$mino_data"
  else
    echo "$mino_data does not exist. recreating and setting permissions"
  fi
  mkdir -p "$mino_data"
  chmod -R 777 "$mino_data"

  if [ $? -ne 0 ]; then
    echo "Error cleaning/creating $mino_data"
    exit 1
  fi

  # Run docker-compose up -d
  echo "Starting Docker Compose..."
  DOCKER_HOST=unix:///home/sanjeet/.docker/desktop/docker.sock docker compose up -d --build
  if [ $? -ne 0 ]; then
    echo "Error starting Docker Compose"
    exit 1
  fi

  echo "Docker compose started"

elif [ "$1" == "down" ]; then
  # Run docker-compose down
  echo "Stopping Docker Compose..."
  DOCKER_HOST=unix:///home/sanjeet/.docker/desktop/docker.sock docker compose down
  if [ $? -ne 0 ]; then
    echo "Error stopping Docker Compose"
    exit 1
  fi
  echo "Docker compose stopped"
else
  echo "Usage: $0 {start|down}"
  exit 1
fi

exit 0