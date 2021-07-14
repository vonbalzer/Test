from bokin import add_new_doc, get_doc_owner_name, get_doc_shelf, delete_doc
from yandex import creat_folder

class TestBookkeeping:

    def test_sbook1(self):
        assert add_new_doc('789','doc', 'Mish Bi', '3') == '3'

    def test_book2(self):
        assert get_doc_owner_name('789') == 'Mish Bi'

    def test_book3(self):
        assert  get_doc_shelf('789') == '3'

    def test_book4(self):
        assert delete_doc('789') == ('789', True)

    def test_book5(self):
        assert  get_doc_shelf('789') == None

    def test_ya(self):
        assert creat_folder('AQAAAABWJXu6AADLWxMjEvsREEV6voCafcSxa-Q', '4') == 'Создана папка с именем на YandexDisk: 4'

    def test_ya1(self):
        assert creat_folder('AQAAAABWJXu6AADLWxMjEvsREEV6voCafcSxa-e', '4') == f'Указанный вами токен YandexDisk неверный или не предоставляет достаточных прав для заливки фотографий.'