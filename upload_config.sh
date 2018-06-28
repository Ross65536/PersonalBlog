if [ -z "$1" ]
    then
    echo "Specify destination user and machine as command argument: <user>:<machine>"
    exit 1
fi

ssh $1 'mkdir -p /code/nginx'
ssh $1 'mkdir -p /code/uploads'
scp nginx/PersonalWebsite.conf $1:/code/nginx/PersonalWebsite.conf
scp docker-compose.yml $1:/code/docker-compose.yml
scp dotenv.sh $1:/code/dotenv.sh
scp default.env $1:/code/default.env
scp deploy.sh $1:/code/deploy.sh
