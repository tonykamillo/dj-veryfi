from django.db import models
from django.core.files.storage import default_storage

# from .veryfi import VeryfiService


class OCRInvoiceOrReceiptField(models.JSONField):
    def __init__(self, upload_to="", *args, **kwargs):
        self.upload_to = upload_to
        # self._veryfi = VeryfiService()
        super(OCRInvoiceOrReceiptField, self).__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        data = {"foo": "bar"}
        fileobj = getattr(instance, self.attname, None)
        if fileobj:
            path = default_storage.save(fileobj.name.split("/")[-1], fileobj)
            data["_filepath"] = path
        return data
