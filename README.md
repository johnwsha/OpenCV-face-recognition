Followed:

https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

Background information:

https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78



Device Tested on:

MacBook Pro (15-inch, 2018) (macOS Mojave Ver 10.14.5)
Intel Core i7-8850H @ 2.6 GHz, 6 core
Radeon Pro 560X 4 GB
16 GB ram
General Notes:
Using OpenCV to do facial detection and recognition on images, videos, and webcam streams. It is fairly resource intense as even using a brand new 15" MacBook Pro resulted in lag in the video and webcam facial recognition. Perhaps if the output was not displayed it would speed up? Not sure. This method of using OpenCV and HoG (Histogram of Oriented Gradients) will definitely not run well on any resource limited device like a Raspberry Pi. 



Installation:
pip install dlib
pip install face_recognition
sudo -H pip2.7 install imutils
sudo -H pip2.7 install opencv-python
sudo -H pip2.7 install opencv-contrib-python


Training dataset on new faces:
To create our facial embeddings open up a terminal and execute the following command:

(For more information on what facial embeddings are, see the post referred to at the top of this page.)

cd face-recognition-opencv/
python encode_faces.py --dataset dataset --encodings encodings.pickle
On a Macbook Pro (no GPU), encoding 218 images took approximately 20 minutes.



Alternatively, build dlib with CUDA GPU support to encode the images in about 1-2 minutes.

Note: Macbook Pro's do not have NVIDIA GPU's unless 2013 and older. 

To do so:

git clone https://github.com/davisking/dlib.git
cd dlib
python setup.py install
The setup will automatically enable/disable optional features (such as CUDA) based on hardware compatibilities on your computer. 

For more information: http://dlib.net/compile.html



Demo:
Image:
recognize_faces_image.py
python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png --detection-method hog
Use –detection-method hog as this model is less intensive (default CNN face detector performs better with GPU; if GPU use is desired, a slightly altered setup is required, see link in first section)



Video: 
recognize_faces_video_file.py
python recognize_faces_video_file.py --encodings encodings.pickle --input videos/lunch_scene.mp4 --output output/lunch_scene_output.avi --detection-method hog
Using the --display 0 argument made the program unresponsive so I omitted it in the code block above

This video is 3:55 long.

Webcam:
recognize_faces_video.py
python recognize_faces_video.py --encodings encodings.pickle --output output/webcam_face_recognition_output.avi --detection-method hog
The webcam is set to shut off after 15 seconds (length can be changed in the file)

Webcam output is saved to an .avi file at 3 frames per second, saved to the directory /output/

Performance:
recognize_faces_video.py:
Average processing time: 0.148s

About a 0.5s delay when viewing webcam output facial recognition in real time for 1 face (~3 FPS).



recognize_faces_video_file.py:
Average processing time: 0.138s

Total runtime: 778.880s for a 235s video





recognize_faces_video_file.py with --display 0:
Average processing time: 0.139 s

Total runtime: 787.618s

Number of frames: 5641

FPS: 7.162

Length of video: 235s



Resizing images for training:
Used OpenCV for transforming/resizing and saving the result

Referenced: 

https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/

https://stackoverflow.com/questions/9868963/cvimwrite-could-not-find-a-writer-for-the-specified-extension



python resize.py --dataset [image_directory]

python resize.py --dataset john_sha
Use spacebar (waitKey(0)) to continue/iterate through the dataset of images.

Resizing scale is hardcoded, currently at 15% (used iPhone X camera for taking images).

The resized images will be saved in a directory named [directory]_resized (eg: john_sha_resized)



Add your newly resized images into the directory /dataset/



For this demo, I added my face to the training data in order to try to have the facial recognition model recognize my face in the webcam feed.

webcam_face_recognition_output.avi

