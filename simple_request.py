# with help from https://github.com/jrosebr1/simple-keras-rest-api/blob/master/simple_request.py
# import the necessary packages
import requests
import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description='simple_request.py')
    parser.add_argument('--image', help='Point to image file.', default='./dog.jpg', type=str)

    args = parser.parse_args()

    return args

def main():

    args = arg_parser()


    # initialize the Keras REST API endpoint URL along with the input
    # image path
    KERAS_REST_API_URL = "http://localhost:4000/predict"
    #IMAGE_PATH = "dog.jpg"
    IMAGE_PATH = args.image

    # load the input image and construct the payload for the request
    image = open(IMAGE_PATH, "rb").read()
    payload = {"image": image}

    # submit the request
    r = requests.post(KERAS_REST_API_URL, files=payload).json()

    # ensure the request was sucessful
    if r["success"]:
      # loop over the predictions and display them
      for (i, result) in enumerate(r["predictions"]):
          print("{}. {}: {:.4f}".format(i + 1, result["label"],
              result["probability"]))

    # otherwise, the request failed
    else:
      print("Request failed")

if __name__ == '__main__':
    main()