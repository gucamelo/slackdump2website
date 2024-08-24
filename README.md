# Slack Archive Project - slackdump2website

This project converts exported Slack messages into an HTML view.
I'm open to changes to the project. I did this very fast to get a minimal copy of a slack workspace with their latest change in its policy regarding data conservation.

## Project Structure

The project should have the following structure:
```
slackdump2website/ 
│
├── src/ 
│   ├── init.py 
│   ├── emoji_utils.py 
│   ├── file_utils.py 
│   ├── message_processor.py
│   ├── html_generator.py
│   ├── main.py
│   └── templates/
│       ├── main_template.html
│       ├── channel_template.html
│       └── index_template.html
│   
├── data/
│       ├── emojis.json
│       └── dump/
│
├── output/
│
├── requirements.txt
└── README.md
```

## Prerequisites

Make sure you have Python 3.6 or higher installed.

## Setting Up the Environment

1. **Clone the Repository**

   If you haven't cloned the repository yet, do so:

   ```bash
   git clone https://github.com/your_username/your_repository.git slackdump2website
   cd slackdump2website
   ```
2. **Install the Dependencies**

    Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

To generate the HTML view of the exported message files:

1. Run the Main Script

    ```bash
    python main.py
    ```

    This will process the data and generate HTML files in the output/ folder.
    Check the output Folder and you will see a folder with the date and time of when it was generated
2. Serve the page as a webserver
    
    You can serve the page anyway you want but if you're a beginner you can run this code
   ```bash
   python3 -m http.server 8080
   ```
   And you can access it from your browser at http://localhost:8080

# Contributing

If you wish to contribute to this project, please follow these steps:
  1. **Fork the repository.**
  2. **Create a branch for your modification.**
  3. **Commit your changes.**
  4. **Submit a pull request.**
