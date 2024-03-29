from django.utils.translation import gettext_lazy as _

REGION_CHOICES = (
    ('1', _('Alabama')),
    ('2', _('Arizona')),
    ('3', _('Arkansas')),
    ('4', _('Northern California')),
    ('5', _('Central California')),
    ('6', _('Southern California')),
    ('7', _('Colorado')),
    ('8', _('Connecticut')),
    ('9', _('Wisconsin')),
    ('10', _('Texas')),
)

CENTER_CHOICES = (
    ('1', _('Northern California')),
    ('2', _('Rancho Cordova')),
    ('3', _('Reno')),
    ('4', _('Montana')),
    ('5', _('Central California')),
    ('6', _('Southern California')),
    ('7', _('Arizona')),
    ('8', _('New Mexico')),
    ('9', _('Pacific Northwest')),
    ('10', _('Bend, Oregon')),
)

MANAGER_CHOICES = (
    ('1', _('Emma')),
    ('2', _('Noah')),
    ('3', _('Bobby')),
    ('4', _('Theodore')),
    ('5', _('Henry')),
    ('6', _('Evelyn')),
    ('7', _('Isabella')),
    ('8', _('Benjamin')),
    ('9', _('Sophia')),
    ('10', _('James')),
)

WARRANTY_CODES = (
    ('1', _('Non-Warranty')),
    ('2', _('00-02 Years (Full Warranty)')),
    ('3', _('03-10 Years (Glass/Clad Finish)')),
    ('4', _('03-10 Years (Hardware/Screen)')),
    ('5', _('03-10 Years (Panel/Sash Warp)')),
    ('6', _('03-20 Years (Glass 100%)')),
    ('7', _('11-20 Years (Glass 60%)')),
)

SERVICE_CODES = (
    ('1', _('Adjust Door(s)')),
    ('2', _('Adjust Window(s)')),
    ('3', _('Adjust Window(s)& Door(s)')),
    ('4', _('Warped Panel')),
    ('5', _('Warped Sash')),
    ('6', _('Glass Problems')),
    ('7', _('Hardware Problems')),
    ('8', _('Hinges')),
    ('9', _('Fogged Glass')),
    ('10', _('Lock & Slide')),
    ('11', _('Mis-Manufacture')),
    ('12', _('Missing Product')),
    ('13', _('Sales Problem')),
    ('14', _('Outside Vendor')),
    ('15', _('Shipping Problem')),
    ('16', _('Door Leak(s)')),
    ('17', _('Window Leak(s)')),
    ('18', _('Mull Leak(s)')),
    ('19', _('Clad Finish')),
    ('20', _('Other')),
    ('21', _('Screen Problems')),
    ('22', _('Glazing Leak')),
    ('23', _('Weatherstrip')),
    ('24', _('Wood Appearance')),
    ('25', _('Wrong Product Delivered')),
    ('26', _('Damaged at Job Site')),
    ('27', _('Diagnosis')),
    ('28', _('Template')),
    ('29', _('Installation')),
    ('30', _('Field Mull Assist')),
    ('31', _('Scratched glass')),
    ('32', _('Low-E issue')),
    ('33', _('Interior IG')),
    ('34', _('Clam shell/birds eye')),
    ('35', _('Wavy glass')),
    ('36', _('Broken locking mechanism')),
    ('37', _('Aspen tape')),
    ('38', _('Finish issues')),
    ('39', _('Operator issues')),
    ('40', _('Wheel issues')),
    ('41', _('Glass broken by brad nail')),
    ('42', _('Hardware location')),
    ('43', _('OPC error')),
    ('44', _('Color/Type of hardware')),
    ('45', _('Frame dimensions')),
    ('46', _('Panel/Sash dimensions')),
    ('47', _('Jamb size')),
    ('48', _('Tempered glass')),
    ('49', _('Delaminating')),
    ('50', _('Panel separation')),
    ('51', _('Raised grain')),
    ('52', _('Wood rot')),
    ('53', _('Adhesion')),
    ('54', _('Fading')),
    ('55', _('Cracked Glass')),
    ('56', _('Delayed Shipment')),
    ('99', _('Claim')),
)

# Comment Type
COMMENT_TYPE = (
    ('Q', _('Quote')),
    ('E', _('External')),
    ('P', _('Plant')),
    ('T', _('Technition')),
    ('S', _('Schedule')),
    ('O', _('Service Order')),
    ('R', _('Job Request')),
    ('J', _('Job Site')),

    
)
# Service Status
STATUS_CODES = (
    ('1', _('Pending')),
    ('2', _('Ready')),
    ('3', _('QCd')),
    ('4', _('Shipped')),
    ('5', _('Recevied')),
)

APPOINTMENT_TYPES = (
    ('ORDR', _('Service Order')),
    ('TRVL', _('Travel Time')),
    ('MISC', _('miscellaneous')),
)