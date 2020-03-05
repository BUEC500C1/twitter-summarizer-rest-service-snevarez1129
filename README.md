# video-snevarez1129

## Assignment:
Use Flask as your WEB service platform
Integrate your module to become a RESTFUL system
Deploy your system to free AWS services: https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc
Develop simple WEB applications to test your system.
Document your REST APIs on your Github
Keep your server off until we request it for grading. We dont want you to waste money.

## Introduction:
This assignment is a continuation of HW4 in which we were tasked with creating a system to convert a twitter feed into a video summary. In my HW4 assignment I included flask making my system a RESTFUL one already. For HW5... STILL NEED TO deploy on AWS, develop a simple web application, go back over threading (add more threads?).

## Main Requirements:
flask & flask_restful were used as my WEB service platform and to make the system a RESTFUL one
twippy was used to get twitter info - the user's profile picture and their twitter feed
pillow was used to convert text into image frames
ffmpeg was used to create a video using the converted image frames

## How to Run:
After installing the dependencies listed in requirements.txt, in a new terminal window run the command:

`python3 main_api.py`

Now open a second terminal window or launch your favorite web browser and run the following:

In a terminal window: `curl http://127.0.0.1:5000/<twitter_handle>`
In a web browser: `http://127.0.0.1:5000/<twitter_handle>`

If there exists a valid keys file in the root directory of this project, the API will return the location of newly created video. If there is no valid keys file, the API will run the stub functions and return a JSON object that tells the user there was an error and includes a tweet from a group of saved tweets.

## Usage Examples
