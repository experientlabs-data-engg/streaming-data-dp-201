#!/bin/bash

# Configure Kafka for KRaft mode
echo "process.roles=broker,controller" >> ${KAFKA_HOME}/config/kraft/server.properties
echo "node.id=1" >> ${KAFKA_HOME}/config/kraft/server.properties
echo "controller.quorum.voters=1@localhost:9093" >> ${KAFKA_HOME}/config/kraft/server.properties
echo "listeners=PLAINTEXT://:9092,CONTROLLER://:9093" >> ${KAFKA_HOME}/config/kraft/server.properties
echo "advertised.listeners=PLAINTEXT://localhost:9092" >> ${KAFKA_HOME}/config/kraft/server.properties
echo "log.dirs=/var/lib/kafka/data" >> ${KAFKA_HOME}/config/kraft/server.properties

# Format the storage directory for KRaft
${KAFKA_HOME}/bin/kafka-storage.sh format -t $( ${KAFKA_HOME}/bin/kafka-storage.sh random-uuid ) -c ${KAFKA_HOME}/config/kraft/server.properties


# Start Kafka in KRaft mode
${KAFKA_HOME}/bin/kafka-server-start.sh ${KAFKA_HOME}/config/kraft/server.properties &

# Start Kafka UI
java -jar ${KAFKA_UI_JAR} --kafka.clusters.0.name=local --kafka.clusters.0.bootstrapServers=localhost:9092 &

# Start Python WebSocket emitter
python3 /app/websocket_message_generator.py &

# Start Kafka producer
python3 /app/kafka_producer.py &

# Start Kafka consumer
python3 /app/kafka_consumer.py &

# Keep the container running
tail -f /dev/null
