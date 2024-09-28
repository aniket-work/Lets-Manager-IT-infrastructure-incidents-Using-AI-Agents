import logging

def setup_logging(config):
    logging.basicConfig(
        level=getattr(logging, config['level']),
        format=config['format'],
        handlers=[
            logging.FileHandler(config['file'], mode='w'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)