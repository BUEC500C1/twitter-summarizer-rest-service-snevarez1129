# twitter-summarizer-rest-service-snevarez1129

## Assignment:
1. Use Flask as your WEB service platform
2. Integrate your module to become a RESTful system
3. Deploy your system to free AWS services: https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc
4. Develop simple WEB applications to test your system.
5. Document your REST APIs on your Github
6. Keep your server off until we request it for grading. We dont want you to waste money.

## Running the API
(1) Set Up Python Virtual Environment

`python3 -m venv env`
`source env/bin/activate`

(2) Install Requirements

`pip3 install -r requirements.txt`

Requirements for this project include:
* flask & flask_restful used as my WEB service platform and to make the system a RESTFUL one
* twippy was used to get twitter info - the user's profile picture and their twitter feed
* pillow was used to convert text into image frames
* ffmpeg was used to create a video using the converted image frames

(3) Start the Server

`python3 main_api.py`

(4) Use the API

* In a new terminal window: `curl http://127.0.0.1:5000/<twitter_handle>`
* In your favorite web browser: `http://127.0.0.1:5000/<twitter_handle>`

## API Response
If there exists a valid keys file in the root directory of this project, the API will return the location of newly created video. If there is no valid keys file, the API will run the stub functions and return a JSON object that tells the user there was an error and includes a tweet from a group of saved tweets.
