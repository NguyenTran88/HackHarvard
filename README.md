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

There are 2 ways to run the file:
1. Provide an audio file
```bash
$ python main.py audio_file [--local]
```
- audio_file: url to audio file or local path to audio file.
- --local: use if audio_file is a local file.

2. Provide the ID of an already processed audio file on the [AssemblyAI website](https://app.assemblyai.com/processing-queue).
```bash
$ python main.py --id id
```
- id: the id of the processed audio file (e.g. `oris9w0oou-f581-4c2e-9e4e-383f91f7f14d`)
