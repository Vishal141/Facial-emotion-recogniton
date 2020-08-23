# Facial-emotion-recogniton
In this project i have created a deep learning
model to recognise emotion of human faces.

In this project first model take image 
using device camera than resize image to 
detect face .
it's also recognise faces in images taken before.
I use 
pretrained harcascade face detector classifier to 
detect face in the image.

My deep_learning model contain 4 Convolutional 
layer and two pooling layer(conv-conv-pool)
formate and than Flatten , dense and final dense for 
calculate probability each classes.
i also use dropout layer after each pooling layer and between 
dense layer.
this model 
trained on approx 27000 images
and validated on 7000 images with validation
accuracy 89%.

this model contain 7 categories of emotion
1. angry
2. disgust
3. fear
4. happy
5. neutral 
6. sad 
7. surprise
