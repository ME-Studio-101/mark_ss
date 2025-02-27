import requests
import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


logger = logging.getLogger(__name__)

# Стартовая страница


def index(request):
    template = "index/index.html"
    return render(request, template)


def index_mobile(request):
    data = {
        "was": render_to_string("index/was.html", request=request),
        "wc": render_to_string("index/wc.html", request=request),
        "cg": render_to_string("index/cg.html", request=request),
        "lf": render_to_string("index/lf-sm.html", request=request),
        "um_core": render_to_string("index/um-core.html", request=request),
        "um": render_to_string("index/um-sm.html", request=request),
        "tr_core": render_to_string("index/tr-core.html", request=request),
        "tr": render_to_string("index/tr-sm.html", request=request),
        "ti": render_to_string("index/ti.html", request=request),
        "rs": render_to_string("index/rs.html", request=request),
    }
    return JsonResponse(data)


def index_mobile_additional(request):
    data = {
        "lf": render_to_string("index/lf-lgmd.html", request=request),
        "um": render_to_string("index/um-lgmd.html", request=request),
        "tr": render_to_string("index/tr-lgmd.html", request=request),
    }
    return JsonResponse(data)


def index_tablet(request):
    data = {
        "was": render_to_string("index/was.html", request=request),
        "wc": render_to_string("index/wc.html", request=request),
        "cg": render_to_string("index/cg.html", request=request),
        "lf": render_to_string("index/lf-lgmd.html", request=request),
        "um_core": render_to_string("index/um-core.html", request=request),
        "um": render_to_string("index/um-lgmd.html", request=request),
        "tr_core": render_to_string("index/tr-core.html", request=request),
        "tr": render_to_string("index/tr-lgmd.html", request=request),
        "ti": render_to_string("index/ti.html", request=request),
        "rs": render_to_string("index/rs.html", request=request),
    }
    return JsonResponse(data)


def index_tablet_additional(request):
    data = {
        "lf": render_to_string("index/lf-sm.html", request=request),
        "um": render_to_string("index/um-sm.html", request=request),
        "tr": render_to_string("index/tr-sm.html", request=request),
    }
    return JsonResponse(data)


def index_desktop(request):
    data = {
        "was": render_to_string("index/was.html", request=request),
        "wc": render_to_string("index/wc.html", request=request),
        "cg": render_to_string("index/cg.html", request=request),
        "lf": render_to_string("index/lf-lgmd.html", request=request),
        "um_core": render_to_string("index/um-core.html", request=request),
        "um": render_to_string("index/um-lgmd.html", request=request),
        "tr_core": render_to_string("index/tr-core.html", request=request),
        "tr": render_to_string("index/tr-lgmd.html", request=request),
        "ti": render_to_string("index/ti.html", request=request),
        "rs": render_to_string("index/rs.html", request=request),
    }
    return JsonResponse(data)


def index_desktop_additional(request):
    data = {
        "lf": render_to_string("index/lf-sm.html", request=request),
        "um": render_to_string("index/um-sm.html", request=request),
        "tr": render_to_string("index/tr-sm.html", request=request),
    }
    return JsonResponse(data)


# Курс 1 - Занятия для детей


def course1(request):
    template = "courses/course1.html"
    return render(request, template)


def course1form(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        contacts = request.POST.get("contacts")
        message = request.POST.get("message")

        # Здесь вы можете обработать данные, например, сохранить их в базе данных
        # ...

        # Возвращаем JSON-ответ
        return JsonResponse(
            {"status": "success", "message": "Данные успешно обработаны!"}
        )

    return JsonResponse(
        {"status": "error", "message": "Неверный метод запроса."}, status=400
    )


# Курс 2 - Курс интенсив


def course2(request):
    template = "courses/course2.html"
    return render(request, template)


def course2form(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        contacts = request.POST.get("contacts")
        message = request.POST.get("message")

        # Здесь вы можете обработать данные, например, сохранить их в базе данных
        # ...

        # Возвращаем JSON-ответ
        return JsonResponse(
            {"status": "success", "message": "Данные успешно обработаны!"}
        )

    return JsonResponse(
        {"status": "error", "message": "Неверный метод запроса."}, status=400
    )


# Курс 3 - Индивидуальные занятия


def course3(request):
    template = "courses/course3.html"
    return render(request, template)


def course3form(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        contacts = request.POST.get("contacts")
        message = request.POST.get("message")

        # Здесь вы можете обработать данные, например, сохранить их в базе данных
        # ...

        # Возвращаем JSON-ответ
        return JsonResponse(
            {"status": "success", "message": "Данные успешно обработаны!"}
        )

    return JsonResponse(
        {"status": "error", "message": "Неверный метод запроса."}, status=400
    )


# Курс 4 - Курсы английского


def course4(request):
    template = "courses/course4.html"
    return render(request, template)


def course4form(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        contacts = request.POST.get("contacts")
        message = request.POST.get("message")

        # Здесь вы можете обработать данные, например, сохранить их в базе данных
        # ...

        # Возвращаем JSON-ответ
        return JsonResponse(
            {"status": "success", "message": "Данные успешно обработаны!"}
        )

    return JsonResponse(
        {"status": "error", "message": "Неверный метод запроса."}, status=400
    )


# О нас


def about(request):
    template = "about/about.html"
    return render(request, template)


# Тесты

T1_WORDS = [
    "to sing",
    "change",
    "to approve",
    "to strengthen",
    "to tell",
    "to emit",
    "to inscribe",
    "prevalence",
    "road",
    "variety",
    "tomorrow",
    "to pick up",
    "benefit",
    "rigid",
    "influence",
    "blind",
    "precisely",
    "land",
    "fast",
    "relatives",
    "to supersede",
    "discerning",
    "to distract",
    "to estimate",
    "to respond",
    "three",
    "bias",
    "cow",
]


T2_QUESTIONS = [
    {
        "question": "Mary is _____ teacher.",
        "answer1": "an",
        "answer2": "a",
        "answer3": "-",
        "correct_answer": "b",
    },
    {
        "question": "I _____ in the morning.",
        "answer1": "drink tea usually",
        "answer2": "drink usually tea",
        "answer3": "usually drink tea",
        "correct_answer": "c",
    },
    {
        "question": "_____ go for a walk?",
        "answer1": "Would you like to",
        "answer2": "Do you like",
        "answer3": "Would you like",
        "correct_answer": "a",
    },
    {
        "question": "My sister _____  in Canada.",
        "answer1": "lives",
        "answer2": "living",
        "answer3": "live",
        "correct_answer": "a",
    },
    {
        "question": "Where _____  ?",
        "answer1": "Peter does work",
        "answer2": "works Peter",
        "answer3": "does Peter work",
        "correct_answer": "c",
    },
    {
        "question": "I don’t have _____ problems.",
        "answer1": "much",
        "answer2": "any",
        "answer3": "some",
        "correct_answer": "b",
    },
    {
        "question": "I  _____ for you all day yesterday.",
        "answer1": "have been looking",
        "answer2": "was looking",
        "answer3": "looking",
        "correct_answer": "b",
    },
    {
        "question": "Tim should spend  _____ time on the computer.",
        "answer1": "a few",
        "answer2": "fewer",
        "answer3": "less",
        "correct_answer": "c",
    },
    {
        "question": "The student apologised _____ the professor _____ being late.",
        "answer1": "to, for",
        "answer2": "to, of",
        "answer3": "for, of",
        "correct_answer": "a",
    },
    {
        "question": "We haven't heard from him for ten years. He _____ .",
        "answer1": "might have died",
        "answer2": "should have died",
        "answer3": "had to die",
        "correct_answer": "a",
    },
    {
        "question": "_____ this morning.",
        "answer1": "My hair had cut",
        "answer2": "I had my hair cut",
        "answer3": "I had cut my hair",
        "correct_answer": "b",
    },
    {
        "question": "Mr Jones _____ at the meeting, but he had to cancel because of his illness.",
        "answer1": "was to speak",
        "answer2": "was speaking",
        "answer3": "was to have spoken",
        "correct_answer": "c",
    },
    {
        "question": "It's been snowing for days. If only it _____ .",
        "answer1": "stopped",
        "answer2": "stops",
        "answer3": "would stop",
        "correct_answer": "c",
    },
    {
        "question": "Where would you rather  _____ ?",
        "answer1": "i slept",
        "answer2": "i’ll sleep",
        "answer3": "i’d sleep",
        "correct_answer": "c",
    },
]



def test1(request):
    template = "tests/test1.html"
    context = {
        "words": T1_WORDS,
        "questions": T2_QUESTIONS,
    }
    return render(request, template, context)


## Обработка форм
@require_POST
# @csrf_exempt  # Используйте это, только если у вас проблемы с CSRF. В идеале, лучше настроить правильную отправку CSRF-токена
def form_handler(request):
    form_id = request.POST.get("form_id")

    # Собираем все данные из формы
    form_data = {
        key: value
        for key, value in request.POST.items()
        if key != "csrfmiddlewaretoken"
    }

    # Формируем сообщение для Telegram
    message = "\n"
    for key, value in form_data.items():
        if key != "form_id":
            message += f"<b>{key}</b>: {value}\n"
    message += "\n"
    # Отправляем сообщение в Telegram
    telegram_response = send_telegram_message(message)

    # Проверяем все ответы в списке
    if all(response.get("ok", False) for response in telegram_response):
        # Все сообщения отправлены успешно
        return JsonResponse({"status": "success"})
    else:
        # Хотя бы одно сообщение не было отправлено
        return JsonResponse({"status": "error", "message": "Failed to send some messages"})


def send_telegram_message(message):
    bot_token = "7648691583:AAHIQ229i4oHdOFHvCR0Bfn9rIuNp6DHcXI"
    # bot_token = "7760390376:AAFgmoxyvVFMKIem6Zdo0zAuMYN0PvNUQEo"
    chat_ids = [1060927499, 5259772234]
    # chat_ids = [1060927499,]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    logger.info(f"Starting to send telegram message to {len(chat_ids)} recipients")

    responses = []
    for chat_id in chat_ids:
        try:
            payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}
            response = requests.post(url, json=payload)
            responses.append(response.json())
        except Exception as e:
            logger.error(f"Error sending message to chat_id {chat_id}: {e}")
            responses.append({"ok": False, "error": str(e)})

    return responses


# def send_telegram_message(message):
#     bot_token = "7648691583:AAHIQ229i4oHdOFHvCR0Bfn9rIuNp6DHcXI"
#     chat_id = 1060927499
#     url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
#     payload = {
#         "chat_id": chat_id,
#         "text": message,
#         "parse_mode": "HTML"
#     }
#     response = requests.post(url, json=payload)
#     return response.json()

# 

RESULTS = {
    "A0": {
        "level": "А0 (beginner)",
        "result_hello": "Привет, пионер английского!",
        "result_text": "На уровне Beginner ты делаешь свои первые шаги в изучении языка. Здесь ты учишься самым базовым элементам: как сказать 'Привет', 'Как дела?' и 'До свидания'. Ты узнаешь, как назвать предметы вокруг тебя, обозначить основные действия и даже составить несколько простых предложений.Практика и непринуждённое общение — вот твои лучшие помощники на этом этапе. Даже простое 'Hello' от тебя уже большой успех, так что дерзай и не сомневайся!",
    },
    "A1": {
        "level": "A1 (elementary)",
        "result_hello": "Привет, путешественник в мире английского языка!",
        "result_text": "Ты только начал, но уже можешь справляться с самыми основными вещами: представиться, спросить дорогу, заказать что-нибудь в кафе. Это как раз первые шаги, чтобы не чувствовать себя потерянным в англоязычной стране. Вперед, за новыми словами!",
    },
    "A2": {
        "level": "A2 (pre-intermediate)",
        "result_hello": "Теперь ты не просто турист, а уже исследователь!",
        "result_text": "Ты можешь говорить о своих увлечениях, обсуждать простые сюжеты и участвовать в коротких диалогах. Твой английский уже достаточно хорош, чтобы рассказать о своих планах на выходные или обсудить последний просмотренный фильм. Не останавливайся на достигнутом, продолжай расширять свой словарный запас!",
    },
    "B1": {
        "level": "B1 (intermediate)",
        "result_hello": "Кажется, ты начинаешь чувствовать себя уверенно!",
        "result_text": "Ты можешь поддержать разговор на широкий круг тем, высказывать и аргументировать своё мнение. Теперь ты в состоянии решать более сложные коммуникативные задачи, такие как описание опыта, выражение чувств и обсуждение некоторых абстрактных идей. Это отличная база для дальнейшего углубления в язык!",
    },
    "B2": {
        "level": "B2 (upper-intermediate)",
        "result_hello": "Ты уже действительно впечатляешь!",
        "result_text": "Твои навыки позволяют тебе свободно общаться на английском в различных ситуациях, читать статьи, смотреть фильмы без перевода и даже понимать шутки и идиомы. Ты можешь обсуждать профессиональные и академические темы, которые интересуют тебя. Этот уровень открывает перед тобой почти безграничные возможности использования языка!",
    },
    "C1": {
        "level": "C1 (advanced)",
        "result_hello": "Вау, ты на вершине!",
        "result_text": "Твой английский настолько хорош, что ты можешь спокойно участвовать в любых академических и профессиональных дискуссиях, понимать сложные тексты и даже создавать подробные и структурированные тексты по специализированным темам. Твой уровень позволяет тебе чувствовать себя как рыба в воде в англоязычной среде, будь то работа, учёба или путешествия.",
    },
    "C2": {
        "level": "C2 (proficient)",
        "result_hello": "Поздравляю, мастер английского!",
        "result_text": "Уровень C2 — это вершина языкового мастерства, куда добираются лишь самые упорные и целеустремленные. На этом уровне ты обладаешь исключительными навыками понимания, говорения, чтения и письма. Ты можешь легко участвовать в любых дискуссиях и академических спорах, понимать сложные идеи и абстракции, излагать свои мысли ясно и убедительно как в устной, так и в письменной форме.",
    },
}


def test_results(request):
    # Получаем количество правильных ответов из параметра URL
    correct_answers = int(request.GET.get('correct', 0))

    total_questions = 52
    # percentage = (correct_answers / total_questions) * 100

    if correct_answers == 52:
        level = "C2"
    elif correct_answers >= 49:
        level = "C1"
    elif correct_answers >= 45:
        level = "B2"
    elif correct_answers >= 36:
        level = "B1"
    elif correct_answers >= 24:
        level = "A2"
    elif correct_answers >= 11:
        level = "A1"
    else:
        level = "A0"

    context = {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'level': RESULTS[level]['level'],
        'result_hello': RESULTS[level]['result_hello'],
        'result_text': RESULTS[level]['result_text'],
    }
    
    template = "tests/test_results.html"
    return render(request, template, context)
