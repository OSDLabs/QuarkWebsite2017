from django import forms
from .models import *

GENDER_CHOICES = (
    (u'M',u'Male'),
    (u'F',u'Female'),
    (u'N',u"Don't wish to reveal")
    )

YEAR_CHOICES = (
    (u'U1',u'Undergraduate 1st year'),
    (u'U2',u'Undergraduate 2nd year'),
    (u'U3',u'Undergraduate 3rd year'),
    (u'U4',u'Undergraduate 4th year'),
    (u'P1',u'Postgraduate 1st year'),
    (u'P2',u'Postgraduate 2nd year'),
    (u'SS',u'Schooling'),
    (u'PH',u'PhD.'),
    )



PANEL_DES = (
    (u'Burnout',u'Burnout'),
    (u'Mortar Kombat',u'Mortar Kombat'),
    (u'Trailblazers',u'Trailblazers'),
    (u'Creation',u'Creation'),
    (u'Contraption',u'Contraption'),
    )

PANEL_ELIXIR = (
    (u'Quark National Quiz',u'Quark National Quiz'),
    (u'Carpe Dictum',u'Carpe Dictum'),
    (u'Ganimatoonics',u'Ganimatoonics'),
    (u'The Mayday Mystery',u'The Mayday Mystery'),
    (u'Edorado',u'Edorado'),
    (u'Numb3rs',u'Numb3rs'),
    (u'Celesticon',u'Celesticon'),
    )

PANEL_ROBO = (
    (u'RoboKombat',u'RoboKombat'),
    (u'RoboKick',u'RoboKick'),
    (u'RoboSumo',u'RoboSumo'),
    (u'RoboRace',u'RoboRace'),
    (u'Line Following Bot',u'Line Following Bot'),
    )

PANEL_PROG = (
    (u'Reverse Coding',u'Reverse Coding'),
    (u'Cryptic Enigma',u'Cryptic Enigma'),
    (u'BITSCTF',u'BITSCTF'),
    (u'CodeJam',u'CodeJam'),
    (u'Hackathon',u'Hackathon'),
    (u'Code-O-Shuffle',u'Code-O-Shuffle'),
    )

PANEL_SPECIALS = (
    (u'Open Showcase',u'Open Showcase'),
    (u'Paper Presentation',u'Paper Presentation'),
    (u'Industrial Process Design',u'Industrial Process Design'),
    (u'School Bag',u'School Bag'),
    (u'Shutter Up',u'Shutter Up'),
    )

PANEL_INIT = (
    (u'Principal Initiatives',u'Principal Initiatives'),
    (u'My Green Idea',u'My Green Idea'),
    (u'Smart Cities, Smart Solutions',u'Smart Cities, Smart Solutions'),
    (u'Design for Disaster',u'Design for Disaster'),
    (u'IN Justice',u'IN Justice'),
    )

PANEL_ELECT = (
    (u'Digilogica',u'Digilogica'),
    (u'Arduino Open',u'Arduino Open'),
    (u'Analog Tussle',u'Analog Tussle'),
    (u'Matmania',u'Matmania'),
    (u'Embition',u'Embition'),
    )

PANEL_CORPORATE = (
    (u'Quest',u'Quest'),
    (u'OpStrat',u'OpStrat'),
    (u'BlueChip Beatdown',u'BlueChip Beatdown'),
    (u'Wolf of Wallstreet',u'Wolf of Wallstreet'),
    (u'Wallstreet Revolution',u'Wallstreet Revolution'),
    (u'Bitcoin Ideation Challenge',u'Bitcoin Ideation Challenge'),
    )

WORKSHOP = (
    (u'ReactJS', u'Sabre - ReactJS'),
    (u'Spark', u'Sabre - Apache Spark'),
    (u'Deep Learning', u'NVIDIA - Deep Learning'),
    (u'Fusion 360', u'AUTODESK - Product Design using Fusion 360'),
    (u'App Development', u'MathWorks - App Development'),
    (u'Webench', u'Texas Instruments - Webench'),
    (u'Financial Workshop', u'Zerodha, Bajaj - Financial Workshop'),
    (u'Networking', u'CISCO - Networking Workshop '),
    )

class QuickForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuickForm, self).__init__(*args, **kwargs)

        self.fields['panel_des'].label = 'Design & Build'
        self.fields['panel_elixir'].label = 'Elixir'
        self.fields['panel_robo'].label = 'Roboficial'
        self.fields['panel_prog'].label = 'Programming Inc.'
        self.fields['panel_specials'].label = 'Specials'
        self.fields['panel_init'].label = 'Initiatives'
        self.fields['panel_elect'].label = 'Electrify'
        self.fields['panel_corporate'].label = 'Corporate'
        self.fields['workshop'].label = 'Workshop'

    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    institute = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    panel_des = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_DES,
        )
    panel_elixir = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_ELIXIR,
        )
    panel_robo = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_ROBO,
        )
    panel_prog = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_PROG,
        )
    panel_specials = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_SPECIALS,
        )
    panel_init = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_INIT,
        )
    panel_elect = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_ELECT,
        )
    panel_corporate = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PANEL_CORPORATE,
        )
    workshop = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=WORKSHOP,
        )
        