from .test import BaseTest, ValidatorError
import uuid

class Test_Id_Error_Random(BaseTest):
    label = 'Random identifier gives 404'
    level = 1
    category = 1
    versions = [u'1.0', u'1.1', u'2.0', u'3.0']
    validationInfo = None

    def run(self, result):
        try:
            url = result.make_url({'identifier': str(uuid.uuid1())})
            error = result.fetch(url)
            self.validationInfo.check('status', result.last_status, 404, result)
            return result
        except Exception as error:
            raise ValidatorError('url-check', str(error), 404, result, 'Failed to get random identifier from url: {}.'.format(url))
