# docker-things


### Filter and grep docker container
* Example
```
$ nvidia-docker ps --filter "status=exited" --filter "since=determined_chatterjee" | awk '{print $1}' | xargs --no-run-if-empty nvidia-docker rm
```

### Docker Command Line
```
# Inspect contatiner 
$ docker inspect <container_id> | grep IPAddress

# Look at image history
$ docker history <image_name>:<tag>

# Create new image from running container
$ docker commit -a "SeoHyeonDeok <centrifugal4@gmail.com>" -m "Add messages about commit" <container_id> <image_name>:<tag>

# Check for changed files in container
# A: Added files, C: Changed files, D: Deleted files
$ docker diff <contatiner_id>
```

### Remove all containers and images
```
$ docker stop $(docker ps -a -q)
$ docker rm $(docker ps -a -q)
$ docker rmi $(docker images -q)
```
