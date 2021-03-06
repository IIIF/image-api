from .test import BaseTest, ValidatorError

class Test_Quality_Error_Random(BaseTest):
    label = 'Random quality gives 400'
    level = 1
    category = 5
    versions = [u'1.0', u'1.1', u'2.0', u'3.0']
    validationInfo = None

    def run(self, result):
        try:
            url = result.make_url({'quality': self.validationInfo.make_randomstring(6)})
            error = result.fetch(url)
            self.validationInfo.check('status', result.last_status, 400, result)
            return result 
        except Exception as error:
            raise ValidatorError('url-check', str(error), 400, result, 'Failed to get random quality from url: {}.'.format(url))
