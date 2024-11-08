# soroban-rpc-docker-compose

## Check health

```
curl http://127.0.0.1:18779/health
```

```
curl --location 'http://127.0.0.1:18777' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "getHealth",
    "params": null
}'
```

## Get Latest Ledger

```
curl --location 'http://127.0.0.1:18777' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "id": "198cb1a8-9104-4446-a269-88bf000c2721",
    "method": "getHealth",
    "params": null
}'
```
