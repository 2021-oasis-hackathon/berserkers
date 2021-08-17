from django.shortcuts import render, redirect
from .models import VillageInfo, IndivInfo, IndivTopic, Topic


def main(request):
    """
    처음 메인 페이지
    """
    village_list = VillageInfo.objects.all()
    context = {'village_list': village_list}
    return render(request, 'honameuro/main.html', context)


def indiv(request):
    """
    개인 메인 페이지: 주제 목록
    """
    topic_list = Topic.objects.all()
    context = {'topic_list': topic_list}
    return render(request, 'honameuro/indiv/indiv.html', context)


def indiv_topic(request, topic_id):
    """
    개인 회원- 주제 선택 시 보이는 페이지: 각 주제에 해당하는 개인 모집 목록
    """
    topic = Topic.objects.get(id=topic_id)
    indivtopic_list = IndivTopic.objects.filter(topic_id=topic_id)
    indiv_list = []
    for i in range(len(list(indivtopic_list))):
        indiv_list.append(IndivInfo.objects.get(id=indivtopic_list[i].indiv_id))
    context = {'indiv_list': indiv_list, 'topic': topic}
    return render(request, 'honameuro/indiv/indiv_topic.html', context)


def indiv_detail(request, indiv_id):
    """
    개인 회원- 목록에서 선택 시 상세 내용 페이지
    """
    indiv = IndivInfo.objects.get(id=indiv_id)
    context = {'indiv': indiv}
    return render(request, 'honameuro/indiv/indiv_detail.html', context)


def indiv_local(request):
    """
    개인 회원- 마을 목록을 보여주는 페이지
    """
    village_list = VillageInfo.objects.all()
    context = {'village_list': village_list}
    return render(request, 'honameuro/indiv/indiv_local.html', context)


def indiv_create(request):
    """
    개인 회원- 모임을 만드는 폼 페이지
    """
    return render(request, 'honameuro/indiv/indiv_create.html')


def indiv_submit(request):
    """
    개인 회원- 모임 폼 전송
    """
    indiv = IndivInfo(content=request.POST.get('content'), title=request.POST.get('title'))
    indiv.save()
    return redirect('honameuro:indiv_topic')


def local(request):
    """
    지역 메인 페이지
    """

    return render(request, 'honameuro/local/local.html')


def local_detail(request):
    """
    지역 회원- 지역 상세 페이지
    """
    village_list = VillageInfo.objects.all()
    context = {'village_list': village_list}
    return render(request, 'honameuro/local/local_detail.html', context)


def local_match(request):
    """
    지역 회원- 개인 회원 모임 목록 페이지
    """
    indiv_list = IndivInfo.objects.all()
    context = {'indiv_list': indiv_list}
    return render(request, 'honameuro/local/local_match.html', context)


def match_detail(request, indiv_id):
    """
    지역 회원- 개인 회원 모임 상세 페이지
    """
    indiv = IndivInfo.objects.get(id=indiv_id)
    context = {'indiv': indiv}
    return render(request, 'honameuro/local/match_detail.html', context)


def apply(request, village_id):
    village = VillageInfo.objects.get(id=village_id)
    village.selected += 1
    village.save()
    return redirect('honameuro:detail', village_id=village.id)

# Create your views here.
