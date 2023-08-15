# Step 1: While-loop-test.py
code snippet source:
- https://cloud.google.com/video-intelligence/docs/analyze-shots

what I'm trying to do:

I'm using Google Cloud Video Intelligence API to analyze videos for a project. I have a list of videos stored in a bucket that I want to analyze using the shot change detection function from Video Intelligence. I want to create a while loop to iterate through my list of videos. So far, I don't know how to go to the next index of my list at the end of my loop.

# Step 2: Quantitative-functions-all.py
code snippet sources:
- https://cloud.google.com/video-intelligence/docs/face-detection
- https://cloud.google.com/video-intelligence/docs/people-detection
- https://cloud.google.com/video-intelligence/docs/analyze-shots
- https://cloud.google.com/video-intelligence/docs/text-detection

error:
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
# Step 3: Quantitative-functions-1.py & Quantitative-functions-2.py

Alternative to fix the previous error: Put the detect-person function in a separate file (it runs perfectly when put in a separate file)
