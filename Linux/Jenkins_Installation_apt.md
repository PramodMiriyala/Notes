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

1. Add the Jenkins repository to your apt sources list:
```bash
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null
```
### Note:
```
This command adds the Jenkins repository to the /etc/apt/sources.list.d/jenkins.list file. It specifies that the repository is signed by the key downloaded in the previous step.

* echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]":
This part constructs a line that specifies a new APT repository. The deb keyword indicates that this is a binary package repository.
The [signed-by=/usr/share/keyrings/jenkins-keyring.asc] part tells APT to use the specified GPG key to verify the packages from this repository. This is important for security, ensuring that the packages are from a trusted source.

* https://pkg.jenkins.io/debian-stable binary/:
This is the URL of the Jenkins APT repository. It points to the stable version of Jenkins packages for Debian-based systems.

* | sudo tee /etc/apt/sources.list.d/jenkins.list:
The | operator pipes the output of the echo command to the tee command.
sudo tee /etc/apt/sources.list.d/jenkins.list writes the repository information to a new file named jenkins.list in the /etc/apt/sources.list.d/ directory. This directory is where APT looks for additional sources of packages.

* > /dev/null:
This part suppresses the output of the tee command, so it doesn’t display the repository line in the terminal.
```
---

1. Update your apt package manager and Install jenkins:
```bash
sudo apt update
sudo apt install jenkins
```
