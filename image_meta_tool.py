from PIL import Image, ExifTags
from typing import Any, Dict


def image_metadata(path: str) -> Dict[str, Any]:
    """
    Return basic image metadata and EXIF when available.

    Args:
        path: Local image path.

    Returns:
        Dict with format, size, mode, and exif dict (when present).
    """
    with Image.open(path) as im:
        info = {"format": im.format, "size": im.size, "mode": im.mode}
        exif = {}
        try:
            raw_exif = im._getexif() or {}
            for k, v in raw_exif.items():
                tag = ExifTags.TAGS.get(k, k)
                exif[tag] = v
        except Exception:
            exif = {}
    info["exif"] = exif
    return info


@mcp.tool()
def image_meta_tool(path: str) -> Dict[str, Any]:
    """
    Image metadata tool that returns format, dimensions and EXIF data.

    Args:
        path: Local path to image file.

    Returns:
        Dictionary of metadata.
    """
    return image_metadata(path)

