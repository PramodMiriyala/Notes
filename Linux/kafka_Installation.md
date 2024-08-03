# KAFKA
## Installation steps:

```bash
sudo adduser kafka
sudo passwd -d kafka
sudo adduser kafka sudo
su -l kafka
sudo apt update
sudo apt install openjdk-11-jdk
mkdir ~/downloads
cd ~/downloads
wget https://archive.apache.org/dist/kafka/3.4.0/kafka_2.12-3.4.0.tgz
cd ~
tar -xvzf ~/downloads/kafka_2.12-3.4.0.tgz
mv kafka_2.12-3.4.0/ kafka/
```
---
### configuring kafka servers
```bash
nano ~/kafka/config/server.properties
```

```
Look for the following variables and add:
log.dirs=/home/kafka/kafka-logs
num.partition=3
```
---
### Starting the Kafka server
```bash
~/bin/zookeeper-server-start.sh  ~/kafka/config/zookeeper.properties
~/kafka/bin/kafka-server-start.sh  ~/kafka/config/server.properties
```
### adding Unit files
```bash
sudo nano /etc/systemd/system/zookeeper.service
```
#### Unit File for Zookeeper:
```
[Unit]
Description=Apache Zookeeper Service
Requires=network.target                 
After=network.target                 

[Service]
Type=simple
User=kafka
ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties        
ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

```bash
sudo nano /etc/systemd/system/kafka.service
```
#### Unit File for Kafka:
```
[Unit]
Description=Apache Kafka Service that requires zookeeper service
Requires=zookeeper.service
After=zookeeper.service

[Service]
Type=simple
User=kafka
ExecStart= /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties                            
ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl start kafka
sudo systemctl status kafka
```
---
### Testing the Kafka server
```bash
nc -vz localhost 9092
cat ~/kafka/logs/server.log
~/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic firstTopic 
~/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
~/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic firstTopic
> Hi, Hello Welcome to kafka
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic firstTopic --from-beginning
```
[Refer here](https://hostman.com/tutorials/install-apache-kafka-on-ubuntu-22-04/) for the full article