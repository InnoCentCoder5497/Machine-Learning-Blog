# Logistic Regression

Classification is a supervised learning approach in which the computer program learns from the data input given to it and then uses this learning to classify new observation. We try to assign a label to our input. For example, if we were to told, whether the image shown to us is of a Bird or a Dog, we are assigning a label to that image. If it's of a Dog, it's a Dog image else its a Bird Image. These systems answer the questions of type "Yes of No" or "Which category does it belong?".

In Logistic Regression we try to find a decision boundary that seperate our data into diffrent classes.
There are two types of classification problems,
- **Binary Classification** : Here, their are only 2 discrete classes. The model try to predict whether the input belong to class 1 or 2.
- **Multiclass Classifiction** : Here, their are more than 2 classes.

Below image shows how the model creates a decision boundary between two classes in a dataset,

<p align="center">
    <img src="./imgs/LogReg.png" width=512 height = 512 />
</p>

The <b>Disadvantage</b> of Logistic regression is that it makes a linear boundary and is very inefficient when we try to model non-linear boundaries.

The notebook titled `Logistic Regression - Binary Classification` Demonstrate the concept of Binary classification.

## References
- Logistic regression : https://en.wikipedia.org/wiki/Logistic_regression
- Cross Entropy : https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html
- Admission Dataset : https://web.stanford.edu/class/archive/cs/cs109/cs109.1176/lectures/23-LogisticRegression.pdf
- BFGS : https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm
- Lower back pain Dataset : https://www.kaggle.com/sammy123/lower-back-pain-symptoms-dataset
