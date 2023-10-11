# First Place!!!🏆🏆🏆🏆
[Devpost Page](https://devpost.com/software/noname-pht40q?ref_content=my-projects-tab&ref_feature=my_projects)
 
 # No Notes (HappyHacks October 2023 Project 

## Overview

The **No Notes** app is a powerful tool that allows users to record audio and automatically convert it into text notes using advanced AI technology. This app is designed to simplify the process of transcribing spoken words, making it easier to capture and organize information from meetings, interviews, lectures, and more. With its user-friendly interface and robust AI capabilities, this app is perfect for professionals, students, and anyone looking to streamline the process of converting spoken content into written notes.

## Features

- **Audio Recording**: Easily record audio using your device's microphone.
- **Transcription**: The app transcribes the audio into text.
- **Notes**: Uses AI to turn your raw audio into summarized point-form notes.
- **Save Notes**: Save your transcriptions, and transcribed notes for easy access.
- **Secure and Private**: Your audio and transcribed notes are kept private and secure.

## Installation

To install the **No Notes** app, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Alex-Jando/HappyHack-Oct2023
   ```

2. Navigate to the app's directory:

   ```bash
   cd HappyHack-October2023
   ```

3. Install the necessary packages:

   ```bash
   .\setup.bat
   ```

   __OR__

   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   python -c "import nltk;nltk.download('punkt')"
   ```

5. Start the app:

   ```bash
   python src/main.py
   ```

The app will be accessible in your web browser at `http://localhost:80`.
It may take a few minutes to configure the AI the first time it's run.

## Usage

1. Open the **No Notes** app in your web browser.
2. Click the "Record" button to start recording audio.
3. Speak clearly into your device's microphone.
4. Press the "Stop" button when you're finished recording.
5. Watch as the app transcribes your audio into text notes.
6. Click "Save" to store your transcription, and transcribed notes for later reference.
7. Export your notes in your preferred format or share them with       others.
8. Click the notes icon and view your saved notes

## Configuration

You can customize the app's behavior by modifying the arguments passed when running the `main.py` file.

```bash
python src/main.py --ip "HOST IP" --port "HOST PORT"
```

## Dependencies

The **No Notes** app uses the following packages:

- flask
- requests
- bert-extractive-summarizer
- speechrecognition
- torch
- pydub
- record.js

## License

This project is licensed under the [MIT License](LICENSE.md).

---

Thank you for using the **No Notes** app. We hope it enhances your productivity and simplifies the process of turning audio recordings into valuable text notes. If you have any questions or encounter issues, please don't hesitate to reach out to us.
