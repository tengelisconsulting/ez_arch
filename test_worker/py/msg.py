import logging

import zmq

from app import App
from app import Frames


def send(
        app: App,
        frames: Frames
)-> None:
    frames = [b"", b"\x01"] + frames # INPUT FLAT
    app.dealer.send_multipart(frames)
    return


def send_heartbeat(app: App)-> None:
    frames = [
        b"\x01",          # WORKER LEVEL 1
        app.service_name  # LEVEL 2 HEARTBEAT
    ] 
    return send(app, frames)


def connect(app: App)-> App:
    router = app.c.socket(zmq.ROUTER)
    router.connect(app.in_con_s)
    logging.info("router connected to %s", app.in_con_s)
    dealer = app.c.socket(zmq.DEALER)
    dealer.connect(app.out_con_s)
    logging.info("dealer connected to %s", app.out_con_s)
    app.poller.register(router, zmq.POLLIN)
    return app._replace(
        dealer = dealer,
        router = router,
    )