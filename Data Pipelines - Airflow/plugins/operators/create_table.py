from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class CreateTableOperator(BaseOperator):
    ui_color = '#358140'
    
    @apply_defaults
    def __init__(self, redshift_conn_id="", *args, **kwargs):
        
        super(CreateTableOperator, sekf).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        
    def execute(self, context):
        self.log.info("Creating Postgress SQL hook")
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        self.log.info("Postgress SQL hook created")
        
        self.log.info("Creating tables in redshift")
        
        # Open and read the file as a single buffer
        fd = open('/home/workspace/airflow/create_tables.sql', 'r')
        sqlFile = fd.read()
        redshift.run(sqlFile)
        self.log.info("Done creating tables.")
        fd.close()
      