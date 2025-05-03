# Audio Transcription with AssemblyAI



A lightweight Python script and workflow for uploading local audio files to the [AssemblyAI](https://www.assemblyai.com/) REST API, requesting an asynchronous transcription job, polling until completion, and saving the transcript to a text file.

---

##  Features

- **Chunked Upload**: Streams audio in 5 MB chunks to avoid timeouts and large memory spikes.  
- **Asynchronous Transcription**: Submits your file and immediately returns a job ID—no need to block your script.  
- **Polling Loop**: Checks the job status every few seconds (configurable) until it’s done or errors out.  
- **Interactive Output Naming**: Prompt for a friendly output filename, automatically suffixed with `.txt`.  
- **Batch-Processing Ready**: Easily wrap the workflow in a loop to process entire directories of audio files.  

---

## 📋 Prerequisites

- **Python 3.7+**  
- **[requests](https://pypi.org/project/requests/)** library  
  ```bash

## 🎬 Usage

1. **Prepare your audio files**  
   Make sure your audio files are ready for transcription.

2. **Place them in the same level
