import os 

from google.cloud import videointelligence_v1 as videointelligence

list = ["gs://00233-uk-master-1/first_test.mp4", "gs://00233-uk-master-1/video-test-decryptage.mp4"]
gcs_uri = list[0]
length = len(list)
index = 0
while index < length:
    def detect_shot_changes(gcs_uri):
        """Detects camera shot changes."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SHOT_CHANGE_DETECTION]
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": gcs_uri}
    )
    print("\nProcessing video for shot change annotations:")

    result = operation.result(timeout=90)
    print("\nFinished processing.")

    # first result is retrieved because a single video was processed
    for i, shot in enumerate(result.annotation_results[0].shot_annotations):
        start_time = (
            shot.start_time_offset.seconds + shot.start_time_offset.microseconds / 1e6
        )
        end_time = (
            shot.end_time_offset.seconds + shot.end_time_offset.microseconds / 1e6
        )
        print("\tShot {}: {} to {}".format(i, start_time, end_time))

    print(detect_shot_changes(gcs_uri))
    list[index] += 1