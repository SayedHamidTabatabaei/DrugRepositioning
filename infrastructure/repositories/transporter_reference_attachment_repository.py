from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TransporterReferenceAttachmentRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'transporter_references_attachments'

    def insert(self, attachments: [], transporter_id: int):
        columns = ('transporter_id', 'ref_id', 'title', 'url')
        values = [(transporter_id, attachment.ref_id, attachment.title, attachment.url) for attachment in attachments]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
