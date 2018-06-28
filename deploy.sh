if [ -z "$1" ]
    then 
    echo "Specify a .env file location"
    exit 1
fi

source dotenv.sh $1
docker pull $DOCKER_TAG_NAME
docker-compose stop && docker-compose up -d
unset ADMIN_PASS
unset ADMIN_EMAIL