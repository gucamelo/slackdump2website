import json

def load_emojis(emojis_file):
    with open(emojis_file, 'r') as file:
        return json.load(file)

def replace_emojis(text, emojis):
    for shortcode, url in emojis.items():
        text = text.replace(f":{shortcode}:", f'<img src="{url}" alt="{shortcode}" class="emoji">')
    return text
