# Voice Assistant Project

This project is a simple voice assistant built using Python. It can perform various tasks like playing music from YouTube, telling the current time, fetching information from Wikipedia, telling jokes, and sending WhatsApp messages.

## Features

- **Voice Recognition**: The assistant uses the SpeechRecognition library to recognize voice commands.
- **Text-to-Speech**: It utilizes the pyttsx3 library to convert text to speech for responses.
- **Task Execution**: The assistant can execute tasks like playing music, fetching information, telling jokes, and sending WhatsApp messages based on voice commands.
- **Wikipedia Integration**: It can provide brief information about a person or topic by fetching data from Wikipedia.
- **YouTube Music Player**: The assistant can play songs from YouTube using the pywhatkit library.

## Requirements

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)
- pyttsx3 library (`pip install pyttsx3`)
- pywhatkit library (`pip install pywhatkit`)
- Wikipedia library (`pip install wikipedia`)
- pyjokes library (`pip install pyjokes`)

## Usage

1. Clone the repository:

    ```
    git clone https://github.com/your_username/voice-assistant.git
    ```

2. Navigate to the project directory:

    ```
    cd voice-assistant
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the script:

    ```
    python voice_assistant.py
    ```

5. Start speaking commands prefixed with "Alexa".

## Commands

- **Play [song_name]**: Plays the specified song from YouTube.
- **Time**: Tells the current time.
- **Who [person_name]**: Provides a brief summary of the specified person from Wikipedia.
- **Date**: Responds humorously about having a boyfriend.
- **Are you single?**: Responds humorously about being in a relationship with Wi-Fi.
- **Joke**: Tells a random joke.
- **Send message**: Sends a WhatsApp message. It will prompt for the recipient and the message.

## Author

- Your Name
- GitHub: [Your GitHub Profile](https://github.com/your_username)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
