from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from ice.routes import agents, traces
from ice.trace import trace_dir

dist_dir = trace_dir.parent.parent / "dist"

app = FastAPI()
app.include_router(agents.router)
app.include_router(traces.router)
app.mount("/api/traces/", StaticFiles(directory=trace_dir), name="static")
app.mount("/assets/", StaticFiles(directory=dist_dir / "assets"), name="static")

@app.get("/{_full_path:path}")
async def catch_all(_full_path: str):
    return FileResponse(dist_dir / "index.html")
