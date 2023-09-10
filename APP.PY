from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import pytz
import random


app = FastAPI()
class ResponseData(BaseModel):
STATUS_CODE = 200
NAME = "ahmed_bukar"
TRACK = "backend"
GITHUB_REPO_URL = "https://github.com/Yerwahub/INTERSHIP"
GITHUB_FILE_URL = "https://github.com/Yerwahub/INTERSHIP/blob/main/task1/APP.PY"
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

@app.get("/api", response_model=ResponseData)
async def get_data(slack_name: str = "ahmed_bukar", track: str = "backend", status_code: int = 200):
    current_time_utc = datetime.datetime.now(pytz.utc)
    offset_minutes = random.randint(-2, 2)
    current_time_with_offset = current_time_utc + datetime.timedelta(minutes=offset_minutes)
    current_time_with_offset_str = current_time_with_offset.strftime("%Y-%m-%dT%H:%M:%SZ")
   

    response_data = ResponseData {
        "slack_name": slack_name,
        "current_day": weekday[datetime.datetime.today().weekday()],
        "utc_time": current_time_with_offset_str,
        "track": track,
        "github_file_url": GITHUB_FILE_URL,
        "github_repo_url": GITHUB_REPO_URL,
        "status_code": status_code
    }

    return response_data
