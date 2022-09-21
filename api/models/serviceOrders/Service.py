from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



# Service Order Comments
class ServiceComment(ServiceBase):  
    # Sequence Number Two
    sequenceNumberTwo = models.IntegerField()
    # Key Date *Optional
    keyDate = models.DateField(null=True)
    # Comment Type
    commentType = models.CharField(max_length=1)
    # Last Update By Id
    lastUpdateById = models.IntegerField()
    # Last Update By Name
    lastUpdateByName = models.CharField(max_length=20)
    # Last Update Date
    lastUpdateDate = models.DateField()
    # Comment/Note
    comment = models.CharField(max_length=2048)

class ServiceHeader(ServiceBase):
    # Current Region
    curRegion = models.IntegerField()
    # Current Terr Mgr
    curTerritoryManager = models.CharField(max_length=3)
    # Remote Svc Office
    remoteServiceOffice = models.IntegerField()
    # Gate Code
    gateCode = models.CharField(max_length=15)
    # Open Site Y/N
    openSite = models.BooleanField()
    # Requester Name
    requesterName = models.CharField(max_length=60)
    # Owner Name
    ownerName = models.CharField(max_length=60)
    # PO Number
    poNumber = models.CharField(max_length=10)
    # Exclude Tax Yes/No
    excludeTax = models.BooleanField()   
    # Walk-Thru Reqd Y/N
    # Est Labor Hrs
    laborHours = models.IntegerField()
    # Est Travel Hrs
    travelHours = models.IntegerField()
    # Estimated Trips
    trips = models.IntegerField()
    # Charge Per Trip
    # Ship Direct Y/N
    # Ship Direct Type
    # Ship Direct Chg
    # Notified Date
    # Actual Complete Date
    # Walk-Thru Date
    # Walk-Thru Done By
    # Old SO Number
    # Open By
    # Open Date
    # Open Time
    # S/O Save By
    # S/O Save Date
    # S/O Save Time
    # Last Update Date
    # Last Update Time
    # Last Update BY
    # Release By
    # Release Date
    # Release Time
    # Last Reject Date
    # Last Reject Time
    # Last Approve Date
    # Last Approve Time
    # Last Approve By
    # Claim Approval Date
    # Claim Approval Time
    # Last Reverse Date
    # Last Reverse Time
    # Last Reverse RsnCd
    # Last Invoice Date
    # Last Invoice Time
    # Invoice Pend Flag
    # Closed By
    # Closed Date
    # Closed Time
    # Orig Release Date
    # Orig Approve Date
    # Orig Srvc Date
    # Hide Discount
    # S/O Subtype
    # Original Subtype
    # Windbid Required Y
    # Windbid Verified Y
    # Windbid Order Number
    winBidOrder = models.CharField(max_length=8)
    # Parts Ordered Y/N
    # S/O Valid? Y/N
    # Address Validated
    # Soft Delete Flag
    # Service Description
    # Sched On/After Date
    # Total Sched Hrs
    # Schedule Priority
    # Techs Required
    techsRequired = models.BooleanField()
    # SpcTools Required
    spcToolsRequired = models.BooleanField()
    # Automated Emails?
    # UnSched Hrs
    # UnSched Dlvry
    # Srvc Status
    status = models.CharField(max_length=4)
    # Srvc Sts Date
    statusDate = models.DateField()

    
    # Restrict Code
    # Restrict EffDate
    # Create Date
    # Last Update
    # Last Update By
    # SO Region
    # SO/NF Sequence
    # SO Addendum
    # Service Region
    # Service Center
    # Scheduled By
    # Scheduled Date
    # Tech Number
    # Tech Qualifier
    # Travel Hrs
    # Arrival HH:MM
    # OnSite Hrs
    # Return Hrs
    # Lunch HH:MM
    # Confirmed By
    # Msc Hrs Desc
    # Tech Number
    # Tech Qualifier
    # Tech Type E/V
    # Primary Region
    # Primary SvcCtr
    # Rank W/In SvcCtr
    # Tech Name Short
    # Tech Name Long
    # Tech Work Days
    # SPI Managed (Y/N)
    # Date Inactivated

