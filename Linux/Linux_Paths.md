#  Add an environment variable and update the PATH on Ubuntu
# User-Specific
---
### Steps:
1. Open the .bashrc file:  
    
```bash
nano ~/.bashrc
```

2. Add the following lines at the end:

```bash
export JAVA_HOME="/opt/openlogic-openjdk-17.0.12+7-linux-x64"
export PATH="$JAVA_HOME/bin:$PATH"
```
3. Save and exit
4. Apply the changes:

```bash
source ~/.bashrc
```
5. Verify the changes:
```bash
echo $JAVA_HOME
echo $PATH
```
---

# System-Wide
### Steps:
1. Open the /etc/environment file:
```bash
sudo nano /etc/environment
```
2. Add or modify the PATH variable:
```bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/openlogic-openjdk-17.0.12+7-linux-x64/bin"
```
3. `source /etc/environment`
4. Verify the changes:
```bash
echo $PATH
```
## Editing the /etc/profile File
```bash
sudo nano /etc/profile
export JAVA_HOME="/opt/openlogic-openjdk-17.0.12+7-linux-x64"
export PATH="$JAVA_HOME/bin:$PATH"
exit and log back
echo $PATH
```
---
## Using the /etc/profile.d/ Directory

```bash
sudo nano /etc/profile.d/java.sh
export JAVA_HOME="/opt/openlogic-openjdk-17.0.12+7-linux-x64"
export PATH="$JAVA_HOME/bin:$PATH"
exit & log back
echo $PATH
```