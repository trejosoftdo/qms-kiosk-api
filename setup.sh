# Steps to install chrome dependencies:

apt-get install -y wget
apt-get install -y gnupg


wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Install Chrome and chromium driver.
apt-get update && apt-get -y install google-chrome-stable && apt-get update && apt-get -y install chromium-driver
