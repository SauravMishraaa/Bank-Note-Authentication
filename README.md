# Bank-Note-Authentication
## This will predict whether a Note is a valid Bank Note or not on the basis of the skewness, entropy,curtosis and variance.
## Here, I have also used to FastAPI to deploy my model.

Requirements:
1. fastapi
2. uvicorn
3. gunicorn==19.9.0
4. anaconda prompt

How to run FastAPI for my project:

• Go to the particular directory here you have kept all the above files.

• Navigate to that directory using command prompt/anaconda prompt.

```bash
uvicorn app:app -reload
```
Note: Make sure that you have installed Fastapi . If not then install by this command:

```bash
pip install fastapi
```
• Then you will see the url like http://127.0.0.1:8000 , copy it and paste it in your web browser.

• To execute it go on to this url:

http://127.0.0.1:8000/docs
