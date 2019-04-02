import os
from util import get_file_extension
from urls_service import UrlService
from models import get_code_result_model

class HR_Scrapper:


    PREFIX = "__"
    urlService = UrlService.instance()
    def __init__(self) -> None:
        return

    def get_track(self, track) -> None:
        tracks = self.urlService.get_track_request(track)
        models = tracks.json()['models']
        for i in models:
            chal_slug = i.get('slug')
            sub_domain = i.get('track').get('slug')
            if chal_slug is None:
                raise Exception("Chal_slug:"+str(chal_slug))


            sub_domain_string = "Domain: "+sub_domain
            print(track+ " "+sub_domain_string + chal_slug.rjust(70 - len(sub_domain_string)))

            sub_id = self.get_submissions(chal_slug)
            code = False
            if sub_id:
                 result= self.get_code(chal_slug, sub_id)
                 code = result['code']
                 lang = result['language']

            if code:
                 ext = get_file_extension(track, lang)
                 self.create_code_file(track, sub_domain, chal_slug, code, ext)

    def create_code_file(self, track, sub_domain, filename, code, ext ) -> None:
        dir = '../hackerrank_submissions/'+self.PREFIX+track+"/"+sub_domain+"/"
        file_path = dir+ filename + ext
        if not os.path.exists(dir): #os.path.isdir(dir):
                os.makedirs(dir)
                if not os.path.isfile(file_path):
                    print(code, file=open(file_path, 'w'))
        else:
            print(code, file=open(file_path, 'w'))

    def get_submissions(self, chal_slug) -> None:
      submissions = self.urlService.get_submissions_request(chal_slug)
      if submissions is None:
          raise Exception("Submissions: "+str(submissions))

      models = submissions.json()['models']
      if len(models) > 0:
             sub_id = models[0]['id']
             return sub_id
      else:
            return False


    def get_code(self, chal_slug, sub_id) -> get_code_result_model:
        code_res = self.urlService.get_particular_submission(chal_slug, sub_id)
        if code_res is None:
            raise Exception("Code_res: "+code_res)

        model = code_res.json()['model']
        code = model['code']
        language = model['language']
        result = dict()
        result['code'] = code
        result['language'] = language
        return result