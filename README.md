# Docker Webhook

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

## Trigger

### Trigger webhook locally for testing

You can use the following url trigger a webhook for test locally:

```http
http://127.0.0.1:8000/webhook/{webhook_id}
```

### Trigger webhook on Docker Hub

It's recommended to use a reverse proxy like Nginx to proxy the webhook server.

Config new webhook on Docker Hub, set the `Webhook URL` to `https://{your_public_domain}/webhook/{webhook_id}`.

## Similar Projects

- [almir/docker-webhook](https://github.com/almir/docker-webhook)
- [staticfloat/docker-webhook](https://github.com/staticfloat/docker-webhook)
- [iaincollins/docker-deploy-webhook](https://github.com/iaincollins/docker-deploy-webhook)
