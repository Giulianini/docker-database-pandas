# Influx service
## NB
Backup is copied inside the image during creation -> mapped volumes are always very slow in throughput and a backup loading would cost 5 minutes.

**So, when you edit something in `docker-compose.yaml` or `Dockerfile` clear all the images created before with `docker down -v --rmi all`**