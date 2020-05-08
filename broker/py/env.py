import os
from typing import NamedTuple


DEFAULT_POLL_INTERVAL_MS = 3000
DEFAULT_WORKER_LIVENESS = 3
DEFAULT_WORKER_LIFETIME_S = (DEFAULT_WORKER_LIVENESS * DEFAULT_POLL_INTERVAL_MS) / 1000.0


class _ENV(NamedTuple):
    BROKER_PIPE_HOST: str = os.environ["BROKER_PIPE_HOST"]
    BROKER_BROADCAST_PORT: int = int(os.environ["BROKER_BROADCAST_PORT"])
    BROKER_PIPE_IN_PORT: int = int(os.environ["BROKER_PIPE_IN_PORT"])
    IN_PIPE_HOST: str = os.environ["IN_PIPE_HOST"]
    IN_PIPE_PORT: int = int(os.environ["IN_PIPE_PORT"])
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")
    POLL_INTERVAL_MS: int = int(os.environ.get(
        "POLL_INTERVAL_MS", DEFAULT_POLL_INTERVAL_MS
    ))
    WORKER_LIFETIME_S: int = int(
        os.environ.get("WORKER_LIFETIME_S", DEFAULT_WORKER_LIFETIME_S)
    )
    WORKER_LIVENESS: int = int(os.environ.get(
        "WORKER_LIVENESS", DEFAULT_WORKER_LIVENESS
    ))
    WORKER_PIPE_HOST: str = os.environ["WORKER_PIPE_HOST"]
    WORKER_PIPE_PORT: int = int(os.environ["WORKER_PIPE_PORT"])
ENV = _ENV()
