import cv2
import requests
import os



def uploadFun(image, age, gender, date, location):
    files = {"image": image}
    data = {
        "age": age,
        "gender": gender,
        "date": date,
        "location": location}
    return requests.post("https://mafkoud-api.herokuapp.com/api/camera", files=files, data=data)


def downloadFun():
    return requests.get('https://mafkoud-api.herokuapp.com/api/match')


def downloadImage(link, id):
    r = requests.get(link)
    file = open(id + ".jpg", "wb")
    file.write(r.content)
    file.close()
    img = cv2.imread(id + '.jpg')
    os.remove(id + '.jpg')
    return img


def matchResult(childId, location):
    data = {
        "childID": childId,
        "location": location,
    }
    return requests.post("https://mafkoud-api.herokuapp.com/api/match/result", data=data)
