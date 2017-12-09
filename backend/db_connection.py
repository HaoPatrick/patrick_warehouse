import pymysql
# from backend.config import MYSQL_CONFIG
from backend import config as MYSQL_CONFIG
from backend import app
from flask import g


class Connection():
  def __init__(self, db_name: str):
    self._db_name = db_name
    self._connection = self._get_connection()
    self._cursor = self._connection.cursor()
  
  def _get_connection(self) -> pymysql.cursors:
    mysql_conn = pymysql.connect(
      host=MYSQL_CONFIG['host_name'],
      user=MYSQL_CONFIG['user'],
      password=MYSQL_CONFIG['password'],
      port=MYSQL_CONFIG['server_port'],
      db=self._db_name
    )
    return mysql_conn
  
  @property
  def cursor(self) -> pymysql.cursors:
    return self._cursor
  
  def close(self):
    self._connection.close()
  
  def commit(self):
    self._connection.commit()
  
  def commit_and_close(self):
    self.commit()
    self.close()


def get_db(db_name: str):
  if not hasattr(g, 'db_list'):
    setattr(g, 'db_list', [])
  if not hasattr(g, db_name):
    setattr(g, db_name, Connection(db_name))
    g.db_list.append(db_name)
  return getattr(g, db_name)


@app.teardown_appcontext
def close_db(error):
  if not hasattr(g, 'db_list'): return
  for conn in g.db_list:
    connection = getattr(g, conn)
    connection.close()


class WeatherDB():
  def __init__(self):
    self._TABLE = 'weather'
    self._TEMP = 'temp'
    self._HUMIDITY = 'humidity'
    self._DB_NAME = 'iot_data'
    self.connection = get_db('iot_data')
  
  def insert_data(self, temp: float, humidity: float):
    insert_sql = 'INSERT INTO {table}(temp,humidity) VALUES (%s,%s)'.format(table=self._TABLE)
    self.connection.cursor.execute(insert_sql, (temp, humidity))
    self.connection.commit()
  
  def get_data_limited(self, limit_to: int) -> list:
    get_data_sql = 'select * from {table} ORDER BY id desc LIMIT {limit}'.format(table=self._TABLE, limit=limit_to)
    self.connection.cursor.execute(get_data_sql)
    return self.connection.cursor.fetchall()
