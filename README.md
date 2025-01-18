# wol_api_docker
HTTP server for WOL using an API key.

I've set up this little project to work with my Moonlight fork (coming soon) so that I can wake up my PC outside my local network, directly from the application and transparently.


To build the Docker image: 
```
docker build -t wake-on-lan-app .
```

To run the container:
```
docker run -d -p 8080:8080 -e API_KEY=your_secret_key -e MAC_ADDRESS=XX:XX:XX:XX:XX wake-on-lan-app
```
If you use Docker Compose:
```
docker-compose up --build
```

To wake up the computer:

```
curl -X POST http://<votre_ip>:8080/wake \
-H "Content-Type: application/json" \
-d '{"key":"your_secret_key"}'
```

⚠️ This solution is sufficiently secure for my purposes. If you want even greater security, solutions like https://github.com/andygrundman/tailscale-wakeonlan are available.
