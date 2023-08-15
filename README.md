# Project

I need to analyze the visual content of videos for a research project. This analysis aims at looking for correlations between the amount of views and different visual elements of YouTube video in order to determine whether or not there are specific elements that help boost the popularity of these videos in terms of views. For this project, I focus on French popular science videos.

I have a list of videos for which I want to analyse :
- if there are people appearing on screen and if so, what are their characteristics;
- if there is text appearing on screen and if so, how often;
- and how many shots there are per minute.

# Tools

I'm using [Google Cloud Video Intelligence API](https://cloud.google.com/video-intelligence/docs). The videos are stored in a bucket using 4 functions function from Video Intelligence: face-detection, people-detection, analyze-shots and text-detection.
I installed the Google Cloud Library locally and I'm using Python to work with the API in a virtual environment.

### Troubleshooting the local installation of Video Intelligence
#### ModuleNotFound
```
Traceback (most recent call last):
  File "/Users/romanemeissonnier/Script pour Hugo.svg", line 3, in <module>
    from google.oauth2 import service_account
ModuleNotFoundError: No module named 'google'
```
Solution: [https://sebhastian.com/python-no-module-named-google-cloud](https://sebhastian.com/python-no-module-named-google-cloud/#:~:text=In%20summary%2C%20the%20ModuleNotFoundError%3A%20No,Google%20Cloud%20API%20using%20pip). Section: "Issue with IDE using a different Python version"

#### <function … at 0x…>
Solution: add a `print(function_name(gcs_uri)` at the end of each function.

# Process

1. Create a loop that will run through all 4 functions we want to use (test it out with one function and 2 iterations first).
2. Combined the 4 functions into 1 file.
3. Remove the outputs from the functions that are unecessary for my projet.

## Step 1: While-loop-test.py
Code snippet source:
- https://cloud.google.com/video-intelligence/docs/analyze-shots

## Step 2: Quantitative-functions-all.py
Code snippets sources:
- https://cloud.google.com/video-intelligence/docs/face-detection
- https://cloud.google.com/video-intelligence/docs/people-detection
- https://cloud.google.com/video-intelligence/docs/analyze-shots
- https://cloud.google.com/video-intelligence/docs/text-detection

Error:
```
Traceback (most recent call last):
  File "/Users/romanemeissonnier/Documents/video_intelligence_api/master_env/quantitative-functions-all.py", line 119, in <module>
    print(detect_person(gcs_uri))
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/romanemeissonnier/Documents/video_intelligence_api/master_env/quantitative-functions-all.py", line 50, in detect_person
    config = videointelligence.types.PersonDetectionConfig(
             ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'google.cloud.videointelligence' has no attribute 'types'
```
## Step 3: Quantitative-functions-1.py & Quantitative-functions-2.py

Alternative to fix the previous error: Put the detect-person function in a separate file (it runs perfectly when put in a separate file)
