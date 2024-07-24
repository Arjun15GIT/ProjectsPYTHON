#STEP 1: IMPORTING REQUIRED LIBRARARIES

import cv2
import os
from werkzeug.utils import secure_filename
from flask import Flask,request,render_template
UPLOAD_FOLDER = 'C:\Users\lenovo\OneDrive\Desktop\AI ML\PYTHON\Python Projects\sketchapp\static\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

#STEP 2: DEFINING SKETCH MAKING APP USING FLASK

app = Flask(__name__)  #defining fals app
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  #remove that file from the cache after its use.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

#STEP 3: DEFINING THE SKETCH FUNCTION
'''allowed_file function which basically checks whether the file 
   we have uploaded is having an allowed extension or not.'''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 #allowed_file function which basically checks whether the file 
 #we have uploaded is having an allowed extension or not.

'''make_sketch function which is the backbone of this app.
   This function simply takes an Image and returns its sketch.'''

def make_sketch(img):
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(grayed)
    blurred = cv2.GaussianBlur(inverted, (19, 19), sigmaX=0, sigmaY=0)
    final_result = cv2.divide(grayed, 255 - blurred, scale=256)
    return final_result

#STEP 4: DEFINING FLASK ROUTING FUNCTION

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sketch',methods=['POST'])
def sketch():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = cv2.imread(UPLOAD_FOLDER+'/'+filename)
        sketch_img = make_sketch(img)
        sketch_img_name = filename.split('.')[0]+"_sketch.jpg"
        _ = cv2.imwrite(UPLOAD_FOLDER+'/'+sketch_img_name, sketch_img)
        return render_template('home.html',org_img_name=filename,sketch_img_name=sketch_img_name)


if __name__ == '__main__':
    app.run(debug=True) 

'''Here we have defined two routing functions.
   1.The first one is the home page function.
     Its URL will be http://127.0.0.1:5000/. ('/' in the end is called route)

   2.The second is the sketch-making route function which will run when we hit the Submit Button after uploading the Image.
    Its URL will be http://127.0.0.1:5000/sketch'''