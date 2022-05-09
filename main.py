import logging
import os

import hydra
from hydra.utils import instantiate
import numpy as np

from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)


@hydra.main(config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    logger.info(OmegaConf.to_yaml(cfg))
    logger.info("Working directory : {}".format(os.getcwd()))
    data_reader = instantiate(cfg.data_reader)



if __name__ == '__main__':
    main()
