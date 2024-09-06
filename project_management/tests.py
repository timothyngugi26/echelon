from django.test import TestCase
from django.urls import reverse

class ProjectManagementTests(TestCase):

    def test_profile_page(self):
        """Test if the profile page loads successfully."""
        response = self.client.get(reverse('profile_page'))  # Uses the URL name from urls.py
        self.assertEqual(response.status_code, 200)  # Check if the page loads correctly (status code 200)
        self.assertTemplateUsed(response, 'profile_page.html')  # Check if the correct template is used

    def test_projects_page(self):
        """Test if the projects page loads successfully."""
        response = self.client.get(reverse('projects'))  # Uses the URL name from urls.py
        self.assertEqual(response.status_code, 200)  # Check if the page loads correctly
        self.assertTemplateUsed(response, 'projects.html')  # Check if the correct template is used

    def test_project_in_progress_page(self):
        """Test if the project in progress page loads successfully."""
        response = self.client.get(reverse('project_in_progress'))  # Uses the URL name from urls.py
        self.assertEqual(response.status_code, 200)  # Check if the page loads correctly
        self.assertTemplateUsed(response, 'project_in_progress.html')  # Check if the correct template is used

