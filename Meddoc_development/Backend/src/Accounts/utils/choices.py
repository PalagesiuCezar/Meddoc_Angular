from django.utils.translation import ugettext_lazy as _

SEX = (
       ('1', _('Male')),
       ('2', _('Female')),
       ('3', _('Prefer not to say...')),
    )

TYPE = (
        ('1' , _('Minor Emergency')),
        ('2', _('Major Emergency')),
        ('3', _('Emergent')),
    )

HOSPITALS = (
    ('1', _('Spitalul Judetean Timisoara')),
    ('2', _('Spitalul Militar Timisoara')),
    ('3', _('Spitalul Louis Turcanu Timisoara')),
    ('4', _('Spitalul Clinic Victor Babes ')),
    ('6', _('Spitalul Regina Maria')),
    ('5', _('Other..')),
)

DEPARTMENT = (
    ('1', _('Urgente')),
    ('2', _('Fizio-terapie')),
    ('3', _('Dentist')),
    ('4', _('Urologie')),
    ('5', _('Kineto-terapie')),
    ('6', _('Chirurgie Plastica')),
    ('7', _('Neurologie')),
    ('8', _('Cardiologie')),
    ('9', _('Ortopedie')),
    ('10', _('Ginecologie')),
    ('11', _('Chirurgie Generala')),
    ('12', _('Other..')),
)