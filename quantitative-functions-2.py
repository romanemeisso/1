import os 

from google.cloud import videointelligence_v1 as videointelligence

list = ["gs://00233-uk-master-1/first_test.mp4", "gs://00233-uk-master-1/video-test-decryptage.mp4"]
gcs_uri = list[0]
length = len(list)
index = 0

while index < length:
    print("\n")
    print(gcs_uri)
    def detect_person(gcs_uri):
        """Detects people in a video."""

        client = videointelligence.VideoIntelligenceServiceClient()

        # Configure the request
        config = videointelligence.types.PersonDetectionConfig(
            include_bounding_boxes=True,
            include_attributes=True,
            include_pose_landmarks=True,
        )
        context = videointelligence.types.VideoContext(person_detection_config=config)

        # Start the asynchronous request
        operation = client.annotate_video(
            request={
                "features": [videointelligence.Feature.PERSON_DETECTION],
                "input_uri": gcs_uri,
                "video_context": context,
            }
        )

        print("\nPerson detection annotations:")
        result = operation.result(timeout=300)

        print("Finished processing.")

        # Retrieve the first result, because a single video was processed.
        annotation_result = result.annotation_results[0]

        for annotation in annotation_result.person_detection_annotations:
            print("Person detected:")
            for track in annotation.tracks:
                print(
                    "Segment: {}s to {}s".format(
                        track.segment.start_time_offset.seconds
                        + track.segment.start_time_offset.microseconds / 1e6,
                        track.segment.end_time_offset.seconds
                        + track.segment.end_time_offset.microseconds / 1e6,
                    )
                )

                # Each segment includes timestamped objects that include
                # characteristics - -e.g.clothes, posture of the person detected.
                # Grab the first timestamped object
                timestamped_object = track.timestamped_objects[0]
                box = timestamped_object.normalized_bounding_box
                print("Bounding box:")
                print("\tleft  : {}".format(box.left))
                print("\ttop   : {}".format(box.top))
                print("\tright : {}".format(box.right))
                print("\tbottom: {}".format(box.bottom))

                # Attributes include unique pieces of clothing,
                # poses, or hair color.
                print("Attributes:")
                for attribute in timestamped_object.attributes:
                    print(
                        "\t{}:{} {}".format(
                            attribute.name, attribute.value, attribute.confidence
                        )
                    )

                # Landmarks in person detection include body parts such as
                # left_shoulder, right_ear, and right_ankle
                print("Landmarks:")
                for landmark in timestamped_object.landmarks:
                    print(
                        "\t{}: {} (x={}, y={})".format(
                            landmark.name,
                            landmark.confidence,
                            landmark.point.x,  # Normalized vertex
                            landmark.point.y,  # Normalized vertex
                        )
                    )
    print(detect_person(gcs_uri))
    index += 1
