import os
import json
from datetime import datetime
from .emoji_utils import replace_emojis

def format_timestamp(ts):
    dt = datetime.utcfromtimestamp(float(ts.split('.')[0]))
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def process_message(message, emojis):
    message['text'] = replace_emojis(message.get('text', ''), emojis)
    if 'reactions' in message:
        for reaction in message['reactions']:
            reaction['name'] = replace_emojis(f":{reaction['name']}:", emojis)
    if 'replies' in message:
        for reply in message['replies']:
            reply['text'] = replace_emojis(reply.get('text', ''), emojis)

def read_messages_from_folders(root_folder, emojis):
    messages_by_channel = {}
    
    for channel_name in os.listdir(root_folder):
        channel_path = os.path.join(root_folder, channel_name)
        if os.path.isdir(channel_path):
            channel_messages = {}
            for filename in os.listdir(channel_path):
                if filename.endswith('.json'):
                    filepath = os.path.join(channel_path, filename)
                    with open(filepath, 'r') as file:
                        messages = json.load(file)
                        for message in messages:
                            process_message(message, emojis)
                            message['formatted_ts'] = format_timestamp(message['ts'])
                            if 'replies' in message:
                                for reply in message['replies']:
                                    process_message(reply, emojis)
                            thread_ts = message.get('thread_ts', message['ts'])
                            if thread_ts not in channel_messages:
                                channel_messages[thread_ts] = {
                                    "thread_ts": thread_ts,
                                    "original_message": None,
                                    "replies": []
                                }
                            if message['ts'] == thread_ts:
                                channel_messages[thread_ts]['original_message'] = message
                            else:
                                channel_messages[thread_ts]['replies'].append(message)
            messages_by_channel[channel_name] = sorted(
                channel_messages.values(),
                key=lambda x: x['original_message']['ts']
            )
    
    return messages_by_channel