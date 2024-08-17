## Firefox-dev Installation Process: 
### Steps: 

#### Download and unpack 

```bash 
wget “https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=en-US” -O Firefox-dev.tar.bz2 
sudo tar xjf Firefox-dev.tar.bz2 -C /opt/ 
rm -r Firefox-dev.tar.bz2
```
---
#### Installation

```bash
sudo ln -s /opt/firefox/firefox /usr/local/bin/firefox-dev 
vi Firefox-dev.desktop 
```

```bash
[Desktop Entry]
Name=Firefox-developer-edition
Exec=/usr/local/bin/firefox-dev
Icon=/opt/firefox/browser/chrome/icons/default/default128.png
comment=browser
Type=Application
Terminal=false
Encoding=UTF-8
Categories=Utility;
``` 
#### Updating: 

```bash
wget "https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=en-US" -O Firefox-dev.tar.bz2
 sudo tar xjf Firefox-dev.tar.bz2 -C /opt/
```
#### Removing completely:
 
```bash
sudo rm -r /opt/firefox/
 sudo rm /usr/local/bin/firefox-dev
 sudo rm /usr/share/applications/Firefox-dev.desktop
 rm ~/Desktop/Firefox-dev.desktop
```
