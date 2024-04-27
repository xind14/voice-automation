# Voice Automation - Hey Ayana

## Version 1: Voice Assistant for YouTube Search

This Python project implements a voice assistant that allows users to interactively search for videos on YouTube using voice commands. It combines speech recognition capabilities, web automation with Selenium, and text-to-speech functionality.

### Features

1. **Voice Recognition**: Utilizes the `speech_recognition` library to recognize voice commands from the user.
2. **Text-to-Speech Response**: Converts textual responses into speech using the `gtts` (Google Text-to-Speech) library and plays them back to the user.
3. **Web Automation**: Utilizes Selenium WebDriver to open Google Chrome and perform searches on YouTube based on user input.
4. **Interactive Interaction**: The assistant responds to specific wake-up phrases ("hey ayana") and engages in a conversation loop until the user exits.

### Dependencies

- `speech_recognition`: for speech recognition functionality.
- `selenium`: for web automation tasks.
- `pydub`: for audio manipulation, specifically converting TTS output to a playable format.
- `gtts`: for text-to-speech functionality.
- `os`: for system-level operations.
- `time`: for time-related operations.

### Usage

1. **Voice Interaction**: The user interacts with the assistant by speaking commands, such as "hey ayana, search YouTube for cats".
2. **Web Search**: Upon receiving a search command, the assistant opens Google Chrome, navigates to YouTube, and performs the requested search.
3. **Response Feedback**: The assistant provides feedback on actions taken, such as confirming successful searches or notifying the user about unrecognized commands.
4. **Exiting**: The user can exit the program by saying "exit".

### Setup

1. Install the required Python libraries using `pip`:

   ```bash
   pip install speech_recognition selenium pydub gtts
   ```

2. Ensure you have the necessary drivers for Selenium WebDriver (e.g., ChromeDriver for Google Chrome) installed and configured properly.

### Running the Program

1. Run the Python script `python voice_automation/voice_automation.py`.
2. Speak the wake-up phrase "hey ayana" followed by your command (e.g., "search YouTube for dogs").
3. Interact with the assistant as needed, following the prompts and responses.

### Notes

- Make sure your system has a working microphone for speech input and speakers/headphones for TTS output.
- Customize wake-up phrases, responses, and additional functionalities as desired within the code.

