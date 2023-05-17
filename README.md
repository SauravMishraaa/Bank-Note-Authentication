# Bank-Note-Authentication
This will predict whether a Note is a valid Bank Note or not on the basis of the skewness, entropy,curtosis and variance.
Here, I have also used to FastAPI to deploy my model.

Skewness: Skewness measures the asymmetry of a distribution. In the context of banknote authentication, skewness can be calculated for specific features such as the intensity or color distribution of the banknote. Counterfeit banknotes often have different skewness values compared to genuine banknotes due to variations in printing techniques.

Entropy: Entropy is a measure of randomness or uncertainty in a distribution. It quantifies the amount of information contained in a banknote feature. Genuine banknotes tend to have consistent and structured patterns, resulting in lower entropy values. Counterfeit banknotes, on the other hand, may exhibit higher entropy due to imperfections or inconsistencies in their features.

Kurtosis: Kurtosis measures the sharpness or peakedness of a distribution. It indicates whether the distribution has heavy or light tails compared to a normal distribution. Different features of banknotes can have varying kurtosis values, and counterfeit banknotes may deviate from the expected kurtosis patterns observed in genuine banknotes.

Variance: Variance measures the dispersion or spread of a distribution. In banknote authentication, variance can be computed for features like texture, color, or geometric attributes. Genuine banknotes usually have consistent and tightly controlled printing processes, resulting in lower variance values. Counterfeit banknotes may exhibit higher variance due to inconsistencies in printing quality.

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
• Then you will see the url like  
```bash
 http://127.0.0.1:8000 
```
copy it and paste it in your web browser.

• To execute it go on to this url:

```bash
http://127.0.0.1:8000/docs
```

