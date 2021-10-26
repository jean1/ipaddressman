from django.db import models
from core.validators import (VrfNameValidator)
from macaddress.fields import MACAddressField

# Create your models here.
class Vrf(models.Model):
    name = models.Textfield(validators=[VrfNameValidator()],
                            blank=False, unique=True)

    def __str__(self):
        return self.name

class IpAddress(models.Model):
    addr = models.GenericIPAddressField(blank=False)
    mac = MACAddressField(null=True, blank=True)
    vrf = models.ForeignKey(Vrf, on_delete=models.CASCADE, blank=False)
    rr_fwd = models.ForeignKey(Rr, on_delete=models.CASCADE, null=True)
    rr_rev = models.ForeignKey(Rr, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.addr.to_str()}"
