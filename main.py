import subprocess

from fastapi import FastAPI, HTTPException, Request
from yuanfen import Config, Logger, SuccessResponse

app = FastAPI()
config = Config("/etc/docker-webhook/config.yaml")
logger = Logger()


@app.get("/health")
def health_check():
    return SuccessResponse(data="OK")


@app.get("/webhook/{webhook_id}")
def webhook(webhook_id: str, request: Request):
    if config["webhooks"]:
        for webhook in config["webhooks"]:
            if webhook["id"] == webhook_id:
                logger.info(f"`{webhook_id}` webhook triggered from {request.client.host}")
                logger.info(f"`{webhook_id}` webhook command: {webhook['command']}")
                result = subprocess.run(webhook["command"], shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    logger.info(f"`{webhook_id}` webhook executed successfully:\n{result.stdout}")
                else:
                    logger.error(f"`{webhook_id}` webhook executed with error:\n{result.stderr}")
                return SuccessResponse()
        raise HTTPException(status_code=404, detail=f"`{webhook_id}` webhook not found in config.yaml")
    raise HTTPException(status_code=500, detail="`webhooks` not found in config.yaml")
