FROM amazoncorretto:21-alpine3.18
RUN apk --update add bash openssl wget unzip && rm -rf /var/cache/apk/*

WORKDIR /kafka

RUN wget https://dlcdn.apache.org/kafka/3.5.0/kafka_2.13-3.5.0.tgz
RUN tar -xzf kafka_2.13-3.5.0.tgz

WORKDIR ./kafka_2.13-3.5.0
COPY start-kafka.sh .
COPY server.properties config/

CMD ["/bin/sh", "start-kafka.sh"]
