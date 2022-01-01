from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .forms import RegistrationForm
from .models import Meetup,Participant,Location
# Create your views here.

def index(request):
    all_obj=Meetup.objects.all()


    return render(request,'meetups/index.html',{
        'meetups': all_obj,

    })
def meetup_details(request,slug):
    obj=get_object_or_404(Meetup,slug=slug)
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        # print(form.cleaned_data)
        if form.is_valid():
            user_email=form.cleaned_data.get('email')
            # parti,was_created=Participant.objects.get_or_create(email=user_email)
            # print(was_created)
            # participant=form.save()
            # print(participant)
            # print(type(participant))
            # class
            # |__> output:test@test.com
            # print('##################')
            # print(form)
            # |__> output:
            #   <tr>
            #     <th><label for="id_email">Email:</label></th>
            #     <td>
            #       <input type="email" name="email" value="cleandata@test.com" maxlength="254" required id="id_email">
            #     </td>
            #   </tr>
            # print('##################')
            # print(form.cleaned_data)
            # |__> output:{'email':'test@test.com'}
            # clean_d=form.cleaned_data.get('email')
            # print(clean_d)
            # print(type(clean_d))
            # str
            # user_email=form.cleaned_data['email']
            # if Participant.objects.filter(email=user_email).exist():
            #     print('exist')
            # print('##############')
            # print(form.cleaned_data in Participant)
            # print('$$$$ parti: $$$')
            # print(Participant.objects.all())
            # print('$$$$ metup: $$$')
            # print(Meetup.objects.all())
            # print('$$$$ locatin: $$$')
            # print(Location.objects.all())
            print('')
            # how to check an object exist or not (because uniq Model):(3_way)

            # solve_1
            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # if Participant.objects.filter(email=user_email).exists():
            #     part_obj = Participant.objects.get(email=user_email)
            #     obj.participant.add(part_obj)
            #     print('obj is exist just add**********')
            # else:
            #     part_obj=Participant.objects.create(email=user_email)
            #     obj.participant.add(part_obj)
            #     print('obj is creat and add**********')

            # solve_2
            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # try:
            #     # Participant.objects.get(email=user_email)
            #     parti=Participant.objects.get(email=user_email)
            #     print('try:get object from db query****',parti)
            # except Participant.DoesNotExist:
            #     parti=Participant.objects.create(email=user_email)
            #     print('except:object created******')
            # finally:
            #     obj.participant.add(parti)

            # solve_3
            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            parti_object,was_created=Participant.objects.get_or_create(email=user_email)
            #parti_object, _ = Participant.objects.get_or_create(email=user_email)
            # =--> for ignore was_created flag ,should use UnderScore(_) instead of was_created!!
            print('object is created?## ',was_created,' ##')
            obj.participant.add(parti_object)
            return redirect('register_success',slug=slug)
    else:
        form=RegistrationForm()
    return render(request,'meetups/meetup-detail.html',{
        'meetup':obj,
        'form':form,
    })
def register_success(request,slug):
    meetup=Meetup.objects.get(slug=slug)
    return render(request,'meetups/registration-success.html',{
        'obj':meetup,
    })