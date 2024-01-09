# googlepycraft/__init__.py

import subprocess
import sys
import os
import time

def run_begin_script():
    script_path = os.path.join(os.path.dirname(__file__), 'begin.py')
    subprocess.run([sys.executable, script_path])


def show_loading_animation():
    print("Installing \033[94mgooglepycraft start files\033[0m package...")

    animation_chars = ["\033[96m⠋\033[0m", "\033[96m⠙\033[0m", "\033[96m⠹\033[0m", "\033[96m⠸\033[0m", "\033[96m⠼\033[0m", "\033[96m⠴\033[0m", "\033[96m⠦\033[0m", "\033[96m⠧\033[0m", "\033[96m⠇\033[0m", "\033[96m⠏\033[0m"]
    
    for _ in range(20):
        for char in animation_chars:
            time.sleep(0.1)
            sys.stdout.write("\r" + f"Running script {char} ")
            sys.stdout.flush()

    print("\nInstallation complete: [app_config.yaml, workfile.py].")
# loading animation
show_loading_animation()

# Running begin.py script
run_begin_script()
