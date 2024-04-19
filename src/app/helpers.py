
# import yaml
# import os
# import subprocess

# with open ("../../discord_commands.yaml", "r") as file:
# 	yaml_content = file.read()

# commands = yaml.safe_load(yaml_content)
# folder_path = "slash_commands"  # Path to the folder containing the scripts

# print(commands)

# def execute_slash_command(incoming_command):
#     for file_info in commands:
#         if file_info['name'] == incoming_command:
#             file_name = f"{file_info['name']}.py"
#             file_path = os.path.join(folder_path, file_name)
#             print(os.path.exists(file_path))
#             if os.path.exists(file_path):
#                 try:
#                     #another helper in here
#                     # output = subprocess.check_output(['python', file_path])
#                     output = subprocess.check_output(['python', file_path], universal_newlines=True)
#                     # output = pickle.loads(output)
#                     # subprocess.run(["python", file_path])
#                     print(f"Ran {file_path} successfully")
#                     print(f"output is {output}")
#                     return output
#                     # return process here
#                 except subprocess.CalledProcessError:
#                     print(f"Failed to run {file_path}")
#             else:
#                 print(f"File {file_path} not found")
#             break  # Stop searching once a match is found
#     else:
#         print(f"No file found with name '{incoming_command}'")


# execute_slash_command('hello')


#################
import os
import subprocess

folder_path = "slash_commands"  # Path to the folder containing the scripts

def execute_slash_command(incoming_command):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)
    for file_name in files:
        # Check if the file name matches the incoming command
        if file_name.startswith(incoming_command) and file_name.endswith(".py"):
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                try:
                    # Execute the script and capture its output
                    output = subprocess.check_output(['python', file_path], universal_newlines=True)
                    print(f"Ran {file_path} successfully")
                    print(f"output is {output}")
                    return output
                except subprocess.CalledProcessError:
                    print(f"Failed to run {file_path}")
                break  # Stop searching once a match is found
    else:
        print(f"No file found with name '{incoming_command}'")


# Example usage


print(type(execute_slash_command('hello')))