import unittest
from unittest.mock import MagicMock, patch
import azure.functions as func

class TestGetResumeCounter(unittest.TestCase):

    @patch('azure.cosmos.CosmosClient')
    def test_http_trigger_structure(self, mock_cosmos):
        # Simula una richiesta HTTP GET
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/GetResumeCounter'
        )
        
        # Verifica la costruzione dell'oggetto HttpRequest
        self.assertEqual(req.method, 'GET')
        self.assertEqual(req.url, '/api/GetResumeCounter')

if __name__ == '__main__':
    unittest.main()
