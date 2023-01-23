We have tried to reduce human effort by using surveillance cameras and face recognition.
The system makes use of real-time analysis of video captured by the surveillance camera to detect the most recent presence of missing child.

These days we face a big problem that impacts negatively our society. Most children
being missed or kidnapped from their families.

Our project aims to try to find these children in a local area and send them back to their
families. We target phones as it’s easy to use them and anyone these days has a smart
phone. We made our app works in a local area and we selected the malls as a begin to our
project, cause we can control the area of the mall instead of a public street where we don’t have a lot of cameras.

------
#### Tools
 - Five cameras
      - Camera on the entrance “detecting and store children faces”
      - Camera on the exit gate “detecting and store children faces”
      - 3 Cameras around the mall.
 - Desktop for security man.
 - Application for user and security man.
-----

Our project simply will be a mobile application which will help you to know the place of
your child. The app can be used by parents to report missing their child or by any vigilant
citizen who can report any vulnerable child on the mall. The app will take the child image,
then detect the child face from it, then compare images in the database with the child
image, trying to find the missing child by matching images. Also, the app works with
surveillance systems if any camera detected any missing child and identifies him by
comparing his face with the missing child, it will send a notification to his parents with
his location.

------
# Machine learning models
 - ## Face detection
   - we used OpenCV and Tensorflow
 -  ## Tracking
   -  Object Tracking with Opencv and Python 
   -  Object tracking does frame-by-frame tracking but keeps the history of where the
   -  object is at a time after time. We will talk first about object detection and then about 
   -  how to apply object tracking to the detection.
      -  Object tracking is the process of:
        -  Taking an initial set of object detections (such as an input set of bounding 
box coordinates)
        -  Creating a unique ID for each of the initial detections
        -  And then tracking each of the objects as they move around frames in a video, 
maintaining the assignment of unique IDs  
 -  ## Age and gender Models
    -   We used VGG net Caffe model( pretrained model).
![image](https://user-images.githubusercontent.com/46052811/214091236-21149cc9-0bc3-4d38-90d7-85802c14e17f.png)

 -  ##  Matching Structural Similarity Model
    -   we have same requrments to get the match faces in the project 
       -   1 photo to every id (person)
       -   1 photo to lost person 
![image](https://user-images.githubusercontent.com/46052811/214091800-d4cafc59-1136-4082-a74b-d55cb3a2b885.png)



------

# Flutter Application using Flutter and Dart
#### The application consist of:
    - Authentication part Login, Register pages.
    - Presentation for children data in the Home page.
    - Add missing child data found or lost.
    - User page.
    - Notification page
    
-----

 - User can register via email by adding required data like email, name, phone 
number and password, we get data from custom input widgets by using Text
Editing Controller to build request body.
Then send post request, if the request return success status code: save the 
returned access token in shared preferences and open Home page.

    ![signup](https://user-images.githubusercontent.com/46052811/214084266-a9c91003-ca80-4815-8823-e8758192918f.jpg)

----

 - User can login via email and password, we get data from custom input 
widgets by using TextEditingController to build request body.
Then send post request, if the request return success status code: save the 
returned access token in shared preferences and open Home page

   ![login](https://user-images.githubusercontent.com/46052811/214084226-11bfd39d-6433-462c-bc44-998f0c778c1e.jpg)

-----

   ![forget pass](https://user-images.githubusercontent.com/46052811/214083969-e02edf34-32d5-4c13-b59d-c28479ccab6a.png)

  ![forget pass2](https://user-images.githubusercontent.com/46052811/214084007-89cb46a7-3456-494d-8d1b-36df808dde41.png)

  ![set information](https://user-images.githubusercontent.com/46052811/214084498-68b5cc68-7e39-4385-b235-d4ce27f69cb8.jpg)

 ![setting page](https://user-images.githubusercontent.com/46052811/214084529-25a27912-2da9-4b9b-b58c-628b343d72c5.png)

-----
 - In the home page we have two main buttons:
     - Lost Child: used for open Lost page so can added required information about child.
     - Found Child: used for open Found page.
 - Second part is list of found and lost children every card have simple information about child. 
 - We get children data from post request and get the response list then map 
it to card widgets and push them to List view.

- ![homepage](https://user-images.githubusercontent.com/46052811/214084330-46be1c02-d192-4875-9e6d-15c57cdb6035.png)

 ![notification](https://user-images.githubusercontent.com/46052811/214084356-170bd9a5-4a07-473f-b414-18df8cf503ad.png)


-----

  - We get the required information like name, location, age, gender and the time 
child lost in. Then take the image which user uploaded to detect child face by 
using FaceDetector from FirebaseVisionImage package, then pass the face 
coordinates to other function to crop specified face from image. Then build post 
request using multi part request to upload the image


![found someone](https://user-images.githubusercontent.com/46052811/214084393-9d598f62-0324-4dc6-802a-26b23636c5bd.jpg)

![lost someone](https://user-images.githubusercontent.com/46052811/214084412-9d78e834-eb0a-4171-aa29-fe23f5ba253a.jpg)


