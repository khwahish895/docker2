import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", f"Exception: {e}"

# ---------------------------------------
# 1. Terminal Interface
# ---------------------------------------
def terminal_mode():
    print("🔧 Linux Command Runner (CLI Mode)")
    print("Type 'exit' to quit.\n")
    while True:
        cmd = input("💻 Enter Linux command: ")
        if cmd.lower() in ['exit', 'quit']:
            break
        out, err = run_command(cmd)
        print("📤 Output:\n", out)
        if err:
            print("⚠️ Error:\n", err)

# ---------------------------------------
# 2. Flask Web Interface
# ---------------------------------------
def flask_mode():
    from flask import Flask, request, render_template_string
    app = Flask(__name__)
    TEMPLATE = '''
    <!DOCTYPE html>
    <html>
    <head><title>Linux Command Executor</title></head>
    <body style="font-family: Arial; background-color: #222; color: #eee; padding: 30px;">
        <h1>🖥️ Linux Command Executor (Flask)</h1>
        <form method="post">
            <input name="command" style="width: 500px;" placeholder="Enter Linux command">
            <button type="submit">Run</button>
        </form>
        {% if output %}
        <h3>📤 Output:</h3>
        <pre style="background-color: #333; padding: 10px;">{{ output }}</pre>
        {% endif %}
    </body>
    </html>
    '''
    @app.route('/', methods=['GET', 'POST'])
    def index():
        output = ""
        if request.method == 'POST':
            cmd = request.form['command']
            out, err = run_command(cmd)
            output = out or err
        return render_template_string(TEMPLATE, output=output)

    app.run(debug=True)

# ---------------------------------------
# 3. Streamlit Interface
# ---------------------------------------
def streamlit_mode():
    import streamlit as st
    st.set_page_config(page_title="Linux Command Runner", layout="centered")
    st.title("💻 Linux Command Executor (Streamlit)")

    cmd = st.text_input("Enter Linux Command", placeholder="e.g. ls -la")
    if st.button("Run"):
        if cmd:
            out, err = run_command(cmd)
            if out:
                st.success("📤 Output:")
                st.code(out)
            if err:
                st.error("⚠️ Error:")
                st.code(err)

# ---------------------------------------
# Entry Point
# ---------------------------------------
if __name__ == "__main__":
    print("Choose Mode:\n1. Terminal\n2. Flask Web UI\n3. Streamlit Dashboard")
    choice = input("Enter 1 / 2 / 3: ")

    if choice == '1':
        terminal_mode()
    elif choice == '2':
        flask_mode()
    elif choice == '3':
        streamlit_mode()
    else:
        print("❌ Invalid choice. Exiting.")
