import os

access_key = os.getenv("AWS_ACCCESS_KEY")
secret_key = os.getenv("AWS_SECRET_KEY")

import boto3


def uploadPublicFile(path, folder = ""):
    s3 = boto3.client('s3')
    filename = (path.split("/"))[-1]
    if folder == "":
        finalPath = filename
    else:
        finalPath = folder + "/" + filename
    response = s3.upload_file(
        path, "files-work", finalPath,
        ExtraArgs={'ACL': 'public-read'}
    )
    print("File uploding: ", response)

# uploadPublicFile("cat.png", "bot_test")