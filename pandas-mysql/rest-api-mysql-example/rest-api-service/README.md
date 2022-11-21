# Rest api service
It's a docker-compose multi-service.
## Sql service
It's a standard mysql image set up with a simple docker compose
The volume is mapped on general volumes so remove it before relaunching the instance.

### Development
Run only sql service with:
- `docker-compose up -d --build sql-service`

Delete container with:
- `docker-compose down -v`
## App service
The rest-api service

### Development
Service dependencies:
- `pip instal pymysql`
- `pip install sqlalchemy`
- `pip install flask`

Execute the app:
- `cd restapi`
- `python -m flask run`

## General Commands
- `docker-compose up -d --build`
- `docker-compose down -v`
- `docker-compose logs sql-service`