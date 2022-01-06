# from rest_framework import models

# class Employee(models.Model):
#     id = models.CharField(default=ObjectId, max_length=40)
#     first_name = models.CharField(defaul='', max_length=50)
#     last_name = models.CharField(defaul='', max_length=50)
#     email_id = models.CharField(default='', max_length=60)
#     date_of_birth = models.DateField(auto_now_add=False)


# def aggregate_dob():
#     Employee.objects.all().annotate(date_of_birth)
#     Employee.objects.filter(first_name__icontains='XY')

# SELET * FROM
# EMPLOYEE 
# GROUP BY date_of_birth


a={
   "c26ed839-d5db-3782-999f-1316c954b525=c589df75-8880-37c1-bd76-6b84b129d7fa":{
      "reporter":"Health Care professional",
      "drug":"METOPROLOL",
      "event":"Heart attack",
      "relation":"Not Associated"
   },
   "c26f777-d5db-3782-999f-1316c954b525=c589df75-8880-37c1-bd76-6b84b129d7fa":{
      "reporter":"Company",
      "drug":"METOPROLOL",
      "event":"cardiac arrest",
      "relation":"Not Associated"
   },
   "c26ed839-d5db-3782-999f-1316c954b525=2049252d-dce7-3596-a95f-d5e8e787ffa5":{
      "reporter":"Health Care professional",
      "drug":"METOPROLOL",
      "event":"Bradycardia",
      "relation":"Doubtful"
   },
   "c26ed839-d5db-3782-999f-1316c954b525=ca8f54b2-f9dd-3abe-a1db-321ea2af10f9":{
      "reporter":"Health Care professional",
      "drug":"METOPROLOL",
      "event":"Weakness"
   },
   "c26ed839-d5db-3782-999f-1316c954b525=b97d73a3-088a-3a93-bdc0-5ea4aad1daa8":{
      "reporter":"Health Care professional",
      "drug":"METOPROLOL",
      "event":"Drug ineffective",
      "relation":"Certain"
   },
   "c26ed839-d5db-3782-999f-1316c954b525=5ab19c5b-0380-4ae3-9acb-bd423aad8abc":{
      "reporter":"Health Care professional",
      "drug":"METOPROLOL",
      "event":"Heart attack",
      "relation":"Doubtful"
   }
}

 

ans={
   "METOPROLOL":{
      "Not Associated":[
         "Heart attack"
      ],
      "Doubtful":[
         "Bradycardia",
         "Heart attack"
      ],
      "Certain":[
         "Drug ineffective"
      ]
   }
}

print(a)
print(ans)