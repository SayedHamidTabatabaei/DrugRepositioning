def generate_insert_query(table_name, columns):
    return f"INSERT INTO {table_name}({', '.join([name for name in columns])}) VALUES ({', '.join(['%s' for _ in columns])})"
