# Instats
Instats is an instagram bot I made using Python and Selenium to help me automate the boring parts of growing my account.

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
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && sudo cp chromedriver /usr/local/bin && cd /usr/local/bin && sudo chmod a+x chromedriver
```

Now, it's easy, clone this repo, cd into it and run the following:
```
python3 main.py
```
And you're good to go.


## Features

* Farming and sorting the accounts of people who liked certain posts
* Farming and sorting the followers and following of specific accounts
* Farming commenters (Not yet implemented)
* Sorting your followers and your followings
* Realistic key presses

It also has its flaws. Since it's dependent on the website, it's also dependent on your internet connection. When scraping likers, followers and followings, if the website doesn't feel like loading more, you will end up with a number of accounts scrapped much lower than expected, so you might have to restart the scraping a couple of times before you get what you need. Once the bot collect what it needs, it's all good.

## Contributing
If you think you can help me make this bot better and more reliable, feel free to make a new issue and talk to me about what you plan to do.

## Licensing
https://github.com/thisSyntaxSucksAndYouKnowIt/instats/blob/master/LICENSE
