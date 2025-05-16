import psycopg2

conn_params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "infomaz-db",
    "user": "admin",
    "password": "pwd"
}

columns_to_clean = {
    "cadastro_estoque": ["VALOR ESTOQUE"],
    "vendas": ["VALOR NOTA", "VALOR ITEM"]
}

def clean_columns(table_column_map):
    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                for table, columns in table_column_map.items():
                    for column in columns:
                        sql = f"""
                        ALTER TABLE {table}
                        ALTER COLUMN "{column}" TYPE NUMERIC USING
                            REPLACE(REPLACE("{column}", '.', ''), ',', '.')::NUMERIC;
                        """
                        cur.execute(sql)
                print("✅ All specified columns cleaned and converted to NUMERIC.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    clean_columns(columns_to_clean)
