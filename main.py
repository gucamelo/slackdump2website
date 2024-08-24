from src.emoji_utils import load_emojis
from src.file_utils import copy_attachments, adjust_file_urls
from src.message_processor import read_messages_from_folders, process_message
from src.html_generator import generate_html_pages

def main():
    root_folder = "data/dump"  # Substitua pelo caminho correto dos seus dados
    emojis_file = "data/emojis.json"  # Substitua pelo caminho correto do seu arquivo de emojis
    
    # Carregar emojis
    emojis = load_emojis(emojis_file)
    
    # Ler e processar mensagens
    messages_by_channel = read_messages_from_folders(root_folder, emojis)
    
    # Gerar páginas HTML
    generate_html_pages(messages_by_channel, root_folder)

if __name__ == "__main__":
    main()
