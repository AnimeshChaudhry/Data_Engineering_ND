import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Delete pre-existing tables in the database
    This way, we can run create_tables.py to reset the database and test the ETL pipeline.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create staging and dimensional tables from sql_queries.py
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Set up the database and create all the tables with the appropriate fields 
    """
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()