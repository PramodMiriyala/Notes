# steps to install Jenkins using apt on Ubuntu:
---

1. Download the Jenkins repository key:
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
```
### Note:
```
This command downloads the Jenkins repository key from the official Jenkins website and saves it to the /usr/share/keyrings/jenkins-keyring.asc file
```
---

2. Add the Jenkins repository to your apt sources list:
```bash
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null
```
### Note:
```
This command adds the Jenkins repository to the /etc/apt/sources.list.d/jenkins.list file. It specifies that the repository is signed by the key downloaded in the previous step.
```
---

3. Update your apt package manager and Install jenkins:
```bash
sudo apt update
sudo apt install jenkins
```
