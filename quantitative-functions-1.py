# COMMAND LINE COMMANDS:
    # cd /Users/romanemeissonnier/Documents/video_intelligence_api
    # source master_env/bin/activate
    # cd master_env
    # /Users/romanemeissonnier/Documents/video_intelligence_api/master_env/bin/python /Users/romanemeissonnier/Documents/video_intelligence_api/master_env/quantitative-functions-1.py

import os 

from google.cloud import videointelligence_v1 as videointelligence

# "gs://00233-uk-master-1/video-test-decryptage.mp4"

list = ["gs://00233-uk-master-1/first_test.mp4"]
gcs_uri = list[0]
length = len(list)
index = 0

while index < length:
    print("\n=============================================================\n")
    print(gcs_uri)
    
    # detect shot changes

    def detect_shot_changes(gcs_uri):
        """Detects camera shot changes."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SHOT_CHANGE_DETECTION]
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": gcs_uri}
    )
    print("\n---### SHOT CHANGES ###---")

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
    print("\n//  NEXT FUNCTION //\n")

    # detect faces
    def detect_faces(gcs_uri="gs://00233-uk-master-1/first_test.mp4"):
        """Detects faces in a video."""

        client = videointelligence.VideoIntelligenceServiceClient()

        # Configure the request
        config = videointelligence.FaceDetectionConfig(
            include_bounding_boxes=True, include_attributes=True
        )
        context = videointelligence.VideoContext(face_detection_config=config)

        # Start the asynchronous request
        operation = client.annotate_video(
            request={
                "features": [videointelligence.Feature.FACE_DETECTION],
                "input_uri": gcs_uri,
                "video_context": context,
            }
        )

        print("\n---### FACE DETECTION ###---")
        result = operation.result(timeout=300)

        print("\nFinished processing.\n")

        # Retrieve the first result, because a single video was processed.
        annotation_result = result.annotation_results[0]

        for annotation in annotation_result.face_detection_annotations:
            print("Face detected:")
            for track in annotation.tracks:
                print(
                    "Segment: {}s to {}s".format(
                        track.segment.start_time_offset.seconds
                        + track.segment.start_time_offset.microseconds / 1e6,
                        track.segment.end_time_offset.seconds
                        + track.segment.end_time_offset.microseconds / 1e6,
                    )
                )

                # Each segment includes timestamped faces that include
                # characteristics of the face detected.
                # Grab the first timestamped face
                timestamped_object = track.timestamped_objects[0]
                box = timestamped_object.normalized_bounding_box
                print("Bounding box:")
                print("\tleft  : {}".format(box.left))
                print("\ttop   : {}".format(box.top))
                print("\tright : {}".format(box.right))
                print("\tbottom: {}".format(box.bottom))

                # Attributes include glasses, headwear, smiling, direction of gaze
                print("Attributes:")
                for attribute in timestamped_object.attributes:
                    print(
                        "\t{}:{} {}".format(
                            attribute.name, attribute.value, attribute.confidence
                    )
                )
    print(detect_faces(gcs_uri))
    print("\n//  NEXT FUNCTION //\n")

    # recognize text

    def recognize_text(gcs_uri):
        """Detect text in a video stored on GCS."""
    from google.cloud import videointelligence

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.TEXT_DETECTION]

    operation = video_client.annotate_video(
        request={"features": features, "input_uri": gcs_uri}
    )

    print("\n---### TEXT DETECTION ###---")
    result = operation.result(timeout=600)

    print("\nFinished processing.")

    # The first result is retrieved because a single video was processed.
    annotation_result = result.annotation_results[0]

    for text_annotation in annotation_result.text_annotations:
        print("\nText: {}".format(text_annotation.text))

        # Get the first text segment
        text_segment = text_annotation.segments[0]
        start_time = text_segment.segment.start_time_offset
        end_time = text_segment.segment.end_time_offset
        print(
            "start_time: {}, end_time: {}".format(
                start_time.seconds + start_time.microseconds * 1e-6,
                end_time.seconds + end_time.microseconds * 1e-6,
            )
        )

        print("Confidence: {}".format(text_segment.confidence))

        # Show the result for the first frame in this segment.
        frame = text_segment.frames[0]
        time_offset = frame.time_offset
        print(
            "Time offset for the first frame: {}".format(
                time_offset.seconds + time_offset.microseconds * 1e-6
            )
        )

    print(recognize_text(gcs_uri))
    index += 1
