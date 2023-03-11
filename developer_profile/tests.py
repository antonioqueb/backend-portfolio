from django.test import TestCase
from developer_profile.models import DeveloperProfile

class DeveloperProfileTest(TestCase):
    
    def setUp(self):
        print("setUp method called")
        self.profile = DeveloperProfile.objects.create(
            artistic_name='dev', full_name='John Smith',
            title='Web Developer', nationality='American',
            short_description='Experienced Web Developer',
            long_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            identity='developer', actual_job='Software Engineer',
            tag_line='Building great websites', date_of_birth=("1990,01,01"),
            github='https://github.com/johnsmith', linkedin='https://www.linkedin.com/in/johnsmith',
            twitter='https://twitter.com/johnsmith', whatsapp=123456789,
            languages=['Python', 'JavaScript'], website='https://johnsmith.com',
            strength=['Problem solving', 'Attention to detail'],
            soft_skills=['Communication', 'Teamwork'], hard_skills=['Backend development', 'Frontend development'],
            goals=['Learn new technologies', 'Improve coding skills'],
            technologies=['Django', 'React'], libraries=['NumPy', 'Pandas'],
            frameworks=['Bootstrap', 'Materialize'], microframeworks=['Flask'],
            location='New York', certifications=['AWS Certified Developer'],
            profile_image='files/profile_image.png', illustrations='files/illustrations.png',
            graphics_design='files/graphics_design.png'
        )
    
    def test_profile_creation(self):
        profile = DeveloperProfile.objects.get(id=1)
        self.assertEqual(profile.artistic_name, 'dev')
        self.assertEqual(profile.full_name, 'John Smith')
        self.assertEqual(profile.title, 'Web Developer')
        self.assertEqual(profile.nationality, 'American')
        self.assertEqual(profile.short_description, 'Experienced Web Developer')
        self.assertEqual(profile.long_description, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        self.assertEqual(profile.identity, 'developer')
        self.assertEqual(profile.actual_job, 'Software Engineer')
        self.assertEqual(profile.tag_line, 'Building great websites')
        self.assertEqual(profile.date_of_birth, '1990-01-01')
        self.assertEqual(profile.github, 'https://github.com/johnsmith')
        self.assertEqual(profile.linkedin, 'https://www.linkedin.com/in/johnsmith')
        self.assertEqual(profile.twitter, 'https://twitter.com/johnsmith')
        self.assertEqual(profile.whatsapp, 123456789)
        self.assertEqual(profile.languages, ['Python', 'JavaScript'])
        self.assertEqual(profile.website, 'https://johnsmith.com')
        self.assertEqual(profile.strength, ['Problem solving', 'Attention to detail'])
        self.assertEqual(profile.soft_skills, ['Communication', 'Teamwork'])
        self.assertEqual(profile.hard_skills, ['Backend development', 'Frontend development'])
        self.assertEqual(profile.goals, ['Learn new technologies', 'Improve coding skills'])
        self.assertEqual(profile.technologies, ['Django', 'React'])
        self.assertEqual(profile.libraries, ['NumPy', 'Pandas'])
        self.assertEqual(profile.frameworks, ['Bootstrap', 'Materialize'])
        self.assertEqual(profile.microframeworks, ['Flask'])
        self.assertEqual(profile.location, 'New York')
        self.assertEqual(profile.certifications, ['AWS Certified Developer'])
