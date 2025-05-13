import mysql.connector

id = input("ID: ")
results = get_student_schedule(id)

for result in results:
  print(f"Period: {row[0]} \nCourse: {row[1]} \nRoom: {row[2]} \nTeacher: {row[3]}\n")

def get_database_connection(u, p, h, d):
  connection = mysql.connector.connect(user=u,
                                    password=p,
                                    host=h,
                                    database=d)
  return connection

def execute_statement(connection, statement):
  cursor = connection.cursor()
  cursor.execute(statement)
  results = []
  for row in cursor:
    results.append(row)
  cursor.close()
  connection.close(0
  return results

def get_student_schedule(student_id):
  statement = f"call FindSchedule({studentid});"
  return execute_statement(get_database_connection(), statement)
