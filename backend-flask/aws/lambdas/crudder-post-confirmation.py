import os
import json
import psycopg2

def lambda_handler(event, context):
    print("Entering lambda")
    user = event['request']['userAttributes']
    print("user: ", user)
    try:
        conn = psycopg2.connect(
            host=(os.getenv('PG_HOSTNAME')),
            database=(os.getenv('PG_DATABASE')),
            user=(os.getenv('PG_USERNAME')),
            password=(os.getenv('PG_SECRET'))
        )
        print("Got connection")
        cur = conn.cursor()
        print("Got cursor")
        cur.execute("INSERT INTO users (display_name, handle, cognito_user_id) VALUES(%s, %s, %s)", (user['name'], user['email'], user['sub']))
        conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')
    
    print("Finished! Returning...")

    return event