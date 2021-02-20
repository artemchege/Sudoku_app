from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Matrix
from django.urls import reverse
from django.views import View
from .utils import validate_form, turn_matrix, return_session, solve_matrix, check_sudoku_rules
import copy


class SudokuMain(View):
    def post(self, request):
        """
        Handles the incoming form, validate it, trying to solve matrix, writes result into DB as matrix in
        appropriate shape.
        :param request:
        :return: response
        """

        matrix = list()
        for i in range(1, 10):
            matrix.append(request.POST.getlist(str(i)))

        if not validate_form(matrix):
            return render(request, 'main/main.html', {'error': 'an error occurred due to invalid incoming data,'
                                                               'leave zeroes if there is no number and provide '
                                                               'only integers'})

        matrix_t = turn_matrix(matrix)

        if not check_sudoku_rules(matrix_t):
            return render(request, 'main/main.html', {'error': 'you had better do not violate sudoku rules'})

        session_key = return_session(request)

        # deepcopy bc we have mutable array that consists of mutable arrays
        solved_matrix = solve_matrix(copy.deepcopy(matrix_t))

        if solved_matrix:
            m = Matrix.objects.create(array=matrix_t, user=session_key, if_solved=True, result=solved_matrix)
            m.save()
            return HttpResponseRedirect(reverse('main:result', args=(m.id,)))
        else:
            Matrix.objects.create(array=matrix_t, user=session_key, if_solved=False)
            return render(request, 'main/main.html', {'error': 'matrix does not have solutions'})

    def get(self, request):
        print('get')
        context = {}
        return render(request, 'main/main.html', context)


class SudokuResult(View):
    def get(self, request, id):
        """
        Just renders the result page.
        :param request:
        :param id: int
        :return: render
        """

        user = return_session(request)
        matrix = get_object_or_404(Matrix, id=id, user=user)

        context = {'matrix_before': matrix.array, 'matrix_after': matrix.result}
        return render(request, 'main/result.html', context)


class SudokuHistory(View):
    def get(self, request):
        """
        Just renders the history page. Instead we could use ListView.
        :param request:
        :param id: int
        :return: render
        """

        user = return_session(request)
        history = Matrix.objects.filter(user=user)

        context = {'history': history}
        return render(request, 'main/history.html', context)
