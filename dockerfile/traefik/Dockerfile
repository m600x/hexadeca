FROM rbekker87/armhf-alpine:3.8

ENV TRAEFIK_VERSION 1.7.10
ENV ARCH arm64

ADD https://github.com/containous/traefik/releases/download/v${TRAEFIK_VERSION}/traefik_linux-${ARCH} /traefik

RUN apk add --no-cache ca-certificates && chmod +x /traefik && rm -rf /var/cache/apk/*

EXPOSE 80 8080 443

ENTRYPOINT ["/traefik"]
