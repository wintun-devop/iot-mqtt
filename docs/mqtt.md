### Mosquitto
```
https://mosquitto.org/download/
```
### EMQX
```
https://www.emqx.com/en/downloads-and-install/enterprise
```
- Basic Docker for EMQX 
- default:(username:admin,password:public)
```
docker pull emqx/emqx-enterprise:5.10.1
```
```
docker run -d --name emqx-enterprise -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx-enterprise:5.10.1
```
- custom volume and network 
```
docker run -d --name emqx-enterprise --network dev-net-1 -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 -v D:/docker_volumes/emqx-data:/opt/emqx/data emqx/emqx-enterprise:5.10.1
```