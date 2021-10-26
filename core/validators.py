from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError
from django.core.validators import validate_ipv4_address,validate_ipv6_address
import re

class NamespaceNameValidator(RegexValidator):
    regex = '^[-0-9a-z.]+$'
    message = "Invalid Namespace name"

