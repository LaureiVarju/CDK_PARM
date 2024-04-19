import json

print("inside hello.py")

message_content = "Hello there!!!!"
response_data = {
    "type": 4,
    "data": {"content": message_content},
}

print(f"response_data is: {response_data}")

# Convert dictionary to JSON string
json_data = json.dumps(response_data)

# Return serialized JSON data
print(json_data)