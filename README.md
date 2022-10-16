# HavardHackathon AssemblyAI Challenge
2022 Harvard Hackathon Project Columbia University / Tecnológico de Monterrey

Uses [AssemblyAI](https://www.assemblyai.com) to detect negative speech in games.
Code based on [this repository](https://github.com/AssemblyAI-Examples/assemblyai-and-python-in-5-minutes).

## Requirements

```bash
$ pip install requests
$ pip install matplotlib
```

## Usage

Make an account on AssemblyAI.
Make a new file called `.api-key`, and paste your API key into that file.

There are 2 ways to run the file:
1. Provide an audio file. Place the audio file in the same folder as the main.py script, or upload the audio file to an external service (e.g. Google Drive or DropBox) and provide a direct download link.
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
# Our Project

Assembly AI *Name* is a detection system for harmful speeches in online video games. Using AssemblyAI’s Audio Intelligence APIs, we can distinguish players who display verbally abusive behaviors in the video game community. Data extracted is plotted to have track of the possible abusive language along the video or streaming. Thus, large video game companies and streaming platforms can use this data-monitoring to identify the most toxic users to create a safer environment for their community. We are willing to take part in the new generation of voice-controlled games and streaming. 

## Problematics

Gaming is a competitive environment where the majority of members in the gaming community resorts to bullying. What’s more, even with today’s security technology, the online gaming industry still suffers from endless negative users practicing violence, cyberbullying, hate speech, harassment, death threats, and direct attacks against different groups of people including minors. Bullying victims generally face verbal harassment in multiplayer lobbies and in-game chats. According to ResearchGate & ScienceDaily, cyberbullying victims are 1.9 times more likely to commit suicide. 
 
How are companies dealing with this problem? 
 
Video game companies detect toxic players via in-game reporting which most of the time, is not quite precise. Additionally, games like Clash of Clans use a text detection system that only replaces the ‘inappropriate’ words with asterisks. However, these prevention methods have not been helpful at all, since cyberbullying statistics do nothing but to increase daily. 

## What is *name*?

With AssemblyAI Audio Intelligence Content Monitoring and Sentiment Analysis APIs, video game companies could monitor users and finally implement a secure system by training the AI based on every user’s audio files;  thus, detecting if any sensitive content is spoken in those files and pinpointing exactly when and what was spoken so that after a short period, Our final aim is to make train the system so that it can successfully identify when someone is just joking around and when it is being an intentional threat, insult, and so on. For each audio we generate a graph to better comprehend the harmful behavior of each user. Therefore, these video game platforms could finally create a safe and regulated environment for all players and try to eliminate negative and toxic users once and for all. 

## Tech implementation / Tools 

1. AssemblyAI Audio Intelligence:
        - Content Moderation API
        - Sentiment Analysis API

2. VS Code
3. Python
   - matplotlib.pyplot to generate graphs and figures
   - Requests module to create HTTP requests to interact with API
   
## Mission 

Thanks to this protection implementation, thousands of gaming users will safely coexist with each other in both a well-protected and monitored environment. Understanding the severity and confidence of the scores accurately will allow us to detect the intentions of the user so companies can identify them, take further action, and prevent mental health issues such as suicide. Our goal is to find only those hurtful comments without restricting the users to express themselves with others. Implementing this project correctly will make the detection more efficient and as a result, users won’t have to worry about reporting toxic players on their own anymore.
 
We are aware that these APIs are available to the public and are ready to use in practically no time. Nonetheless, what we do with them is what matters. Having a groundbreaking technology means nothing if it does not have a beneficial purpose and positive impact on the community.

## What we learned:
            
During the last 36 hours, we learned to think outside the box, challenge ourselves, and acquire skills we never thought we could gain. Furthermore, meeting incredible people who took this experience to the next level has been a privilege; realizing that we can create something beneficial and unique in such a short time is truly remarkable.

## Possible setbacks / Next steps: 
 
- Possible Setbacks: 

Some companies might not be willing to change or replace their current user’s security/protection systems. 
Users flow could decrease due to these restrictions.
Conflict of interest.
 
- Next Steps: 

Using machine learning to increase the accuracy of the program to fulfill the goal of correctly identifying if a player is truly bothering or joking with others. 
Provide a more effective visual and detailed analysis of each detected toxic user to ease the data outcome interpretation. We are looking only for toxic users to make a healthier environment. 
