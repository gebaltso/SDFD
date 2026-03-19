![Example images SDFD](https://github.com/gebaltso/SDFD/blob/main/examplesSDFD.png?raw=true "Example Images of SDFD")

[![MAI_BIAS toolkit](https://img.shields.io/badge/MAI_BIAS-⚖️_AI_fairness_tool-white)](https://mammoth-eu.github.io/mammoth-commons/index.html)

This software is part of MAI-BIAS; a low-code toolkit for
fairness analysis and mitigation, with an accompanying suite of coding
tools. Our ecosystem operates in multidimensional and multi-attribute 
settings (safeguarding multiple races, genders, etc), and across multiple 
data modalities (like tabular data, images, text, graphs). Learn more 
[here](https://mammoth-eu.github.io/mammoth-commons/index.html).

## 👥 Who is this for?

- **If you build or evaluate AI systems that involve faces** such as identity verification or access control — SDFD gives you a ready-made evaluation set that goes far beyond what standard datasets offer. It was specifically designed to challenge your system with the full range of faces it will encounter in the real world: different races, ages, hairstyles, accessories, religious coverings, makeup styles, and more.
- **If you are a policymaker, auditor, or compliance officer**, there is no need to understand how the dataset was made. What matters is this: when an AI vendor tells you their face recognition or demographic prediction system is "fair" or "accurate," you should ask — accurate on what kinds of faces? SDFD was built precisely to expose the gaps. Our experiments show that even well-known fairness-focused datasets miss faces that commonly appear in the real world. If your organization deploys a face analysis system, you can ask your vendor to benchmark their system on SDFD and report results broken down by race and/or gender group.
- **Are you a non-expert?** Ask your organization's AI team whether the face analysis tools they use have been tested on datasets that include people wearing hijabs, turbans, having face paint, unconventional hairstyles, or non-binary gender presentations. If not, SDFD is a concrete resource to point them to.

## ✨ About

Face recognition and demographic analysis are no longer tools used only by specialists — they are embedded in hiring platforms, border control systems, banking apps, smart cameras, and employee monitoring tools.
**SDFD (Stable Diffusion Face Dataset)** is a dataset of 1,000 photorealistic synthetic face images, purpose-built to evaluate whether an AI system truly works for everyone. Unlike most face datasets — which define diversity narrowly in terms of skin tone, age, and gender — SDFD also captures the enormous variety of how people actually look: different hairstyles and colors, glasses, hats, religious head coverings (hijabs, turbans, veils), tattoos, makeup, facial hair, and a wide range of emotional expressions.
**Why does this matter for your organization?**
- **For risk and legal teams:** Laws and regulations — including the EU AI Act — are increasingly requiring organizations to prove that their AI systems treat everyone fairly. SDFD gives you clear, documented test results that show how a system performs across different groups of people, including groups that are typically left out of standard testing.
- **For product and innovation managers:** If your product includes a face analysis feature — even one bought from an external provider — any errors or unfair outcomes will reflect on you. SDFD helps you catch those problems early, before your customers do.
- **For ethics and DEI leads:** Fairness in AI goes beyond race and gender. SDFD is one of the first datasets to deliberately include people wearing religious coverings, people with non-binary gender expressions, and a wide range of cultural styles and accessories. It puts a broader, more realistic picture of human diversity into the testing process.

### Details
-----

:large_orange_diamond: We created various prompts that guide a state-of-the-art text-to-image model **(Stable Diffusion 2.1)**) in generating a comprehensive dataset of high-quality realistic images and can be used as an evaluation set in face analysis systems.

:large_blue_diamond: File finalPrompts.csv contains all the corresponding prompts that we used to get the SDFD dataset.

:large_blue_diamond: File finalPromptsSeparated.csv contains the same prompts with finalPrompts.csv but the attributes are comma separated.

### How to Use to Reproduce the Images
-----

:exclamation: The first step is to install the Diffusers. We recommend installing them in a virtual environment from Conda. For more information see the [official documentation](https://github.com/huggingface/diffusers) . 

:arrow_right: In order to produce images run the **SDFD.py** file:

`python3 SDFD.py`

:warning: Do not forget to change image output directory path as well as any other variable as needed.

### Citation
-----
``` 
@INPROCEEDINGS{10581864,
  author={Baltsou, Georgia and Sarridis, Ioannis and Koutlis, Christos and Papadopoulos, Symeon},
  booktitle={2024 IEEE 18th International Conference on Automatic Face and Gesture Recognition (FG)}, 
  title={SDFD: Building a Versatile Synthetic Face Image Dataset with Diverse Attributes}, 
  year={2024},
  volume={},
  number={},
  pages={1-10},
  keywords={Training;Systematics;Face recognition;Text to image;Gesture recognition;Skin;Robustness},
  doi={10.1109/FG59268.2024.10581864}}

```

## Acknowledgments
This research was supported by the EU Horizon Europe project MAMMOth
(Grant Agreement 101070285).

