# Instats
Instats is an instagram bot made with Python and Selenium to automate the boring parts and help you grow your account.

## Getting started

Here's a list of all the things you will need to run this bot

* Python 3
* Pip3
* Selenium
* Geckodriver
* Chromedriver


## In Linux
###  For Ubuntu and its variants, here's how you do it:
First get Python:
```
sudo apt install python3
```
Then Pip3:
```
sudo apt install python3-pip
```
Now, get Selenium:
```
pip3 install selenium
```

Geckodriver (Firefox) for 32 bits systems:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz && tar xvfs geckodriver-v0.24.0-linux64.tar.gz && sudo cp geckodriver /usr/local/bin/
```
Geckodriver (Firefox) for 64 bits systems:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz && tar xvfs geckodriver-v0.24.0-linux64.tar.gz && sudo cp geckodriver /usr/local/bin/
```

Chromedriver (Chrome/Chromium) for 64 bits systems:
```
wget https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && sudo cp chromedriver /usr/local/bin
```

Now, it's easy, clone this repo, cd into it and run the following:
```
python3 main.py
```
And you're good to go.


## Features

* Farming accounts of people who liked certain posts
* Farming commenters
* Sorting your followers and your followings
* Realistic key presses

## Contributing
If you think you can help me make this bot better and more reliable, feel free to make a new issue and talk to me about what you plan to do.

