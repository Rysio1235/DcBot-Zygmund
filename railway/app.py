from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/v")
def video():
    url = request.args.get("url")
    base = os.environ.get("BASE_URL", "http://localhost:5000")
    return f"""
    <html>
      <head>
        <meta property="og:type" content="video.other" />
        <meta property="og:video" content="{url}" />
        <meta property="og:video:type" content="video/mp4" />
        <meta property="og:video:width" content="1280" />
        <meta property="og:video:height" content="720" />
        <meta property="og:url" content="{url}" />
        <link rel="alternate" type="application/json+oembed"
          href="{base}/oembed?url={url}"
          title="video" />
      </head>
      <body>
        <video src="{url}" controls width="1280" height="720"></video>
      </body>
    </html>
    """, 200, {"Content-Type": "text/html"}