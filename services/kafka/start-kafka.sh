#!/bin/sh

export KAFKA_ADVERTISED_LISTENERS="PLAINTEXT://$UDACONNECT_KAFKA_SERVICE_HOST:$UDACONNECT_KAFKA_SERVICE_PORT"

./bin/zookeeper-server-start.sh config/zookeeper.properties &
./bin/kafka-server-start.sh config/server.properties &

./bin/kafka-topics.sh --create --topic udaconnect-location --bootstrap-server localhost:9092

wait -n
exit $?

