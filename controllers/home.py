
'''
Preset controller by torn for / route
'''
from .modules import *
class homeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
            <!doctype html>
            <title>Face Compare API</title>
            <h1>Upload your images here</h1>
            <hr>
            <form method="POST" enctype="multipart/form-data">
              <input type="file" name="img1"><br><br>
            <input type="file" name="img2"><br><br>
              <input type="submit" value="Upload">
            </form>
            ''')
    @tornado.gen.coroutine
    def post(self):
        try:		
            __uploads__='uploads'
            files=self.request.files
            img1='img1'
            img2='img2'
            body1=files['img1'][0]['body']
            body2=files['img2'][0]['body']
            with open(__uploads__+'/'+img1,'wb') as face1:
                face1.write(body1)
            with open(__uploads__+'/'+img2,'wb') as face2:
                face2.write(body2)
            t1=time.time()
            simple_compare_result=Simple_Faces_Compare(__uploads__+'/'+img1,__uploads__+'/'+img2)
            t2=time.time()
            forced_compare_result_chake1=Foreced_Faces_Compare(__uploads__+'/'+img1,__uploads__+'/'+img2)
            t3=time.time()
            forced_compare_result_chake2=Foreced_Faces_Compare(__uploads__+'/'+img2,__uploads__+'/'+img1)
            if simple_compare_result==True:
                self.write({
                    'result':"True",
                    'description':"Face Match 100%",
                    'time':f'{time.time()-t1}s'
                })
            elif(isinstance(simple_compare_result,str)):
                self.write({
                    'result':"None",
                    'description':f"{simple_compare_result}",
                    'time':f'{time.time()-t2}s'
                })
            elif forced_compare_result_chake1==True:
                self.write({
                    'result':"True",
                    'description':"Face Match 100%",
                    'time':f'{time.time()-t3}s'
                })
            elif isinstance(forced_compare_result_chake1,str):
                self.write({
                    'result':"None",
                    'description':f"{simple_compare_result}",
                    'time':f'{time.time()-t3}s'
                })
            elif forced_compare_result_chake2==True:
                self.write({
                    'result':"True",
                    'description':"Face Match 100%",
                    'time':f'{time.time()-t3}s'
                })
            else:
                self.write({
                    'result':"False",
                    'description':"No Match Found",
                    'time':f'{time.time()-t3}s'
                })
        except Exception as e:
            print(e)
            self.write({'result':'unsupported extension'})