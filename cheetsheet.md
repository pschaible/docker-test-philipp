# Dockerfile for SSH-Container

> from: https://docs.docker.com/engine/examples/running_ssh_service/

```Dockerfile
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:THEPASSWORDYOUCREATED' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```

- `docker exec -it <MyContainer> bash`
  // hiermit kann man sich in den localen docker-container einloggen mit bash

- `passwd`
  // ändern des passwords

- `docker port test_sshd 22`
  // herausfinden welches port wurde auf des port 22 (standard für ssh) gemaped

- `ssh root@localhost -p <port>`
  // ssh als root into the container

- `docker image ls -q`
  // lists all immages

- `$(docker image ls -q)`
  if you need the list for e.g. delete all

- `echo username:newpassword | chpasswd`
  // change password of a container from the beginning.

- `docker system prune -a`
  // delete all Containers and all images. 
    
https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes-de