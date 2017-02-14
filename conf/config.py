# config.py
configs = config_default.configs

try:
    import config_asiestock
    configs = merge(configs, config_asiestock.configs)
except ImportError:
    pass