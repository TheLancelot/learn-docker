Docker is used to containerize applications, so that they run on any hardware

Container has all necessary components to run application. In prod we just need to take the container and deploy it on to server. no other hassle.

Main idea is reproducibility (if it runs on my system then should run on others system also)

Use docker becuase of portability,scalability, no worry about compatibility issues or hardware requirements.

Containers can be deployed on any OS, cloud etc. It is OS level virtualization.
Virtual machines each have thein own OS (more isolated), containers share the OS and resources.

else VM/containers each have their own app source code, libraries etc.
_________

components of docker

DockerFile- It is a blue print for builiding image, (every instruction is a layer, previous layers are cached when updated)

Images are made up of layers. When you make changes, you add a new layer instead of modifying the old one.
Image - template for running docker container, image made using dockerfile
```docker build -t <name>```

Container - it is the running process (runnable instance of image)
```docker run <image id/tag>```

Port Mapping/ forwarding: Containers are isolated, so you have to explicitly map ports. port of container is exposed not local. so we need to expose the one in  localhost

volumes- persistent storage that lives outside the container

docker-compose.yml for multiple container

_______________
general steps
1) write source code
2) write the docker file
3) build the image  $ docker build -t <images_name> .
4) can see image in docker desktop and cli
5) run a container with the image   $ docker run -p <host_port>:<container_port> <image_name>
6) stop container
_____________
pushing image to docker hub
1) login
2) create image
3) push to docker hub
4) anyone can now pull that image and run container