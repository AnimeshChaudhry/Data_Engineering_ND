from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    
    copy_query = " COPY {} \
    FROM '{}' \
    ACCESS_KEY_ID '{}' \
    SECRET_ACCESS_KEY '{}' \
    FORMAT AS json '{}'; \
    "

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 aws_credential_id="",
                 table_name="",
                 s3_bucket="", 
                 s3_key="",
                 file_format="",
                 log_json_file="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credential_id= aws_credential_id
        self.table_name= table_name
        self.s3_bucket= s3_bucket
        self.s3_key= s3_key
        self.file_format= file_format
        self.log_json_file = log_json_file
        self.execution_date = kwargs.get('execution_date')
        
    def execute(self, context):
        aws_hook = AwsHook(self.aws_credential_id)
        credentials=aws_hook.get_credentials()
        
        s3_path=f"s3://{self.s3_bucket}/{self.s3_key}"
        self.log.info(f"Staging files for {self.table_name} from {s3_path}")
        
        if self.log_json_file != "":
            self.log_json_file = f"s3://{s3_bucket}/{log_json_file}"
            copy_query = self.copy_query.format(self.table_name, s3_path, credentials.access_key, credentials.secret_key, self.log_json_file)
        else:
            copy_query = self.copy_query.format(self.table_name, s3_path, credentials.access_key, credentials.secret_key, 'auto')
        
        self.log.info(f'Running the copy task {copy_query}')
        redshift_hook = PostgresHook(postgress_conn_id = self.redshift_conn_id)
        
        redshift_hook.run(copy_query)
        self.log.info(f"Staging of {self.tale_name} was successful.")





