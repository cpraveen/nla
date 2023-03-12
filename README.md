# Numerical Linear Algebra

Codes developed for a course on numerical linear algebra based on the book 

L. N. Trefethen and D. Bau: Numerical Linear Algebra, SIAM

`Original:` https://www.bitbucket.org/cpraveen/nla <br/>
`Mirrored:` https://www.github.com/cpraveen/nla

## Python tutorial

The codes are written in Python and as Jupyter notebooks. A short Python tutorial is available [here](http://www.github.com/cpraveen/python).

## DATA files

Some of the notebooks need some files to run which must be downloaded from bitbucket. If you are running from terminal, you can download all files once

```
cd DATA
sh ./download.sh
```

## Run in SageMaker Studio Lab

You can get a free account at https://studiolab.sagemaker.aws and clone this git repo into your account, and then run/edit the notebooks.

## Run in Binder

Run the code in binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cpraveen/nla/HEAD). When you first click on this link, it may take a few minutes to set up the environment with all required packages. Then you can edit and run the notebooks, but you cannot save them; but you can download the notebooks to your computer.

## Open in nbviewer (read only, cannot run)

Open the `src` directory: https://nbviewer.org/github/cpraveen/nla/tree/master/src

or the individual files

* [Singular value decomposition](https://nbviewer.org/github/cpraveen/nla/blob/master/src/svd.ipynb)
* Applications of SVD
  * [Image compression using SVD](https://nbviewer.org/github/cpraveen/nla/blob/master/src/dog.ipynb)
  * [Ovarian cancer data](https://nbviewer.org/github/cpraveen/nla/blob/master/src/ovarian_cancer.ipynb)
  * [Eigenfaces](https://nbviewer.org/github/cpraveen/nla/blob/master/src/eigenfaces.ipynb)
* [QR factorization](https://nbviewer.org/github/cpraveen/nla/blob/master/src/qr.ipynb)
* [Least squares problems](https://nbviewer.org/github/cpraveen/nla/blob/master/src/least_squares.ipynb)
* [Sensitivity of polynomial roots: Wilkinson polynomial](https://nbviewer.org/github/cpraveen/nla/blob/master/src/wilkinson_poly.ipynb)
* [Floating point arithmetic](https://nbviewer.org/github/cpraveen/nla/blob/master/src/floating_point.ipynb)
* [Stability of Householder triangularization (Lecture 16)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/house_stability.ipynb)
* [Triangular systems](https://nbviewer.org/github/cpraveen/nla/blob/master/src/tri_sys.ipynb)
* [Stability of least squares algorithms](https://nbviewer.org/github/cpraveen/nla/blob/master/src/least_squares_stability.ipynb)
* [Gaussian elimination (Lecture 20,21)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/gauss_elim.ipynb)
* [Stability of Gaussian elimination (Lecture 22)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/gauss_elim_stab.ipynb)
* [Cholesky decomposition (Lecture 23)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/cholesky.ipynb)
* [Reduction to Hessenberg form (Lecture 26)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/hessenberg.ipynb)
* [Power and inverse iteration (Lecture 27)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/power.ipynb)
* [QR algorithm for eigenvalues (Lecture 28)](https://nbviewer.org/github/cpraveen/nla/blob/master/src/qr_eig.ipynb)


## Open in colab

Open the repository in colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cpraveen/nla)

The following links open individual files in colab.

* [Singular value decomposition](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/svd.ipynb)
* Applications of SVD
  * [Image compression using SVD](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/dog.ipynb)
  * [Ovarian cancer data](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/ovarian_cancer.ipynb)
  * [Eigenfaces](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/eigenfaces.ipynb)
* [QR factorization](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/qr.ipynb)
* [Least squares problems](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/least_squares.ipynb)
* [Sensitivity of polynomial roots: Wilkinson polynomial](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/wilkinson_poly.ipynb)
* [Floating point arithmetic](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/floating_point.ipynb)
* [Stability of Householder triangularization (Lecture 16)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/house_stability.ipynb)
* [Triangular systems](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/tri_sys.ipynb)
* [Stability of least squares algorithms](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/least_squares_stability.ipynb)
* [Gaussian elimination (Lecture 20,21)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/gauss_elim.ipynb)
* [Stability of Gaussian elimination (Lecture 22)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/gauss_elim_stab.ipynb)
* [Cholesky decomposition (Lecture 23)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/cholesky.ipynb)
* [Reduction to Hessenberg form (Lecture 26)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/hessenberg.ipynb)
* [Power and inverse iterations (Lecture 27)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/power.ipynb)
* [QR algorihtm for eigenvalues (Lecture 28)](http://colab.research.google.com/github/cpraveen/nla/blob/master/src/qr_eig.ipynb)

## More code examples

http://www.github.com/cpraveen/na

## References

* S. L. Brunton and J. N. Katz, Data Driven Science and Engineering: Machine Learning, Dynamical Systems and Control, Cambridge Univ. Press.
* James Demmel, Applied Numerical Linear Algebra, SIAM.
* E. Darve and M. Wootters, Numerical Linear Algebra with Julia, SIAM.
* G. H. Golub and C. F. Van Loan, Matrix Computations, Hindustan Book Agency.
