# An analysis of spectral similarity measures
Code for the paper *An analysis of spectral similarity measures*. In the paper the most used measures for the assessment of spectral similarity are analyzed. Please read the [paper](https://www.ingentaconnect.com/content/ist/cic/2021/00002021/00000029/art00049) for details.

## Dependencies
* Python 3.9
* numpy
* scikit-image

In order to successfully run the code, install the packages listed in `requirements.txt` as follows:
```
pip install -r requirements.txt
```

## Citation
If you use our code, please consider cite the following:
* Mirko Agarla, Simone Bianco, Luigi Celona, Raimondo Schettini, and Mikhail Tchobanou. An analysis of spectral similarity measures. In _Color and Imaging Conference_, _volume 2021_, Society for Imaging Science and Technology, volume 2021, number 6, pp. 300-305, 2021.
```
@inproceedings{agarla2021spectralmeasures,
 author = {Agarla, Mirko and Bianco, Simone and Celona, Luigi and Schettini, Raimondo and Tchobanou, Mikhail},
 year = {2021},
 title = {An analysis of spectral similarity measures},
 organization = {Society for Imaging Science and Technology},
 booktitle = {Color and Imaging Conference},
 volume = {2021},
 number = {6},
 doi = {https://doi.org/10.2352/issn.2169-2629.2021.29.300},
 pages = {300--305},
}
```

## Available measures
### Mean error measures
* [Mean Square Error (MSE)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/error_measures.py#L4)
* [Root Mean Square Error (RMSE)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/error_measures.py#L28)
* [Mean Relative Absolute Error (MRAE)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/error_measures.py#L51)
* [Back-Projection MRAE (BPMRAE)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/error_measures.py#L74)
* [Peak Signal-to-Noise Ratio (PSNR)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/error_measures.py#L126)

### Similarity measures
* [Goodness-of-Fit Coefficient (GFC)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/similarity_measures.py#L5)
* [Mean Structural SImilarity Measure (MSSIM)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/similarity_measures.py#L29)

### Angular measures
* [Average Per-Pixel Spectral Angle (APPSA)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/angular_measures.py#L4)
* [Mean Angular Error (MAngE)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/angular_measures.py#L29)
* [Spectral Angle Mapper (SAM)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/angular_measures.py#L56)

### Colorimetric error measures
* [Delta E*](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/colorimetric_measures.py#L7)
* [Euclidean distance in ProLab color space](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/colorimetric_measures.py#L42)

### Other measures
* [Mean Spectral Information Divergence (MSID)](https://github.com/CeLuigi/spectral-similarity-metrics-comparison/blob/7f0659041c2982a6bbc85823c5b7b4b9476ad9a7/other_measures.py#L4)

## Acknowledgement
This research was supported by Huawei Technologies Co. Ltd. Russia.
