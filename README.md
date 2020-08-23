# Facial-emotion-recogniton
In this project i have created a deep learning
model to recognise emotion of human faces.

My deep learning model contain 4 Convolutional 
layer and two pooling layer(conv-conv-pool)
formate and than Flatten , dense and final dense for 
calculate probability of each classes.
i also use dropout layer after each pooling layer and between 
dense layers.
this model 
trained on approx 27000 images
and validated on 7000 images with validation
accuracy 89%.

this project a pretrained face detector for 
detecting faces in images.

this deep learning model use device camera to 
to take image then use face detector to detect faces 
and finally give probability of each classes and final class that 
it recognise.

this model contain 7 categories of emotion
1. angry
2. disgust
3. fear
4. happy
5. neutral 
6. sad 
7. surprise
