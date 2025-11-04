import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import RootPlan


# --- EXCEL dışa aktarma aksiyonu ---
@admin.action(description="Seçilen ziyaretleri Excel (XLSX) olarak dışa aktar")
def export_to_excel(modeladmin, request, queryset):
    # Yeni Excel çalışma kitabı oluştur
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ziyaretler"

    # Başlık satırı (kalın ve mavi tonlu)
    headers = [
        "Tarih", "İl", "İlçe", "Ziyaret Türü",
        "Yer Adı", "Ziyaret Amacı", "Notlar", "Kullanıcı"
    ]
    ws.append(headers)

    # Veri satırları
    for p in queryset:
        ws.append([
            str(p.visit_date),
            p.city,
            p.district,
            p.place_type,
            p.place_name,
            p.visit_purpose,
            p.notes,
            p.user.username if p.user else "",
        ])

    # Hücre boyutlarını ayarla (daha okunaklı)
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        ws.column_dimensions[column].width = max_length + 2

    # Response hazırla
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="ziyaretler.xlsx"'
    wb.save(response)
    return response


# --- RootPlan admin ---
@admin.register(RootPlan)
class RootPlanAdmin(admin.ModelAdmin):
    list_display = ("visit_date", "user", "city", "district", "place_type", "place_name")
    list_filter = ("visit_date", "city", "place_type")
    search_fields = ("place_name", "visit_purpose", "notes", "city", "district")
    ordering = ("-visit_date",)
    date_hierarchy = "visit_date"
    actions = [export_to_excel]  # CSV yerine Excel
    actions_on_top = True
    actions_on_bottom = True


# --- LogEntry admin ---
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("action_time", "user", "content_type", "object_repr", "action_flag", "change_message")
    list_filter = ("user", "content_type", "action_flag")
    search_fields = ("object_repr", "change_message")
    readonly_fields = [f.name for f in LogEntry._meta.fields]
    ordering = ("-action_time",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# --- Admin başlıkları ---
admin.site.site_header = "Yönetim Paneli"
admin.site.site_title = "Tabur Mavi Ecza Deposu"
admin.site.index_title = "Ziyaret Yönetimi"
