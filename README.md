# easy-config
## Install directly from git

`git+https://github.com/PhamQuocHuy1101/easy-config.git`

## Usage
- Wraper OmegaConf for recursively loading yaml file & command line args:
- Default, automatically create folder outputs, and change the working dir to outputs (or set **False** in setup_config)

Example

main.py
```
from easyConfig import setup_config
# set change_path = True, change the working dir to arg outputs in command line
config = setup_config('config', 'main_config', True)
```
root tree:

```
config/
├── data
│   └──d1.yaml
│   └──d2.yaml
├── model
│   └── m1.yaml
│   └── m2.yaml
└── main_config.yaml
```

The content of config.yaml:
```
defaults:
  - model: m1
  - data: d2

device: 1
seed: 40
optim:
  lr: [0.01, 0.001]
  weight_decay: 0.1
```

With command `python main.py optim.weight_decay=0.2 seed=1 outputs=out_folder other_arg=123`

The output of config:
```
defaults:
  - model: m1
  - data: d2

device: 1
seed: 1
optim:
  lr: [0.01, 0.001]
  weight_decay: 0.2
  
model:
  ... # recursive content of m1.yaml
  
data:
  ... # recursive content of m2.yaml

outputs: out_folder
other_arg: 123 # other command line args
 ```
