from django.contrib import admin
from .models import *

# def export_xls(modeladmin, request, queryset):
# 	# print(queryset)
#     import xlwt
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=profile.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet("Profile")
    
#     row_num = 0
    
#     columns = [
#         (u"Name", 6000),
#         (u"Email", 4000),
#         (u"Mobile", 6000),
#         (u"Institute", 10000),
#         (u"Gender", 500),
#         (u"DOB", 2000),
#         (u"Year", 1000),
#         (u"Events", 8000),
#         (u"Workshop", 8000),
#     ]

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num][0], font_style)
#         # set column width
#         ws.col(col_num).width = columns[col_num][1]

#     font_style = xlwt.XFStyle()
#     font_style.alignment.wrap = 1


    
#     for obj in queryset:
#         lista = [ field.name for field in Event.objects.filter(event__event_part = obj.user)]
#         listw = [ field.name for field in Workshop.objects.filter(workshop__workshop_part = obj.user)]
#         row_num += 1
#         row = [
#             obj.name,
#             obj.email,
#             obj.mobile,
#             obj.institute,
#             obj.gender,
#             obj.dob,
#             obj.year,
#             str(lista),
#             str(listw)

#         ]
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
            
#     wb.save(response)
#     return response

# export_xls.short_description = u"Export XLS"

# class ProfileAdmin(admin.ModelAdmin):
#     actions = [export_xls,]

admin.site.register(quick)
