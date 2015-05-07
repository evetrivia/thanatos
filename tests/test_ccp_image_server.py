

import mock
import unittest2

from thanatos import ccp_image_server


class CCPImageServerTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    @mock.patch('thanatos.ccp_image_server.get_image_server_link')
    def test_get_character_image_links(self, mock_get_image_server_link):
        """ Test the character image links makes all the right calls to get_image_server_link. """

        links = ccp_image_server.get_character_image_links(123456)

        mock_get_image_server_link.assert_any_call(123456, 'char', 32)
        mock_get_image_server_link.assert_any_call(123456, 'char', 64)
        mock_get_image_server_link.assert_any_call(123456, 'char', 128)
        mock_get_image_server_link.assert_any_call(123456, 'char', 256)
        mock_get_image_server_link.assert_any_call(123456, 'char', 512)
        mock_get_image_server_link.assert_any_call(123456, 'char', 1024)
        self.assertEqual(mock_get_image_server_link.call_count, 6)

    @mock.patch('thanatos.ccp_image_server.get_image_server_link')
    def test_get_corporation_image_links(self, mock_get_image_server_link):
        """ Test the corporation image links makes all the right calls to get_image_server_link. """

        links = ccp_image_server.get_corporation_image_links(123456)

        mock_get_image_server_link.assert_any_call(123456, 'corp', 32)
        mock_get_image_server_link.assert_any_call(123456, 'corp', 64)
        mock_get_image_server_link.assert_any_call(123456, 'corp', 128)
        mock_get_image_server_link.assert_any_call(123456, 'corp', 256)
        self.assertEqual(mock_get_image_server_link.call_count, 4)

    @mock.patch('thanatos.ccp_image_server.get_image_server_link')
    def test_get_type_image_links(self, mock_get_image_server_link):
        """ Test the type image links makes all the right calls to get_image_server_link. """

        links = ccp_image_server.get_type_links(123456)

        mock_get_image_server_link.assert_any_call(123456, 'type', 32)
        mock_get_image_server_link.assert_any_call(123456, 'type', 64)
        mock_get_image_server_link.assert_any_call(123456, 'type', 128)
        mock_get_image_server_link.assert_any_call(123456, 'type', 256)
        mock_get_image_server_link.assert_any_call(123456, 'type', 512)
        self.assertEqual(mock_get_image_server_link.call_count, 5)

    def test_get_image_server_link_char(self):
        """ Test get_image_link returns the correct URL for a character. """

        image_link = ccp_image_server.get_image_server_link(123456, 'char', 32)

        self.assertEqual(image_link, 'https://image.eveonline.com/Character/123456_32.jpg')

    def test_get_image_server_link_corp(self):
        """ Test get_image_link returns the correct URL for a corporation. """

        image_link = ccp_image_server.get_image_server_link(123456, 'corp', 32)

        self.assertEqual(image_link, 'https://image.eveonline.com/Corporation/123456_32.png')

    def test_get_image_server_link_alliance(self):
        """ Test get_image_link returns the correct URL for a alliance. """

        image_link = ccp_image_server.get_image_server_link(123456, 'alli', 32)

        self.assertEqual(image_link, 'https://image.eveonline.com/Alliance/123456_32.png')

    def test_get_image_server_link_faction(self):
        """ Test get_image_link returns the correct URL for a faction. """

        image_link = ccp_image_server.get_image_server_link(123456, 'fac', 32)

        self.assertEqual(image_link, 'https://image.eveonline.com/Alliance/123456_32.png')

    def test_get_image_server_link_other(self):
        """ Test get_image_link returns the correct URL for other. """

        image_link = ccp_image_server.get_image_server_link(123456, 'other', 32)

        self.assertEqual(image_link, 'https://image.eveonline.com/Render/123456_32.png')