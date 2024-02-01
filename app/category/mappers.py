"""Category API mappers
"""

from . import models


def map_status(item: dict) -> models.Status:
    """Maps a status item from the given data

    Args:
        item (dict): Status data

    Returns:
        models.Status: Mapped status
    """
    return models.Status(
        id=item.get("id"),
        name=item.get("name"),
        description=item.get("description"),
        type=item.get("type"),
        isActive=item.get("isActive"),
    )


def map_category(item: dict) -> models.Category:
    """Maps a category item from the given data

    Args:
        item (dict): category data

    Returns:
        models.Category: Mapped category
    """
    return models.Category(
        id=item.get("id"),
        name=item.get("name"),
        description=item.get("description"),
        iconUrl=item.get("iconUrl"),
        isActive=item.get("isActive"),
        status=map_status(item.get("status")),
    )


def map_category_service(item: dict) -> models.CategoryService:
    """Maps a category service from the given data

    Args:
        item (dict): service data

    Returns:
        models.CategoryService: Mapped category service
    """
    return models.CategoryService(
        id=item.get("id"),
        name=item.get("name"),
        description=item.get("description"),
        iconUrl=item.get("iconUrl"),
        isActive=item.get("isActive"),
        prefix=item.get("prefix"),
        category=map_category(item.get("category")),
        status=map_status(item.get("status")),
    )
