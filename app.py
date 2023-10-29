# # # # from fastapi import FastAPI, File, UploadFile
# # # # from fastapi.templating import Jinja2Templates
# # # # from fastapi.staticfiles import StaticFiles
# # # # from tensorflow.keras.models import load_model
# # # # from tensorflow.keras.preprocessing import image
# # # # import numpy as np

# # # # app = FastAPI()

# # # # # Mount the "static" directory for CSS and other static files
# # # # app.mount("/static", StaticFiles(directory="static"), name="static")

# # # # # Load your model
# # # # model = load_model("best_model.h5")

# # # # templates = Jinja2Templates(directory="templates")

# # # # @app.get("/")
# # # # async def read_root(request):
# # # #     return templates.TemplateResponse("index.html", {"request": request})

# # # # # @app.post("/predict/")
# # # # # async def predict(file: UploadFile):
# # # # #     # Check if an image file was uploaded
# # # # #     if file.filename:
# # # # #         # Read the file contents
# # # # #         img_bytes = await file.read()

# # # # #         # Save the uploaded image to a temporary folder
# # # # #         with open("temp.jpg", "wb") as f:
# # # # #             f.write(img_bytes)

# # # # #         # Preprocess the image for prediction
# # # # #         img = image.load_img("temp.jpg", target_size=(224, 224))
# # # # #         img = image.img_to_array(img)
# # # # #         img = np.expand_dims(img, axis=0)

# # # # #         # Make a prediction
# # # # #         prediction = model.predict(img)

# # # # #         # Replace this with code to interpret the prediction
# # # # #         result = f"Prediction: {prediction}"

# # # # #         # Remove the temporary image file
# # # # #         import os
# # # # #         os.remove("temp.jpg")

# # # # #         # return {"prediction": result}

# # # # #         return templates.TemplateResponse("index.html", {"request": request, "prediction_result": prediction_result})
# # # # #     return {"error": "No image provided"}


# # # # @app.post("/predict/")
# # # # async def predict(file: UploadFile):
# # # #     if file.filename:
# # # #         # Read the file contents
# # # #         img_bytes = await file.read()

# # # #         # Save the uploaded image to a temporary folder
# # # #         with open("temp.jpg", "wb") as f:
# # # #             f.write(img_bytes)

# # # #         # Preprocess the image for prediction
# # # #         img = image.load_img("temp.jpg", target_size=(224, 224))
# # # #         img = image.img_to_array(img)
# # # #         img = np.expand_dims(img, axis=0)

# # # #         # Make a prediction
# # # #         prediction = model.predict(img)

# # # #         # Replace this with code to interpret the prediction
# # # #         result = f"Prediction: {prediction}"

# # # #         # Remove the temporary image file
# # # #         import os
# # # #         os.remove("temp.jpg")

# # # #         return templates.TemplateResponse("index.html", {"request": request, "prediction_result": prediction_result})

# # # #     return {"error": "No image provided"}










# # # from fastapi import FastAPI, File, UploadFile
# # # from fastapi.templating import Jinja2Templates
# # # from fastapi.staticfiles import StaticFiles

# # # app = FastAPI()


# # # from pydantic import BaseModel

# # # class UploadFileModel(BaseModel):
# # #     file: UploadFile

# # # # Mount the "static" directory for CSS and other static files
# # # app.mount("/static", StaticFiles(directory="static"), name="static")

# # # templates = Jinja2Templates(directory="templates")

# # # @app.get("/")
# # # async def read_root(request):
# # #     return templates.TemplateResponse("index.html", {})

# # # @app.post("/predict/")
# # # async def predict(file: UploadFile):
# # #     if file:
# # #         # You can handle the uploaded file here.
# # #         # For simplicity, let's assume it's an image and display the filename.

# # #         filename = file.filename
# # #         return {"prediction_result": f"Uploaded file: {filename}"}

# # #     return {"error": "No file uploaded"}



# # from fastapi import FastAPI, File, UploadFile

# # app = FastAPI()

# # @app.post("/uploadfile/")
# # async def upload_file(file: UploadFile):
# #     if file:
# #         return {"message": "File uploaded successfully", "filename": file.filename}
# #     else:
# #         return {"error": "No file uploaded"}

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="127.0.0.1", port=8000)



# from fastapi import FastAPI
# from fastapi.templating import Jinja2Templates
# from fastapi import Request
# from fastapi.staticfiles import StaticFiles
# from fastapi import FastAPI, File, UploadFile
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np



# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


# model = load_model("best_model.h5")
# # Create a Jinja2 templates instance and specify the directory where your templates are located.
# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def root(request: Request):
#     # Render the "index.html" template and pass any required data.
#     return templates.TemplateResponse("index.html", {"request": request})



# @app.post("/predict/")
# async def predict(request: Request, file: UploadFile):
#     print(f"Received request: {request}")
#     print(f"File name: {file.filename}")
#     if file.filename:
#         # Read the file contents
#         img_bytes = await file.read()

#         # Save the uploaded image to a temporary folder
#         with open("temp.jpg", "wb") as f:
#             f.write(img_bytes)

#         # Preprocess the image for prediction
#         img = image.load_img("temp.jpg", target_size=(256, 256))
#         img = image.img_to_array(img)
#         img = np.expand_dims(img, axis=0)

#         # Make a prediction using your model
#         prediction = model.predict(img)

#         # Interpret the prediction result (replace with your logic)
#         result = f"Prediction: {prediction}"

#         # Remove the temporary image file
#         import os
#         os.remove("temp.jpg")

#         return templates.TemplateResponse("index.html", {"request": request, "prediction_result": result})
#     return {"error": "No image provided"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)













# # @app.post("/predict/")
# # async def predict(file: UploadFile):

# #     if file.filename:
# #         # Read the file contents
# #         img_bytes = await file.read()

# #         # Save the uploaded image to a temporary folder
# #         with open("temp.jpg", "wb") as f:
# #             f.write(img_bytes)

# #         # Preprocess the image for prediction
# #         img = image.load_img("temp.jpg", target_size=(224, 224))
# #         img = image.img_to_array(img)
# #         img = np.expand_dims(img, axis=0)

# #         # Make a prediction
# #         prediction = model.predict(img)

# #         # Replace this with code to interpret the prediction
# #         result = f"Prediction: {prediction}"

# #         # Remove the temporary image file
# #         import os
# #         os.remove("temp.jpg")

# #         # return {"prediction": result}

# #         return templates.TemplateResponse("index.html", {"request": request, "prediction_result": prediction_result})
# #     return {"error": "No image provided"}
# #     # if file:
# #     #     # You can handle the uploaded file here.
# #     #     # For simplicity, let's assume it's an image and display the filename.

# #     #     filename = file.filename
# #     #     return {"prediction_result": f"Uploaded file: {filename}"}

# #     # return {"error": "No file uploaded"}




# from fastapi import FastAPI, File, UploadFile
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image


# from fastapi import FastAPI
# from fastapi.templating import Jinja2Templates
# from fastapi import Request
# from fastapi.staticfiles import StaticFiles
# from fastapi import FastAPI, File, UploadFile
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from main import app
# import numpy as np




# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Load your pre-trained model
# model = load_model("best_model.h5")

# # Create a Jinja2 templates instance and specify the directory where your templates are located.
# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})



# # Assuming you already have the 'ref' dictionary
# # ref = dict(zip(list(train.class_indices.values()), list(train.class_indices.keys())))   

# @app.post("/predict/")
# async def predict(request: Request, file: UploadFile):
#     if file:
#         # Read the file contents
#         img_bytes = await file.read()

#         # Save the uploaded image to a temporary folder
#         with open("temp.jpg", "wb") as f:
#             f.write(img_bytes)

#         # Preprocess the image for prediction
#         img = image.load_img("temp.jpg", target_size=(256, 256))
#         img = image.img_to_array(img)
#         img = np.expand_dims(img, axis=0)

#         # Make a prediction using your pre-trained model
#         prediction = model.predict(img)

#         # Extract the predicted class index
#         predicted_class_index = np.argmax(prediction)

#         # Map the predicted class index to the class label using the 'ref' dictionary
#         class_label = ref.get(predicted_class_index, "Unknown Class")

#         # Interpret the prediction result
#         result = f"Prediction: {class_label} (Class {predicted_class_index})"

#         # Print the prediction result to the console
#         print(result)

#         # Remove the temporary image file
#         import os
#         os.remove("temp.jpg")

#         return templates.TemplateResponse("index.html", {"request": request, "prediction_result": result})
#     return {"error": "No image provided"}






# @app.post("/predict/")
# async def predict(request: Request, file: UploadFile):
#     print(f"Received request: {request}")
#     print(f"File name: {file.filename}")
#     if file:
#         # Read the file contents
#         img_bytes = await file.read()

#         # Save the uploaded image to a temporary folder
#         with open("temp.jpg", "wb") as f:
#             f.write(img_bytes)

#         # Preprocess the image for prediction
#         img = image.load_img("temp.jpg", target_size=(256, 256))
#         img = image.img_to_array(img)
#         img = np.expand_dims(img, axis=0)

#         # Make a prediction using your pre-trained model
#         prediction = model.predict(img)

#         print(f"File name: {file.filename}")
#         # Interpret the prediction result (replace with your logic)
#         result = f"Prediction: {prediction}"
#         print(result)

#         # Remove the temporary image file
#         import os
#         os.remove("temp.jpg")

#         return templates.TemplateResponse("index.html", {"request": request, "prediction_result": result})
#     return {"error": "No image provided"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)













from fastapi import FastAPI, Request, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO
import wikipedia
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from transformers import pipeline
from fastapi.responses import HTMLResponse








disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry_(including_sour)___Powdery_mildew',
                   'Cherry_(including_sour)___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___Leaf_scorch',
                   'Strawberry___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

class_label_to_keyword = {
   'Apple___Apple_scab': 'Apple Scab',
    'Apple___Black_rot': 'Apple Black Rot',
    'Apple___Cedar_apple_rust': 'Cedar Apple Rust',
    'Apple___healthy': 'Healthy Apple',
    'Blueberry___healthy': 'Healthy Blueberry',
    'Cherry_(including_sour)___Powdery_mildew': 'Cherry Powdery Mildew',
    'Cherry_(including_sour)___healthy': 'Healthy Cherry',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 'Corn Cercospora Leaf Spot',
    'Corn_(maize)___Common_rust_': 'Corn Common Rust',
    'Corn_(maize)___Northern_Leaf_Blight': 'Corn Northern Leaf Blight',
    'Corn_(maize)___healthy': 'Healthy Corn',
    'Grape___Black_rot': 'Grape Black Rot',
    'Grape___Esca_(Black_Measles)': 'Grape Esca (Black Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Grape Leaf Blight (Isariopsis Leaf Spot)',
    'Grape___healthy': 'Healthy Grape',
    'Orange___Haunglongbing_(Citrus_greening)': 'Orange Haunglongbing (Citrus Greening)',
    'Peach___Bacterial_spot': 'Peach Bacterial Spot',
    'Peach___healthy': 'Healthy Peach',
    'Pepper,_bell___Bacterial_spot': 'Bell Pepper Bacterial Spot',
    'Pepper,_bell___healthy': 'Healthy Bell Pepper',
    'Potato___Early_blight': 'Potato Early Blight',
    'Potato___Late_blight': 'Potato Late Blight',
    'Potato___healthy': 'Healthy Potato',
    'Raspberry___healthy': 'Healthy Raspberry',
    'Soybean___healthy': 'Healthy Soybean',
    'Squash___Powdery_mildew': 'Squash Powdery Mildew',
    'Strawberry___Leaf_scorch': 'Strawberry Leaf Scorch',
    'Strawberry___healthy': 'Healthy Strawberry',
    'Tomato___Bacterial_spot': 'Tomato Bacterial Spot',
    'Tomato___Early_blight': 'Tomato Early Blight',
    'Tomato___Late_blight': 'Tomato Late Blight',
    'Tomato___Leaf_Mold': 'Tomato Leaf Mold',
    'Tomato___Septoria_leaf_spot': 'Tomato Septoria Leaf Spot',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Tomato Spider Mites',
    'Tomato___Target_Spot': 'Tomato Target Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Tomato Yellow Leaf Curl Virus',
    'Tomato___Tomato_mosaic_virus': 'Tomato Mosaic Virus',
    'Tomato___healthy': 'Healthy Tomato'
}

    





app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load your pre-trained model
model = load_model("best_model.h5")

# Create a dictionary to map class indices to class labels


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("carol.html", {"request": request})



@app.post("/predict/")
async def predict(request: Request, file: UploadFile = Form(...)):
    if file:
        # Read the file contents and open it as an image
        img_bytes = await file.read()
        img = Image.open(BytesIO(img_bytes))

        # Preprocess the image for prediction
        img = img.resize((256, 256))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # Make a prediction using your pre-trained model
        prediction = model.predict(img)

        # Extract the predicted class index
        predicted_class_index = np.argmax(prediction)

        # Map the predicted class index to the class label
        class_label = disease_classes[predicted_class_index]

        keyword = class_label_to_keyword.get(class_label)
       
        
        if keyword:
            try:
                global summary
                summary = wikipedia.summary(keyword, sentences = 20)
                
                summarizer = pipeline("summarization")
                summary = summarizer(summary, max_length=300, min_length=100, do_sample=False)
                summary = f"{summary[0]['summary_text']}"
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation errors if needed
                summary = "Multiple results found. Please refine your query."
            except wikipedia.exceptions.PageError as e:
                # Handle page not found errors if needed
                summary = "No information found."
        else:
            summary = "Keyword not found."

        # Interpret the prediction result
        # result = f"Prediction: {class_label} (Class {predicted_class_index})"
        global result
        result = f"The uploaded image is that of {keyword}"
        # Print the prediction result to the console
        print(result)

        return templates.TemplateResponse("result.html", {"request": request, "prediction_result": result, "summary": summary})
        # return RedirectResponse(url="/result")

    return {"error": "No image provided"}
# RedirectResponse(url="result.html")

@app.get("/result", response_class=HTMLResponse)
async def result(request: Request):
    

    return templates.TemplateResponse("result.html", {"request": request, "prediction_result": result, "summary": summary})


# @app.get("/result")
# async def result(request: Request):
#     # Implement logic to render the "result.html" template and return it as a response.
#     return templates.TemplateResponse("result.html", {"request": request, "prediction_result": result, "summary": summary})














# from fastapi import FastAPI, Form, Request
# from transformers import pipeline

# Load the summarization model from Hugging Face
# summarizer = pipeline("summarization")

# @app.post("/regenerate-summary")
# async def regenerate_summary(request: Request, existingSummary: str = Form(...)):
#     # Use the Hugging Face AI to generate a new summary
#     new_summary = summarizer(existingSummary, max_length=150, min_length=30, do_sample=False)

#     # Extract the generated summary
#     new_summary_text = new_summary[0]["summary_text"]
#     print(new_summary_text)

#     return new_summary_text

