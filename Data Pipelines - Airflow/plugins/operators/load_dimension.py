from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    truncate = """
        TRUNCATE TABLE {table}
    """
    insert = """
        INSERT INTO {table} 
        {select_query}
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 select_query="",
                 truncate=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)

        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.select_query = select_query
        self.truncate = truncate

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        if self.truncate:
            self.log.info("Truncate tabke option is set to true. Truncating table...")
            redshift.run(LoadDimensionOperator.truncate.format(
                table=self.table
            ))

        self.log.info(f"Inserting data into the dimension table {self.table_name}...")
        redshift.run(LoadDimensionOperator.insert.format(
            table=self.table,
            select_query=self.select_query
        ))