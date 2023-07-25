# Custom Panda Gym Environments

Student bachelor project at the University of Applied Sciences Dresden (HTW Dresden). The goal
was to Adaptable pick and place using RL for the moving source moving target problem.
The base for this project was the panda-gym repository (https://github.com/balooox/CustomPandaPickAndPlaceEnv.git).

Models were successfully trained with the TQC, TD3 algorithm and also with the SAC algorithm. We used 
stable-baselines3 and sb3-contrib to integrate the algorithms. 

We have a custom gym environment:
- `PandaPickAndPlaceAndMove-v1`

This repository includes trained models for the environments, available as zip files. 
More information at the usage section.

## Installation 

This project was executed in a conda environment. Under Windows we used PyCharm as an execution IDE, 
under Linux (Ubuntu) you can execute the code throw the CLI. 

Following commands were executed:
```bash
conda create -n example_name python=3.10
conda activate name
conda install -c conda-forge stable-baselines3[extra]
conda install -c conda-forge tensorboard
pip install panda-gym==2.0
pip install sb3-contrib
```

Because of the fast developing paste in the reinforcement learning sector the safer way is to use the
`docs/requirements.yaml` file. 
Run conda `conda create --name <env> --file <this file>`

### Step by step installation guide

1. git clone https://github.com/omarayadd/Bachelor-Project.git
2. cd ./Bachelor-Project
3. use Anaconda:
    1. Under Windows: open the anaconda prompt (anaconda3)
    2. Under Linux: make sure anaconda is integrated into the cli
4. conda env create --file ./docs/environment.yml
5. conda activate custom_panda_env

## Usage

### showcase.py 
To get an overview over the custom environment, you can run the script showcase.py !

```bash
python ./showcase.py env
# For example
python ./showcase.py PandaPickAndPlaceAndMove-v1
```

### train.py
You can train a model with the train.py script. Available algorithms are TQC, TD3 and 
SAC ( but you can extend the code and include different algorithms available
through stable-baselines3 and sb3_contrib, like PPO etc... ).

```bash
python ./train env algo amount
# For example
python ./train.py PandaPickAndPlaceAndMove-v1 TQC 1000000
```

During training (or afterwards) you can visualize the training process by
using tensorboard. To do so, run following command in the CLI: 
```bash
tensorboard --logdir ./tensorboard
```

### enjoy.py
After a training, a zip file is saved under the ./trained directory.
You can run enjoy.py two see a visualized result of the training.

```bash
python ./enjoy env algo file
# For example
python ./enjoy.py PandaPickAndPlaceAndMove-v1 TQC trained/PandaPickAndPlaceAndMove-v1/TQC/PandaPickAndPlaceAndMove-v1TQC20230628-1301.zip 
```

### evaluate.py
During training, a printed log on the CLI gives you information about the 
success rate and the mean reward for each episode. To truly evaluate a model use the evaluate.py.

```bash
python  ./evaluate env algo file
# For example
python ./evaluate.py PandaPickAndPlaceAndMove-v1 TQC trained/PandaPickAndPlaceAndMove-v1/TQC/PandaPickAndPlaceAndMove-v1TQC20230628-1301.zip
```

## Environments

This custom environment was used for `PandaPickAndPlaceAndMove-v1`. 

![PandaPickAndPlaceAndMove-v1](showcase_exp3_AdobeExpress.gif)


### Trained model 

#### Trained env for `PandaPickAndPlaceAndMove-v1`:          

![PandaPickAndPlaceAndMove-v1-trained](
Using_TD3_AdobeExpress.gif )

Mean reward: 
                             
<img src="exp3 TQC rew.PNG" width="50%" />

Success rate: 

<img src="exp3 TQC res.PNG" width="50%" />







### Site note

It takes approximately 1 million episodes, before an agent reach 
convergence. Not every experiment reached convergence.


