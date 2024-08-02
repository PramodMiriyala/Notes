# steps to install Jenkins using apt on Ubuntu:
---

1. Download the Jenkins repository key:
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
```
### Note:
```
* The -O option allows you to specify the output filename. In this case, it saves the downloaded file as jenkins-keyring.asc in the /usr/share/keyrings directory.

* This command downloads the Jenkins repository key from the official Jenkins website and saves it to the /usr/share/keyrings/jenkins-keyring.asc file

* https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key:
    This is the URL from which the GPG key is being downloaded. The key is used to verify the integrity and authenticity of the Jenkins packages when you install them via apt.
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

* "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]": This part of the command is the repository entry for Jenkins. It specifies the package type (deb for Debian packages) and the URL where the packages are hosted. The [signed-by=/usr/share/keyrings/jenkins-keyring.asc] indicates that the repository is signed with a specific key located at /usr/share/keyrings/jenkins-keyring.asc.

* https://pkg.jenkins.io/debian-stable binary/: This is the URL of the Jenkins repository for Debian. It points to the binary packages for the stable release.

* |: The pipe symbol (|) is used to redirect the output of the echo command to the input of the next command (sudo tee)

* sudo tee /etc/apt/sources.list.d/jenkins.list: The tee command reads from standard input and writes to a file. Here, it writes the repository entry to the file /etc/apt/sources.list.d/jenkins.list. The sudo prefix ensures that the command runs with superuser privileges.

* > /dev/null:
    This part of the command redirects the standard output of tee to /dev/null, effectively discarding it. It’s commonly used to suppress unnecessary output
```
---

3. Update your apt package manager and Install jenkins:
```bash
sudo apt update
sudo apt install jenkins
```
