FROM amazoncorretto:21.0.0-al2023-headless

WORKDIR /kafka

RUN wget https://www.apache.org/dyn/closer.cgi?path=/kafka/3.5.0/kafka_2.13-3.5.0.tgz
RUN tar -xzf kafka_2.13-3.5.0.tgz

WORKDIR ./kafka_2.13-3.5.0
COPY start-kafak.sh .

CMD start-kafka.sh
