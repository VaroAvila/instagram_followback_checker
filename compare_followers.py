import json
import os

# Function to load data from a JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Function to extract usernames from the list
def extract_usernames(data_list):
    usernames = []
    for item in data_list:
        if 'string_list_data' in item:
            for sub_item in item['string_list_data']:
                usernames.append(sub_item['value'])
    return usernames

# Paths to the JSON files
followers_file = os.path.join('path_to_your_directory', 'followers_1.json')
following_file = os.path.join('path_to_your_directory', 'following.json')

# Load followers and following data
followers = load_data(followers_file)
following = load_data(following_file)

# Extract usernames from followers and following
followers_usernames = set(extract_usernames(followers))
following_usernames = set(extract_usernames(following['relationships_following']))

# Calculate who does not follow back
not_following_back = following_usernames - followers_usernames

# Print the list of users who do not follow back
print("Users who do not follow you back:")
for user in not_following_back:
    print(user)

# Export the list to a text file
output_file = os.path.join('path_to_your_directory', 'not_following_back.txt')
with open(output_file, 'w', encoding='utf-8') as file:
    file.write("Users who do not follow you back:\n")
    for user in not_following_back:
        file.write(f"{user}\n")

print(f"The list of users who do not follow you back has been exported to {output_file}")
