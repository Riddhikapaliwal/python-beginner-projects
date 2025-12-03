# Create a dictionary named test_settings and add some values to it.
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

def add_setting(settings: dict, pair: tuple) -> str:
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, pair: tuple) -> str:
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str) -> str:
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."
    lines = ["Current User Settings:"]
    for k, v in settings.items():
        lines.append(f"{k.capitalize()}: {v}")
    # Ensure the final output ends with a newline character
    return "\n".join(lines) + "\n"