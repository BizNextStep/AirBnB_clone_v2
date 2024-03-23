#!/usr/bin/python3


"""Initialize the engine package."""
from .file_storage import FileStorage


storage = FileStorage()
storage.reload()
