from django.http import JsonResponse
from django.views.generic.edit import FormView
from .forms import MarkSheetForm
from .models import StudentMarkSheet
from django.core.paginator import Paginator
from django.http import JsonResponse


class MarkSheetFormView(FormView):
    form_class = MarkSheetForm
    template_name = 'marksheet_form.html'
    success_url = '/success/'

def ajax_save_marksheet(request):
    if request.method == 'POST':
        form = MarkSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})
def get_students(request):
    page = request.GET.get('page', 1)  # Get the requested page from the query parameters
    per_page = 10  # Number of students per page

    students = StudentMarkSheet.objects.all()
    paginator = Paginator(students, per_page)

    try:
        current_page = paginator.page(page)
    except EmptyPage:
        return JsonResponse({'error': 'No more data.'}, status=404)

    students_data = [{
        'student_name': student.student_name,
        'roll_no': student.roll_no,
        'score1': student.score1,
        'score2': student.score2,
        'score3': student.score3,
        'score4': student.score4,
        'score5': student.score5,
    } for student in current_page]

    return JsonResponse({'data': students_data, 'page_count': paginator.num_pages})
