# soroban-rpc-docker-compose

This is the configuration file used by [sorobanrpc.com](https://sorobanrpc.com) for the quick deployment of the soroban-rpc service.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/lightsail-network/sorobanrpc-docker-compose.git
```

### 2. Add private network configuration (Optional)

This is to allow mutual access between nodes during multi-node deployment.

If you don't have a private network, please check `docker-compose.yml` and pay attention to the `TODO` comments.

```bash
cp env_example .env
nano .env
```

### 3. Start the service

```bash
make start
```

### 4. Check health

```bash
curl http://127.0.0.1:18779/health
```

### 5. Proxy configuration (Optional)

You can use any reverse proxy server you like; I am using Caddy, and the configuration file is in [caddy/Caddyfile](./caddy/Caddyfile). Please refer to [the official documentation](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy) for how to use it.
