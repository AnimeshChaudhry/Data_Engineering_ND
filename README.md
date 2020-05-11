# Data Engineering Nanodegree

Projects and resources developed in the [Data Engineering Nanodegree](https://www.udacity.com/course/data-engineer-nanodegree--nd027) from Udacity.

## Project 1: [Relational Databases - Data Modeling with PostgreSQL](https://github.com/AnimeshChaudhry/Data_Engineering_ND/tree/master/Data%20Modeling%20with%20Postgres).
Developed a relational database using PostgreSQL to model user activity data for a music streaming app.
* Created a relational database using PostgreSQL
* Developed a Star Schema database. Utilized optimized definitions of Fact and Dimension tables. Normalization of tables performed.
* Built out an ETL pipeline to optimize queries in order to gather insight into user activity.

```Utilized: Python, PostgreSql, Star Schema, ETL pipelines, Normalization```


## Project 2: [NoSQL Databases - Data Modeling with Apache Cassandra](https://github.com/AnimeshChaudhry/Data_Engineering_ND/tree/master/Data%20Modeling%20with%20Apache%20Cassandra).
Designed a NoSQL database using Apache Cassandra based on the original schema outlined in the first project.
* Created a nosql database using Apache Cassandra utilizing docker containers.
* Developed denormalized tables optimized for a specific set queries and optimization needs.

```Utilized: Python, Apache Cassandra, Denormalization```


## Project 3: [Data Warehouse - Amazon Redshift](https://github.com/AnimeshChaudhry/Data_Engineering_ND/tree/master/Data%20Warehouse).
Created a database warehouse utilizing Amazon Redshift. Skills include:
* Creating a Redshift Cluster, IAM Roles, Security groups using cloudformation (Iac)
* Develop an ETL Pipeline that copies data from S3 buckets into staging tables to be processed into a star schema.
* Developed a star schema with optimization to specific queries required by the data analytics team.

```Utilized: Python, Amazon Redshift, aws cli, Amazon SDK, SQL, PostgreSQL```

## Project 4: [Data Lake - Spark](https://github.com/AnimeshChaudhry/Data_Engineering_ND/tree/master/Dala%20Lake%20-%20Spark)
Scaled up the current ETL pipeline by moving the data warehouse to a data lake.
* Create an EMR Hadoop Cluster
* Further develop the ETL Pipeline copying datasets from S3 buckets, data processing using Spark and writing to S3 buckets using efficient partitioning and parquet formatting.
* Fast-tracking the data lake buildout using (serverless) AWS Lambda and cataloging tables with AWS Glue Crawler.

```Utilized: Spark, S3, EMR, Athena, Amazon Glue, Parquet.```

## Project 5: [Data Pipelines - Airflow](https://github.com/AnimeshChaudhry/Data_Engineering_ND/tree/master/Data%20Pipelines%20-%20Airflow)
Automate the ETL pipeline and creation of data warehouse using Apache Airflow. 
* Using Airflow to automate ETL pipelines and get them production ready.
* Writing custom operators to perform tasks such as staging data, filling the data warehouse, and validation through defined data quality checks.
* Transforming data from various sources into a star schema optimized for the analytics team's use cases.

```Utilized: Apache Airflow, S3, Amazon Redshift, Python```

