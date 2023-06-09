# Image Stitching project using OpenCV

Image stitching is one of the most successful applications in Computer Vision. Nowadays, it is hard to find a cell phone or an image processing API that does not contain this functionality, In this piece, I will talk about how to perform image stitching using Python and OpenCV. Given a pair of images that share some common region, my goal is to “stitch” them and create a panoramic image scene.
Methods like SIFT and SURF try to address the limitations of corner detection algorithms. Usually, corner detector algorithms use a fixed size kernel to detect regions of interest (corners) on images. It is easy to see that when we scale an image, this kernel might become too small or too big. To address this limitation, methods like SIFT use the Difference of Gaussians (DoD). The idea is to apply DoD on differently scaled versions of the same image. It also uses the neighboring pixel information to find and refine key points and corresponding descriptors.
Feature detection, description, and matching are essential components of various computer vision applications, thus they have received considerable attention in the last decades. Several feature detectors and descriptors have been proposed in the literature with a variety of definitions for what kind of points in an image is potentially interesting (i.e., a distinctive attribute).
Methods such as SIFT and SURF attempt to solve corner algorithms constraints. Corner detector methods often utilize a kernel of defined size to find areas of interest on pictures (corners). It's easy to see that this kernel may go too tiny or too large if you resize a picture.


Methods like SIFT are using Gaussian difference to solve this restriction (DoD). DoD should be applied for copies of the same picture that are different sized. It also uses the next pixel information to locate and improve important spots and descriptions.

Matching feature
We have many characteristics from both photographs, as we can see. Now we want to compare both attributes and stick to the more like-minded pairings.

### Maheshwari Terse
### Roll no.: 201105026
### TE Computer (Sem VI)
