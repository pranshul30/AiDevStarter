import os
import subprocess
import sys

def setup_project(project_name, packages):
    """
    Creates a project directory, sets up a virtual environment,
    and installs specified packages.
    """
    try:
        # 1. Create the project directory
        print(f"--- Creating project directory: {project_name} ---")
        os.makedirs(project_name, exist_ok=True)

        # 2. Set up the virtual environment
        venv_path = os.path.join(project_name, 'venv')
        print(f"--- Creating virtual environment in: {venv_path} ---")
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)

        # 3. Determine the correct pip executable path based on OS
        if sys.platform == "win32":
            pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')
        else:
            pip_executable = os.path.join(venv_path, 'bin', 'pip')
            
        # 4. Install the specified packages
        print(f"--- Installing packages: {', '.join(packages)} ---")
        for package in packages:
            print(f"Installing {package}...")
            subprocess.run([pip_executable, 'install', package], check=True)
        
        print("\n✅ Project setup complete!")
        print(f"To get started, run: cd {project_name} && source venv/bin/activate")

    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred: {e}")
        print("Please check your Python/pip installation and try again.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")