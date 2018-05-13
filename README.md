# docker-things

#### Docker Command Line
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
