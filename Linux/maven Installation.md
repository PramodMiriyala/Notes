## Maven Installation
### Ubuntu 22.04 Steps:
1. Download tar file from Here [Refer here](https://maven.apache.org/download.cgi)
```bash
cd /tmp/
wget https://dlcdn.apache.org/maven/maven-3/3.9.8/binaries/apache-maven-3.9.8-bin.tar.gz
tar -zxvf apache-maven-3.9.8-bin.tar.gz -C /opt/
nano /etc/environment
```
#### Add these files to path:
```bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/apache-maven-3.9.8/bin"
```
```
source /etc/environment
mvn --version
```
---
### Note:
```
wget: downloads file at current directory
tar: this will unzip tar file.
-z: decompress the archive using gzip compression.
-x: Extract files from the archive
-C /path/to/directory: Change to the specified directory before extracting
-v: verbose mode, which means tar will display the names
``` 
