import csv
import json

with open("./files/users.json", "r") as file:
    users = json.load(file)
    user_result = []
    for user in users:
        user_result.append({"name": user['name'],
                            "gender": user['gender'],
                            "address": user['address'],
                            "age": user['age'],
                            "books": []})

with open("./files/books.csv", newline="") as file:
    csv_reader = csv.DictReader(file)
    current_user_index = 0
    max_user_index = len(user_result) - 1

    for row in csv_reader:
        if current_user_index > max_user_index:
            current_user_index = 0

        user_result[current_user_index]["books"].append({"title": row['Title'],
                                                         "autor": row['Author'],
                                                         "pages": row['Pages'],
                                                         "genre": row['Genre']})
        current_user_index += 1

with open('result.json', 'w') as f:
    json.dump(user_result, f, indent=4)
