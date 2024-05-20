start with command
```
docker compose up --watch
```

copy the public url in cloudflared log
```
cloudflared-1  | 2024-05-20T21:48:20Z INF +--------------------------------------------------------------------------------------------+
cloudflared-1  | 2024-05-20T21:48:20Z INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
cloudflared-1  | 2024-05-20T21:48:20Z INF |  https://josh-cheats-nick-pro.trycloudflare.com                                            |
cloudflared-1  | 2024-05-20T21:48:20Z INF +--------------------------------------------------------------------------------------------+
cloudflared-1  | 2024-05-20T21:48:20Z INF Cannot determine default configuration path. No file [config.yml config.yaml] in [~/.cloudflared ~/.cloudflare-warp ~/cloudflare-warp /etc/cloudflared /usr/local/etc/cloudflared]
```

test with curl
```
curl -XPOST -H 'Content-Type: application/json' https://josh-cheats-nick-pro.trycloudflare.com -d '{"foo":"bar"}'
```

request body are logged in flask stderr
```
app-1 exited with code 0
app-1          |  * Debug mode: off
app-1          | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
app-1          |  * Running on all addresses (0.0.0.0)
app-1          |  * Running on http://127.0.0.1:5000
app-1          |  * Running on http://172.20.0.3:5000
app-1          | Press CTRL+C to quit
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:04] "POST / HTTP/1.1" 200 -
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:06] "POST / HTTP/1.1" 200 -
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:08] "POST / HTTP/1.1" 200 -
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:09] "POST / HTTP/1.1" 200 -
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:10] "POST / HTTP/1.1" 200 -
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:10] "POST / HTTP/1.1" 200 -
app-1          | {'foo': 'bar'}
app-1          | 172.20.0.2 - - [20/May/2024 21:57:11] "POST / HTTP/1.1" 200 -
```