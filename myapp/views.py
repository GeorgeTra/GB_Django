from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    logger.info('Main page accessed')
    html = '''
    <h1>Приветствую вас на моем сайте, разработанном на Django!</h1>
    <p>Добро пожаловать на главную страницу.</p>
    <a href="about/" style="text-decoration: none">О себе</a> 
    <p><a href="admin/" style="text-decoration: none">Административная панель</a></p>
    <p><a href="les4/forms/" style="text-decoration: none">Заполнить форму</a></p>
    <p><a href="les4/upload/" style="text-decoration: none">Загрузить изображение</a></p>
    <p><a href="les6/view/" style="text-decoration: none">Посчитать количество товаров в базе данных</a></p>
    <div style="position:absolute; bottom:0px;">
    <p class="brand">
        © 2023  Мой сайт  All Rights Reserved.
    </p>
    </div>	
    '''
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    html = '''
    <p><a href="/" style="text-decoration: none">Главная</a></p>
    <h1>О СЕБЕ</h1>

        <ul>
            <p>
                <li>
                    Более 7 лет работал в направлении
                    продаж и экспорта как на российском
                    рынке, так и на международном.
                    Данный опыт помог мне развить
                    навыки коммуникативности и
                    эмпатии, а также умение
                    декомпозировать задачи и четко
                    следить за их выполнением в
                    ограниченный промежуток времени.
                </li>
            </p>
            <p>
                <li>
                    Заинтересовался IT-направлением, т.к.
                    видел для себя более широкие
                    возможности профессионального
                    развития и отсутствие “потолка” в
                    карьерном росте. Направление Python-разработки выбрал из-за интереса к
                    анализу данных и программированию
                    не только веб-сервисов, но и телеграм-ботов. Программированием
                    занимаюсь более 1,5 лет в рамках
                    GeekBrains, а также кодингом под
                    руководством тех. ментора. На
                    данный момент читаю книгу
                    Васильева А.Н. “Программирование на
                    PYTHON в примерах и задачах”.
                </li>
            </p>
                <li>
                    Заинтересован участвовать в
                    коммерческих проектах, где есть
                    возможность более глубоко изучить
                    Django, улучшить чистоту кодинга
                    благодаря участию в code review и
                    познакомиться с другими
                    фреймворками (FastApi, Flask).
                    Свободно владею английским, а также
                    немецким и немного испанским
                    языками, хотел бы использовать их в
                    работе.
                </li>
        </ul>
            <div style="position:absolute; bottom:0px;">
                <p class="brand">
                    © 2023  Мой сайт  All Rights Reserved.
                </p>
            </div>	
    '''
    return HttpResponse(html)
