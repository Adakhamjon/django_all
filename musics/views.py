from django.shortcuts import render,redirect

from django.http import HttpResponse


musics = [
	{
	"id":1,
	"title":"Gaybulla Tursunov-kocha",
	"file":"musiqalar/Gaybulla-Tursunov-kocha .m4a",
	"thumbnail":"rasmlar/rasm1.jpg"
	},
	{
	"id":2,
	"title":"Seyyid Taleh-Ya Habibi",
	"file":"musiqalar/Seyyid-Taleh-Ey-sevgili-Ya-Habibi.mp3",
	"thumbnail":"rasmlar/rasm2.jpg"
	},
	{
	"id":3,
	"title":"Ava Max-OMG Whats happening",
	"file":"musiqalar/OMG-What s-Happening-Ava-Max.mp3",
	"thumbnail":"rasmlar/rasm3.jpg"
	}
]

def all_music(request):
	context = {
				"musics":musics
		# "xabarlar" : [
		# {"text":"Assalomu Alekum","type":"yaxshi"},
		# {"text":"Safimizga hush kelibsiz","type":"yomon"},
		# {"text":"Biz bilan yangiliklardan xabardor bo'ling","type":"yaxshi"}
		# {"id":1,
		# "title":"Till I collapse",
		# "artist":"Eminem",
		# "year":"2000"},

		# {
		# "id":5,
		# "title":"I am not Afraid",
		# "artist":"Eminem",
		# "year":"2001"},

		# {
		# "id":14,
		# "title":"Lose yourself",
		# "artist":"Eminem",
		# "year":"2001"
		# }
		
	}
	return render(request,"index.html",context)

def single_music(request,_id):
	music = list(filter(lambda music:music["id"]==_id,musics))
	if len(music)>0:
		music = music[0]
	else:
		return redirect("home-page")

	context = {
	"music":music,
	"musics":musics
	}
	return render(request,"music.html",context)




