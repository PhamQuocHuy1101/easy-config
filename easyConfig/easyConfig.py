import os
from omegaconf import OmegaConf
        
def load_seq_config(config_dir, config_name):
    cf = OmegaConf.load(os.path.join(config_dir, config_name  +'.yaml'))
    defaults = []
    sub_module = cf.get('defaults', [])
    for sm in sub_module:
        name, sub = sm.items()[0]
        cf_sub_module = load_seq_config(os.path.join(config_dir, name), sub)
        cf_item = OmegaConf.create()
        OmegaConf.update(cf_item, name, cf_sub_module)
        defaults.append(cf_item)
    cf = OmegaConf.merge(cf.copy(), *defaults)
    if len(sub_module) > 0:
        OmegaConf.update(cf, 'defaults', None)
    return cf

def load_cli_config():
    return OmegaConf.from_cli()

def setup_config(config_dir='config', config_name='config', change_path = True):
    cli_cf = load_cli_config()
    outputs = cli_cf.get('outputs', 'outputs')
    config_dir = cli_cf.get('config_dir', config_dir)
    config_name = cli_cf.get('config_name', config_name)
    assert os.path.exists(os.path.join(config_dir, config_name)), 'config file does not exist'

    yaml_cf = load_seq_config(config_dir, config_name)
    config = OmegaConf.merge(yaml_cf.copy(), cli_cf)

    if change_path == True:
        os.makedirs(outputs)
        os.chdir(outputs)
    return config


if __name__ == '__main__':
    cf = setup_config()
    print(cf)