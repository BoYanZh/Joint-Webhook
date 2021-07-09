import uvicorn

from webhook_elf.config import settings


def main() -> None:
    uvicorn.run(
        "webhook_elf:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        reload_dirs=["webhook_elf"],
    )


if __name__ == "__main__":
    main()
