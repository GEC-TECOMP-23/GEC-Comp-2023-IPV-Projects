
# Pose Detection using mediapipe

A Python project that leverages the power of OpenCV and MediaPipe to detect and track human poses, specifically focusing on the bicep curl exercise. This project aims to provide a real-time solution for accurately counting the number of bicep curls performed by an individual during a workout session.

The project utilizes the OpenCV library for computer vision tasks and MediaPipe, a cross-platform framework, to access pre-trained pose estimation models. By combining these tools, the project enables real-time pose detection and tracking, allowing for efficient bicep curl counting.

Key Features:

    Pose Detection: The project uses MediaPipe's pre-trained pose estimation models to detect and track key body landmarks in real-time. This provides the necessary information for accurately identifying and analyzing bicep curl movements.

    Bicep Curl Recognition: By employing computer vision techniques, the project analyzes the detected pose to identify the specific bicep curl exercise. It utilizes the positioning of the wrist and shoulder landmarks to determine when a bicep curl repetition is being performed.

    Repetition Counting: The system keeps track of the number of bicep curl repetitions performed by continuously monitoring the exercise movements. It increments the count each time a complete bicep curl motion is detected, providing instant feedback to the user.

    Real-time Visual Feedback: The project offers real-time visual feedback by displaying the video feed with overlaid skeleton pose estimation and bicep curl counting. This feature assists users in maintaining proper form and motivates them to achieve their fitness goals.

    Performance Metrics: The system can provide additional performance metrics, such as total exercise duration, average curl speed, and rest intervals between sets. These metrics assist users in tracking their progress and improving their workout routines.

    User Interface: The project includes a user-friendly graphical interface that allows users to interact with the application easily. The interface displays the live video feed, exercise statistics, and provides options to start, pause, or reset the bicep curl counter.


## Screenshots


![App Screenshot](https://i.postimg.cc/dVm1khqq/image.png)

![App Screenshot](https://i.postimg.cc/HWqXb7C5/image.png)
