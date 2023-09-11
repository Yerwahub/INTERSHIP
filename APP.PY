from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime
import pytz
import random

app = FastAPI()

class ResponseData(BaseModel):
    slack_name = str = "ahmed_bukar"
    track = str = "backend"
    github_file_url = str = "https://github.com/Yerwahub/INTERSHIP"
    github_repo_url = str = "https://github.com/Yerwahub/INTERSHIP/blob/main/task1/APP.PY"
    status_code = int = 200
@app.get("/api", response_model=ResponseData)
async def get_data(
    slack_name: str = None,
    track: str = None,
    status_code: int = None
):
    slack_name = slack_name or "ahmed_bukar"
    track = track or "backend"
    status_code = status_code or 200

    current_time_utc = datetime.datetime.now(pytz.utc)
    offset_minutes = datetime.timedelta(minutes=random.randint(-2, 2))
    current_time_with_offset = current_time_utc + datetime.timedelta(minutes=offset_minutes)
    current_time_with_offset_str = current_time_with_offset.strftime("%Y-%m-%dT%H:%M:%SZ")

    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = weekday[datetime.datetime.today().weekday()]

    github_repo_url = "https://github.com/Yerwahub/INTERSHIP"
    github_file_url = "https://github.com/Yerwahub/INTERSHIP/blob/main/task1/APP.PY"

    response_data = ResponseData(
        slack_name=slack_name,
        current_day=current_day,
        utc_time=current_time_with_offset_str,
        track=track,
        github_file_url=github_file_url,
        github_repo_url=github_repo_url,
        status_code=status_code
    )

    return response_data 

