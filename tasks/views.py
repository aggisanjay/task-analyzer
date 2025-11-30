from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    try:
        tasks = json.loads(request.body)
    except:
        return JsonResponse({"error": "Bad JSON"}, status=400)

    for t in tasks:
        t["score"] = calculate_task_score(t)

    sorted_tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)
    return JsonResponse(sorted_tasks, safe=False)

def suggest_tasks(request):
    example_tasks = [
        {"title": "Update Resume", "importance":9, "estimated_hours":2, "due_date":"2025-12-01"},
        {"title": "Apply Jobs", "importance":8, "estimated_hours":3, "due_date":"2025-11-30"},
        {"title": "DSA Practice", "importance":7, "estimated_hours":1},
    ]

    for t in example_tasks:
        t["score"] = calculate_task_score(t)

    top_three = sorted(example_tasks, key=lambda x: x["score"], reverse=True)[:3]

    return JsonResponse({
        "message": "Focus on these tasks today",
        "tasks": top_three
    })
