# AVS

![MathQA](https://img.shields.io/badge/Task-MathQA-red) 
![Mathematical Perception](https://img.shields.io/badge/Task-Mathematical_Perception-red) 
![Multi-Modal](https://img.shields.io/badge/Task-Multi--Modal-red)

![AVSD](https://img.shields.io/badge/Dataset-AVSD-blue)
![AVSD](https://img.shields.io/badge/Dataset-ν--geometry-blue)

![CLIP](https://img.shields.io/badge/Model-CLIP-green)
![SigLIP](https://img.shields.io/badge/Model-SigLIP-green)
![Qwen2.5](https://img.shields.io/badge/Model-Qwen2.5-green)
![LLaVA](https://img.shields.io/badge/Model-LLaVA-green)



## Dataset
* You can find our dataset in (https://huggingface.co/datasets/cobordism/AVSD_25)!


## Installation
```
git clone https://github.com/hs-chae/AVSD25.git
cd AVSD25
pip install -r requirements.txt
```

## Synthetic Data Generation
For ν-geometry generation, use ```generation/nugeo.py``` instead.

### 1. Caption Dataset
```
python generation/caption.py --samples 100 --path data
```

* ```--skills``` is an argument for specifying the skills of questions to generate. It includes all the skills except for the ν-geometry in default. 

* ```--format``` is to choose the dataset format. There are ```json```(default) and ```jsonl``` available.


<details>
<summary> Full Skill List </summary>

* ν-geometry
* absolute_position
* adjacency
* angle
* area
* boundary
* cardinal
* cardinal_direction
* color
* congruence
* connectedness
* convexity
* coordinate
* curvature
* direction
* interior
* intersection
* length
* line
* OCR
* ordinal
* orientation
* orthogonality
* overlap
* parallel
* point
* reflection
* rel_pos
* rotation
* rotational_symmetry
* shape
* sharpness
* similarity
* symbol
* tangency
* texture
* width 

</details>

### 2. Instruction Dataset
```
python generation/instruction.py --samples 100 --path data
```
* You can use ```instruction.py``` almost in the same way to ```caption.py```.

* ```instruction.py``` accumulates the data if there already exist a data at ```--path```. Be careful that its saving starts from the index when the program starts, so two parallel program to the same path may overwrite the other's result, even though they are generating problems of different skills.

* Use ```--reset``` if you want to overwrite the image and the json file. (already existing images are not deleted)

### 3. Instruction Dataset (ControlNet)
```
pip install diffusers
python generation/instruction_controlnet.py --samples 100 --path data
```
* You may need authentification to run the controlnet, or you can use other versions with slight modification.

* You can use ```instruction_controlnet.py``` almost in the same way to ```instruction.py```

* It uses all the available GPU resources in default. (Use ```CUDA_VISIBLE_DEVICES``` environment variable to utilize partial GPU.)

We first generate ControlNet augmented dataset using ```instruction_controlnet.py``` and then accumulate with ```instruction.py``` to mix two formats of data.

## Evaluation
We suggest using lmms-eval ( https://github.com/EvolvingLMMs-Lab/lmms-eval.git ) for evaluation on AVSD and ν-geometry.
After git cloning lmms_eval, you can run evaluation on AVSD by moving our files in avs to ```lmms-eval/lmms_eval/tasks/avs```.
Belows are the example to evaluate LLaVA on AVSD-h and ν-geometry. You can change ```tasks``` to ```vitas``` or ```vitas-controlnet``` for AVSD-s adnd AVSD-c.

```
python3 -m accelerate.commands.launch \
    --num_processes=8 \
    -m lmms_eval \
    --model llava \
    --model_args pretrained="liuhaotian/llava-v1.6-vicuna-13b" \
    --tasks avsbench \
    --batch_size 1 \
    --log_samples \
    --output_path ./logs/
```
```
python3 -m accelerate.commands.launch \
    --num_processes=8 \
    -m lmms_eval \
    --model llava \
    --model_args pretrained="liuhaotian/llava-v1.6-vicuna-13b" \
    --tasks nugeo \
    --batch_size 1 \
    --log_samples \
    --output_path ./logs/
```

You can also use ```extract.py``` and ```score.py``` for custom models.

```
python extract.py \
    --input results/response.json \
    --output results/extract.json
```

```
python score.py \
    --input results/extract.json \
    --output results/score.json
```


