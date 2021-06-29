import unittest
import json

from unittest.mock import patch

from src.sagebase_sc_cfnproduct.models import ResourceHandlerRequest
from src.sagebase_sc_cfnproduct import handlers

class TestHandlers(unittest.TestCase):

  def test_create_handler(self):
    fake_request = ResourceHandlerRequest(baseResRequest)

      # {
      #   "clientRequestToken": "4b90a7e4-b790-456b-a937-0cfdfa211dfe",
      #   "desiredResourceState": {
      #     "Name": "MyBlog",
      #     "SubnetId": "subnet-0bc6136e"
      #   },
      #   "logicalResourceIdentifier": "MyResource"
      # }

    handlers.create_handler(None, fake_request, None)

  def test_update_handler(self):
    handlers.update_handler(None, None, None)

  def test_delete_handler(self):
    handlers.delete_handler(None, None, None)

  def test_read_handler(self):
    handlers.read_handler(None, None, None)

  def test_list_handler(self):
    handlers.list_handler(None, None, None)
