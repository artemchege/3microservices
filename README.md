
Before running please set correct env vars in docker compose 

run: 

    docker-compose up -d --build

    # first run:
    docker exec test3microservices_user_microservice_1 alembic upgrade heads
    docker exec test3microservices_profile_microservice_1 alembic upgrade heads

docs: 

    http://127.0.0.1:1337/notification/docs
    http://127.0.0.1:1337/user/docs
    http://127.0.0.1:1337/profile/docs