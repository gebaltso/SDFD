![Example images SDFD](https://github.com/gebaltso/SDFD/blob/main/examplesSDFD.png?raw=true "Example Images of SDFD")


### Description
-----

:large_orange_diamond: We generated 1000 different synthetic face images that constitute the **SDFD (Stable Diffusion Face-image Dataset)**. SDFD captures a broad spectrum of facial diversity encompassing not only demographics and biometrics but also non-permanent traits like make-up,
hairstyle, and accessories. 

:large_orange_diamond: We created various prompts that guide a state-of-the-art text-to-image model **(Stable Diffusion 2.1)**) in generating a comprehensive dataset of high-quality realistic images and can be used as an evaluation set in face analysis systems.

:large_blue_diamond: File finalPrompts.csv contains all the corresponding prompts that we used to get the SDFD dataset.

:large_blue_diamond: File finalPromptsSeparated.csv contains the same prompts with finalPrompts.csv but the attributes are comma separated.

### How to Use to Reproduce the Images

:exclamation: The first step is to install the Diffusers. For more information see the [official documentation](https://github.com/huggingface/diffusers) . 

:arrow_right: In order to produce images run the **SDFD.py** file:

`python3 SDFD.py`

:warning: Do not forget to change image output directory path as well as any other variable as needed.

### Citation

