from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.forms import RedactorExperienceForm


class ValidExperienceFormTests(TestCase):
    @staticmethod
    def create_form(test_experience_year):
        return RedactorExperienceForm(
            data={"years_of_experience": test_experience_year}
        )

    def test_validation_experience_year_with_valid_data(self):
        self.assertTrue(self.create_form(2).is_valid())

    def test_length_of_experience_year_should_be_not_more_than_30(self):
        self.assertFalse(self.create_form(31).is_valid())

    def test_length_of_experience_year_should_be_not_less_than_0(self):
        self.assertFalse(self.create_form(-1).is_valid())


class RedactorViewsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            years_of_experience=10,
            first_name="Admin",
            last_name="User",
            password="1qwerty2",
        )
        self.client.force_login(self.user)

    def test_update_redactor_years_of_experience_with_valid_data(self):
        test_years_of_experience = 20
        response = self.client.post(
            reverse("newspaper:redactor-update", kwargs={"pk": self.user.id}),
            data={"years_of_experience": test_years_of_experience},
        )
        self.assertEqual(response.status_code, 302)

    def test_update_redactor_years_of_experience_with_not_valid_data(self):
        test_years_of_experience = 35
        response = self.client.post(
            reverse("newspaper:redactor-update", kwargs={"pk": self.user.pk}),
            data={"years_of_experience": test_years_of_experience},
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_redactor(self):
        redactor = get_user_model().objects.create(
            username="bad_admin.user",
            years_of_experience=1,
            first_name="Bad Admin",
            last_name="User2",
            password="qwerty100",
        )
        response = self.client.post(
            reverse("newspaper:redactor-delete", kwargs={"pk": redactor.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            get_user_model().objects.filter(id=redactor.id).exists()
        )
