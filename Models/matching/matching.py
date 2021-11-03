import json
import schedule

from skimage.metrics import structural_similarity
import cv2
import requests
import network.network as nt


class lostChild:
    id = None
    image = None


class matchedChild:
    id = None
    image = None
    location = None
    date = None


def loadMatching():
    arrayOfSimilarImages = []
    lost_chid = lostChild()
    matchchild = matchedChild()
    response = nt.downloadFun()
    data = json.loads(response.text)
    if len(data['data']) > 0:
        for array in data['data']:
            # first index 0 is a object and second is a array of objects
            # x, id, y, user, z, age, a, gender, s, location, d, lostdate, f, img, g, imgid, h, status = array[0]
            lost_chid.id = array[0].get('_id')
            lost_chid.image = cv2.resize((nt.downloadImage(array[0].get('image'), lost_chid.id)), (224, 224), 3)
            # print(data['data'][0][0]['age'])

            for similar in array[1]:
                matchchild.id = similar.get('_id')
                matchchild.image = cv2.resize((nt.downloadImage(similar.get('image'), matchchild.id)), (224, 224), 3)
                matchchild.date = similar.get('date')
                matchchild.location = similar.get('location')
                arrayOfSimilarImages.append(matchchild)

            for obj in arrayOfSimilarImages:
                cv2.imshow('lost', lost_chid.image)
                cv2.imshow('list', obj.image)
                q = cv2.waitKey(0)
                if q == ord('n'):
                    sim = structural_similarity(lost_chid.image, obj.image, multichannel=True)
                    print(sim)
                    if sim > 0.68:
                        print(lost_chid.id)
                        print(obj.location)
                        x = nt.matchResult(lost_chid.id, obj.location)
                        print(x.text)
            arrayOfSimilarImages = []


def structural_sim(img1, img2):
    sim, diff = structural_similarity(img1, img2, full=True)
    print(sim)
    print(diff)
    return sim


def startMatching():
    schedule.every(3).seconds.do(loadMatching)
    while True:
        schedule.run_pending()


