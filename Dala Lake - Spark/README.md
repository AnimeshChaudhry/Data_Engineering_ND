# Project: Data Lake

A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

We are tasked with building an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.

We will be able to test our database and ETL pipeline by running queries given to us by the analytics team from Sparkify and compare our results with their expected results.

## Deployement

Config File `dl.cfg` is not provided here fpr security purposes. File contains :

```
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
```

Using a local development environment - Moving project directory from local to EMR

     scp -i <.pem-file> <Local-Path> <username>@<EMR-MasterNode-Endpoint>:~<EMR-path>

Running spark job (Make sure the EMR has the correct AWS security permissions)

    spark-submit etl.py --master yarn --deploy-mode client --driver-memory 4g --num-executors 2 --executor-memory 2g --executor-core 2

## ETL Pipeline

1.  Read data from S3

    - Song data: `s3://udacity-dend/song_data`
    - Log data: `s3://udacity-dend/log_data`

    The script reads song_data and load_data from S3.

2.  Process data using spark (see etl.py)

    Transforms them to create the following schema:

#### Schema

##### Fact Table

**songplays** - records in log data associated with song plays i.e. records with page `NextSong`

```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

##### Dimension Tables

**users** - users in the app

```
user_id, first_name, last_name, gender, level
```

**songs** - songs in music database

```
song_id, title, artist_id, year, duration
```

**artists** - artists in music database

```
artist_id, name, location, latitude, longitude
```

**time** - timestamps of records in **songplays** broken down into specific units

3.  Writes data into parquet files in S3 partitioned partitioned by specified fields.
