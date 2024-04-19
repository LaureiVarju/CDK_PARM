
import yaml
import os
import subprocess


with open ("../../discord_commands.yaml", "r") as file:
	yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
folder_path = "slash_commands"  # Path to the folder containing the scripts

for file_info in commands:
    if file_info['name'] == incoming_command:
        file_name = f"{file_info['name']}.py"
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            try:
                subprocess.run(["python", file_path])
                print(f"Ran {file_path} successfully")
            except subprocess.CalledProcessError:
                print(f"Failed to run {file_path}")
        else:
            print(f"File {file_path} not found")
        break  # Stop searching once a match is found
else:
    print(f"No file found with name '{incoming_command}'")