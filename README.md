
Before running please set correct env vars in docker compose 

run: 

    docker-compose build . ???
    docker exec test3microservices_user_microservice_1 alembic upgrade heads

docs: 

    http://127.0.0.1:1337/notification/docs
    http://127.0.0.1:1337/user/docs