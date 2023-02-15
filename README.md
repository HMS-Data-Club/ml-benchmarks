# Spring 2023 Session 2

## Introduction

Today we are going to be going through some common machine learning benchmark datasets and try to perform the best basic classification possible. 

We will be using a few datasets from a data package containing machine learning benchmark datasets called [PMBL](https://github.com/EpistasisLab/pmlb). Benchmarking datasets are often used in machine learning research. They are useful for generally understanding how a model might perform, but often suffer from being outdated or having unusual distributions. 

## Datasets

The possible datasets we will be exploring today are below. 
Please choose the dataset which sounds most interesting to you to explore. 

### E. coli promotor region classification

This dataset is a compilation of promoters with known transcriptional start points for E. coli genes. The task is to recognize promoters in strings that represent nucleotides (one of A, G, T, or C). The input features are 57 sequential DNA nucleotides. 53 sample promoters and 53 nonpromoter sequences were used. 

The features are raw sequence information, tarting at position -50 (p-50) and ending at position +7 (p7). Each of the features is filled by one of {a, g, t, c}. Code: a=0; c=1; g=2; t=3.

It is called `molecular_biology_promoters` in the data package. 

More information can be found [here](https://archive.ics.uci.edu/ml/datasets/Molecular+Biology+(Promoter+Gene+Sequences)).
 
### Postoperative discharge decision prediction

The classification task of this dataset is to determine where 90 patients in a postoperative recovery area should be sent to next. Because hypothermia is a significant concern after surgery, the attributes correspond roughly to body temperature measurements. Patients where divided into those who were sent to general hospital floor (labeled 0 in the dateset) and those prepared to go home (labeled 2 in the dataset). 

Measurments were:
1. L-CORE (patient's internal temperature in C):
high (> 37), mid (>= 36 and <= 37), low (< 36)
2. L-SURF (patient's surface temperature in C):
high (> 36.5), mid (>= 36.5 and <= 35), low (< 35)
3. L-O2 (oxygen saturation in %):
excellent (>= 98), good (>= 90 and < 98),
fair (>= 80 and < 90), poor (< 80)
4. L-BP (last measurement of blood pressure):
high (> 130/90), mid (<= 130/90 and >= 90/70), low (< 90/70)
5. SURF-STBL (stability of patient's surface temperature):
stable, mod-stable, unstable
6. CORE-STBL (stability of patient's core temperature)
stable, mod-stable, unstable
7. BP-STBL (stability of patient's blood pressure)
stable, mod-stable, unstable
8. COMFORT (patient's perceived comfort at discharge, measured as
an integer between 0 and 20) 

It is called `postoperative_patient_data` in the data package. 

More information can be [found here](https://archive.ics.uci.edu/ml/datasets/Post-Operative+Patient)
 
### Duchenne muscular dystrophy diagnosis

This is a set of biomedical data containing 209 observations (134 "normal" and 75 "carrier"). The goal is to predict carrier status of Duchenne muscular dystrophy based on some demographic information and 4 blood measurments:
M1- serum creatine kinase.
M2- hemopexin.
M3- pyruvate kinase.
M4- lactate dehydrogenase.

It is called `biomed` in the data package. 

More information can be [found here](https://www.openml.org/search?type=data&status=active&id=481)

## Instructions

The goal today is to find a model and parameters which perform the best on your chosen dataset. You can play with different models and options for each model. An overview of some of these models can be found [here](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html).

If you are having trouble getting your environment setup, you can use [this online notebook](https://colab.research.google.com/drive/1Ma5xMGXug9CzShzLDTCJnJRdh8vxifl6?usp=sharing).
