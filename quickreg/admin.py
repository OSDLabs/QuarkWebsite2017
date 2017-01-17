from django.contrib import admin
from .models import *
from django.http import HttpResponse

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=quick-reg.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Profile")
    
    row_num = 0
    
    columns = [
        (u"Name", 6000),
        (u"Email", 4000),
        (u"Mobile", 6000),
        (u"Institute", 10000),
        (u"Gender", 500),
        (u"Year", 1000),
        (u"Panel Design", 5000),
        (u"Panel Elixir", 5000),
        (u"Panel Roboficial", 5000),
        (u"Panel Programmers", 5000),
        (u"Panel Specials", 5000),
        (u"Panel Initiatives", 5000),
        (u"Panel Electrify", 5000),
        (u"Panel Corporate", 5000),
        (u"Workshop", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1


    
    for obj in queryset:
        row_num += 1
        row = [
            obj.name,
            obj.email,
            obj.mobile,
            obj.institute,
            obj.gender,
            obj.year,
            obj.panel_des,
            obj.panel_elixir,
			obj.panel_robo,
			obj.panel_prog,
			obj.panel_specials,
			obj.panel_init,
			obj.panel_elect,
			obj.panel_corporate,
			obj.workshop
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response

export_xls.short_description = u"Export XLS"

class QuickAdmin(admin.ModelAdmin):
    actions = [export_xls,]

admin.site.register(quick, QuickAdmin)
