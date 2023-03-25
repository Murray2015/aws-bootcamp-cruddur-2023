
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..', ".."))
sys.path.append(parent_path)
from lib.db import db

def get_my_user_uuid():
  sql = """
    SELECT 
      users.uuid,
      users.handle
    FROM users
    WHERE
      users.handle = %(my_handle)s 
  """
  user = db.query_array_json(sql, {
    'my_handle':  'andrewbrown'
  })

  print('get_user_user_uuid')
  print(user)
  return user[0]['uuid']