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
        print("%s - NOME: %s, E-MAIL: %s, SENHA: %s, DATA NASCIMENTO: %s, PROFISSAO: %s, GENERO: %s, CIDADE: %s, ESTADO: %s, PAÍS: %s" %
              (usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], usuario[8], usuario[9]))

    conn.close()

if __name__ == '__main__':
    main()