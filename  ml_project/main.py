import logging
import os

import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)


@hydra.main(config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    logger.info(OmegaConf.to_yaml(cfg))
    logger.info("Working directory : {}".format(os.getcwd()))
    model = instantiate(cfg.mode, dataloader=cfg.dataloader)
    model()


if __name__ == '__main__':
    main()
