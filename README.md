# wol_api_docker
HTTP server for WOL using an API key.

To build the Docker image: docker build -t wake-on-lan-app .

To run the container: docker run -d -p 8080:8080 -e API_KEY=your_secret_key -e MAC_ADDRESS=XX:XX:XX:XX:XX wake-on-lan-app

If you use Docker Compose: docker-compose up --build
