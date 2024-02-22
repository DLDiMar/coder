import json

def process_sql_request(json_data):
    users = json.loads(json_data)["Users"]
    sql_commands = []

    for user in users:
        sql_command = f"INSERT INTO users (name, age, birth_place, birth_date, occupation, id) VALUES ('{user['name']}', {user['age']}, '{user['birth_place']}', '{user['birth_date']}', '{user['occupation']}', '{user['id']}');"
        sql_commands.append(sql_command)

    result = "\n".join(sql_commands)
    return result