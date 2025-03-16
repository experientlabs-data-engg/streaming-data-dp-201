# Kafka Event Stream
This repo contains two sample applications demonstrating stream processing pipelines in its intricacies. 
1. Livewire is a real time synthetic event stream generator
2. AdStream is a ream time synthetic page_view and RTB auction log generator. 


Kafka UI: http://localhost:8081
MinIO Console: http://localhost:9001
Kafka Broker: localhost:9092 (Bootstrap Server)


create a directory minio/data in your project root and give it chmod -R 777 



> Ran into issue of local directory overwriting volume mapped directory. 
To avoid this, image layer should not contain any data. 
Or 



ps aux | grep "python your_script.py"

kill <PID>

Need to cleanup kafka_data directory. 



