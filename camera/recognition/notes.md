Face Recognition
-------------------

In general:
1. Face detection: detect the face in the image. It searchs general human face like segment in the whole image. Output may be one or more than one. the output will be rectangle or rectangles on the faces in the images. [Paul viola method]
2. Face Recognition: recognize input face from the already trained database with highest match score. A single face should be given as input, and the output will be a name, or class name or unknown face. [PCA. LDA]