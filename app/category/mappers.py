from . import models


def map_status(item: dict) -> models.Status:
  return models.Status(
    id = item.get('id'),
    name = item.get('name'),
    description = item.get('description'),
    type = item.get('type'),
    isActive = item.get('isActive'),
  )

def map_category(item: dict) -> models.Category:
  return models.Category(
    id = item.get('id'),
    name = item.get('name'),
    description = item.get('description'),
    iconUrl = item.get('iconUrl'),
    isActive = item.get('isActive'),
    status = map_status(item.get('status')),
  )

def map_category_service(item: dict) -> models.CategoryService:
  return models.CategoryService(
    id = item.get('id'),
    name = item.get('name'),
    description = item.get('description'),
    iconUrl = item.get('iconUrl'),
    isActive = item.get('isActive'),
    prefix = item.get('prefix'),
    category = map_category(item.get('category')),
    status = map_status(item.get('status')),
  )