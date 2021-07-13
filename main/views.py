from django.http import HttpResponse
def home(request):
	return HttpResponse("Bosh sahifa")
	# word = request.GET.get("q",None)
	# if word:
	# 	return HttpResponse(word)
	# else:
	# 	return HttpResponse("free")


def biz_haqimizda(request):
	return HttpResponse("<i>Saytimizga xush kelibsiz!</i>")


def users(request):
	return HttpResponse("Foydalanuvchilar")

def yakka_foydalanuvchi(request,son):
	return HttpResponse(f"{son}- foydalanuvchi")


def test(request):
	x = 5
	y = 0 
	z = x/y

	return HttpResponse("bu ko'rinmaydi")