import logging
import unittest

from eventlet.green import socket
from ListeningSocketHandler import ListeningSocketHandler

class BasicTests(unittest.TestCase):
    def test_ipv4(self):
        lsh4 = ListeningSocketHandler(ipv6=False)
        self.assertIsInstance(lsh4.getsockname()[1], int)
    
    def test_ipv6(self):
        lsh6 = ListeningSocketHandler(ipv6=True)
        self.assertIsInstance(lsh6.getsockname()[1], int)
    
class TestListeningSocketHandler(unittest.TestCase):
    def setUp(self):
        self.log = logging.getLogger('testlisteningsockethandler')
        #self.log.setLevel(logging.DEBUG)
        # default will bind to any unsed port.
        self.lsh = ListeningSocketHandler()
        #self.lsh.setLevel(logging.DEBUG)
        self.log.addHandler(self.lsh)

    def _send_message(self):
        self.log.debug("Sending debugging")
        self.log.info("Sending information")
        self.log.warn("Sending a warning")
        self.log.error("Sending an error")
        self.log.critical("Exploding")

    def test_send_message(self):
        self._send_message()

    def test_recv_message(self):
        port = self.lsh.getsockname()[1]

        c = socket.create_connection(("localhost", port), 2)
        self._send_message()
        self.assertEquals(c.recv(2048),
"""Sending a warning
Sending an error
Exploding
""")
        c.close()

if __name__ == '__main__':
    unittest.main()
