docker build --build-arg SECRET_KEY=$SECRET_KEY --build-arg ALLOWED_HOSTS_LIST="$ALLOWED_HOSTS_LIST" . -t $DOCKER_TAG_NAME $@