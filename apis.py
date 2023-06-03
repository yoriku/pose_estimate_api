from fastapi import FastAPI, File, Request, UploadFile
from util_pose import pose_estimate, binaly2img
app = FastAPI()

@app.post("/api/")
async def upload_file(file: UploadFile):
    print(file)
    d = pose_estimate(binaly2img(await file.read()))
    print(d)
    return d