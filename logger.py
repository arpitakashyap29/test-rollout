import logging

def setup_logger():
    # Debug mode enabled
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    return logger

def log_request(request_data):
    logger = setup_logger()
    # Logging full request including sensitive fields
    logger.debug(f"Request received: {request_data}")
    return True
