# Twitter_Spark_Streaming
This project uses PySpark to find the popular hashtags in the streaming twitter data.

### Requirements
- pyspark 3.x.x (spark-3.1.3-bin-hadoop3.2 used in this project)
- findspark
- tweepy
- flask
- ast
- requests
- psutil

### Usage
First of all, creating a project in your favorite IDE. I used PyCharm.

Then you need to install libraries I listed in the Requirements, I recommend you to use pip3 for its simplicity. For example, I used following code to install libraries:
```
pip3 install findspark
pip3 install tweepy
pip3 install flask
pip3 install ast
pip3 install requests
pip3 install psutil
```

Installing PySpark is a more complex process. To do it, you can refer to [this great tutorial](https://sundog-education.com/spark-streaming/).

After installing PySpark, you need to import findspark library first to make PySpark working properly. For example, my spark directory is `/Users/JunlinHe/ApacheSpark/spark-3.1.3-bin-hadoop3.2`. Therefore I used the following code to import PySpark.
```
import findspark
findspark.init('/Users/JunlinHe/ApacheSpark/spark-3.1.3-bin-hadoop3.2')
import pyspark
```

Then copy and paste all files in this repository into your project folder. Going to the lines 18-21 in the `tweets.py`, and filling up your consumer key, consumer key secret, project access token, project access token secret. 

If you don't know what are these, please applying a twitter developer account and create a twitter project in the Twitter website. You need to set up these things in order to get access to streaming Twitter data. To set up a Twitter developer account, please go to this page:
https://developer.twitter.com/en

Also, I recommend to request "elevated" permissions for your project by filling up a request form:
https://developer.twitter.com/en/portal/petition/standard/basic-info

This project doesn't involve creating tweets, retweets, or anything like that. We are also not going to expose data to any goverment. This project only reads tweets and find the most popular hashtags in the streaming data. When you are asked about these questions, keep this in mind.

Also, you need to go to the line 2 in the `streaming.py` file, and filling up your own PySpark directory.

Then, run files in the order: `tweets.py` -> `streaming.py` -> `app.py`.
Going to http://localhost:5558/ in your browser and watching the magic happens!

*If you made some mistakes and you need to run this project again. You need to reopen your IDE and rerun your project. If you don't do this, you might find an error tells you the port you requested has already been occupied.

