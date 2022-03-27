import tweepy
import socket
import json

# Creating a tweepy.Stream object to receive streaming tweets.
class ReceiveTweets(tweepy.Stream):
    def on_data(self, data):
        try:
            # Data received in this method is in the form of json.
            # We use json.loads() method to transform the received
            # json data into dictionaries.
            # The key and value are all string type in the transformed
            # dictionaries.
            message = json.loads(data)
            print(message['text'].encode('utf-8'))
            # Sending the received text information to spark through a socket.
            c.send(message['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

if __name__ == "__main__":
    # Filling up your confidential information below.
    consumer_key = 'Pbwuyii8Szq168D20yaxOZMf7'
    consumer_secret = "aUOGEl3SfOXGdRRSESiBvPSUQApjRvtvXuEWWEu6bRGa2mXdek"
    access_token = "2850808645-IRswhO0sTBB0dLbRrJGXOILtG0LCy7mYV4RQwWz"
    access_token_secret = "5AlaGKd2gZoGvmCdSwzUz0GyYH3Mb6rAdaZr1mgmjwPta"
    # Defining a socket you are going to use to send and receive data.
    new_skt = socket.socket()
    host = "localhost"
    port = 5556
    new_skt.bind((host, port))
    # Waiting for the client connection.
    new_skt.listen(20)
    print("Waiting for the connection. Listening on the port: %s" % str(port))
    # After the connection is connected, the 'new_skt' object returns
    # a socket object 'c', and the address 'addr' bounding to the socket.
    c, addr = new_skt.accept()
    print("The connection is established through the port: " + str(addr))

    # Creating an object from the class tweepy.Stream.
    tweets_stream = ReceiveTweets(
        consumer_key, consumer_secret,
        access_token, access_token_secret
    )
    # Filtering Streaming Tweets by conditions.
    # The location I'm using here is Toronto, Canada.
    # You can choose anywhere you like by filling up
    # your desired location's latitude and longitude information.
    # You can use Google Earth to find such information.
    # For more detailed information about the filter method,
    # please referring to:
    # https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/api-reference/post-statuses-filter
    tweets_stream.filter(track=['Twitter'], locations=[-120.0, 28, -73.0, 60], languages=['en'])