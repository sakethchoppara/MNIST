from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PredictionSerializer
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np 
from PIL import Image

model = load_model('/home/saketh/saketh/projects/MNIST/mnist/pre/mnist_model.keras')

def pre_proccessing(image):
        image = Image.open(image)
        image = image.convert('L')
        image = image.resize((28,28))
        image = np.array(image)
        image = image/255.0
        image = image.reshape(1,28,28,1)

        return image

class Prediction(APIView):
    def post(self,request):

        data = PredictionSerializer(data = request.data)
        if data.is_valid(raise_exception=True):
            inst = data.save()
            image = pre_proccessing(inst.image)
            prediction = np.argmax(model.predict(image),axis=1)[0]
            print(prediction)
            return Response({
                "result" : prediction,
                "status":True
            })

        return Response(
             {
                  "status":False
             }
        )

        # print(request.data)
        # arr = request.data['image']
        # image = Image.open(arr)
        # image = image.convert('L')
        # image = image.resize((28,28))
        # image = np.array(image)
        # image = image/255.0
        # image = image.reshape(1,28,28,1)

        # prediction = np.argmax(model.predict(image),axis=1)[0]
        # print(prediction)
    
    def get(self,request):
        return Response('hii')

# Create your views here.
