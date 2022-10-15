# HavardHackathon AssemblyAI
2022 Harvard Hackathon Project Columbia University / Tecnológico de Monterrey

Uses [AssemblyAI](https://www.assemblyai.com) to detect negative speech in games.
Code based on [this repository](https://github.com/AssemblyAI-Examples/assemblyai-and-python-in-5-minutes).

## Requirements

```bash
$ pip install requests
```

## Usage

Make an account on AssemblyAI.
Make a new file called `.api-key`, and paste your API key into that file.

```bash
$ python transcribe.py audio_file [--local]
```
- audio_file: url to audio file or local path to audio file.
- --local: use if audio_file is a local file.
