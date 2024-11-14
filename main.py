import json

# Function to extract usernames from the JSON structure
def load_usernames(file_path, key=None):
    usernames = set()
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()  # Read the entire file content as a string
            print(f"File content of {file_path}:\n{file_content[:500]}...")  # Print first 500 chars for inspection
            data = json.loads(file_content)  # Parse JSON
            print("JSON loaded successfully")


            if isinstance(data, list):
                entries = data
            elif isinstance(data, dict) and key in data:
                entries = data.get(key, [])
            else:
                entries = []

            # Loop through the entries (followers or following)
            for entry in entries:
                for item in entry.get("string_list_data", []):
                    usernames.add(item["value"])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return usernames

# Replace 'followers.json' and 'following.json' with actual file paths!!!
followers_file = 'followers_1.json'
following_file = 'following.json'

# Load followers and following usernames
followers = load_usernames(followers_file)
following = load_usernames(following_file, 'relationships_following')


not_following_back = following - followers


if not_following_back:
    print("These users don't follow you back:")
    for user in not_following_back:
        print(user)
else:
    print("Everyone you follow follows you back! :)")
