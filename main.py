from scaffolder import setup_project
from ai_module import get_packages_for_project
import os

def run():
    """
    Main function to run the AI Dev-Starter application.
    """
    print("--- Welcome to the AI Dev-Starter! ---")
    
    try:
        # Get user input for the project
        project_name = input("Enter the name for your new project folder: ")
        project_description = input("Describe the project you want to build: ")

        # Get package recommendations from the AI
        packages_to_install = get_packages_for_project(project_description)

        # If AI fails or returns no packages, exit gracefully.
        if packages_to_install is None or not packages_to_install:
            print("\nCould not determine packages. Exiting.")
            return

        # --- This is our crucial security step: User Confirmation ---
        print(f"\nI am about to perform the following actions:")
        print(f"1. Create a new folder named '{project_name}'.")
        print(f"2. Set up a Python virtual environment inside it.")
        print(f"3. Install the following AI-recommended packages: {', '.join(packages_to_install)}")
        
        confirm = input("\nDo you want to proceed? (y/n): ")
        if confirm.lower() == 'y':
            setup_project(project_name, packages_to_install)
        else:
            print("Operation cancelled by user.")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred in the main application: {e}")

if __name__ == "__main__":
    # Check for API key before running
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ GOOGLE_API_KEY environment variable not found.")
        print("Please set it before running the application.")
    else:
        run()