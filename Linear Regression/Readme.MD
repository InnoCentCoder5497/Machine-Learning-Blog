# Linear Regression

Regression is a method of modelling a target value based on independent predictors. This method is mostly used for forecasting and finding out cause and effect relationship between variables. Simple linear regression is a type of regression analysis where the number of independent variables is one and there is a linear relationship between the independent(x) and dependent(y) variable.

In Linear Regression we try to find a line that `best fits` our dataset. This means that we want a line segment that cuts most of the data points in our dataset. 
Linear regression is of two types,
- **Univariate Linear Regression** : Univariate linear regression has one predictor variable and there is a linear relationship between the predictor (𝑥) and outcome (𝑦) variable. 
- **Multivariate Linear Regression** : Multivariate Regression is a method used to measure the degree at which more than one independent variable (predictors) and more than one dependent variable (responses), are linearly related.

Below is how a Univariate Linear Regression learn the line segment to fit a toy dataset.

<p align="center">
    <img src="./imgs/LineRegression.gif" width=800 height = 400 />
</p>

The <b>Disadvantage</b> of Linear regression is that it only works when data is `linear` as in above case. For non-linear datasets it's , not the best algorithm to use but is a very useful startng point to understand linearity of your dataset.

The notebook titled `Linear Regression with Single variable` Demonstrate the concept of Univariate Linear Regression.

The notebook titled `Multivariate Regression` Demonstrate the concept of Multivariate Linear Regression. 

## References
- Linear Regression, by Wikipedia : https://en.wikipedia.org/wiki/Linear_regression
- Linear Regression, by Yale University : http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm
- Machine Learning course CS229, by Andrew ng : http://cs229.stanford.edu/notes/cs229-notes1.pdf
- Correlation methods, by Statisticssolutions : https://www.statisticssolutions.com/correlation-pearson-kendall-spearman/
- Feature Selection, by Jason Brownlee : https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/
- KFold Cross Validation, by Jason Brownlee : https://machinelearningmastery.com/k-fold-cross-validation/
