import sys
import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import jsonstruct
import requests

if __name__ == "__main__":
    """instantiate spark context to connect with spark and spark stream to instantiate streaming process
    batch_interval = 2
    i.e. time interval to form a single RDD in the DStream = 2s"""
    sc = SparkContext(appName="StreamProcessor")
    ssc = StreamingContext(sc, 5)

    # store intermediate state in local filesystem
    ssc.checkpoint("file:///tmp/spark")

    # listen to host and port passed in as command line arguments
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

    def send_partition(tup):
        """sends a POST request to an external api with the RDD"""
        url = "http://localhost:9000/api"
        data = json.dumps({tup[0]: tup[1]})
        requests.post(url, data)

    def transform(rdd):
        """perform transformations"""
        words = rdd.flatMap(lambda line: line.split(" "))
        pairs = words.map(lambda word: (word, 1))
        word_counts = pairs.reduceByKey(lambda x, y: x + y)
        return word_counts

    transformed_lines = transform(lines)
    transformed_lines.pprint()
    transformed_lines.foreachRDD(lambda rdd: rdd.foreach(send_partition))

    ssc.start()
    ssc.awaitTermination()



