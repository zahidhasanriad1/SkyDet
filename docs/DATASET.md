# SkySeaLand dataset card

## Summary

SkySeaLand is a compact satellite object-detection benchmark focused on transportation objects across terrestrial and maritime scenes. It contains 1,307 images and 19,101 verified horizontal bounding boxes in four classes.

## Classes

| Index | Class | Scope |
|---:|---|---|
| 0 | airplane | Aircraft in airport, runway, and airfield scenes |
| 1 | boat | Small-to-medium watercraft in rivers and coastal regions |
| 2 | car | Road vehicles in highways, parking areas, and urban scenes |
| 3 | ship | Large vessels in ports, harbors, and open water |

## Fixed split

| Split | Images | Annotations | Airplane | Boat | Car | Ship |
|---|---:|---:|---:|---:|---:|---:|
| Train | 1,048 | 15,034 | 3,927 | 2,683 | 5,459 | 2,965 |
| Validation | 132 | 1,992 | 367 | 657 | 679 | 289 |
| Test | 127 | 2,075 | 553 | 334 | 798 | 390 |
| **Total** | **1,307** | **19,101** | **4,847** | **3,674** | **6,936** | **3,644** |

## Geometry profile

- 1,104 images (84.5%) exceed 3,836 px on the longest side.
- 955 images (73.1%) are close to a 3:1 width-to-height ratio.
- 179 images (13.7%) are close to 4:1 and 88 (6.7%) are close to 2:1.
- The median annotated box area is approximately 2,726 px^2; the 10th percentile is below 873 px^2.

The wide-scene distribution makes square-input preprocessing consequential. With letterboxing, a 3:1 image occupies roughly 640 x 213 pixels inside a 640 x 640 tensor, preserving geometry while reducing object scale and devoting much of the tensor to padding.

## Collection and annotation

Images were collected from Google Earth Pro for academic research use across airports, highways, harbors, marinas, and coastal regions. Heavy-noise, cloud-obscured, and duplicate viewpoints were screened. Objects were annotated with axis-aligned boxes using CVAT and Roboflow, followed by a second verification pass.

The release includes:

- COCO JSON annotations;
- per-image YOLO text annotations with class indices 0-3;
- fixed train, validation, and test splits.

## Access

- [Mendeley Data, DOI 10.17632/d42n3cp86p.3](https://doi.org/10.17632/d42n3cp86p.3)
- [Kaggle: SkySeaLand](https://www.kaggle.com/datasets/mdzahidhasanriad/skysealand)

## Intended uses

- Research on small-object detection in wide satellite scenes.
- Accuracy-footprint studies for lightweight detectors.
- Mixed land-maritime transportation detection.
- COCO- and YOLO-format pipeline evaluation.

## Known limitations

- The dataset is smaller than large aerial benchmarks such as DOTA and DIOR.
- Splits are image-level, not geographically separated; regional similarity may remain across subsets.
- Labels are axis-aligned, so oriented detection is outside the current scope.
- Aggregate metrics do not isolate land and maritime performance.
- Scene coverage and class frequency reflect the selected collection regions and are not a census of global transportation activity.

## License and source terms

Dataset files are released under CC BY 4.0 through the official hosts. Source imagery remains subject to the imagery provider's terms. Users are responsible for complying with both the dataset license and applicable provider terms.
