# Rest api service
It's a docker-compose multi-service.
See development sections if you want to test outside a container.
## Docker
- Create and run api and database: `docker-compose up -d --build`
- Check if services are up and running: `docker-compose ps`
- Check errors in sql service: `docker-compose logs sql-service`
- Check errors in app service: `docker-compose logs app-server`
- Put services down: `docker-compose down -v`

### Configuration
Configuration is inside .env files. 
- `docker.env`: configuration passed to docker-compose as a environment file
- `.env`: simple .env file loaded manually if outside container

---
## Sql service
It's a standard mysql image set up with a simple docker compose
The volume is mapped on general volumes so remove it before relaunching the instance.

### Development
Run only sql service with:
- `docker-compose up -d --build sql-service`

Delete container and volumes with:
- `docker-compose down -v`
## App service
The rest-api service

### Development
Service dependencies:
- `pip instal pymysql`
- `pip install sqlalchemy`
- `pip install flask`
- `pip install cryptography`
- `pip install python-dotenv`

Execute the app:
- `cd restapi`
- `python -m flask run`