from reportlab.pdfbase import pdfmetrics, ttfonts
from PyPDF2 import PdfReader , PdfWriter 
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
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

# support chinese
pdfmetrics.registerFont(ttfonts.TTFont('zenhei', os.path.join(
    "/usr/share/fonts/truetype/wqy", 'wqy-zenhei.ttc')))
pdfmetrics.registerFont(ttfonts.TTFont('microhei', os.path.join(
    "/usr/share/fonts/truetype/wqy", 'wqy-microhei.ttc')))


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    print(pdf_file_in, pdf_file_mark, pdf_file_out)
    pdf_output = PdfWriter()
    with open(pdf_file_in, 'rb') as input_stream:
        pdf_input = PdfReader(input_stream, strict=False)

        pageNum = len(pdf_input.pages)
        pdf_watermark = PdfReader(open(pdf_file_mark, 'rb'), strict=False)

        for i in range(pageNum):
            page = pdf_input.pages[i]
            page.merge_page(pdf_watermark.pages[0])
            page.compress_content_streams()
            pdf_output.add_page(page)

        with open(pdf_file_out, 'wb') as f:
            pdf_output.write(f)


def _create_watermark(mark_text, pagesize=(21*cm, 29.7*cm), font="Helvetica", font_size=30, font_color=(0, 0, 0), rotate=0, opacity=1, density=(5*cm, 5*cm)):
    file_name = "/tmp/mark.pdf"
    c = canvas.Canvas(file_name, pagesize=pagesize)
    c.setFont(font, font_size)
    c.rotate(rotate)
    c.setStrokeColorRGB(0, 0, 0)
    r, g, b = font_color
    c.setFillColorRGB(r, g, b)
    c.setFillAlpha(opacity)

    row_gap, col_gap = density
    colN = int(pagesize[0]/col_gap)
    rowN = int(pagesize[1]/row_gap)
    x = colN * 4
    y = rowN * 4

    for i in range(y):
        for j in range(x):
            a = col_gap*(j - 2*colN)
            b = row_gap*(i - 2*rowN)
            c.drawString(a, b, mark_text)

    c.save()


def create_watermark(evt):
    mark_text = evt['mark_text']
    # 1cm = 28.346456692913385， defalut is A4, (21*cm, 29.7*cm)
    pagesize = evt.get(
        'pagesize', [595.275590551181, 841.8897637795275])
    font = evt.get('font', 'Helvetica')
    font_size = evt.get('font_size', 30)
    font_color = evt.get('font_color', (0, 0, 0))
    rotate = evt.get('rotate', 0)
    opacity = evt.get('opacity', 0.1)
    # default is (7*cm, 10*cm)
    density = evt.get('density', [198.4251968503937, 283.46456692913387])
    _create_watermark(mark_text, pagesize, font, font_size,
                      font_color, rotate, opacity, density)
    print('create_watermark success!')


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
        word_file = evt["word_file"]
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
        print('word to pdf  success!')
        pdf_file = os.path.join(fileDir, shortname + ".pdf")
        local_pdf_file = "/tmp/" + shortname + ".pdf"

        # add water mark
        has_watermark = evt.get("mark_text")
        if has_watermark:
            create_watermark(evt)
            local_pdf_file = '/tmp/' + shortname + "_out.pdf"
            add_watermark('/tmp/' + shortname + ".pdf",
                          '/tmp/mark.pdf', local_pdf_file)
            print('pdf add_watermark success!')

        result = bucket.put_object_from_file(
            pdf_file, local_pdf_file)

        subprocess.check_call(["ls", "-ll", "/tmp"])
        subprocess.check_call("rm -rf /tmp/*", shell=True)
        # print("After clean ...")
        # subprocess.check_call(["ls", "-ll", "/tmp"])
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
