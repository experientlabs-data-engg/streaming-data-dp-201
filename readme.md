# Kafka Event Stream
This repo contains two sample applications demonstrating stream processing pipelines in its intricacies. 
1. Livewire is a real time synthetic event stream generator
2. click_flow is a ream time synthetic page_view and RTB auction log generator. 


Kafka UI: http://localhost:8081
MinIO Console: http://localhost:9001
Kafka Broker: localhost:9092 (Bootstrap Server)


create a directory minio/data in your project root and give it chmod -R 777 



> Ran into issue of local directory overwriting volume mapped directory. 
To avoid this, image layer should not contain any data. 
Or 


## From prject root directory run below command to build the Docker Image
docker build -t kafka-kraft-ui .

docker run -d \
  -p 9093:9092 \
  -p 8083:8080 \
  -p 8768:8765 \
  -v s3d_producer:/app/s3d_producer \
  --name kafka-kraft-ui1 \
  kafka-kraft-ui





ps aux | grep "python your_script.py"

kill <PID>

Need to cleanup kafka_data directory. 


sudo lsof -i :9001
sudo kill <PID>









---------------------------





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
  -v s3d_simulator/:/app \
  --name kafka-kraft-ui \
  kafka-kraft-ui
```