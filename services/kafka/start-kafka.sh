#!/bin/sh

./bin/zookeeper-server-start.sh config/zookeeper.properties &
./bin/kafka-server-start.sh config/server.properties &

./bin/kafka-topics.sh --create --topic udaconnect-location --bootstrap-server localhost:9092

wait -n
exit $?

