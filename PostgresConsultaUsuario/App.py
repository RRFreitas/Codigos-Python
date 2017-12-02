import psycopg2

DB_NAME = "GeekWay"
DB_USER = "postgres"
DB_PASSWORD = "rennanbd"

def main():
    conn = psycopg2.connect("dbname=%s user=%s password=%s" % (DB_NAME, DB_USER, DB_PASSWORD))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_usuario;
    """)

    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print("ID:", usuario[0])
        print("NOME:", usuario[1])
        print("E-MAIL:", usuario[2])
        print("SENHA:", usuario[3])
        print("DATA NASCIMENTO:", usuario[4])
        print("PROFISSÃO:", usuario[5])
        print("GÊNERO:", usuario[6])
        print("CIDADE:", usuario[7])
        print("ESTADO:", usuario[8])
        print("PAÍS:", usuario[9])
        print("--------------------------")

    conn.close()

if __name__ == '__main__':
    main()
