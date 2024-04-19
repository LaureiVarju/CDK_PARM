import os
import importlib

def import_functions(folder_path):
    with open(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.py'):
                module_name = file_name[:-3]  # Remove the .py extension
                module = importlib.import_module(f'slash_commands.{module_name}')
                function_name = module_name  # Assuming function name matches the module name
                if hasattr(module, function_name):
                    function = getattr(module, function_name)
                    yield function

def execute_slash_command(command_name, optional_parameters):
    functions = {func.__name__: func for func in import_functions(folder_path)}
    if command_name in functions:
        return functions[command_name](optional_parameters)
    else:
        print(f"Error: '{command_name}' command not found.")


# Get the folder path relative to the current directory
folder_path = os.path.join(os.path.dirname(__file__), "slash_commands")
print(f'folder path is {folder_path}')

# print(execute_slash_command("hello", ""))

