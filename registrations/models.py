from django.db import models

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
YEAR_CHOICES = [('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Final Year', 'Final Year')]
CONTACT_METHOD_CHOICES = [('Phone', 'Phone'), ('Email', 'Email'), ('SMS', 'SMS')]
GYM_HISTORY_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
BRANCH_CHOICES = [('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Final Year', 'Final Year'), ('Faculty', 'Faculty')]
HEALTH_CONDITION_CHOICES = [
    ('High Blood Pressure', 'High Blood Pressure'),
    ('Low Blood Pressure', 'Low Blood Pressure'),
    ('Asthma', 'Asthma'),
    ('Surgery in the last 3 years', 'Surgery in the last 3 years'),
    ('Fainting Spells/Dizzy', 'Fainting Spells/Dizzy'),
    ('Other', 'Other'),
]

class OfflineRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    year_of_study = models.CharField(max_length=20, choices=YEAR_CHOICES)
    preferred_contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES)
    fitness_goals = models.JSONField(blank=True, null=True)
    roll_no = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    fitness_challenges = models.TextField(blank=True, null=True)
    gym_member_before = models.CharField(max_length=3, choices=GYM_HISTORY_CHOICES, blank=True)
    terms_agreed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Offline)"

class OnlineRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    year_of_study = models.CharField(max_length=20, choices=YEAR_CHOICES)
    preferred_contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES)
    fitness_goals = models.JSONField(blank=True, null=True)
    roll_no = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    fitness_challenges = models.TextField(blank=True, null=True)
    gym_member_before = models.CharField(max_length=3, choices=GYM_HISTORY_CHOICES, blank=True)
    terms_agreed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Online)"

class YogaRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    registration_number = models.CharField(max_length=50)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    health_condition = models.CharField(max_length=50, choices=HEALTH_CONDITION_CHOICES)
    other_health_issues = models.TextField(blank=True, null=True)
    acknowledgement = models.BooleanField(default=False)
    submission_date = models.DateField()
    terms_agreed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Yoga)"
