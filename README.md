# Docker Webhook

[![Release](https://img.shields.io/github/actions/workflow/status/hadb/docker-webhook/release.yml)](https://github.com/hadb/docker-webhook/actions/workflows/release.yml)
[![GitHub Release](https://img.shields.io/github/v/release/hadb/docker-webhook)](https://github.com/hadb/docker-webhook/releases/latest)
[![Docker Image Size](https://img.shields.io/docker/image-size/hadb/docker-webhook)](https://hub.docker.com/r/hadb/docker-webhook)
[![License](https://img.shields.io/github/license/hadb/docker-webhook)](https://github.com/hadb/docker-webhook/blob/main/LICENSE)

A lightweight webhook server for redeploying docker containers.

Inspired by [adnanh/webhook](https://github.com/adnanh/webhook) which does not support docker officially.

# Getting started

## Installation

### Using docker command

```bash
docker run -d -p 8000:8000 --name docker-webhook \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/config.yaml:/etc/docker-webhook/config.yaml \
  -v /path/to/compose-files:/data/compose-files \
  hadb/docker-webhook
```

### Using docker compose

```yaml
name: docker-webhook
services:
  docker-webhook:
    container_name: docker-webhook
    image: docker-webhook
    restart: always
    network_mode: bridge
    ports:
      - 8000:8000
    volumes:
      - '/var/run/docker.sock:/var/run/docker.sock'
      - /path/to/config.yaml:/etc/docker-webhook/config.yaml
      - /path/to/compose-files:/data/compose-files
```

## Configuration

config.yaml:

```yaml
webhooks:
  - id: say-hello
    command: echo "Hello, world!"
  - id: docker-info
    command: docker info
  - id: redeploy-nginx-demo
    command: docker compose -f /data/compose-files/nginx-demo.yaml up -d --pull=always --force-recreate
```

## Testing

You can use the following url to trigger a webhook for test locally:

```http
http://127.0.0.1:8000/webhook/{webhook_id}
```

## Triggering from Docker Hub

It's recommended to use a reverse proxy like Nginx to expose the webhook service to the public.

Config new webhook on Docker Hub, set the `Webhook URL` to `https://{your_public_domain}/webhook/{webhook_id}`.

## Similar Projects

- [almir/docker-webhook](https://github.com/almir/docker-webhook)
- [staticfloat/docker-webhook](https://github.com/staticfloat/docker-webhook)
- [iaincollins/docker-deploy-webhook](https://github.com/iaincollins/docker-deploy-webhook)

## License

[MIT](https://github.com/hadb/docker-webhook/blob/main/LICENSE) License © 2024 [Bean Deng](https://github.com/HADB)
