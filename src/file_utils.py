import os
import shutil

def copy_attachments(channel_name, source_folder, destination_folder):
    source_attachments_folder = os.path.join(source_folder, "attachments")
    dest_attachments_folder = os.path.join(destination_folder, channel_name, "attachments")
    
    if os.path.exists(source_attachments_folder):
        if not os.path.exists(dest_attachments_folder):
            os.makedirs(dest_attachments_folder)
        for item in os.listdir(source_attachments_folder):
            s = os.path.join(source_attachments_folder, item)
            d = os.path.join(dest_attachments_folder, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print(f"Copied attachments for {channel_name} to {dest_attachments_folder}")
    else:
        print(f"No attachments folder found for {channel_name}.")

def adjust_file_urls(messages, channel_name):
    for thread in messages:
        if thread['original_message'] and "files" in thread['original_message']:
            for file in thread['original_message']["files"]:
                file_name = f"{file['id']}-{file['name']}"
                file["url_private"] = os.path.join("attachments", file_name)
        for reply in thread['replies']:
            if "files" in reply:
                for file in reply["files"]:
                    file_name = f"{file['id']}_{file['name']}"
                    file["url_private"] = os.path.join("attachments", file_name)
