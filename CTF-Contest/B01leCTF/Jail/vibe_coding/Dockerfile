FROM eclipse-temurin:17@sha256:1ebe50132ef974b48c850acf45f15be971b28d7a4d2c85849ceb26d782e74983 AS app

RUN apt-get update && apt-get install -y python3

FROM pwn.red/jail

COPY --from=app / /srv

COPY ./server.py /srv/app/run
COPY flag.txt /srv/flag.txt

RUN chmod 775 /srv/app/run

ENV JAIL_TIME=120 JAIL_MEM=100M JAIL_PORT=1337 JAIL_CPU=1000 JAIL_TMP_SIZE=10M JAIL_PIDS=35 \
    JAIL_ENV_PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
