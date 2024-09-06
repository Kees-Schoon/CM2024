import subprocess

# Define commands to be run
command1 = "cd C:/Vscode/AI_jaar_2/Computational_Modelling/CM2024"
command2 = "conda activate cmv2b"
command3 = "jupyter-lab"

# Combine commands with an ampersand
combined_command = f"{command1} & {command2} & {command3}"

# Open a single command prompt and run both commands
subprocess.Popen(["cmd.exe", "/k", combined_command], shell=True)