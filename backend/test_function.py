import unittest
from unittest.mock import MagicMock, patch
import azure.functions as func
import azure.cosmos

class TestGetResumeCounter(unittest.TestCase):

    @patch('azure.cosmos.CosmosClient')
    def test_http_trigger_structure(self, mock_cosmos):
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/GetResumeCounter'
        )
        
        self.assertEqual(req.method, 'GET')
        self.assertEqual(req.url, '/api/GetResumeCounter')

if __name__ == '__main__':
    unittest.main()
