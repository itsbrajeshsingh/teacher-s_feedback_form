from django.shortcuts import render, redirect 
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages 
from testapp.models import reporter, subjectcode, subjectname, branchh
import datetime
from django.db.models import Avg
# Create your views here.
def home_view(request):
    request.session.set_expiry(0)
    return render(request,'testapp/home.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username,password = password)
            if user is not None:
                request.session.set_expiry(0)
                auth.login(request,user)
                if user.is_staff:
                    messages.add_message(request, messages.SUCCESS, 'login successfully')
                    return redirect('facultyresult')
                else:
                    messages.success(request,"login successfully")
                    return redirect('studentform')
            else:
                # err = {'error':'username or password not matched'}
                messages.error(request, 'wrong username or password')
                return render(request,'testapp/login.html')

        except ObjectDoesNotExist:
            return render(request,'testapp/login.html',{'err':'please contact to our admin for registration'})
    else:
        return render(request,'testapp/login.html')
      
def logout_view(request):
    if request.method == "POST":
        auth.logout(request)
        return render(request,'testapp/logout.html')
    else:
        return render(request,'testapp/home.html')
@login_required(login_url='login_now')
def faculty_result_view(request):
    request.session.set_expiry(0)
    current_user = request.user.username
    result = reporter.objects.all()
    rst = reporter.objects.filter(f_username = current_user)
    namee = User.objects.filter(username = current_user)
    name = [namee[0].first_name + " " + namee[0].last_name]
    sub_name_lst = []
    sem_lst = []
    branch_name_lst = []
    month_lst = []
    for i in range(len(result)):
        sub_name_lst.append(result[i].subject_name)
        sem_lst.append(result[i].semester)
        branch_name_lst.append(result[i].branch_name) 
        month_lst.append(result[i].update.month)
    sub_name_lst = list(set(sub_name_lst))
    sem_lst = list(set(sem_lst))
    branch_name_lst = list(set(branch_name_lst))
    month_lst = list(set(month_lst))
    subjectlst = []
    branchnamelst = []
    semesterlst = []
    allset = []
    monthlst = []
    sub_know_avg = []
    pra_know_avg = []
    class_main_avg = []
    for month in month_lst:
        for semester in sem_lst:
            for subname in sub_name_lst:
                for branch in branch_name_lst:
                    for i in range(len(rst)):
                        if rst[i].subject_name == subname and rst[i].branch_name == branch and rst[i].semester == semester and rst[i].update.month == month:
                            new_set = [subname,branch,semester,month]
                            if new_set not in allset:
                                branchnamelst.append(branch)
                                semesterlst.append(semester)
                                subjectlst.append(subname)
                                allset.append(new_set)
                                monthlst.append(month)
                                sub_know_avg.append(reporter.objects.filter(f_username = current_user,branch_name = branch,semester = semester,subject_name = subname).aggregate(Avg('subject_knowledge'))['subject_knowledge__avg'])
                                pra_know_avg.append(reporter.objects.filter(f_username = current_user,branch_name = branch,semester = semester,subject_name = subname).aggregate(Avg('pratical_knowledge'))['pratical_knowledge__avg'])
                                class_main_avg.append(reporter.objects.filter(f_username = current_user,branch_name = branch,semester = semester,subject_name = subname).aggregate(Avg('class_maintainance'))['class_maintainance__avg'])
    myzip = zip(subjectlst,semesterlst,branchnamelst,monthlst,sub_know_avg,pra_know_avg,class_main_avg)
    print("hii after zip",subjectlst,semesterlst,branchnamelst,monthlst,sub_know_avg,pra_know_avg,class_main_avg)
    return render(request,'testapp/facultyresult.html',{'myzip':myzip})


@login_required(login_url='login_now')
def student_form_view(request):
    request.session.set_expiry(0)
    name = User.objects.only('first_name','last_name').filter(is_staff=True)  
    subject_code = subjectcode.objects.all()
    subject_name = subjectname.objects.all()
    b_ranch = branchh.objects.all()
    sub_name = []
    sub_code = []
    branch = []
    for i in range(len(subject_code)):
        sub_code.append(subject_code[i].s_code)
    for i in range(len(subject_name)):
        sub_name.append(subject_name[i].s_name)
    for i in range(len(b_ranch)):
        branch.append(b_ranch[i].s_branch)
    
    if request.method == 'POST':
        print('inside if')
        s_semester = request.POST['semester']
        s_branch = request.POST['branch_name']
        s_sub1 = request.POST['subject_name1']
        s_sub2 = request.POST['subject_name2']
        s_sub3 = request.POST['subject_name3']
        s_sub4 = request.POST['subject_name4']
        s_sub5 = request.POST['subject_name5']
        s_sub6 = request.POST['subject_name6']
        s_sub7 = request.POST['subject_name7']
        s_subcode1 = request.POST['subject_code1']
        s_subcode2 = request.POST['subject_code2']
        s_subcode3 = request.POST['subject_code3']
        s_subcode4 = request.POST['subject_code4']
        s_subcode5 = request.POST['subject_code5']
        s_subcode6 = request.POST['subject_code6']
        s_subcode7 = request.POST['subject_code7']
        s_subfac1 = request.POST['f_name1']
        s_subfac2 = request.POST['f_name2']
        s_subfac3 = request.POST['f_name3']
        s_subfac4 = request.POST['f_name4']
        s_subfac5 = request.POST['f_name5']
        s_subfac6 = request.POST['f_name6']
        s_subfac7 = request.POST['f_name7']
        s_sub_know1 = request.POST['sub_know1']
        s_sub_know2 = request.POST['sub_know2']
        s_sub_know3 = request.POST['sub_know3']
        s_sub_know4 = request.POST['sub_know4']
        s_sub_know5 = request.POST['sub_know5']
        s_sub_know6 = request.POST['sub_know6']
        s_sub_know7 = request.POST['sub_know7']
        s_pra_know1 = request.POST['pra_know1']
        s_pra_know2 = request.POST['pra_know2']
        s_pra_know3 = request.POST['pra_know3']
        s_pra_know4 = request.POST['pra_know4']
        s_pra_know5 = request.POST['pra_know5']
        s_pra_know6 = request.POST['pra_know6']
        s_pra_know7 = request.POST['pra_know7']
        s_class_main1 = request.POST['class_main1']
        s_class_main2 = request.POST['class_main2']
        s_class_main3 = request.POST['class_main3']
        s_class_main4 = request.POST['class_main4']
        s_class_main5 = request.POST['class_main5']
        s_class_main6 = request.POST['class_main6']
        s_class_main7 = request.POST['class_main7']
        current_user = request.user
        inst = User.objects.get(username = current_user.username)
        curr_time = datetime.datetime.now()
        rep1 = reporter(s_username = inst,subject_name =s_sub1,subject_code = s_subcode1,f_username = s_subfac1,subject_knowledge = s_sub_know1,pratical_knowledge = s_pra_know1,class_maintainance = s_class_main1,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep2 = reporter(s_username = inst,subject_name =s_sub2,subject_code = s_subcode2,f_username = s_subfac2,subject_knowledge = s_sub_know2,pratical_knowledge = s_pra_know2,class_maintainance = s_class_main2,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep3 = reporter(s_username = inst,subject_name =s_sub3,subject_code = s_subcode3,f_username = s_subfac3,subject_knowledge = s_sub_know3,pratical_knowledge = s_pra_know3,class_maintainance = s_class_main3,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep4 = reporter(s_username = inst,subject_name =s_sub4,subject_code = s_subcode4,f_username = s_subfac4,subject_knowledge = s_sub_know4,pratical_knowledge = s_pra_know4,class_maintainance = s_class_main4,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep5 = reporter(s_username = inst,subject_name =s_sub5,subject_code = s_subcode5,f_username = s_subfac5,subject_knowledge = s_sub_know5,pratical_knowledge = s_pra_know5,class_maintainance = s_class_main5,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep6 = reporter(s_username = inst,subject_name =s_sub6,subject_code = s_subcode6,f_username = s_subfac6,subject_knowledge = s_sub_know6,pratical_knowledge = s_pra_know6,class_maintainance = s_class_main6,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep7 = reporter(s_username = inst,subject_name =s_sub7,subject_code = s_subcode7,f_username = s_subfac7,subject_knowledge = s_sub_know7,pratical_knowledge = s_pra_know7,class_maintainance = s_class_main7,branch_name =s_branch,semester = s_semester,update = curr_time)
        rep1.save()
        rep2.save()
        rep3.save()
        rep4.save()
        rep5.save()
        rep6.save()
        rep7.save()
        return redirect('home')
    
    return render(request,'testapp/studentform.html',{"fname":name,'subjectname':sub_name,'subjectcode':sub_code,'branch':branch})
