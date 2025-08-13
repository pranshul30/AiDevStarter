import os
import google.generativeai as genai
import json

def get_packages_for_project(description):
    """
    Uses the Gemini API to get a list of recommended packages for a project.
    """
    # Ensure the API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
    
    genai.configure(api_key=api_key)

    # This is a Pydantic-style schema that tells the model how to format its response.
    # It ensures the output is always a clean JSON object.
    generation_config = {
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "object",
            "properties": {
                "packages": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    }

    # The prompt is carefully engineered to guide the AI.
    prompt = f"""
    Based on the following project description, identify the essential Python packages needed to get started.
    Return your answer as a JSON object with a single key "packages" which contains a list of the package names.
    
    Do not include packages that are part of the standard Python library (e.g., os, sys).
    Only include the base packages needed. For example, for a "fastapi web server", you only need "fastapi" and "uvicorn".
    
    Project Description: "{description}"
    """

    try:
        print("\n--- 🧠 Contacting AI to get package recommendations... ---")
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt, generation_config=generation_config)
        
        # The response text will be a JSON string, so we parse it.
        result = json.loads(response.text)
        packages = result.get("packages", [])
        
        if not packages:
            print("--- ⚠️ AI did not suggest any packages. Please try a more descriptive prompt. ---")
            return []
            
        print("--- ✨ AI Recommended Packages: ---")
        print(", ".join(packages))
        return packages

    except Exception as e:
        print(f"❌ An error occurred while contacting the AI: {e}")
        return None

