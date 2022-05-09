import logging
import os

import hydra
from hydra.utils import instantiate, get_original_cwd, to_absolute_path
import numpy as np

from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)


@hydra.main(config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    logger.info(OmegaConf.to_yaml(cfg))
    logger.info("Working directory : {}".format(os.getcwd()))
    trainer = instantiate(cfg.mode.trainer, dataloader=cfg.dataloader)
    trainer.fit()



if __name__ == '__main__':
    main()
