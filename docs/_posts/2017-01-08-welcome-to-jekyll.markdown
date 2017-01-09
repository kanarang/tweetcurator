---
layout: post
title:  "Installation and usage instructions"
date:   2017-01-08 01:43:10 +0530
categories: jekyll update
---

## If you want only the executable application, click [here][1], unzip main.zip, and run main.exe. For using the modifiable python source code, refer to the steps below.

<br>

### Step 1. Cloning the repository

Go to the [tweetcurator github page](https://github.com/narangkay/tweetcurator) and clone or download the repository.

<br>

### Step 2. Creating a Twitter Application

Follow this short tutorial to [create a Twitter Application](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/) and generate a Consumer Key and Consumer Secret. Note that we do not need an Access Token or an Access Token Secret even though this is included in the tutorial above.

<br>

### Step 3. Make sure you have pip and Python installed

<br>

### Step 4. Installing dependencies

Open the command line and run the following command:

```
pip install selenium, httplib2, urllib, json, base64, datetime
```

<br>

### Step 5. Running the script

Navigate to the downloaded repository on the command line and run the script:

```
cd <Path Of Your Downloaded Repository>
python3 main.py
```
<br>


[1]:{{ site.url }}docs/download/main.zip

# ALL DONE!


Please report any errors on the [tweetcurator github page](https://github.com/narangkay/tweetcurator).
