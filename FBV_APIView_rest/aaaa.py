"""     django                                                              rest_framework
###########################################################################################################
                                                                      API_View______________>GenericAPIView
                                                                      @api_view(["GET"])
FBV : def func_name(request)                                          FBV : def func_name(request)


                                                                      CBV : def class_name(APIView)
CBV : def class_name(View)
                                                                      view set ----> model vew set
####################################################################################################################


class stuentList(Listmodelmixin,GenericAPIView):

stu = Student.objects.all()
searialized_data = Student_Serializer

def get(self,request,*args,**kwrgs):
    return self.list(request,*args,**kwrgs)






















"""