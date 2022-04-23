import os
from omegaconf import OmegaConf

def load_seq_config(config_dir, config_name):
    cf = OmegaConf.load(os.path.join(config_dir, config_name  +'.yaml'))
    defaults = []
    sub_module = cf.get('defaults', [])
    for sm in sub_module:
        name, sub = sm.items()[0]
        cf_sub_module = load_seq_config(os.path.join(config_dir, name), sub)
        cf_item = OmegaConf.create({})
        OmegaConf.update(cf_item, name, cf_sub_module)
        defaults.append(cf_item)
    cf = OmegaConf.merge(cf.copy(), *defaults)
    return cf