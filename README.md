# AI-voice-assistant
The initial idea for this voice assistant was to be able to have a natural conversation with an AI assistant that uses speech to speech as a primary interface and is able to assist with specific tasks. A specific task we had in mind was to create a short 3 minute executive summary for a project showcase. The exec summary would include spoken narration by the AI assistant, and a visual medium such as a powerpoint slide or a video.

## Breaking down the challenge
This idea can be broken down into the following components, each of which has some difficulty to it:

- [ ] Speech to speech interaction
- [ ] A more natural conversation that includes lots of back and forth
- [ ] Generation of the script for the AI assistant to narrate
- [ ] Generation of a good powerpoint slide by the AI assistant

## High level options for each challenge

### Speech to speech interaction

- OpenAI Whisper (https://github.com/openai/whisper)
Great open source speech recognition model that can run locally.
- PyAudio 
Python library to allow for audio to be captured either live from a microphone or from a file and passed to something like Whisper for speech recognition to be performed.


### Natural conversation

content to be added

### Narrative script generation

content to be added

### PowerPoint slide generation

- python-pptx (https://python-pptx.readthedocs.io/en/latest/)
- pyppt (https://github.com/vfilimonov/pyppt/blob/master/README.md)
- ReportLab (https://docs.reportlab.com/)