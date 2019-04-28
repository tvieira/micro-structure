(this is a WIP)

# Python Flask based micro-service structure

This project is my attempt to find a minimal, but complete, structure
to build efficient microservices with Python and Flask.

## Jaeger

```bash
$ docker run --rm -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp \
  -p5778:5778 -p16686:16686 -p14268:14268 -p9411:9411 jaegertracing/all-in-one:latest
```