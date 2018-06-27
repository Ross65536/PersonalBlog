

ssh root@$1 'mkdir -p /code/nginx'
ssh root@$1 'mkdir -p /code/uploads'
scp nginx/PersonalWebsite.conf root@$1:/code/nginx/PersonalWebsite.conf
scp docker-compose.yml root@$1:/code/docker-compose.yml
scp runtime.env root@$1:/code/runtime.env
