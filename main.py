import mysql.connector

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
  connection.close()
  return results

def get_student_schedule(student_id):
  statement = f"call FindSchedule({student_id});"
  return execute_statement(get_database_connection("shunyic", "231084559", "10.8.37.226", "shunyic_db"), statement)

def print_student_schedule(id):
    results = get_student_schedule(id)

    for result in results:
        print(f"Period: {result[0]} \nCourse: {result[1]} \nRoom: {result[2]} \nTeacher: {result[3]}\n")

def get_teacher_schedule(teacher_id):
    statement = f"call TeacherSchedule({teacher_id});"
    return execute_statement(get_database_connection("shunyic", "231084559", "10.8.37.226", "shunyic_db"), statement)

def print_teacher_schedule(id):
    results = get_teacher_schedule(id)
    for result in results:
        print(f"Period: {result[1]} \nCourse: {result[0]} \nRoom: {result[2]} \n")

job = input("Teacher or Student: ")
id = input("ID: ")
if job == "Teacher":
    print_teacher_schedule(id)
else:
    print_student_schedule(id)
