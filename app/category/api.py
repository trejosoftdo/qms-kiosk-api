import requests
from .. import environment
from . import models


common_headers = {
  'Content-Type': 'application/json',
  'api_key': environment.core_api_key,
}

def get_categories(req: models.GetCategoriesRequest) -> requests.Response:
  """Gets the list of available categories for the application in context

  Args:
      req (models.GetCategoriesRequest): Request to get categories

  Returns:
      requests.Response: The response from the core api.
  """
  categories_url = f"{environment.core_api_base_url}/api/v1/categories"
  params = {
    'active': req.params.active,
    'offset': req.params.offset,
    'limit': req.params.limit,
  }
  headers = {
    **common_headers,
    'application': req.headers.application,
    'authorization': req.headers.authorization,
  }
  return requests.get(categories_url, headers = headers, params = params)


def get_category_services(req: models.GetCategoryServicesRequest) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        req (models.GetCategoryServicesRequest): Request to get the services of a category
        
    Returns:
        models.CategoryServicesListResponse: The list of services for the category
    """
    services_url = f"{environment.core_api_base_url}/api/v1/categories/{req.categoryId}/services"
    params = {
      'active': req.params.active,
      'offset': req.params.offset,
      'limit': req.params.limit,
    }
    headers = {
      **common_headers,
      'application': req.headers.application,
      'authorization': req.headers.authorization,
    }
    return requests.get(services_url, headers = headers, params = params)