"""
This file contains the unit tests for the Flask application.
"""

import unittest
from app import app


class TestApp(unittest.TestCase):
    """
    Tests for search methods for Flask app
    """

    def setUp(self):
        """This function sets up the test client for the Flask application.
        Args:
            None
        Returns:
            None
        """
        self.app = app.test_client()

    def test_homepage(self):
        """Test homepage
        Args:
            None
        Returns:
            None

        """
        response = self.app.get("/")
        self.assertEqual(
            b'To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;". \
    The options for field are title, author, and genre.',
            response.data,
        )

    def test_search_author(self):
        """Test for a valid author search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/author/Kristin Cast")
        self.assertEqual(
            b"Kalona's Fall by Kristin Cast, P.C. Cast (ISBN not found)",
            response.data,
        )

    def test_search_title(self):
        """Test for valid title search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/title/kaleidoscope")
        self.assertEqual(
            b"Kaleidoscope by Danielle Steel (ISBN: 0440236924)<br>Kaleidoscope Song by Fox Benwell (ISBN: 1481477676)",
            response.data,
        )

    def test_search_genre(self):
        """Test for valid genre search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/genre/lgbt")
        self.assertEqual(
            b"Kapaemahu by Joe Wilson, Daniel Sousa, Hinaleimoana Wong-Kalu, Dean Hamer (ISBN: 0593530063)<br>Kaleidoscope Song by Fox Benwell (ISBN: 1481477676)<br>Kate in Waiting by Becky Albertalli (ISBN: 0062643835)",
            response.data,
        )

    def test_search_invalid_field(self):
        """Test for invalid field search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/bad-field/search")
        self.assertEqual(400, response.status_code)

    def test_unknown_page(self):
        """Test for unknown page
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/not/a/real/page")
        self.assertEqual(
            b'404: Page not found<br>To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;". \
    The options for field are title, author, and genre.',
            response.data,
        )
