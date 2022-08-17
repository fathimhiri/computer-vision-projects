
in this project we will have to detect the hand and then,  classsify what sign represented by the hand.
for the simplicity, i did just 3 classes for a, b and c signs

Data Collection:
the first part of the project is data (image) collection, the code is in the main.py file.
every time you want to collect img for a class, you just have to change the path to on line 14 in main.py file.

Training:
using the teachable machine website provided by google https://teachablemachine.withgoogle.com/  : 
we select image project , then we select standard image mdoel, where we write our classes abc in this case, upload all our images then we train the model.
then we click on export model, we choose tensorflow, choose ekras, then download the model and put it under model folder.(get 2 files in total under model)


test
we can then test our mdoel using test.py file

