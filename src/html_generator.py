import os
from jinja2 import Environment, FileSystemLoader
from .file_utils import copy_attachments, adjust_file_urls
import datetime

def load_templates(template_folder='src/templates'):
    env = Environment(loader=FileSystemLoader(template_folder))
    return {
        'main': env.get_template('main_template.html'),
        'channel': env.get_template('channel_template.html'),
        'index': env.get_template('index_template.html')
    }

def generate_html_pages(messages_by_channel, root_folder, output_folder=f'output/html-{datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")}'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    templates = load_templates()
    channels = list(messages_by_channel.keys())
    
    # Generate index page
    rendered_index_content = templates['index'].render()
    rendered_index = templates['main'].render(title="Home", channels=channels, content=rendered_index_content)
    
    with open(os.path.join(output_folder, 'index.html'), 'w') as file:
        file.write(rendered_index)
    
    for channel, messages in messages_by_channel.items():
        channel_output_folder = os.path.join(output_folder, channel)
        if not os.path.exists(channel_output_folder):
            os.makedirs(channel_output_folder)
        
        copy_attachments(channel, os.path.join(root_folder, channel), output_folder)
        adjust_file_urls(messages, channel)
        
        rendered_channel_content = templates['channel'].render(channel_name=channel, threads=messages)
        rendered_channel = templates['main'].render(title=channel, channels=channels, content=rendered_channel_content)
        
        with open(os.path.join(channel_output_folder, f'{channel}.html'), 'w') as file:
            file.write(rendered_channel)
    
    print(f"HTML website generated in folder: {output_folder}")
