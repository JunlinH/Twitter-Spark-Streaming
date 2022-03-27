import findspark
findspark.init('FILLING UP YOUR SPARK DIRECTORY HERE')
import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext
import sys
import requests
import time


def send_df_to_dashboard(df):
    # Extracting the hashtags from the dataframe and converting them into a Python list.
    top_tags = [str(t.word) for t in df.select("word").collect()]
    # Extracting the counts from the dataframe and converting them into a Python list.
    tags_count = [p.word_count for p in df.select("word_count").collect()]
    # Sending the data to the socket using the Python library 'requests'.
    url = 'http://localhost:5558/updateData'
    request_data = {'label': str(top_tags), 'data': str(tags_count)}
    requests.post(url, data=request_data)


def get_sql_context_instance(spark_context):
    if 'sqlContextSingletonInstance' not in globals():
        globals()['sqlContextSingletonInstance'] = SQLContext(spark_context)
    return globals()['sqlContextSingletonInstance']


def process_rdd(time, rdd):
    print("----------- %s -----------" % str(time))
    try:
        # Converting a RDD into a Row RDD.
        row_rdd = rdd.map(lambda w: Row(word=w[0], word_count=w[1]))
        # Creating a spark sql singleton context object from the rdd context.
        sql_context = get_sql_context_instance(rdd.context)
        # Creating a dataframe object from the Row RDD object.
        hashtags_df = sql_context.createDataFrame(row_rdd)
        # Updating the table 'hashtags' using the 'hashtags_df'.
        hashtags_df.registerTempTable("hashtags")
        # Using SQL to retrieve the top 10 hashtags in the table 'hashtags' and print them out.
        hashtag_counts_df = sql_context.sql(
            "select word, word_count from hashtags order by word_count desc limit 10")
        hashtag_counts_df.show()
        # Sending the top ten hashtags to flask through a socket and display them using flask.
        # Flask is a python library.
        send_df_to_dashboard(hashtag_counts_df)
    except:
        pass


def aggregate_tags_count(new_values, total_sum):
    return sum(new_values) + (total_sum or 0)


def processing_streaming_data(ssc):
    # Reading data from the port your defined in tweets.py.
    dataStream = ssc.socketTextStream("localhost", 5556)
    # Splitting each tweet into words.
    words = dataStream.flatMap(lambda line: line.split(" "))
    # Filtering non-hashtag words, and creating a tuple (hashtag, 1) from each hashtag.
    hashtags = words.filter(lambda w: '#' in w).map(lambda x: (x, 1))
    # Updating the count for each hashtag.
    tags_totals = hashtags.updateStateByKey(aggregate_tags_count)
    # do processing for each RDD generated in each interval
    tags_totals.foreachRDD(process_rdd)


def set_up_spark():
    # Defining the configuration for spark.
    conf = SparkConf()
    conf.setMaster("local[*]").setAppName("twitter_streaming")
    # Creating a SparkContext object with the above configuration.
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")
    # Creating a StreamingContext object with the interval size 2 seconds.
    ssc = StreamingContext(sc, 2)
    # Creating the checkpoints to allow the RDD recovery.
    ssc.checkpoint("checkpoint_TwitterApp")
    return ssc


if __name__ == "__main__":
    # Setting up the spark for streaming.
    ssc = set_up_spark()
    # Processing the streaming data to find the top 10 trending hashtags,
    # and showing them in a live dashboard.
    processing_streaming_data(ssc)
    # Starting the streaming.
    ssc.start()
    # Waiting for the streaming to be finished.
    # Be aware that the streaming won't stop until
    # you manually terminate the program.
    ssc.awaitTermination()
