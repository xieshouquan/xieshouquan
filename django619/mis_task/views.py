from django.shortcuts import render
from django.views import View
from mis_task.models import Mis_task
# Create your views here.

def get_xiaoque(request):
    return render(request, 'mis_task/xiaoque1.html')


class Mis_taskq(View):
    def get(self,request,*args,**kwargs):
        return render(request,'mis_task/xiaoque1.html')
    def post(self,request,*args,**kwargs):
        data=request.POST
        task_id=data.get('task_id')
        task_name =data.get('task_name')
        patrol_circuit =data.get('patrol_circuit')
        Inspector =data.get('Inspector')
        enabled_state =data.get('enabled_state')
        Initial_pole_number =data.get('Initial_pole_number')
        termination_pole_number =data.get('termination_pole_number')
        sender =data.get('sender')
        departure_time =data.get('departure_time')
        remarks =data.get('remarks')
        mis_task = Mis_task(
            task_id=task_id,
            task_name =task_name,
            patrol_circuit =patrol_circuit,
            Inspector =Inspector,
            enabled_state =enabled_state,
            Initial_pole_number =Initial_pole_number,
            termination_pole_number =termination_pole_number,
            sender =sender,
            departure_time =departure_time,
            remarks =remarks,
        )
        mis_task.save()
        return render(request,'mis_task/xiaoque1.html')

def check(request):
    mistask =Mis_task.objects.filter(task_id=2018)
    data=dict(task_id =mistask.task_id,
    task_name = mistask.task_name,
    patrol_circuit = mistask.patrol_circuit,
    Inspector = mistask.Inspector,
    enabled_state = mistask.enabled_state,
    Initial_pole_number = mistask.Initial_pole_number,
    termination_pole_number = mistask.termination_pole_number,
    sender = mistask.sender,
    departure_time = mistask.departure_time,
    remarks = mistask.remarks)
