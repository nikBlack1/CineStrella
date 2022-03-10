from django.shortcuts import render


# Create your views here.


def index(request):
    # vampires = Vampire.objects.all()
    return render(request, 'index.html', {
        # 'vampires_list': vampires
    })


# def vampire_profile(request, vampire_slug):
#     try:
#         selected_vampire = Vampire.objects.get(slug=vampire_slug)
#         return render(request, 'vampire.html', {
#             'vampire_found': True,
#             'vampire_name': selected_vampire.name,
#             'vampire_title': selected_vampire.title
#         })
#     except Exception as exc:
#         return render(request, 'vampire.html', {
#             'vampire_found': False
#         })
