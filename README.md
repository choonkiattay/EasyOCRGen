# EasyOCRGenerator

EasyOCRGenerator is a tools to generate OCR dataset for optical
character recognition.

#### Generator
1. Malaysia license plate
2. Philippine license plate **(TODO)**
3. English words **(TODO)**
4. Non lexicon words

#### Imitator
1. Malaysia license plate

#### Image augmentation
1. Perspective Transformation
2. Color Inversion
3. Salt & Pepper
4. Singularity: Double line plate Slicer

#### Notebook
There are logic behind this generator is briefly describe in
`TightPlateGeneration.ipynb`

### Dependencies
- OpenCV
- numpy
- [imgaug](https://gist.github.com/adamjohnson/5682757)
- pillow
- argparse

## Malaysia License Plate
Road Transport Department Malaysia (JPJ) issues various plate layout as below:

| Type                             | Layout                     |
| :------------------------------- | :------------------------- |
| Private & commercial vehicles	   | ABC 1234 or W/Q/SAB 4567 C |
| Taxi                      	   | HAB 1234                   |
| Military	                       | ZA 1234                    |
| KL (Transition)             	   | W 1234 A                   |
| Diplomatic corps          	   | 12-34-DC                   |
| Royal & government           	   | (Full title)               |

#### Random Plate Generation
This will generate Malaysia plate with the proportion of each plate type stated below: 

| Layout                           | Proportion                 |
| :------------------------------- | :------------------------- |
| Priv & Comm, Taxi, Military, KL  | 85%                        |
| Diplomatic corps            	   | 10%                        |
| Special Plate                	   | 5%                         |
| Limousine	                       | 1%                         |

>Please to be reminded the proportion is not based on empirical study but an 
assumption made for training a good OCR model, that is different plate 
layout with balance character distribution.

##### Code
**Arguments**
- `--number` Total number plate to generate. *Integer*
- `--mode` Generation mode. Use *my_plate*
- `--pers_trans` Perspective Transform. *On / Off*
- `--augment` Augmentation. *On / Off*
- `--single_line` Singularity. *On / Off*
- `--save_dir` Directory to save images. *Full path directory, Include
  "/" at EOL*

**Example**

```
python3 generator.py --number 1000 --mode my_plate --pers_trans on --augment on --single_line on --save_dir /home/user/my_plate/
```
#### Plate Imitator
This will read the real license plate image with groundtruth as file
name and generate the synthetic version of them.

##### Code
**Arguments**
- `--imitatee_dir` Directory to real plate image. *Full path directory,
  Include "/" at EOL*
- `--pers_trans` Perspective Transform. *On / Off*
- `--augment` Augmentation. *On / Off*
- `--single_line` Singularity. *On / Off*
- `--save_dir` Directory to save images. *Full path directory, Include "/" at EOL*

**Example**
```
python3 imitator_my_plate.py --imitatee_dir /home/user/real_plate/ --pers_trans on --augment on --single_line on --save_dir /home/user/my_plate/
```

### TODO
- Lexicon Word Font & background -> license plate style 
- Non lexicon word generation
- Philippine Plate
