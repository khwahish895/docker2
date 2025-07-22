import streamlit as st
import subprocess

# Whitelist of allowed commands for security
ALLOWED_COMMANDS = {'ls', 'cal', 'date', 'pwd', 'whoami', 'df'}

def run_command(cmd):
    # Extract command name
    cmd_name = cmd.split()[0]
    if cmd_name not in ALLOWED_COMMANDS:
        return "Command not allowed!"
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

st.title("Linux Command Runner (Safe Demo)")

command = st.text_input("Enter a Linux command:", "ls")

if st.button("Run"):
    output = run_command(command)
    st.code(output)
