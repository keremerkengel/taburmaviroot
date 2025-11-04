from django.conf import settings
from django.db import models

class RootPlan(models.Model):
    PLACE_CHOICES = [
        ("klinik", "Klinik"),
        ("eczane", "Eczane"),
        ("ciftlik", "Çiftlik"),
        ("diger", "Diğer"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rootplans")
    city = models.CharField("İl", max_length=64)
    district = models.CharField("İlçe", max_length=64)
    place_type = models.CharField("Ziyaret Türü", max_length=16, choices=PLACE_CHOICES)
    place_name = models.CharField("Yer Adı", max_length=128)
    visit_purpose = models.CharField("Ziyaret Amacı", max_length=200)
    visit_date = models.DateField("Tarih")
    notes = models.TextField("Notlar", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-visit_date", "-created_at"]
        verbose_name = "Ziyaret"
        verbose_name_plural = "Ziyaretler"

    def __str__(self):
        return f"{self.visit_date} - {self.place_name} ({self.city}/{self.district})"
