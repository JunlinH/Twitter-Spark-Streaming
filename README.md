# Twitter_Spark_Streaming
This project uses PySpark to find trending hashtags in the streaming tweets.

### Requirements
- pyspark 3.*.* (spark-3.1.3-bin-hadoop3.2 used in this project)
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

### Result
In Tweepy, we can specify the region and the language so that we only receive tweets written in a speciﬁc language from a speciﬁc region - this enables us to analyze the popular hashtags among speciﬁc areas and ethnic groups. We can also specify the keywords to track so that we only receive tweets containing keywords we are interested in - this enables us to analyze the most popular hashtags related to speciﬁc topics. Our experiments explored different regions, languages, and keywords settings. Below is our result.

#### Different Regions
The most popular hashtags in Canada and US, March 27th, 2022.
<img width="925" alt="canada us" src="https://user-images.githubusercontent.com/29801160/163589527-84c03fed-2e96-49b2-a4f7-c1dc1711bcee.png">

The most popular hashtags in Australia, April 12th, 2022.
<img width="780" alt="australia" src="https://user-images.githubusercontent.com/29801160/163589885-9ad9c74d-d832-4e14-94cb-d695aedb32a6.png">

#### Different Ethnic Groups
The most popular hashtags among people who speak French, April 12th, 2022.
<img width="742" alt="french" src="https://user-images.githubusercontent.com/29801160/163589950-3cb0b604-10c5-41e3-9ae6-834e3d45989c.png">

The most popular hashtags among people who speak Korean, April 12th, 2022.
<img width="749" alt="korean" src="https://user-images.githubusercontent.com/29801160/163590015-832c3ad9-c457-47ec-8151-45b7b2b0a9c3.png">

#### Different Topics
The most popular hashtags related to the keyword ‘Ukraine’, April 12th, 2022.
<img width="747" alt="ukraine" src="https://user-images.githubusercontent.com/29801160/163590095-ef33f57b-16e8-48ad-8680-95ed25fe4a61.png">

The most popular hashtags related to the keyword ‘movie’, April 12th, 2022.
<img width="756" alt="movie" src="https://user-images.githubusercontent.com/29801160/163590120-3ac6559c-b297-4ad5-99c3-5e4796c9097b.png">


### References:
- [Apache Spark Streaming Tutorial: Identifying Trending Twitter Hashtags](https://www.toptal.com/apache/apache-spark-streaming-twitter)
- [Twitter data analysis through Spark Streaming](https://pgirish.github.io/spark-project/index.html)

