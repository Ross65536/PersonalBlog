if [ -z "$1" ]
    then 
    echo "Please specify the .env file as command argument"
    exit 1
fi

set -o allexport
source $1
set +o allexport