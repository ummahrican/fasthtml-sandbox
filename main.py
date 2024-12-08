from fasthtml.common import *
from fastapi.middleware.gzip import GZipMiddleware
from pages import index

# TODO Add OAuth: https://docs.fastht.ml/explains/oauth.html#a-minimal-login-flow-github
hdrs = (
    Html(lang="en"),
    Link(rel="stylesheet", href="app.css", type="text/css"),
)


app = FastHTML(
    lang="en",
    hdrs=hdrs,
)
app.add_middleware(GZipMiddleware, minimum_size=500)


@app.get("/{fname:path}.{ext:static}")
def tailwind(fname: str, ext: str):
    headers = {"Cache-Control": "public, max-age=31536000"}
    return FileResponse(f"public/{fname}.{ext}", headers=headers)


@app.get("/")
def landing():
    return (
        Title("Nordic Store"),
        Meta(
            name="description",
            content="A store for Nords to fulfill all their shopping and business needs for the next viking raid.",
        ),
        index.content,
    )


serve()
