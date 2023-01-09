from pdf2image import convert_from_path


def make_jpg_from_pdf(file):
    '''
    Преобразует PFF в несколько jpg изображений, которые
    сохраняются в корневой директории
    :param file: должен быть PDF
    :return: файлы jpg
    '''
    pages = convert_from_path(file, 500, poppler_path = r"D:\YandexDisk\Прогр\pdftojpg\poppler-22.12.0\Library\bin")
    for i, page in enumerate(pages):
        page.save(f'out{i}.jpg', 'JPEG')


