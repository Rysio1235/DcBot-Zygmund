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
        <link rel="alternate" type="application/json+oembed"
          href="{base}/oembed?url={url}"
          title="video" />
      </head>
      <body></body>
    </html>
    """, 200, {"Content-Type": "text/html"}

@app.route("/oembed")
def oembed():
    url = request.args.get("url")
    return jsonify({
        "type": "video",
        "version": "1.0",
        "title": "Video",
        "width": 1280,
        "height": 720,
        "html": f'<video src="{url}" controls></video>',
        "provider_name": "VideoEmbed",
        "provider_url": os.environ.get("BASE_URL", "http://localhost:5000")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)