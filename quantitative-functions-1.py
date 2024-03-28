import os 

from google.cloud import videointelligence_v1 as videointelligence

index = 0
list = ["gs://00233-uk-master-1/VID1.mp4","gs://00233-uk-master-1/VID2.mp4","gs://00233-uk-master-1/VID3.mp4","gs://00233-uk-master-1/VID4.mp4","gs://00233-uk-master-1/VID5.mp4","gs://00233-uk-master-1/VID6.mp4","gs://00233-uk-master-1/VID7.mp4","gs://00233-uk-master-1/VID8.mp4","gs://00233-uk-master-1/VID9.mp4","gs://00233-uk-master-1/VID10.mp4","gs://00233-uk-master-1/VID11.mp4","gs://00233-uk-master-1/VID12.mp4","gs://00233-uk-master-1/VID13.mp4","gs://00233-uk-master-1/VID14.mp4","gs://00233-uk-master-1/VID15.mp4","gs://00233-uk-master-1/VID16.mp4","gs://00233-uk-master-1/VID17.mp4","gs://00233-uk-master-1/VID18.mp4","gs://00233-uk-master-1/VID19.mp4","gs://00233-uk-master-1/VID20.mp4","gs://00233-uk-master-1/VID21.mp4","gs://00233-uk-master-1/VID22.mp4","gs://00233-uk-master-1/VID23.mp4","gs://00233-uk-master-1/VID24.mp4","gs://00233-uk-master-1/VID25.mp4","gs://00233-uk-master-1/VID26.mp4","gs://00233-uk-master-1/VID27.mp4","gs://00233-uk-master-1/VID28.mp4","gs://00233-uk-master-1/VID29.mp4","gs://00233-uk-master-1/VID30.mp4","gs://00233-uk-master-1/VID31.mp4","gs://00233-uk-master-1/VID32.mp4","gs://00233-uk-master-1/VID33.mp4","gs://00233-uk-master-1/VID34.mp4","gs://00233-uk-master-1/VID35.mp4","gs://00233-uk-master-1/VID36.mp4","gs://00233-uk-master-1/VID37.mp4","gs://00233-uk-master-1/VID38.mp4","gs://00233-uk-master-1/VID39.mp4","gs://00233-uk-master-1/VID40.mp4","gs://00233-uk-master-1/VID41.mp4","gs://00233-uk-master-1/VID42.mp4","gs://00233-uk-master-1/VID43.mp4","gs://00233-uk-master-1/VID44.mp4","gs://00233-uk-master-1/VID45.mp4","gs://00233-uk-master-1/VID46.mp4","gs://00233-uk-master-1/VID47.mp4","gs://00233-uk-master-1/VID48.mp4","gs://00233-uk-master-1/VID49.mp4","gs://00233-uk-master-1/VID50.mp4","gs://00233-uk-master-1/VID51.mp4","gs://00233-uk-master-1/VID52.mp4","gs://00233-uk-master-1/VID53.mp4","gs://00233-uk-master-1/VID54.mp4","gs://00233-uk-master-1/VID55.mp4","gs://00233-uk-master-1/VID56.mp4","gs://00233-uk-master-1/VID57.mp4","gs://00233-uk-master-1/VID58.mp4","gs://00233-uk-master-1/VID59.mp4","gs://00233-uk-master-1/VID60.mp4","gs://00233-uk-master-1/VID61.mp4","gs://00233-uk-master-1/VID62.mp4","gs://00233-uk-master-1/VID63.mp4","gs://00233-uk-master-1/VID64.mp4","gs://00233-uk-master-1/VID65.mp4","gs://00233-uk-master-1/VID66.mp4","gs://00233-uk-master-1/VID67.mp4","gs://00233-uk-master-1/VID68.mp4","gs://00233-uk-master-1/VID69.mp4","gs://00233-uk-master-1/VID70.mp4","gs://00233-uk-master-1/VID71.mp4","gs://00233-uk-master-1/VID72.mp4","gs://00233-uk-master-1/VID73.mp4","gs://00233-uk-master-1/VID74.mp4","gs://00233-uk-master-1/VID75.mp4","gs://00233-uk-master-1/VID76.mp4","gs://00233-uk-master-1/VID77.mp4","gs://00233-uk-master-1/VID78.mp4","gs://00233-uk-master-1/VID79.mp4","gs://00233-uk-master-1/VID80.mp4","gs://00233-uk-master-1/VID81.mp4","gs://00233-uk-master-1/VID82.mp4","gs://00233-uk-master-1/VID83.mp4","gs://00233-uk-master-1/VID84.mp4","gs://00233-uk-master-1/VID85.mp4","gs://00233-uk-master-1/VID86.mp4","gs://00233-uk-master-1/VID87.mp4","gs://00233-uk-master-1/VID88.mp4","gs://00233-uk-master-1/VID89.mp4","gs://00233-uk-master-1/VID90.mp4","gs://00233-uk-master-1/VID91.mp4","gs://00233-uk-master-1/VID92.mp4","gs://00233-uk-master-1/VID93.mp4","gs://00233-uk-master-1/VID94.mp4","gs://00233-uk-master-1/VID95.mp4","gs://00233-uk-master-1/VID96.mp4","gs://00233-uk-master-1/VID97.mp4","gs://00233-uk-master-1/VID98.mp4","gs://00233-uk-master-1/VID99.mp4","gs://00233-uk-master-1/VID100.mp4","gs://00233-uk-master-1/VID101.mp4","gs://00233-uk-master-1/VID102.mp4","gs://00233-uk-master-1/VID103.mp4","gs://00233-uk-master-1/VID104.mp4","gs://00233-uk-master-1/VID105.mp4","gs://00233-uk-master-1/VID106.mp4","gs://00233-uk-master-1/VID107.mp4","gs://00233-uk-master-1/VID108.mp4","gs://00233-uk-master-1/VID109.mp4","gs://00233-uk-master-1/VID110.mp4","gs://00233-uk-master-1/VID111.mp4","gs://00233-uk-master-1/VID112.mp4","gs://00233-uk-master-1/VID113.mp4","gs://00233-uk-master-1/VID114.mp4","gs://00233-uk-master-1/VID115.mp4","gs://00233-uk-master-1/VID116.mp4","gs://00233-uk-master-1/VID117.mp4","gs://00233-uk-master-1/VID118.mp4","gs://00233-uk-master-1/VID119.mp4","gs://00233-uk-master-1/VID120.mp4","gs://00233-uk-master-1/VID121.mp4","gs://00233-uk-master-1/VID122.mp4","gs://00233-uk-master-1/VID123.mp4","gs://00233-uk-master-1/VID124.mp4","gs://00233-uk-master-1/VID125.mp4","gs://00233-uk-master-1/VID126.mp4","gs://00233-uk-master-1/VID127.mp4","gs://00233-uk-master-1/VID128.mp4","gs://00233-uk-master-1/VID129.mp4","gs://00233-uk-master-1/VID130.mp4","gs://00233-uk-master-1/VID131.mp4","gs://00233-uk-master-1/VID132.mp4","gs://00233-uk-master-1/VID133.mp4","gs://00233-uk-master-1/VID134.mp4","gs://00233-uk-master-1/VID135.mp4","gs://00233-uk-master-1/VID136.mp4","gs://00233-uk-master-1/VID137.mp4","gs://00233-uk-master-1/VID138.mp4","gs://00233-uk-master-1/VID139.mp4","gs://00233-uk-master-1/VID140.mp4","gs://00233-uk-master-1/VID141.mp4","gs://00233-uk-master-1/VID142.mp4","gs://00233-uk-master-1/VID143.mp4","gs://00233-uk-master-1/VID144.mp4","gs://00233-uk-master-1/VID145.mp4","gs://00233-uk-master-1/VID146.mp4","gs://00233-uk-master-1/VID147.mp4","gs://00233-uk-master-1/VID148.mp4","gs://00233-uk-master-1/VID149.mp4","gs://00233-uk-master-1/VID150.mp4","gs://00233-uk-master-1/VID151.mp4","gs://00233-uk-master-1/VID152.mp4","gs://00233-uk-master-1/VID153.mp4","gs://00233-uk-master-1/VID154.mp4","gs://00233-uk-master-1/VID155.mp4","gs://00233-uk-master-1/VID156.mp4","gs://00233-uk-master-1/VID157.mp4","gs://00233-uk-master-1/VID158.mp4","gs://00233-uk-master-1/VID159.mp4","gs://00233-uk-master-1/VID160.mp4","gs://00233-uk-master-1/VID161.mp4","gs://00233-uk-master-1/VID162.mp4","gs://00233-uk-master-1/VID163.mp4","gs://00233-uk-master-1/VID164.mp4","gs://00233-uk-master-1/VID165.mp4","gs://00233-uk-master-1/VID166.mp4","gs://00233-uk-master-1/VID167.mp4","gs://00233-uk-master-1/VID168.mp4","gs://00233-uk-master-1/VID169.mp4","gs://00233-uk-master-1/VID170.mp4","gs://00233-uk-master-1/VID171.mp4","gs://00233-uk-master-1/VID172.mp4","gs://00233-uk-master-1/VID173.mp4","gs://00233-uk-master-1/VID174.mp4","gs://00233-uk-master-1/VID175.mp4","gs://00233-uk-master-1/VID176.mp4","gs://00233-uk-master-1/VID177.mp4","gs://00233-uk-master-1/VID178.mp4","gs://00233-uk-master-1/VID179.mp4","gs://00233-uk-master-1/VID180.mp4","gs://00233-uk-master-1/VID181.mp4","gs://00233-uk-master-1/VID182.mp4","gs://00233-uk-master-1/VID183.mp4","gs://00233-uk-master-1/VID184.mp4","gs://00233-uk-master-1/VID185.mp4","gs://00233-uk-master-1/VID186.mp4","gs://00233-uk-master-1/VID187.mp4","gs://00233-uk-master-1/VID188.mp4","gs://00233-uk-master-1/VID189.mp4","gs://00233-uk-master-1/VID190.mp4","gs://00233-uk-master-1/VID191.mp4","gs://00233-uk-master-1/VID192.mp4","gs://00233-uk-master-1/VID193.mp4","gs://00233-uk-master-1/VID194.mp4","gs://00233-uk-master-1/VID195.mp4","gs://00233-uk-master-1/VID196.mp4","gs://00233-uk-master-1/VID197.mp4","gs://00233-uk-master-1/VID198.mp4","gs://00233-uk-master-1/VID199.mp4","gs://00233-uk-master-1/VID200.mp4","gs://00233-uk-master-1/VID201.mp4","gs://00233-uk-master-1/VID202.mp4","gs://00233-uk-master-1/VID203.mp4","gs://00233-uk-master-1/VID204.mp4","gs://00233-uk-master-1/VID205.mp4","gs://00233-uk-master-1/VID206.mp4","gs://00233-uk-master-1/VID207.mp4","gs://00233-uk-master-1/VID208.mp4","gs://00233-uk-master-1/VID209.mp4","gs://00233-uk-master-1/VID210.mp4"]
length = len(list)

while index < length:
    gcs_uri = list[index]
    
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

    result = operation.result(timeout=1000)
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
        result = operation.result(timeout=3000)

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
    result = operation.result(timeout=3000)

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
