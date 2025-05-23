from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views import View
from tasks.models import MemoModel
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .utils import choose_better_key, build_major_scale

def index(request):
    if request.method == "GET":
        return render(request, "tasks/index.html")
    return HttpResponse("Method Not Allowed", status=405)

class MemoCreateView(View):
    def get(self,request):
        key = request.GET.get("key")
        scale = []
        selected_key = None
        
        if key:
           selected_key = choose_better_key(key)
           scale = build_major_scale(selected_key)
            
        return render(request, "tasks/create.html",{
            "scale": scale,
            "selected_key": selected_key
        })

    
    
    def post(self, request):
        title = request.POST.get("title")
        key = request.POST.get("key")
        code = request.POST.get("code")
        degree = request.POST.get("degree")
        scale = request.POST.get("scale")
        
        memo = MemoModel.objects.create(
            title = title,
            key = key,
            code = code,
            degree = degree,
            scale =scale,
        )
        return JsonResponse({"message": f"追加しました: {memo.title}"})

class MemoDetailView(View):
    def get(self, request, memo_id):
        memo = get_object_or_404(MemoModel, id = memo_id)
        return render(request, "tasks/memo_view.html", {"memo": memo})
 
class MemoListView(View):   
    def get(self, request):
        memos = MemoModel.objects.all()
        return render(request, "tasks/memo_list.html", {"memos": memos})

class MemoDeleteView(View):
    def delete(self, request, memo_id):
        memo = get_object_or_404(MemoModel, id = memo_id)
        memo.delete()
        return JsonResponse({"message": f"削除しました: {memo.title}"})

class MemoEditView(View):
    def get(self, request, memo_id):
        memo = get_object_or_404(MemoModel, id=memo_id)
        return render(request, "tasks/memo_edit.html", {"memo": memo})
    
    def post(self, request, memo_id):
        memo = get_object_or_404(MemoModel, id=memo_id)
        memo.title = request.POST.get("title")
        memo.key = request.POST.get("key")        
        memo.code = request.POST.get("code")
        memo.degree = request.POST.get("degree") 
        memo.save()
        return redirect("memo_detail_view", memo_id=memo.id)
         
    