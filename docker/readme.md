

### Build the Docker Image
```shell
docker build -t kafka-kraft-ui .
```

### Run the docker container
```shell
docker run -d -p 9092:9092 -p 8081:8080 --name kafka-kraft-ui kafka-kraft-ui
```

### Kafka and Kafka UI
- Kafka Broker: localhost:9092
- Kafka UI: http://localhost:8080


### URL's
- https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
- https://github.com/provectus/kafka-ui/releases/download/v0.7.2/kafka-ui-api-v0.7.2.jar


### Port 8080 was in use, we can reclaim it
```shell
# stop the process using port 8080:

sudo lsof -i :8080
sudo kill <PID>
```


java -jar /opt/kafka-ui/kafka-ui.jar



### Kafka 
```shell
# Create Kafka Topic
bin/kafka-topics.sh --create --topic websocket_s3d --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Check if topic created
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```


```shell
docker run -d \
  -p 9092:9092 \
  -p 8080:8080 \
  -p 8765:8765 \
  -v /path/to/your/python/programs:/app \
  --name kafka-kraft-ui \
  kafka-kraft-ui
```