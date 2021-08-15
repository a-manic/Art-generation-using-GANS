# Art-generation-using-GANS

This project aims to use GANs (Generative Adversarial Networks) to generate artwork. The goal of the project is to see the quality of artworks generated by using a GAN of the smallest size possible. In this model, we have built a GAN with no more that 6 layers in both the Generative and Discriminiative networks. 

The datasets for this project have been collected from various sources such as Kaggle[[1]](#1) and WikiArt[[2]](#2),and also from this Google drive of images[[3]](#3).

The images are of varying sizes, so the first step is to use resize.py to resize all images to be 64x64 pixels. 

We tested the model for varying number of epochs for different datasets. Datasets with nearly 10k images yielded the best results.

A genenerated image while using the landscape dataset containing nearly 15k images.
![alt text](https://github.com/a-manic/Art-generation-using-GANS/blob/main/sample%20results/Landscapes.png)

A genenerated image while using the portrait dataset containing nearly 15k images.
![alt text](https://github.com/a-manic/Art-generation-using-GANS/blob/main/sample%20results/Portraits.png)

Using datasets with less than 6k images led to mode collape and hence repetitive images.

## References
<a id="1">[1]</a>
https://www.kaggle.com/ikarus777/best-artworks-of-all-time

<a id="2">[2]</a>
https://www.wikiart.org/

<a id="3">[3]</a>
https://drive.google.com/file/d/1yHqS2zXgCiI9LO4gN-X5W18QYXC5bbQS/view
