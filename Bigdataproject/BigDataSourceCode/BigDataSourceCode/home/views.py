from django.shortcuts import render, get_object_or_404
# from django.views import generic
from django.http.response import Http404, JsonResponse
import json
import math
from .models import Tag, UserStats, PostStats, TopQ, TopU

# Create your views here.
def index(request):

    if request.method == "GET" and request.is_ajax():
        if request.GET.has_key('query'):
            query = request.GET['query']
            tokens = query.strip().lower().split()
    
            tags = {}
    
            for token in tokens:
                try:
                    q = Tag.objects.get(name=token)
                    tags[q.name] = q.count
                except:
                    pass
    
            toptags = sorted(tags, key=tags.get, reverse=True)
    
            # Function that takes tokens as input and returns tags?
            return JsonResponse({"results":toptags})
        
        if request.GET.has_key('selected[]'):
            selections = request.GET.getlist('selected[]')
            
            results = []
            topq = {}
            topu = {}
            # Get tag objects for each
            for selection in selections:
                tag_stat = []                
                poststats = PostStats.objects.all().filter(tag=selection)
                post_annual_count = {}
                for poststat in poststats:
                    post_annual_count[poststat.year] = {'total_questions':poststat.total_questions,
                                                        'total_answers':poststat.total_answers,
                                                        'accepted_answers':poststat.accepted_answers,
                                                        'deleted_questions':poststat.deleted_questions,
                                                        'closed_questions':poststat.closed_questions,
                                                        'score':poststat.score,
                                                        'open_questions': poststat.total_questions - poststat.accepted_answers,
                                                        }
                                    
                userstats = UserStats.objects.all().filter(tag=selection)
                user_annual_count = {}
                for userstat in userstats:
                    user_annual_count[userstat.year] = {'users':userstat.count}
                
                for year in sorted(post_annual_count):
                    year_stats = {'year':year, 'tag':selection}
                    year_stats.update(post_annual_count[year])
                    year_stats.update(user_annual_count[year])
                    
                    tag_stat.append(year_stats)
                
                
                results.append(tag_stat)
                
                topquestions = TopQ.objects.all().filter(tag=selection)
                topq_list = []
                for question in topquestions:
                    mini_dict = {}
                    mini_dict['tag'] = selection
                    mini_dict['viewcount'] = question.viewcount
                    mini_dict['question_id'] = question.question_id
                    mini_dict['title'] = question.title
                    mini_dict['tag1'] = question.tag1
                    mini_dict['tag2'] = question.tag2
                    mini_dict['tag3'] = question.tag3
                    mini_dict['tag4'] = question.tag4
                    mini_dict['tag5'] = question.tag5
                    topq_list.append(mini_dict)
                
                topq[selection] = topq_list

                topusers = TopU.objects.all().filter(tag=selection)
                topu_list = []
                for tuser in topusers:
                    mini_dict = {}
                    mini_dict['tag'] = selection
                    mini_dict['questioncount'] = tuser.questioncount
                    mini_dict['user_id'] = tuser.user_id
                    mini_dict['displayname'] = tuser.displayname
                    mini_dict['urlpicture'] = tuser.urlpicture
                    topu_list.append(mini_dict)

                topu[selection] = topu_list
            
            return JsonResponse({"results":results,'topq':topq,'topu':topu})

    return render(request, 'home/index.html', context={})