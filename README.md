# CoviApp


# Docker build and Run

docker build -t "covid-flask" .
docker run -d -p 15000:5000 --name=covid-mono covid-flask
