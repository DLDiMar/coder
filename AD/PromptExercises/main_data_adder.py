import json
from id_generator import id_generator
from sql_request_output import process_sql_request

def main():
    print("Enter JSON data:")
    json_data = input()
    users = json.loads(json_data)["Users"]
    num_users = len(users)
    ids = id_generator(num_users)

    for i, user in enumerate(users):
        user["id"] = ids[i]

    modified_json = json.dumps({"Users": users})
    print("Modified JSON:")
    print(modified_json)

    result = process_sql_request(modified_json)
    print("Result:")
    print(result)

if __name__ == "__main__":
    main()