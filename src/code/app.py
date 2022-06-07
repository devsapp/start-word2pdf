import logging
import sys
import subprocess
import traceback
import oss2
import os
import json
from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/invoke', methods=['POST'])
def invoke():
    # See FC docs for all the HTTP headers: https://www.alibabacloud.com/help/doc-detail/132044.htm#common-headers
    request_id = request.headers.get("x-fc-request-id", "")
    print("FC Invoke Start RequestId: " + request_id)

    # Get function input, data type is bytes, convert as needed
    event = request.get_data()
    event_str = event.decode("utf-8")

    # Use the following code to get temporary STS credentials to access Alibaba Cloud services
    # access_key_id = request.headers['x-fc-access-key-id']
    # access_key_secret = request.headers['x-fc-access-key-secret']
    # access_security_token = request.headers['x-fc-security-token']

    region = request.headers['x-fc-region']
    oss_endpoint = "http://oss-{}-internal.aliyuncs.com".format(region)

    # do your things
    try:
        print(event_str)
        evt = json.loads(event)
        word_file = evt["oss_file"]
        fileDir, tempfilename = os.path.split(word_file)
        shortname, _ = os.path.splitext(tempfilename)
        accessKeyId = request.headers['x-fc-access-key-id']
        accessKeySecret = request.headers['x-fc-access-key-secret']
        securityToken = request.headers['x-fc-security-token']
        auth = oss2.StsAuth(accessKeyId, accessKeySecret, securityToken)
        bucket = oss2.Bucket(auth, oss_endpoint, os.environ['OSS_BUCKET'])
        bucket.get_object_to_file(word_file, '/tmp/' + tempfilename)
        subprocess.check_call(["soffice", "--convert-to", "pdf:writer_pdf_Export", "--outdir",
                               "/tmp", '/tmp/' + tempfilename])
        subprocess.check_call(["ls", "-ll", "/tmp"])
        pdf_file = os.path.join(fileDir, shortname + ".pdf")
        result = bucket.put_object_from_file(
            pdf_file, '/tmp/' + shortname + ".pdf")

        subprocess.check_call(["rm", "-rf", '/tmp/' + tempfilename])
        subprocess.check_call(["rm", "-rf", '/tmp/' + shortname + ".pdf"])
        print("FC Invoke End RequestId: " + request_id)
        if result.status == 200:
            return "upload to oss success!"
        else:
            return "upload fail, error code %s " % result.status

    except Exception as e:
        exc_info = sys.exc_info()
        trace = traceback.format_tb(exc_info[2])
        errRet = {
            "message": str(e),
            "stack": trace
        }
        print(errRet)
        print("FC Invoke End RequestId: " + request_id +
              ", Error: Unhandled function error")
        return errRet, 404, [("x-fc-status", "404")]


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9000)
