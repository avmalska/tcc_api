import typer
import uvicorn
from config import settings


cli = typer.Typer(name="Tcc API")


@cli.command()
def run(
    port: int = settings["port"],
    host: str = settings["host"],
    log_level: str = settings["log_level"],
    reload: bool = settings["reload"]
):
    uvicorn.run(
        "app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )
